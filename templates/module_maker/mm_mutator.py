import config

from base.mutator.mutator import Mutator

class MMutator(Mutator):

    def __init__(self):

        if config.debug:
            print('calling MMutator.__init__()')

        super().__init__()

        self.name = '{{ name }}'
        self.mtype = 'mutator'
        self.author = '{{ author }}'
        self.description = '{{ description }}'

        self.compatible_interfaces = [

            {% for c in compatible_interfaces %}
            '{{ c }}',
            {% endfor %}
        ]

    def transform(self, x):

        ## add transformation code here

        return x

