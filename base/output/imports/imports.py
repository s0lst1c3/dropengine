from jinja2 import Environment, FileSystemLoader

from base.output.output_modules.output_module import OutputModule

class Imports(OutputModule):

    def __init__(self):

        self.imports = set([])

        super().__init__()

    def add(self, imports):

        if type(imports) == set or type(imports) == list:

            for i in imports:
                self.imports.add(i)

        elif type(imports) == str:

            self.imports.add(imports)

        else:
            raise ValueError('Invalid parameter type'+str(imports))

    def render(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(self.template)
        return template.render(imports=list(self.imports))
