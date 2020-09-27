import sys
import argparse

from antlr4 import *
from CSharpLexer import CSharpLexer
from CSharpParser import CSharpParser
from CSharpParserListener import CSharpParserListener


from symbol_ini import SymbolINI


OMODULE_TYPES = [

    'decrypter',
    'dkey',
    'executor',
    'imports',
    'inner_shell',
    'output_modules',
    'payload_main',
    'postmodule',
    'premodule',
    'runner',
]

IMODULE_TYPES = [

]

MODULE_DIRECTIONS = [

    'output',
    'input',
]

def cli():

    parser = argparse.ArgumentParser()

    parser.add_argument('--input-file', '-i',
                        dest='input_file',
                        type=str,
                        required=True,
                        help='Specify source code file to input')

    parser.add_argument('--output-file', '-o',
                        dest='output_file',
                        type=str,
                        required=True,
                        help='Specify name for output INI file')

    args = parser.parse_args()

    return args

def gather(args):

    input_handle = FileStream(args.input_file)
    lexer = CSharpLexer(input_handle)
    tokens = CommonTokenStream(lexer)
    parser = CSharpParser(tokens)
    tree = parser.compilation_unit()

    listener = CSharpParserListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    with open(args.output_file, 'w') as output_handle:

        output_handle.write('[vars]\n')
        for v in listener.vars:
            output_handle.write(v+'\n')
        output_handle.write('\n')

        output_handle.write('[methods]\n')
        for v in listener.methods:
            output_handle.write(v+'\n')
        output_handle.write('\n')

        output_handle.write('[class_decls]\n')
        for v in listener.class_decls:
            output_handle.write(v+'\n')
        output_handle.write('\n')

        output_handle.write('[params]\n')
        for v in listener.params:
            output_handle.write(v+'\n')
        output_handle.write('\n')

        output_handle.write('[delegates]\n')
        for v in listener.delegates:
            output_handle.write(v+'\n')
        output_handle.write('\n')

        output_handle.write('[imports]\n')
        for v in listener.imports:
            output_handle.write(v+'\n')
        output_handle.write('\n')

def main():

    args = cli()

    gather(args)

if __name__ == '__main__':
    cli()
    main()
