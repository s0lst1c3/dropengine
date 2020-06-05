import json
import inspect
import config

from jinja2 import Environment, FileSystemLoader

from core.helpers.error import pattr_missing
from core.helpers.error import pmeth_missing
from core.helpers.error import check_attr

from base.de_component import DEComponent
from base.has_cli import HasCLI

class OutputModule(HasCLI, DEComponent):


    def __init__(self):

        if config.debug:
            print('calling OutputModule.__init__()')
        
        self.function_mappings = {}
        self.var_mappings = {}
        self.comment_mappings = {}
        self.whitespace_mappings = {}
        self.special = {}

        self.required_attrs([

            'compatible_interfaces',
            'functions',
            'func_name',
            '_vars',
            'comments',
            'whitespaces',
            'template',
            'imports',
            'mutate_func_name',
        ])


        super().__init__()

    def mutate(self, mutator):

        if self.mutate_func_name:
            self.func_name = mutator.transform(self.func_name)

        for var in self._vars:
            self.var_mappings[var] = mutator.transform(var)

        for function in self.functions:
            self.function_mappings[function] = mutator.transform(function)

        for whitespace in self.whitespaces:
            self.whitespace_mappings[whitespace] = mutator.transform(whitespace)

        for comment in self.comments:
            self.comment_mappings[comment] = mutator.transform(comment)

    def render(self):

        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(self.template)

        return template.render(special=self.special,
                               func_name=self.func_name,
                               function_mappings=self.function_mappings,
                               var_mappings=self.var_mappings,
                               v=self.var_mappings,
                               comment_mappings=self.comment_mappings,
                               whitespace_mappings=self.whitespace_mappings)
