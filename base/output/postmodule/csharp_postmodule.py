from base.output.postmodule.postmodule import PostModule
from base.output.output_modules.csharp_output_module import CSharpOutputModule

class CSharpPostModule(CSharpOutputModule, PostModule):

    def __init__(self):
        super().__init__()
