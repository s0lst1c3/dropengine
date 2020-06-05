import config

from base.output.runner.runner import ShellcodeRunner

class MRunner(ShellcodeRunner):

    def __init__(self):

        if config.debug:
            print('calling MRunner.__init__()')

        super().__init__()

        self.name = 'msbuild_csharp_runner'
        self.mtype = 'runner'
        self.author = '@s0lst1c3'
        self.description = 'Basic CSharp shellcode runner'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.functions = []
        self._vars = [

            'ShellCodeInjector',
            'FragmentExample',
        ]
        self.comments = []
        self.whitespaces = []

        self.imports = [

            'System',
            'Microsoft.Build.Framework',
            'Microsoft.Build.Utilities',
            'System.Net',
            'System.Net.Sockets',
            'System.Runtime.InteropServices',
            'System.Text',
            'System.IO',
        ]

        self.template = 'runners/msbuild_csharp_runner.csproj'

        self.mutate_class = False
        self.mutate_entrypoint = False

        self.class_name = 'FragmentExample'
        self.func_name = 'Execute'

        self.mutate_class_name = False
        self.mutate_func_name = False
