from base.output.output_modules.csharp_output_module import CSharpOutputModule
from base.output.payload_main.payload_main import PayloadMain

class CSharpPayloadMain(PayloadMain, CSharpOutputModule):

    def __init__(self):
        
        super().__init__()

        self.name = 'csharp_payload_main'
        self.mtype = 'payload_main'
        self.author = '@s0lst1c3'
        self.description = 'Payload main written in csharp'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.functions = []
        self._vars = [
            'shellcode',
            'dkey',
            'pre',
            'dkey_str',

        ]
        self.comments = []
        self.whitespaces = []

        self.imports = []

        self.template = f'payload_main/{self.name}.cs'

        self.func_name = 'payload_main'
        self.class_name = 'PayloadMain'

        self.mutate_class_name = True
        self.mutate_func_name = True
