import json
import config

from base.output.executor.csharp_executor import CSharpExecutor

class MExecutor(CSharpExecutor):

    def __init__(self):

        if config.debug:
            print('calling MExecutor.__init__()')
        super().__init__()

        self.name = 'executor_csharp_virtual_alloc_thread'
        self.mtype = 'executor'
        self.author = '@s0lst1c3'
        self.description = 'Copies payload into memory Allocated using VirtualAlloc, passes payload address to VirtualProtect to make it executable, and runs the payload in a local thread.'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]

        self.functions = []
        self._vars = [
            'shellcode',
            'oldprotect',
            'module',
            'valloc',
            'cthread',
            'vfree',
            'vprotect',
            'waitforso',
            'chandle',
            'pvalloc',
            'pvfree',
            'pcthread',
            'pvprotect', 
            'pwaitforso',
            'pchandle',
            'func_addr',
            'info', 
            'pinfo',
            'hThread',
            'thread_id',
        ]
        self.comments = []
        self.whitespaces = []

        self.imports = []

        self.template = 'executors/executor_csharp_virtual_alloc_thread.cs'

        self.func_name = 'execute_shellcode'
        self.class_name = 'Executzors'

        self.mutate_func_name = True
        self.mutate_class_name = True
