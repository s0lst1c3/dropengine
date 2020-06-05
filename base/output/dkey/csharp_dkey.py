from base.output.output_modules.csharp_output_module import CSharpOutputModule
from base.output.dkey.dkey import DKey

class CSharpDKey(CSharpOutputModule, DKey):

    def __init__(self):

        super().__init__()
