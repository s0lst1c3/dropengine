import json
import config

from base.output.dkey.csharp_dkey import CSharpDKey

class MDKey(CSharpDKey):

    def __init__(self):

        if config.debug:
            print('calling MDKey.__init__()')

        super().__init__()

        self.name = 'dkey_csharp_env_ad_domain_name'
        self.mtype = 'dkey'
        self.author = '@s0lst1c3'
        self.description = 'Environmental key derived from AD domain name'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]
        self.compatible_imodules = [

            'ekey_env_ad_domain_name',
        ]

        self.functions = []
        self._vars = [
        ]
        self.comments = []
        self.whitespaces = []

        self.imports = [


            'System.DirectoryServices',
        ]

        self.template = 'dkeys/dkey_csharp_env_ad_domain_name.cs'

        self.func_name = 'derive'
        self.class_name = 'DKeyCSharpADDomainName'

        self.mutate_func_name = True
        self.mutate_class_name = True
