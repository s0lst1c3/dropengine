import config

from base.output.inner_shell.inner_shell import InnerShell

class CSharpInnerShell(InnerShell):

    def __init__(self):

        if config.debug:
            print('calling MExecutor.__init__()')

        super().__init__()

        self.name = 'csharp_inner_shell'
        self.mtype = 'inner_shell'
        self.author = '@s0lst1c3'
        self.description = 'Inner shell written in csharp'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.functions = []
        self._vars = []
        self.comments = []
        self.whitespaces = []

        self.imports = []

        self.template = f'inner_shell/{self.name}.cs'

        self.func_name = 'inner_shell'

        self.mutate_func_name = True
        self.mutate_class_name = True
