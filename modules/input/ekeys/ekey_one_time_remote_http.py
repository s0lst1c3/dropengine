import base64
import config
import core.helpers.crypto

from base.input.ekey.ekey import EKey

from models.models import Database

# TODO: NEED TO FILL OUT DKEY FUNCTIONS / TEMPLATE RENDERING BECAUSE I FORGOT

class MEKey(EKey):

    def __init__(self):

        if config.debug:
            print('calling MEKey.__init__()')

        super().__init__()

        self.name = 'ekey_one_time_remote_http'
        self.mtype = 'ekey'
        self.author = '@s0lst1c3'
        self.description = 'One-time remote HTTP key'

        self.compatible_omodules = [

            'dkey_remote_csharp_otk_http',
        ]

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

    def add_arguments(self):

        self.parser.add_argument('--http-otk-lhost',
                                dest='http_otk_lhost',
                                type=str,
                                required=False,
                                default=None,
                                help='FQDN or IP from which to retrieve OTK')

        self.parser.add_argument('--http-otk-lport',
                                dest='http_otk_lport',
                                type=str,
                                required=False,
                                default=None,
                                help='HTTP(S) port from which to retrieve OTK')

        self.parser.add_argument('--http-otk-protocol',
                                dest='http_otk_protocol',
                                type=str,
                                required=False,
                                choices=['http', 'https'],
                                default='http',
                                help='Choose between http or https')

    def generate(self):

        assert self.args.http_otk_lhost is not None
        assert self.args.http_otk_protocol is not None
    
        if self.args.http_otk_lport is None:

            if self.args.http_otk_protocol == 'http':
                self.args.http_otk_lport = 80
            else:
                self.args.http_otk_lport = 443

        ekey_val = core.helpers.crypto.random_key(length=32)
        self.ekey_val = ekey_val

        db = Database()
        db.initialize()
        implant_id, remote_key = db.add(ekey_val)

        use_alt_port = not any([
            self.args.http_otk_protocol == 'http' and self.args.http_otk_lport == 80,
            self.args.http_otk_protocol == 'https' and self.args.http_otk_lport == 443,
        ])
        if use_alt_port:
            source = f'{self.args.http_otk_protocol}://{self.args.http_otk_lhost}:{self.args.http_otk_lport}'
        else:
            source = f'{self.args.http_otk_protocol}://{self.args.http_otk_lhost}'


        return {
            'val' : ekey_val,
            'source' : source,
            'len' : 32,
            'implant_id' : implant_id,
            'options' : self.args.__dict__,
        }
