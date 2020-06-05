import config

from base.output.output_modules.output_module import OutputModule

class Executor(OutputModule):

    def __init__(self):

        if config.debug:
            print('calling Executor.__init__()')
        super().__init__()
