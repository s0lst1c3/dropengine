import config

from base.output.output_modules.output_module import OutputModule

class Decrypter(OutputModule):
    
    def __init__(self):
    
        super().__init__()

        if config.debug:
            print('calling Decrypter.__init__()')
