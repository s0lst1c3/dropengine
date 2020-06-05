import json
import config

from base.output.dkey.csharp_dkey import CSharpDKey

class MDKey(CSharpDKey):

    def __init__(self):

        if config.debug:
            print('calling MDKey.__init__()')

        super().__init__()

        self.name = 'dkey_csharp_static'
        self.mtype = 'dkey'
        self.author = '@s0lst1c3'
        self.description = 'Static dkey for testing purposes'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]
        self.compatible_imodules = [

            'ekey_static',
        ]

        self.functions = []
        self._vars = [

            'dkey',
        ]
        self.comments = []
        self.whitespaces = []

        self.imports = []

        self.template = 'dkeys/dkey_csharp_static.cs'

        self.func_name = 'derive'
        self.class_name = 'DKeyCSharpStaticTestDummy'

        self.mutate_func_name = True
        self.mutate_class_name = True
