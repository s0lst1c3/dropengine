import config

from base.output.output_modules.csharp_output_module import CSharpOutputModule
from base.output.runner.runner import ShellcodeRunner

class CSharpShellcodeRunner(CSharpOutputModule, ShellcodeRunner):

    def __init__(self):

        if config.debug:
            print('calling CSharpDecrypter.__init__()')
        
        self.required_attrs([
            'mutate_class_name',
        ])
