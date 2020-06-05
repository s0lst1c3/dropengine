import config

from base.output.output_modules.csharp_output_module import CSharpOutputModule
from base.output.decrypter.decrypter import Decrypter

class CSharpDecrypter(CSharpOutputModule, Decrypter):

    def __init__(self):
        if config.debug:
            print('calling CSharpDecrypter.__init__()')
        super().__init__()
