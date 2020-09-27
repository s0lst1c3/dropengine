import json
import config

from base.output.executor.csharp_executor import CSharpExecutor

class MExecutor(CSharpExecutor):

    def __init__(self):

        if config.debug:
            print('calling MExecutor.__init__()')
        super().__init__()

        self.name = '{{ name }}'
        self.mtype = 'executor'
        self.author = '{{ author }}'
        self.description = '{{ description }}'


        self.functions = []
        self.comments = []
        self.whitespaces = []

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


        self.mutate_func_name = True
        self.mutate_class_name = True
