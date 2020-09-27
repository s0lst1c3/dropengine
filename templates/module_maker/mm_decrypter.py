import json
import config

from base.output.decrypter.csharp_decrypter import CSharpDecrypter

class MDecrypter(CSharpDecrypter):

    def __init__(self):

        if config.debug:
            print('calling MDecrypter.__init__()')
        super().__init__()

        self.name = '{{ name }}'
        self.mtype = 'decrypter'
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

        self.functions = []
        self._vars = [

            {% for v in _vars %}
            '{{ v }}',
            {% endfor %}
        ]
        self.comments = []
        self.whitespaces = []

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
