import json
import inspect
import config

from base.de_component import DEComponent
from base.has_cli import HasCLI

class InputModule(HasCLI, DEComponent):

    def __init__(self):

        if config.debug:
            print('calling input module init')
        super().__init__()


