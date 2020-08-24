from base.output.output_modules.output_module import OutputModule

class DKey(OutputModule):

    def __init__(self):

        super().__init__()

        self.required_attrs(['compatible_imodules'])
