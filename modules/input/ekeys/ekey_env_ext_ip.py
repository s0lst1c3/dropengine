import base64
import config
import core.helpers.crypto

from base.input.ekey.ekey import EKey


class MEKey(EKey):

    def __init__(self):

        if config.debug:
            print('calling MEKey.__init__()')

        super().__init__()

        self.name = 'ekey_env_ext_ip'
        self.mtype = 'ekey'
        self.author = '@s0lst1c3'
        self.description = 'Environmental key derived from external IP address'


        self.compatible_omodules = [

            'dkey_env_csharp_ext_ip',
        ]
        self.compatible_interfaces = [
        
            'csharp_runner_interface',
        ]

    def add_arguments(self):

        self.parser.add_argument('--ekey-ext-ip',
                                dest='ekey_ext_ip',
                                type=str,
                                required=False,
                                default=None,
                                help='Set encryption key to external IP address')

        self.parser.add_argument('--ekey-ext-ip-source',
                                dest='ekey_ext_ip_source',
                                type=str,
                                required=False,
                                default='http://ifconfig.io/ip',
                                help='Set source URI from which to retrieve external IP address (default: http://ifconfig.io/ip)')

    def generate(self):

        assert self.args.ekey_ext_ip is not None

        self.ekey_val = self.args.ekey_ext_ip.encode()
        self.source = self.args.ekey_ext_ip_source

        return {
            'val' : self.ekey_val,
            'source' : self.source,
            'len' : len(self.ekey_val),
            'options' : self.args.__dict__,
        }
