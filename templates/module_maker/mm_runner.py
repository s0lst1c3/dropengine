import config

from base.output.runner.runner import ShellcodeRunner

class MRunner(ShellcodeRunner):

    def __init__(self):

        if config.debug:
            print('calling MRunner.__init__()')

        super().__init__()

        self.functions = []
        self.comments = []
        self.whitespaces = []

        self.mtype = 'runner'

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


        self.class_name = 'Program'
        self.func_name = 'Main'

        self.mutate_class_name = False
        self.mutate_func_name = False
