import config

from base.de_component import DEComponent
from core.helpers.error import pmeth_missing

class Shellcode(DEComponent):

    def __init__(self):

        if config.debug:
            print('calling Shellcode init')
        
        super().__init__()

    def render(self):
        pmeth_missing(self, 'render')
