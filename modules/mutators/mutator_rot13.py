import config
import string

from base.mutator.mutator import Mutator
from core.helpers.crypto import rot13

class MMutator(Mutator):

    def __init__(self):

        if config.debug:
            print('calling MMutator.__init__()')

        super().__init__()

        self.name = 'mutator_rot13'
        self.mtype = 'mutator'
        self.author = '@s0lst1c3'
        self.description = 'Converts symbols using rot13'

        self.compatible_interfaces = '*'

    def transform(self, x):

        return rot13(x)
