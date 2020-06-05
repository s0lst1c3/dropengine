import logging
import os

from importlib import util
from core.module_store import ModuleStore

class Loader:

    def __init__(self, mtype=None, paths=[]):

        assert mtype is not None

        self.type = mtype
        self.paths = paths
        self.loaded = []

        self.get_loadables()

    def load(self, path):

        spec = util.spec_from_file_location(self.type, path)
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def get_loadables(self):

        self.loaded = []

        for path in self.paths:
            for module in os.listdir(path):
                if module.endswith('.py') and not module.startswith('--'):
                    try:

                        m = self.load(os.path.join(path, module))

                        # interface - public
                        if self.type == 'MRunnerInterface':

                            module = m.MRunnerInterface()
                            module.validate()
                            self.loaded.append(module)

                        # input - public
                        elif self.type == 'MEKey':

                            module = m.MEKey()
                            module.validate()
                            self.loaded.append(module)

                        elif self.type == 'MCrypter':

                            module = m.MCrypter()
                            module.validate()
                            self.loaded.append(module)

                        # output - public 
                        elif self.type == 'MExecutor':

                            module = m.MExecutor()
                            module.validate()
                            self.loaded.append(module)

                        elif self.type == 'MPostModule':

                            module = m.MPostModule()
                            module.validate()
                            self.loaded.append(module)

                        elif self.type == 'MPreModule':

                            module = m.MPreModule()
                            module.validate()
                            self.loaded.append(module)

                        elif self.type == 'MMutator':

                            module = m.MMutator()
                            module.validate()
                            self.loaded.append(module)

                        # output - private
                        elif self.type == 'MDKey':
                            self.loaded.append(m.MDKey())

                            module = m.MDKey()
                            module.validate()
                            self.loaded.append(module)

                        elif self.type == 'MDecrypter':

                            module = m.MDecrypter()
                            module.validate()
                            self.loaded.append(module)

                        elif self.type == 'MRunner':

                            module = m.MRunner()
                            module.validate()
                            self.loaded.append(module)

                    except Exception as e:
                        print(e)
                        logging.error('Module loading did not work')
        logging.debug(f'Loaded {len(self.loaded)} {self.type}(s)')
        return ModuleStore(modules=self.loaded)
