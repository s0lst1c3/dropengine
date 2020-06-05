import base64
import config
import core.helpers.crypto

from base.input.ekey.ekey import EKey


class MEKey(EKey):

    def __init__(self):

        if config.debug:
            print('calling MEKey.__init__()')

        super().__init__()

        self.name = 'ekey_env_ext_fqdn'
        self.mtype = 'ekey'
        self.author = '@s0lst1c3'
        self.description = 'Environmental key derived from external FQDN'
        self.compatible_omodule = [
        ]

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]
        self.compatible_dkeys = [


            'dkey_env_csharp_ext_fqdn',
        ]

    def add_arguments(self):

        self.parser.add_argument('--ekey-ext-fqdn',
                                dest='ekey_ext_fqdn',
                                type=str,
                                required=False,
                                default=None,
                                help='Set encryption key to external IP address')

        self.parser.add_argument('--ekey-ext-fqdn-source',
                                dest='ekey_ext_fqdn_source',
                                type=str,
                                required=False,
                                default='http://ifconfig.io/host',
                                help='Set source URI from which to retrieve external IP address (default: http://ifconfig.io/host)')

    def generate(self):

        assert self.args.ekey_ext_fqdn is not None

        self.ekey_val = self.args.ekey_ext_fqdn.encode()
        self.source = self.args.ekey_ext_fqdn_source

        return {
            'val' : self.ekey_val,
            'source' : self.source,
            'len' : len(self.ekey_val),
            'options' : self.args.__dict__,
        }
