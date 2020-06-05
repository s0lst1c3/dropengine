import base64
import hashlib
import config
import core.helpers.crypto

from base.input.crypter.crypter import Crypter

from Crypto.Cipher import AES

# TODO: NEED TO FILL OUT DKEY FUNCTIONS / TEMPLATE RENDERING BECAUSE I FORGOT

class MCrypter(Crypter):

    def __init__(self):

        if config.debug:
            print('calling MEKey.__init__()')

        super().__init__()

        self.name = 'crypter_aes'
        self.mtype = 'crypter'
        self.author = '@s0lst1c3'
        self.description = 'AES crypter'
        self.compatible_omodules = [

            'decrypter_csharp_rijndael_aes',
        ]

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

    def add_arguments(self):

        self.parser.add_argument('--crypter-iv',
                                dest='iv',
                                type=str,
                                required=False,
                                default=None,
                                help='Initialization Vector (IV)')

        self.parser.add_argument('--crypter-iv-b64',
                                dest='iv_b64',
                                action='store_true',
                                help='Decode manually set IV from base64')

    def encrypt(self, pt, ekey_val):

        if type(pt) != bytes:
            pt = pt.encode()

        if self.args.iv is None:
            iv = core.helpers.crypto.random_bytes(length=16)

        BS = 16
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()

        padded_key = hashlib.sha256(ekey_val).digest()

        padded_pt = pad(pt)
        cipher = AES.new(padded_key, AES.MODE_CBC, iv)
        ct = cipher.encrypt(padded_pt)

        return {

            'pt' : pt,
            'ekey' : ekey_val,
            'ct' : ct,
            'iv' : iv,
            'options' : self.args.__dict__,
        }
