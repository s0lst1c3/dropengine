import config

from base.output.runner.runner import ShellcodeRunner

class MRunner(ShellcodeRunner):

    def __init__(self):

        if config.debug:
            print('calling MRunner.__init__()')

        super().__init__()

        self.name = 'csharp_installutil'
        self.mtype = 'runner'
        self.author = '@s0lst1c3'
        self.description = 'CSharp installUtil shellcode runner (uninstall)'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.functions = []
        self._vars = []
        self.comments = []
        self.whitespaces = []

        self.imports = [

            'System',
            'System.Diagnostics',
            'System.Reflection',
            'System.Configuration.Install',
            'System.Net',
            'System.Net.Sockets',
            'System.Runtime.InteropServices',
        ]

        self.template = 'runners/installUtil.cs'

        self.mutate_class = False
        self.mutate_entrypoint = False

        self.class_name = 'Sample'
        self.func_name = 'Uninstall'

        self.mutate_class_name = False
        self.mutate_func_name = False
