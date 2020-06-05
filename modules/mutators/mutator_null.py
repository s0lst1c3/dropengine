import config

from base.mutator.mutator import Mutator

class MMutator(Mutator):

    def __init__(self):

        if config.debug:
            print('calling MMutator.__init__()')

        super().__init__()

        self.name = 'mutator_null'
        self.mtype = 'mutator'
        self.author = '@s0lst1c3'
        self.description = 'Null mutator - leaves function names exactly the same.'

        self.compatible_interfaces = '*'

    def transform(self, x):

        return x

