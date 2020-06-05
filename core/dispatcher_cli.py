
import json
import sys

#from core.loader import Loader
#from base64 import b64decode as b64
from argparse import ArgumentParser
from core.loader import Loader

class Dispatcher:

    def __init__(self):

        # dirty hack to obtain help message without initializing the -h flag
        parser = ArgumentParser()
        self.add_arguments(parser)
        self._print_help = parser.print_help
        parser = ArgumentParser(add_help=False)
        self.add_hidden_help_method(parser)
        self.add_arguments(parser)

        self.all_modules = []
        self.master_parser = parser

        self.init_loaders()
        self.init_loadables()

        self.dispatch = { 

            'crypter' : None,
            'ekeys' : [],
            'executor' : None,
            'runner' : None,
            'master' : None,
            'mutator' : None,
            'dkeys' : [],
            'decrypter' : None,
            'postmodules' : [],
            'premodules' : [],
            'interface' : None,
        }

        self.options = { 

            'crypter' : {},
            'ekeys' : [],
            'executor' : {},
            'runner' : {},
            'master' : {},
            'mutator' : {},
            'dkeys' : [],
            'decrypter' : {},
            'postmodules' : [],
            'premodules' : [],
            'interface' : {},
        }

        #dispatch = {
        #
        #    'crypter' : crypter_parser,
        #    'ekey' : ekey_parser,
        #    'executor' : executor_parser,
        #    'mutator' : mutator_parser,
        #    'postmodules' : {
        #        'postmodule_a' : postmodule_a_parser,
        #        'postmodule_b' : postmodule_b_parser,
        #    },
        #    'premodules' : {
        #        'premodule_a' : premodule_a_parser,
        #        'premodule_b' : premodule_b_parser,
        #    },
        #}

    @staticmethod
    def at_least_one_module_type_is_selected(args):

        return any([

            #args.ekey is not None,
            args.ekeys != [],
            args.dkeys != [],
            args.crypter is not None,
            args.decrypter is not None,
            args.executor is not None,
            args.mutator is not None,
            args.runner is not None,
            args.premodules != [],
            args.postmodules != [],
        ])

    def print_help(self):

        #todo: dkey / decryptor appear to be missing
        if self.at_least_one_module_type_is_selected(self.master_args):

            if self.master_args.executor is not None:
                self.executors[self.master_args.executor].print_help()
            if self.master_args.runner is not None:
                self.runners[self.master_args.runner].print_help()
            #if self.master_args.ekey is not None:
            #    self.ekeys[self.master_args.ekey].print_help()
            if self.master_args.crypter is not None:
                self.crypters[self.master_args.crypter].print_help()
            if self.master_args.decrypter is not None:
                self.decrypters[self.master_args.decrypter].print_help()
            if self.master_args.mutator is not None:
                self.mutators[self.master_args.mutator].print_help()
            if self.master_args.postmodules != []: 
                for post in self.master_args.postmodules:
                    self.premodules[post].print_help()
            if self.master_args.premodules != []: 
                for pre in self.master_args.premodules:
                    self.premodules[pre].print_help()
            if self.master_args.ekeys != []:
                for e in self.master_args.ekeys:
                    self.ekeys[e].print_help()
            
        else:
            self._print_help()


    def init_loaders(self):

        ## interface - public
        self.interface_loader = Loader(paths=['./modules/interfaces'], mtype='MRunnerInterface')

        # input - public 
        self.ekey_loader = Loader(paths=['./modules/input/ekeys'], mtype='MEKey')
        self.crypter_loader = Loader(paths=['./modules/input/crypters'], mtype='MCrypter')

        # output - public
        self.executor_loader = Loader(paths=['./modules/output/executors'], mtype='MExecutor')
        self.premodule_loader = Loader(paths=['./modules/output/premodules'], mtype='MPreModule')
        self.postmodule_loader = Loader(paths=['./modules/output/postmodules'], mtype='MPostModule')
        self.decrypter_loader = Loader(paths=['./modules/output/decrypters'], mtype='MDecrypter')
        self.dkey_loader = Loader(paths=['./modules/output/dkeys'], mtype='MDKey')

        self.mutator_loader = Loader(paths=['./modules/mutators'], mtype='MMutator')

        self.runner_loader = Loader(paths=['./modules/output/runners'], mtype='MRunner')

    def init_loadables(self):

        ## interface - public
        self.interfaces = self.interface_loader.get_loadables()
        self.all_modules += self.interfaces

        ## input - public 
        self.ekeys = self.ekey_loader.get_loadables()
        self.all_modules += self.ekeys
        self.crypters = self.crypter_loader.get_loadables()
        self.all_modules += self.crypters

        # output - public
        self.executors = self.executor_loader.get_loadables()
        self.all_modules += self.executors
        self.mutators = self.mutator_loader.get_loadables()
        self.all_modules += self.mutators
        self.premodules = self.premodule_loader.get_loadables()
        self.all_modules += self.premodules
        self.postmodules = self.postmodule_loader.get_loadables()
        self.all_modules += self.postmodules
        self.decrypters = self.decrypter_loader.get_loadables()
        self.all_modules += self.decrypters
        self.dkeys = self.dkey_loader.get_loadables()
        self.all_modules += self.dkeys

        self.runners = self.runner_loader.get_loadables()
        self.all_modules += self.runners
    

    def parse_args(self):

        self.master_args, unknown = self.master_parser.parse_known_args()

        self.options['master'] = self.master_args.__dict__

        if self.master_args.debug:
            self.print_args()

        if self.master_args.print_help:
            self.print_help()
            sys.exit()

        if self.master_args.validate_modules:

            for m in self.all_modules:
                m.validate()

            sys.exit()


        if self.master_args.list is not None:
            print()

            list_all = self.master_args.list == [] or 'all' in self.master_args.list

            if list_all or 'ekeys' in self.master_args.list:
                print('Listing ekeys:')
                print()
                for _ in self.ekeys:
                    print(f'    {_}')
                print()
            if list_all or 'dkeys' in self.master_args.list:
                print('Listing dkeys:')
                print()
                for _ in self.dkeys:
                    print(f'    {_}')
                print()
            if list_all or 'executors' in self.master_args.list:
                print('Listing executors:')
                print()
                for _ in self.executors:
                    print(f'    {_}')
                print()
            if list_all or 'crypters' in self.master_args.list:
                print('Listing crypters:')
                print()
                for _ in self.crypters:
                    print(f'    {_}')
                print()
            if list_all or 'decrypters' in self.master_args.list:
                print('Listing decrypters:')
                print()
                for _ in self.decrypters:
                    print(f'    {_}')
                print()
            if list_all or 'mutators' in self.master_args.list:
                print('Listing mutators:')
                print()
                for _ in self.mutators:
                    print(f'    {_}')
                print()
            if list_all or 'runners' in self.master_args.list:
                print('Listing runners:')
                print()
                for _ in self.runners:
                    print(f'    {_}')
                print()
            if list_all or 'interfaces' in self.master_args.list:
                print('Listing interfaces:')
                print()
                for _ in self.interfaces:
                    print(f'    {_}')
                print()
            if list_all or 'premodules' in self.master_args.list:
                print('Listing premodles:')
                print()
                for _ in self.premodules:
                    print(f'    {_}')
                print()
            if list_all or 'postmodules' in self.master_args.list:
                print('Listing postmodules:')
                print()
                for _ in self.postmodules:
                    print(f'    {_}')
                print()
            sys.exit()

        elif self.at_least_one_module_type_is_selected(self.master_args):

            #if self.master_args.ekey is not None:

            #    self.dispatch['ekey'] = self.ekeys[self.master_args.ekey]
            #    unknown = self.ekeys[self.master_args.ekey].parse_args(unknown)
            #    self.options['ekey'] = self.ekeys[self.master_args.ekey].get_options()


            if self.master_args.interface is not None:

                self.dispatch['interface'] = self.interfaces[self.master_args.interface]


            #if self.master_args.dkey is not None:

            #    self.dispatch['dkey'] = self.dkeys[self.master_args.dkey]
            #    unknown = self.dkeys[self.master_args.dkey].parse_args(unknown)
            #    self.options['dkey'] = self.dkeys[self.master_args.dkey].get_options()

            if self.master_args.executor is not None:

                self.dispatch['executor'] = self.executors[self.master_args.executor]
                unknown = self.executors[self.master_args.executor].parse_args(unknown)
                self.options['executor'] = self.executors[self.master_args.executor].get_options()
        
            if self.master_args.crypter is not None:

                self.dispatch['crypter'] = self.crypters[self.master_args.crypter]
                unknown = self.crypters[self.master_args.crypter].parse_args(unknown)
                self.options['crypter'] = self.crypters[self.master_args.crypter].get_options()

            if self.master_args.decrypter is not None:

                self.dispatch['decrypter'] = self.decrypters[self.master_args.decrypter]
                unknown = self.decrypters[self.master_args.decrypter].parse_args(unknown)
                self.options['decrypter'] = self.decrypters[self.master_args.decrypter].get_options()

            if self.master_args.mutator is not None:

                self.dispatch['mutator'] = self.mutators[self.master_args.mutator]
                unknown = self.mutators[self.master_args.mutator].parse_args(unknown)
                self.options['mutator'] = self.mutators[self.master_args.mutator].get_options()

            if self.master_args.runner is not None:

                self.dispatch['runner'] = self.runners[self.master_args.runner]
                unknown = self.runners[self.master_args.runner].parse_args(unknown)
                self.options['runner'] = self.runners[self.master_args.runner].get_options()

            if self.master_args.premodules != []: 

                for pre in self.master_args.premodules:
                    self.dispatch['premodules'].append(self.premodules[pre])
                    unknown = self.premodules[pre].parse_args(unknown)
                    self.options['premodules'].append(self.premodules[pre].get_options())

            if self.master_args.postmodules != []: 

                for post in self.master_args.postmodules:
                    self.dispatch['postmodules'].append(self.postmodules[post])
                    unknown = self.postmodules[post].parse_args(unknown)
                    self.options['postmodules'].append(self.postmodules[post].get_options())

            if self.master_args.ekeys != []:

                for ekey in self.master_args.ekeys:
                    self.dispatch['ekeys'].append(self.ekeys[ekey])
                    unknown = self.ekeys[ekey].parse_args(unknown)
                    self.options['ekeys'].append(self.ekeys[ekey].get_options())

            if self.master_args.dkeys != []:

                for dkey in self.master_args.dkeys:
                    self.dispatch['dkeys'].append(self.dkeys[dkey])
                    unknown = self.dkeys[dkey].parse_args(unknown)
                    self.options['dkeys'].append(self.dkeys[dkey].get_options())

    def print_args(self):

        print(json.dumps(self.options, indent=4, sort_keys=True))

    def print_dispatch(self):

        print(self.dispatch)

    @staticmethod
    def add_hidden_help_method(parser):

        parser.add_argument('--help', '-h',
                                dest='print_help',
                                action='store_true',
                                help='Print help message')

    @staticmethod
    def get_choices(path, mtype):
        return [
            c for c in Loader(paths=[path], mtype=mtype).get_loadables().modules
        ]

    @staticmethod
    def add_arguments(parser):

        modules_group = parser.add_argument_group('Modules')

        modules_group.add_argument('--crypter',
                                dest='crypter',
                                type=str,
                                required=False,
                                default=None,
                                choices=Dispatcher.get_choices('./modules/input/crypters', 'MCrypter'),
                                help='Select crypter')


        
        modules_group.add_argument('--interface',
                                dest='interface',
                                type=str,
                                required=False,
                                default=None,
                                help='Select interface')
        
        #modules_group.add_argument('--ekey',
        #                        dest='ekey',
        #                        type=str,
        #                        required=False,
        #                        default=None,
        #                        choices=Dispatcher.get_choices('./modules/input/ekeys', 'MEKey'),
        #                        help='Select ekey')

        #modules_group.add_argument('--dkey',
        #                        dest='dkey',
        #                        type=str,
        #                        required=False,
        #                        default=None,
        #                        choices=Dispatcher.get_choices('./modules/output/dkeys', 'MDKey'),
        #                        help='Select dkey')


        parser.add_argument('--debug',
                                dest='debug',
                                action='store_true',
                                help='Display debug output')


        parser.add_argument('--output-file', '-o',
                                dest='output_file',
                                type=str,
                                default=None,
                                help='Store finished payload in output file.')

        modules_group.add_argument('--decrypter',
                                dest='decrypter',
                                type=str,
                                required=False,
                                default=None,
                                choices=Dispatcher.get_choices('./modules/output/decrypters', 'MDecrypter'),
                                help='Select decrypter')
        
        modules_group.add_argument('--executor',
                                dest='executor',
                                type=str,
                                required=False,
                                default=None,
                                choices=Dispatcher.get_choices('./modules/output/executors', 'MExecutor'),
                                help='Select executor')
        
        modules_group.add_argument('--mutator',
                                dest='mutator',
                                type=str,
                                required=False,
                                default=None,
                                choices=Dispatcher.get_choices('./modules/mutators', 'MMutator'),
                                help='Select mutator')

        modules_group.add_argument('--runner',
                                dest='runner',
                                type=str,
                                required=False,
                                default=None,
                                choices=Dispatcher.get_choices('./modules/output/runners', 'MRunner'),
                                help='Select runner')
        
        modules_group.add_argument('--postmodules',
                                dest='postmodules',
                                type=str,
                                required=False,
                                nargs='*',
                                default=[],
                                choices=Dispatcher.get_choices('./modules/output/postmodules', 'MPostModule'),
                                help='Select postmodules')
        
        modules_group.add_argument('--premodules',
                                dest='premodules',
                                type=str,
                                required=False,
                                nargs='*',
                                choices=Dispatcher.get_choices('./modules/output/premodules', 'MPreModule'),
                                default=[],
                                help='Select premodules')

        modules_group.add_argument('--ekeys',
                                dest='ekeys',
                                type=str,
                                required=False,
                                nargs='*',
                                default=[],
                                choices=Dispatcher.get_choices('./modules/input/ekeys', 'MEKey'),
                                help='Select ekey')

        modules_group.add_argument('--dkeys',
                                dest='dkeys',
                                type=str,
                                required=False,
                                nargs='*',
                                default=[],
                                choices=Dispatcher.get_choices('./modules/output/dkeys', 'MDKey'),
                                help='Select dkey')


        modes_group = parser.add_argument_group('Modes')

        modes_group.add_argument('--list', 
                            dest='list',
                            type=str,
                            required=False,
                            default=None,
                            nargs='*',
                            choices=[
                                'all',
                                'crypters',
                                'ekeys',
                                'decrypters',
                                'dkeys',
                                'mutators',
                                'executors',
                                'interfaces',
                                'postmodules',
                                'premodules',
                                'runners',
                            ],
                            help='List modules')

        modes_group.add_argument('--build', 
                            dest='build',
                            action='store_true',
                            help='Build a payload')

        modes_group.add_argument('--validate-modules', 
                            dest='validate_modules',
                            action='store_true',
                            help='Build a payload')

        build_group = parser.add_argument_group('Build')

        build_group.add_argument('--shellcode',
                                dest='shellcode',
                                type=str,
                                required=False,
                                default=None,
                                help='Select shellcode')

if __name__ == '__main__':

    mp = Dispatcher()
    mp.parse_args()
    mp.print_args()

