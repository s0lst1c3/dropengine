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

        self.name = 'ekey_env_ad_domain_name'
        self.mtype = 'ekey'
        self.author = '@s0lst1c3'
        self.description = 'Environmental key derived from AD domain name'
        self.compatible_omodule = [
        ]

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.compatible_dkeys = [
            'dkey_csharp_env_ad_domain_name',
        ]

    def add_arguments(self):

        self.parser.add_argument('--ekey-ad-domain',
                                dest='ekey_ad_domain',
                                type=str,
                                required=False,
                                default=None,
                                help='Set encryption key to AD domain name')

    def generate(self):

        assert self.args.ekey_ad_domain is not None

        self.ekey_val = self.args.ekey_ad_domain.encode()

        return {
            'val' : self.ekey_val,
            'len' : len(self.ekey_val),
            'options' : self.args.__dict__,
        }
