import base64
import config
import core.helpers.crypto

from base.input.ekey.ekey import EKey


class MEKey(EKey):

    def __init__(self):

        if config.debug:
            print('calling MEKey.__init__()')

        super().__init__()

        self.name = 'ekey_env_moonphase'
        self.mtype = 'ekey'
        self.author = '@s0lst1c3'
        self.description = 'Environmental key derived from the phase of the moon.'
        self.compatible_omodules = [

            'dkey_env_csharp_moonphase',
        ]

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

    def add_arguments(self):

        self.parser.add_argument('--moonphase',
                                dest='moonphase',
                                type=str,
                                required=False,
                                choices=[

                                    'New Moon',
                                    'Waxing Crescent',
                                    'First Quarter',
                                    'Waxing Gibbous',
                                    'Full Moon',
                                    'Waning Gibbouos',
                                    'Third Quarter',
                                    'Waning Crescent',
                                ],
                                default=None,
                                help='Set encryption key to moon phase')


    def generate(self):

        assert self.args.moonphase is not None

        self.ekey_val = self.args.moonphase.encode()

        return {
            'val' : self.ekey_val,
            'len' : len(self.ekey_val),
            'options' : self.args.__dict__,
        }
