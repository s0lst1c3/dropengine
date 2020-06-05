from base.output.premodule.csharp_premodule import CSharpPreModule

class MPreModule(CSharpPreModule):

    def __init__(self):

        super().__init__()

        self.name = 'csharp_amsi_bypass_scanbuf'
        self.mtype = 'premodule'
        self.author = '@s0lst1c3'
        self.description = 'Bypass AMSI using RastaMouse\'s AmsiScanBuffer patch technique'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.functions = []
        self._vars = [

            'a',
            'b',
            'c',
            'd',
            'v',
            'e',
            'x86',
            'x64',
            'Win32',
            'is64Bit',
            'e',
            'patch',
            'addr',
            'oldProtect',
            'lib',
            'PatchAmsi',
            'foo',
            'bar',
            'baz',
            'bop',
            'burt',
            'bing',
            'boop',

        ]
        self.comments = []
        self.whitespaces = []

        self.imports = [

            'System',
            'System.Runtime.InteropServices',

        ]

        self.template = 'premodules/csharp_amsi_bypass_scanbuf.cs'

        self.func_name = 'Bypass'
        self.class_name = 'Amsi'

        self.mutate_class_name = True
        self.mutate_func_name = True
