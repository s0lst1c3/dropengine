import config

from argparse import ArgumentParser
from base.de_component import DEComponent

class HasCLI(object):

    def __init__(self):

        if config.debug:

            print('calling HasCLI.__init__()')

        # dirty hack to obtain help message without initializing the -h flag
        self.parser = ArgumentParser()
        self.add_arguments()
        self._print_help = self.parser.print_help
        self.parser = ArgumentParser(add_help=False)
        self.add_arguments()
        self.add_hidden_help_method()

        self.options = { }
        super().__init__()

    def add_arguments(self):
        if config.debug:
            print('!!!!Calling HasCLI add arguments')

    def print_help(self):
        print(self)
        self._print_help()

    def add_hidden_help_method(self):

        self.parser.add_argument('--help', '-h',
                                dest='print_help',
                                action='store_true',
                                help='Print help message')

    def get_options(self):

        return self.options

    def parse_args(self, unknown):

        if config.debug:
            print(self)
            print(unknown)

        self.args, unknown = self.parser.parse_known_args(unknown)
        if config.debug:
            print()
            print(self.args)
            print()
        self.options = self.args.__dict__
        self.options['name'] = self.name
        return unknown

    def print_args(self):

        print(json.dumps(self.options, indent=4, sort_keys=True))

