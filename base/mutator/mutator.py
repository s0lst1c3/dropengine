import config

from base.de_component import DEComponent
from base.has_cli import HasCLI

class Mutator(HasCLI, DEComponent):

    def __init__(self):

        if config.debug:
            print('calling Mutator.__init__()')
        super().__init__()

    def transform(self, x):
        raise Exception('self.transform() function not implemented')
