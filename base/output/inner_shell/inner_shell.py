from base.output.output_modules.output_module import OutputModule

from jinja2 import Environment, FileSystemLoader

class InnerShell(OutputModule):

    def __init__(self):

        #self.rendered_dkey = None
        self.rendered_dkeys = []
        self.rendered_decrypter = None
        self.rendered_executor = None
        self.rendered_payload_main = None
        self.rendered_pre_modules = []
        self.rendered_post_modules = []
        #self.rendered_imports = None

        super().__init__()

    def render(self):

        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(self.template)
        #return template.render(rendered_imports=self.rendered_imports,
        #    rendered_dkey=self.rendered_dkey,
        #    rendered_decrypter=self.rendered_decrypter,
        #    rendered_executor=self.rendered_executor,
        #    rendered_payload_main=self.rendered_payload_main,
        #    rendered_pre_modules=self.rendered_pre_modules,
        #    rendered_post_modules=self.rendered_post_modules)
        return template.render(rendered_dkeys=self.rendered_dkeys,
            rendered_decrypter=self.rendered_decrypter,
            rendered_executor=self.rendered_executor,
            rendered_payload_main=self.rendered_payload_main,
            rendered_pre_modules=self.rendered_pre_modules,
            rendered_post_modules=self.rendered_post_modules)
