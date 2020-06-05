from base.output.premodule.premodule import PreModule
from base.output.output_modules.csharp_output_module import CSharpOutputModule

class CSharpPreModule(CSharpOutputModule, PreModule):

    def __init__(self):
        super().__init__()
