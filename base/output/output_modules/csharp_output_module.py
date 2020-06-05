import config

from base.output.output_modules.output_module import OutputModule

class CSharpOutputModule(OutputModule):

    def __init__(self):

        if config.debug:
            print('calling HasCLI.__init__()')

        self.required_attrs([
                    'class_name',
                    'mutate_class_name',
        ])

        super().__init__()


    def render(self):

        self.special['class_name'] = self.class_name
        return super().render()

    def mutate(self, mutator):

        if self.mutate_class_name:
            self.class_name = mutator.transform(self.class_name)

        super().mutate(mutator)
