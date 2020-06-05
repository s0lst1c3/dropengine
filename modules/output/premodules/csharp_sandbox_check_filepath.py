from base.output.premodule.csharp_premodule import CSharpPreModule

class MPreModule(CSharpPreModule):

    def __init__(self):

        super().__init__()

        self.name = 'csharp_sandbox_check_filepath'
        self.mtype = 'premodule'
        self.author = '@s0lst1c3'
        self.description = 'Sandbox detection via known filepaths'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.functions = []
        self._vars = [

            'fps',
            'fp',
        ]
        self.comments = []
        self.whitespaces = []

        self.imports = [

            'System',
            'System.IO',
            'Microsoft.Win32',
            'System.Collections.Generic',
        ]

        self.template = 'premodules/csharp_sandbox_check_filepath.cs'

        self.func_name = 'run'
        self.class_name = 'SandboxCheckFilepath'

        self.mutate_class_name = True
        self.mutate_func_name = True
