from base.output.output_modules.output_module import OutputModule

from jinja2 import Environment, FileSystemLoader

class ShellcodeRunner(OutputModule):

    def __init__(self):

        self.rendered_inner_shell = None
        self.rendered_imports = None

        self.required_attrs([
            'mutate_entrypoint',
        ])

        super().__init__()

    def render(self):

        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(self.template)
        return template.render(func_name = self.func_name,
                            class_name = self.class_name,
                            var_mappings=self.var_mappings,
                            v=self.var_mappings,
                            special= self.special,
                            whitespace_mappings=self.whitespace_mappings,
                            comment_mappings=self.comment_mappings,
                            rendered_imports=self.rendered_imports,
                            rendered_inner_shell=self.rendered_inner_shell)
