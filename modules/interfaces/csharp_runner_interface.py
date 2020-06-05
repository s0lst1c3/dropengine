import config

from base.interfaces.runner_interface import RunnerInterface
from modules.output.inner_shell.csharp_inner_shell import CSharpInnerShell
from modules.output.payload_main.csharp_payload_main import CSharpPayloadMain
from modules.output.imports.csharp_imports import CSharpImports
from modules.shellcode.csharp_bytes import CSharpBytesShellcode

class MRunnerInterface(RunnerInterface):

    def __init__(self):

        super().__init__()

        self.name = 'csharp_runner_interface'
        self.mtype = 'runner_interface'
        self.author = '@s0lst1c3'
        self.description = 'Interface for generating CSharp payloads'

        self.imports = CSharpImports()
        self.inner_shell = CSharpInnerShell()
        self.payload_main = CSharpPayloadMain()
        self.shellcode_format = CSharpBytesShellcode()

    def set_special(self):

        decrypter_class_name = self.dispatch['decrypter'].class_name
        executor_class_name = self.dispatch['executor'].class_name
        runner_class_name = self.dispatch['runner'].class_name
        payload_main_class_name = self.payload_main.class_name

        # set executor specials
        self.dispatch['executor'].special['executor_class_name'] = executor_class_name
        self.dispatch['executor'].special['decrypter_class_name'] = decrypter_class_name

        # set premodule specials
        for premodule in self.dispatch['premodules']:
            premodule.special['decrypter_class_name'] = decrypter_class_name
            premodule.special['executor_class_name'] = executor_class_name

        # set postmodule specials
        for postmodule in self.dispatch['postmodules']:
            postmodule.special['decrypter_class_name'] = decrypter_class_name
            postmodule.special['executor_class_name'] = executor_class_name

        self.payload_main.special['decrypter_class_name'] = decrypter_class_name
        self.payload_main.special['executor_class_name'] = executor_class_name
        #self.payload_main.special['dkey_class_name'] = dkey_class_name

        self.payload_main.special['premodule_calls'] = [
            f'{pre.class_name}.{pre.func_name}' for pre in self.dispatch['premodules']
        ]

        self.payload_main.special['postmodule_calls'] = [
            f'{post.class_name}.{post.func_name}' for post in self.dispatch['postmodules']
        ]


        if config.debug:
            for dkey in self.dispatch['dkeys']:
                print('!!!AAA!!!', dkey.class_name)
                print('!!!AAA!!!', dkey.func_name)
        self.payload_main.special['dkey_calls'] = [

            f'{dkey.class_name}.{dkey.func_name}' for dkey in self.dispatch['dkeys']
        ]


        # set runner specials
        self.dispatch['runner'].special['payload_main_class_name'] = payload_main_class_name

        super().set_special()
        

    def __str__(self):

        return f'{self.mtype} - {self.name} - {self.description}'
