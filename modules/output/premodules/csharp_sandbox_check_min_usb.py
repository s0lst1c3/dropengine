from base.output.premodule.csharp_premodule import CSharpPreModule

class MPreModule(CSharpPreModule):

    def __init__(self):

        super().__init__()

        self.name = 'csharp_sandbox_check_min_usb'
        self.mtype = 'premodule'
        self.author = '@s0lst1c3'
        self.description = 'Sandbox detection via minimum number of USB devices ever used'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.functions = []
        self._vars = [

        ]
        self.comments = []
        self.whitespaces = []

        self.imports = [

            'System',
            'System.IO',
            'Microsoft.Win32',
        ]

        self.template = 'premodules/csharp_sandbox_check_min_usb.cs'

        self.func_name = 'run'
        self.class_name = 'SandboxCheckMinUSB'

        self.mutate_class_name = True
        self.mutate_func_name = True
