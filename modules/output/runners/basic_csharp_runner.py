import config

from base.output.runner.runner import ShellcodeRunner

class MRunner(ShellcodeRunner):

    def __init__(self):

        if config.debug:
            print('calling MRunner.__init__()')

        super().__init__()

        self.name = 'basic_csharp_runner'
        self.mtype = 'runner'
        self.author = '@s0lst1c3'
        self.description = 'Basic CSharp shellcode runner'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.functions = []
        self._vars = []
        self.comments = []
        self.whitespaces = []

        self.imports = []

        self.template = 'runners/basic_csharp_runner.cs'

        self.mutate_class = False
        self.mutate_entrypoint = False

        self.class_name = 'Program'
        self.func_name = 'Main'

        self.mutate_class_name = False
        self.mutate_func_name = False
