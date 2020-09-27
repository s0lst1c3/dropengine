import sys
import argparse
import os
import json
import re
import base64

from antlr4 import *
from module_maker.CSharpLexer import CSharpLexer
from module_maker.CSharpParser import CSharpParser
from module_maker.CSharpParserListener import CSharpParserListener


from module_maker.symbol_ini import SymbolINI

from jinja2 import Environment, FileSystemLoader

from pathlib import Path

from core.dispatcher_cli import Dispatcher

OMODULE_TYPES = [

    'decrypter',
    'dkey',
    'executor',
    'postmodule',
    'premodule',
    'runner',
]

IMODULE_TYPES = [

    'crypter',
    'ekey',
]

MUTATOR_TYPES = [

    'mutator',
]

MODULE_DIRECTIONS = [

    'output',
    'input',
]

def display_xmodule_choices(xmodule_choices):


    print('[!] The following are valid choices:')
    print()
    for m in xmodule_choices:

        print(f'{m}')
    print()

def cli():

    parser = argparse.ArgumentParser()


    interface_choices = Dispatcher.get_choices('./modules/interfaces', 'MRunnerInterface')

    decrypter_imodule_choices = Dispatcher.get_choices('./modules/input/crypters', 'MCrypter')
    dkey_imodule_choices = Dispatcher.get_choices('./modules/input/ekeys', 'MEKey')
    
    crypter_omodule_choices = Dispatcher.get_choices('./modules/output/decrypters', 'MDecrypter')
    ekey_omodule_choices = Dispatcher.get_choices('./modules/output/dkeys', 'MDKey')

    module_attributes_group = parser.add_argument_group('Module Attributes')

    parser.add_argument('--debug',
                        dest='debug',
                        action='store_true',
                        help='Show debug output.')

    parser.add_argument('--force',
                        dest='force',
                        action='store_true',
                        help='Overwrite existing modules')

    parser.add_argument('--check-mods-exists',
                        dest='validate_compatibility',
                        action='store_true',
                        help='Ensure that compatible modules actually exist')


    module_attributes_group.add_argument('--type',
                        dest='mtype',
                        type=str,
                        required=False,
                        default=None,
                        choices=IMODULE_TYPES+OMODULE_TYPES,
                        help='Specify the type of module you wish to create (--create mode only).')

    module_attributes_group.add_argument('--compatible-interfaces',
                        dest='mcompatible_interfaces',
                        type=str,
                        required=False,
                        nargs='*',
                        default=[],
                        help='Specify the compatible interfaces for your module')

    module_attributes_group.add_argument('--compatible-imodules',
                        dest='mcompatible_imodules',
                        type=str,
                        required=False,
                        nargs='*',
                        default=[],
                        help='Specify compatible input modules for new output module. ')

    module_attributes_group.add_argument('--compatible-omodules',
                        dest='mcompatible_omodules',
                        type=str,
                        required=False,
                        nargs='*',
                        default=[],
                        help='Specify compatible output modules for new input module. ')

    module_attributes_group.add_argument('--name',
                        dest='mname',
                        type=str,
                        required=False,
                        default=None,
                        help='Specify the name of your new module.')

    module_attributes_group.add_argument('--author',
                        dest='mauthor',
                        type=str,
                        required=False,
                        default='',
                        help='Specify the author of your new module.')

    module_attributes_group.add_argument('--description',
                        dest='mdescription',
                        type=str,
                        required=False,
                        default='',
                        help='Specify the description of your new module.')

    template_vars_group = parser.add_argument_group('Template Vars')

    template_vars_group.add_argument('--class-name',
                        dest='mclass_name',
                        type=str,
                        required=True,
                        default=None,
                        help='Specify the class name of your template code.')

    template_vars_group.add_argument('--func-name',
                        dest='mfunc_name',
                        type=str,
                        required=True,
                        default=None,
                        help='Specify the entrypoint function to your code.')

    template_vars_group.add_argument('--symbol-file',
                        dest='symbol_file',
                        type=str,
                        required=False,
                        help='Load vars, methods, params, delegates, and imports from INI file')

    template_vars_group.add_argument('--source-file',
                        dest='source_file',
                        type=str,
                        required=False,
                        help='Raw CSharp source file from which to create template')

    args = parser.parse_args()


    if args.mtype:

        if args.mtype in IMODULE_TYPES:

            if args.mcompatible_imodules != []:

                print()
                print(f'[!] The --compatible-imodules flag should is '
                       'incompatible with module of type {args.mtype}. '
                       'Please use the --compatible-omodules flag '
                       'instead')
                print()

                sys.exit(1)

            if args.mtype == 'crypter' and args.validate_compatibility:

                for m in args.mcompatible_imodules:

                    if m not in crypter_omodule_choices:

                        print()
                        print(f'[!] Module "{m} specified as compatible '
                              f'output module but no module named "{m}" '
                              f'found.')
                        print()
                        display_xmodule_choices(crypter_omodule_choices)

                        sys.exit(1)

            elif args.mtype == 'ekey' and args.validate_compatibility:

                for m in args.mcompatible_omodules:

                    if m not in ekey_omodule_choices:

                        print()
                        print(f'[!] Module "{m} specified as compatible '
                              f'output module but no  module named "{m}" '
                              f'found.')
                        print()
                        display_xmodule_choices(ekey_omodule_choices)

                        sys.exit(1)


            args.mcompatible_xmodules = args.mcompatible_omodules
            

        elif args.mtype in OMODULE_TYPES:

            if args.mcompatible_omodules != []:

                print()
                print(f'[!] The --compatible-omodules flag should is '
                      f'incompatible with module of type {args.mtype}. '
                      f'Please use the --compatible-imodules flag '
                      f'instead')
                print()

                sys.exit(1)

            if args.mtype == 'decrypter' and args.validate_compatibility:

                for m in args.mcompatible_imodules:

                    if m not in decrypter_imodule_choices:

                        print()
                        print(f'[!] Module "{m}" specified as compatible '
                              f'input module but no module named "{m}" '
                              f'found.')
                        print()
                        display_xmodule_choices(decrypter_imodule_choices)

                        sys.exit(1)

            elif args.mtype == 'dkey' and args.validate_compatibility:

                for m in args.mcompatible_imodules:

                    if m not in dkey_imodule_choices:

                        print()
                        print(f'[!] Module "{m} specified as compatible '
                              f'input module but no module named "{m}" '
                              f'found.')
                        print()
                        display_xmodule_choices(dkey_imodule_choices)

                        sys.exit(1)

            args.mcompatible_xmodules = args.mcompatible_imodules

        elif args.mtype in MUTATOR_TYPES:

            if args.mcompatible_imodules != []:

                print()
                print(f'[!] Modules of type {args.mtype} should not have a '
                      f'corresponding input module, and as such the '
                      f'--compatible-imodules flag shuold not be used.')
                print()

            elif args.mcompatible_omodules != []:

                print()
                print(f'[!] Modules of type {args.mtype} should not have a '
                      f'corresponding output module, and as such the '
                      f'--compatible-omodules flag shuold not be used.')
                print()
    if args.validate_compatibility:

        for i in args.mcompatible_interfaces:

            if i not in interface_choices:
                print()
                print(f'[!] Interface "{i} specified as compatible '
                      f'interface but no interface named "{i}" '
                      f'found.')
                print()
                display_xmodule_choices(interface_choices)

                
    # check to make sure module of name mname does not already exist

    if not args.force:

        if args.mtype == 'mutator':

            if args.mname in Dispatcher.get_choices('./modules/mutators', 'MMutator'):

                print(f'[!] Error: {args.mtype} module of name {args.mname} already exists')
                sys.exit(1)

        elif args.mtype == 'decrypter':

            if args.mname in Dispatcher.get_choices('./modules/output/decrypters', 'MDecrypter'):

                print(f'[!] Error: {args.mtype} module of name {args.mname} already exists')
                sys.exit(1)

        elif args.mtype == 'dkey':

            if args.mname in Dispatcher.get_choices('./modules/output/dkeys', 'MDKey'):

                print(f'[!] Error: {args.mtype} module of name {args.mname} already exists')
                sys.exit(1)

        elif args.mtype == 'executor':

            if args.mname in Dispatcher.get_choices('./modules/output/executors', 'MExecutor'):

                print(f'[!] Error: {args.mtype} module of name {args.mname} already exists')
                sys.exit(1)


        elif args.mtype == 'postmodules':

            if args.mname in Dispatcher.get_choices('./modules/output/postmodules', 'MPostModule'):

                print(f'[!] Error: {args.mtype} module of name {args.mname} already exists')
                sys.exit(1)

        elif args.mtype == 'premodule':

            if args.mname in Dispatcher.get_choices('./modules/output/premodules', 'MPreModule'):

                print(f'[!] Error: {args.mtype} module of name {args.mname} already exists')
                sys.exit(1)

        elif args.mtype == 'runners':

            if args.mname in Dispatcher.get_choices('./modules/output/runners', 'MRunner'):

                print(f'[!] Error: {args.mtype} module of name {args.mname} already exists')
                sys.exit(1)

        elif args.mtype == 'crypter':

            if args.mname in Dispatcher.get_choices('./modules/input/crypters', 'MCrypter'):

                print(f'[!] Error: {args.mtype} module of name {args.mname} already exists')
                sys.exit(1)

        elif args.mtype == 'ekey':

            if args.mname in Dispatcher.get_choices('./modules/input/ekeys', 'MEKey'):

                print(f'[!] Error: {args.mtype} module of name {args.mname} already exists')
                sys.exit(1)

    # ensure input files actually exist and are not directories
    
    if not os.path.exists(args.source_file):

        print(f'[!] Error: source file {args.source_file} does not exist')
        sys.exit(1)

    if not os.path.isfile(args.source_file):

        print(f'[!] Error: source file {args.source_file} is a directory')
        sys.exit(1)

    if not os.path.exists(args.symbol_file):

        print(f'[!] Error: symbol file {args.symbol_file} does not exist')
        sys.exit(1)

    if not os.path.isfile(args.symbol_file):

        print(f'[!] Error: symbol file {args.symbol_file} is a directory')
        sys.exit(1)

    return args

def replace_symbols_in_line(symbol, base64_strs, sub_val, line):

    b64_sub_val = base64.b64encode(sub_val.encode()).decode()
    base64_strs[sub_val] = b64_sub_val

    # base64_strs will be updated, since all variables in python
    # are passed by reference. however, symbol is a string, and
    # as such is immutable, therefore we need to return it.
    return line.replace(symbol, b64_sub_val)

def namespace_in_imports(line, imports):

    namespace = line[len('using'):].strip().rstrip(';').strip()
    return namespace in imports

def sub_file_symbols(input_handle,
                      func_name='',
                      class_name='',
                      _vars=[],
                      methods=[],
                      params=[],
                      class_decls=[],
                      delegates=[],
                      imports=[]):

    base64_strs = {}
    output_lines = []
    for line in input_handle:
    
        if line.startswith('using'):
    
            if namespace_in_imports(line, imports):
                continue
    
        for v in _vars:
            line = replace_symbols_in_line(v,
                                           base64_strs,
                                           '{{ v[\''+v+'\'] }}',
                                           line)
    
        for v in methods:
    
            if v == func_name:
                line = replace_symbols_in_line(v,
                                               base64_strs,
                                               '{{ func_name }}',
                                               line)
            else:
                line = replace_symbols_in_line(v,
                                              base64_strs,
                                              '{{ v[\''+v+'\'] }}',
                                              line)
    
        for v in class_decls:
    
            if v == class_name:
                line = replace_symbols_in_line(v,
                                               base64_strs,
                                               '{{ special[\'class_name\'] }}',
                                               line)
            else:
                line = replace_symbols_in_line(v,
                                              base64_strs,
                                              '{{ v[\''+v+'\'] }}',
                                              line)
    
    
        for v in params:
            line = replace_symbols_in_line(v,
                                           base64_strs,
                                           '{{ v[\''+v+'\'] }}',
                                           line)
        for v in delegates:
            line = replace_symbols_in_line(v,
                                           base64_strs,
                                           '{{ v[\''+v+'\'] }}',
                                           line)
    
        output_lines.append(line)
    
    raw_output = ''.join(output_lines)
    for sub_val,b64_sub_val in base64_strs.items():
        raw_output = raw_output.replace(b64_sub_val, sub_val)

    return raw_output

def create(args):

    if args.debug:

        print(json.dumps(args.__dict__, indent=4, sort_keys=True))

    # set vars from args
    mname = args.mname
    mtype = args.mtype
    mauthor = args.mauthor
    mdescription = args.mdescription
    compatible_interfaces = args.mcompatible_interfaces
    compatible_xmodules = args.mcompatible_xmodules
    class_name = args.mclass_name
    func_name = args.mfunc_name

    symbol_file = args.symbol_file

    source_file = args.source_file

    if mtype in OMODULE_TYPES:

        module_direction = 'output'

        if symbol_file is not None:

            # set vars from symbol ini
            s_ini = SymbolINI(symbol_file)

            _vars = s_ini.vars()
            methods = s_ini.method_names()
            class_decls = s_ini.class_decls()
            params = s_ini.formal_params()
            delegates = s_ini.delegates()
            imports = s_ini.imports()

            _vars.sort(key=lambda item: (-len(item), item))
            methods.sort(key=lambda item: (-len(item), item))
            class_decls.sort(key=lambda item: (-len(item), item))
            params.sort(key=lambda item: (-len(item), item))
            delegates.sort(key=lambda item: (-len(item), item))
            imports.sort(key=lambda item: (-len(item), item))

        else:

            _vars = []
            methods = []
            params = []
            class_decls = []
            delegates = []
            imports = []

        if args.debug:

            print('_vars:', _vars)
            print('methods:', methods)
            print('params:', params)
            print('delegates:', delegates)
            print('imports:', imports)

        # calculate template path
        output_cs_template_path = os.path.join(f'{mtype}s', f'{mname}.cs')
        input_py_template_path = os.path.join('module_maker', f'mm_{mtype}.py')
        output_py_template_path = f'modules/output/{mtype}s/{mname}.py'
        
        if args.debug:

            print('output_cs_template_path :', output_cs_template_path)
            print('input_py_template_path :', input_py_template_path)
            print('output_py_template_path :', output_py_template_path)
        
        env = Environment(loader=FileSystemLoader('templates'))

        template = env.get_template(input_py_template_path)

        rendered_template = template.render(name=mname,
                               author=mauthor,
                               description=mdescription,
                               compatible_interfaces=compatible_interfaces,
                               compatible_xmodules=compatible_xmodules,
                               _vars=_vars+methods+params+delegates,
                               imports=imports,
                               template_path=output_cs_template_path,
                               func_name=func_name,
                               class_name=class_name)

        with open(output_py_template_path, 'w') as output_handle:
            output_handle.write(rendered_template+'\n')

        if source_file is not None:

            with open(source_file) as input_handle:
                raw_output = sub_file_symbols(input_handle,
                                             func_name=func_name,
                                             class_name=class_name,
                                             _vars=_vars,
                                             methods=methods,
                                             params=params,
                                             class_decls=class_decls,
                                             delegates=delegates,
                                             imports=imports)

            output_file = os.path.join('templates', output_cs_template_path)
            with open(output_file, 'w') as output_handle:
                output_handle.write(raw_output)

    else:

        module_direction = 'input'

        # calculate template path
        input_py_template_path = os.path.join('module_maker', f'mm_{mtype}.py')
        output_py_template_path = f'modules/input/{mtype}s/{mname}.py'
        
        if args.debug:

            print('input_py_template_path :', input_py_template_path)
            print('output_py_template_path :', output_py_template_path)
        
        env = Environment(loader=FileSystemLoader('templates'))

        template = env.get_template(input_py_template_path)

        rendered_template = template.render(name=mname,
                               author=mauthor,
                               description=mdescription,
                               compatible_interfaces=compatible_interfaces,
                               compatible_xmodules=compatible_xmodules)

        with open(output_py_template_path, 'w') as output_handle:
            output_handle.write(rendered_template+'\n')

def main():

    args = cli()

    create(args)

if __name__ == '__main__':
    cli()
    main()
