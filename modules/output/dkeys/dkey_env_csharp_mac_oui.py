import json
import config

from base.output.dkey.csharp_dkey import CSharpDKey

class MDKey(CSharpDKey):

    def __init__(self):

        if config.debug:
            print('calling MDKey.__init__()')

        super().__init__()

        self.name = 'dkey_env_csharp_mac_oui'
        self.mtype = 'dkey'
        self.author = '@s0lst1c3'
        self.description = 'Environmental key derived from MAC address OUI'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]
        self.compatible_imodules = [

            'ekey_env_mac_oui',
        ]

        self.functions = []
        self._vars = [

            'nic',
            'n',
        ]
        self.comments = []
        self.whitespaces = []

        self.imports = [

            'System',
            'System.IO',
            'System.Net.NetworkInformation',
        ]

        self.template = 'dkeys/dkey_env_csharp_mac_oui.cs'

        self.func_name = 'derive'
        self.class_name = 'DKeyCSharpMacOUI'

        self.mutate_func_name = True
        self.mutate_class_name = True
