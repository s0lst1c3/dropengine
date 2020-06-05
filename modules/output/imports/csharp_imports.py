import config

from base.output.imports.imports import Imports
class CSharpImports(Imports):


    def __init__(self):

        super().__init__()

        if config.debug:
            print('calling MExecutor.__init__()')

        super().__init__()

        self.name = 'csharp_imports'
        self.mtype = 'imports'
        self.author = '@s0lst1c3'
        self.description = 'Imports written in csharp'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.functions = []
        self._vars = []
        self.comments = []
        self.whitespaces = []

        self.template = f'imports/{self.name}.cs'

