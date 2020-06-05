import json
import config

from base.output.dkey.csharp_dkey import CSharpDKey

class MDKey(CSharpDKey):

    def __init__(self):

        if config.debug:
            print('calling MDKey.__init__()')

        super().__init__()

        self.name = 'dkey_env_csharp_moonphase'
        self.mtype = 'dkey'
        self.author = '@s0lst1c3'
        self.description = 'Environmental key derived from username'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]
        self.compatible_imodules = [

            'ekey_env_moonphase',
        ]

        self.functions = []
        self._vars = [

            'year',
            'month',
            'day',
            'g',
            'e',
        ]
        self.comments = []
        self.whitespaces = []

        self.imports = [

            'System',
            'System.IO',
        ]

        self.template = 'dkeys/dkey_env_csharp_moonphase.cs'

        self.func_name = 'derive'
        self.class_name = 'DKeyCSharpMoonphase'

        self.mutate_func_name = True
        self.mutate_class_name = True
