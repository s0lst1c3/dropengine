import json
import config

from base.output.decrypter.csharp_decrypter import CSharpDecrypter

class MDecrypter(CSharpDecrypter):

    def __init__(self):

        if config.debug:
            print('calling MDKey.__init__()')
        super().__init__()

        self.name = 'decrypter_csharp_rijndael_aes'
        self.mtype = 'decrypter'
        self.author = '@s0lst1c3'
        self.description = 'CSharp Rijndael AES decrypter'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.compatible_imodules = [

            'crypter_aes',
        ]

        self.functions = []
        self._vars = [
            'ct',
            'ekey',
            'iv',
            'hashstring',
            'hashed_key',
            'rijAlg',
            'decryptor',
        ]
        self.comments = []
        self.whitespaces = []

        self.imports = [
            'System',
            'System.Runtime.InteropServices',
            'System.Text',
            'System.Linq',
            'System.IO',
            'System.Security.Cryptography',
        ]

        self.template = 'decrypters/decrypter_csharp_rijndael_aes.cs'

        self.func_name = 'decrypt'
        self.class_name = 'Decrypter'

        self.mutate_func_name = True
        self.mutate_class_name = True
