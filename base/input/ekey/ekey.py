import config

from base.input.input_module.input_module import InputModule

class EKey(InputModule):

    def __init__(self):

        if config.debug:
            print('calling EKey.__init__()')
        self.ekey_val = None
        super().__init__()

    def value(self):
        self.ekey_val

    def generate(self):
        return None
