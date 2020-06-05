import config

from base.output.postmodule.csharp_postmodule import CSharpPostModule

class MPostModule(CSharpPostModule):

    def __init__(self):

        if config.debug:
            print('calling MPostModule.__init__()')

        super().__init__()

        self.name = 'csharp_post_cmd_del_from_disk'
        self.mtype = 'postmodule'
        self.author = '@s0lst1c3'
        self.description = 'Uses the cmd to delete file after execution'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.functions = []
        self._vars = [
            'process',
        ]

        self.comments = []
        self.whitespaces = []

        self.imports = [

            'System',
            'System.Diagnostics',
        ]

        self.template = 'postmodules/csharp_post_cmd_del_from_disk.cs'

        self.func_name = 'delete_from_disk'
        self.class_name = 'DeleteFromDisk'

        self.mutate_class_name = True
        self.mutate_func_name = True
