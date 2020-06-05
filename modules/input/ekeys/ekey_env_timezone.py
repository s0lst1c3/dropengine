import base64
import config
import core.helpers.crypto

from base.input.ekey.ekey import EKey


class MEKey(EKey):

    def __init__(self):

        if config.debug:
            print('calling MEKey.__init__()')

        super().__init__()

        self.name = 'ekey_env_timezone'
        self.mtype = 'ekey'
        self.author = '@s0lst1c3'
        self.description = 'Environmental key derived from current timezone'
        self.compatible_omodules = [

            'dkey_env_csharp_timezone',
        ]

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

    def add_arguments(self):

        self.parser.add_argument('--ekey-utc-offset',
                                dest='ekey_timezone',
                                type=str,
                                required=False,
                                default=None,
                                help='Select timezone via UTC offset')

    def generate(self):

        assert self.args.ekey_timezone is not None

        self.ekey_val = self.args.ekey_timezone.encode()

        return {
            'val' : self.ekey_val,
            'len' : len(self.ekey_val),
            'options' : self.args.__dict__,
        }
