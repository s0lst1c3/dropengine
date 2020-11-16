import config

from base.output.postmodule.csharp_postmodule import CSharpPostModule

class MPostModule(CSharpPostModule):

    def __init__(self):

        if config.debug:
            print('calling MPostModule.__init__()')

        super().__init__()

        self.functions = []
        self.comments = []
        self.whitespaces = []

        self.mtype = 'postmodule'

        self.name = '{{ name }}'
        self.author = '{{ author }}'
        self.description = '{{ description }}'

        self.compatible_interfaces = [

            {% for c in compatible_interfaces %}
            '{{ c }}',
            {% endfor %}
        ]
        self.compatible_imodules = [

            {% for c in compatible_xmodules %}
            '{{ c }}',
            {% endfor %}
        ]

        self._vars = [

            {% for v in _vars %}
            '{{ v }}',
            {% endfor %}
        ]

        self.imports = [

            {% for i in imports %}
            '{{ i }}',
            {% endfor %}
        ]

        self.template = '{{ template_path }}'

        self.func_name = '{{ func_name }}'
        self.class_name = '{{ class_name }}'

        self.mutate_class_name = True
        self.mutate_func_name = True
