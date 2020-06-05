import base64
import config
import core.helpers.crypto

from base.input.ekey.ekey import EKey

# TODO: NEED TO FILL OUT DKEY FUNCTIONS / TEMPLATE RENDERING BECAUSE I FORGOT

class MEKey(EKey):

    def __init__(self):

        if config.debug:
            print('calling MEKey.__init__()')

        super().__init__()

        self.name = 'ekey_static'
        self.mtype = 'ekey'
        self.author = '@s0lst1c3'
        self.description = 'Static encryption key.'
        self.compatible_omodules = [

            'dkey_csharp_static',
        ]

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

    def add_arguments(self):

        self.parser.add_argument('--ekey-len',
                                dest='ekey_len',
                                type=int,
                                required=False,
                                default=32,
                                help='Length of encryption key')

        self.parser.add_argument('--ekey-val',
                                dest='ekey_value',
                                type=str,
                                required=False,
                                default=None,
                                help='Manually set encryption key')

        self.parser.add_argument('--ekey-b64',
                                dest='ekey_b64',
                                action='store_true',
                                help='Decode manually set encryption key from base64')

    def generate(self):

        if self.args.ekey_value is not None:
            if self.args.ekey_b64:
                ekey_val = self.args.ekey_val
            else:
                ekey_val = base64.b64decode(self.args.ekey_val)
        else:
            ekey_val = core.helpers.crypto.random_key(length=self.args.ekey_len)
        self.ekey_val = ekey_val
        return {
            'val' : ekey_val,
            'len' : self.args.ekey_len,
            'options' : self.args.__dict__,
        }
