import config
import string

from base.mutator.mutator import Mutator
from core.helpers.crypto import random_string

class MMutator(Mutator):

    def __init__(self):

        if config.debug:
            print('calling MMutator.__init__()')

        super().__init__()

        self.name = 'mutator_random_string'
        self.mtype = 'mutator'
        self.author = '@s0lst1c3'
        self.description = 'Converts symbols into random alphabetic strings'

        self.compatible_interfaces = '*'

        self.varlog = []

    def transform(self, x):

        retval = random_string(keyspace=string.ascii_letters,
                            exclude=self.varlog)

        self.varlog.append(retval)

        return retval
