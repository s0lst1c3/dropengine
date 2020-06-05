import config

from base.output.output_modules.csharp_output_module import CSharpOutputModule
from base.output.executor.executor import Executor

class CSharpExecutor(CSharpOutputModule, Executor):

    def __init__(self):
        if config.debug:
            print('calling CSharpExecutor.__init__()')
        super().__init__()
