import config
import string

from base.mutator.mutator import Mutator
from core.helpers.error import pexit

class MMutator(Mutator):

    def __init__(self):

        if config.debug:
            print('calling MMutator.__init__()')

        super().__init__()

        self.name = 'mutator_wordlist'
        self.mtype = 'mutator'
        self.author = '@s0lst1c3'
        self.description = 'Converts symbols using rot13'

        self.compatible_interfaces = '*'

        self.varlog = []
        self.wordlist = None
        self.index = 0

    def add_arguments(self):

        self.parser.add_argument('--mutator-wordlist',
                            dest='wordlist_path',
                            type=str,
                            required=False,
                            default=None,
                            help=('Wordlist from which to '
                                  'perform symbol substitutions'))


    def transform(self, x):
    
        print(self.args)

        try:
            assert self.args.wordlist_path is not None
        except AssertionError:
            pexit(('No wordlist specified. Please use the --mutator-wordlist flag '
                'to specify a wordlist path'))

        if self.wordlist is None:
            self.wordlist = []
            with open(self.args.wordlist_path) as input_handle:
                for line in input_handle:
                    line = line.strip()
                    self.wordlist.append(line)

        if self.index >= len(self.wordlist):
            pexit(('The number of symbols to transform exceeds the '
                    'length of the provide wordlist.'))
            
        word = self.wordlist[self.index]
        self.index = self.index + 1

        return word
