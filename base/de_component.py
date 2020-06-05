import config

from core.helpers.error import check_attr

class DEComponent(object):

    def __init__(self):
        
        if config.debug:

            print('calling DEComponent.__init__()')

        self.required_attrs([ 
            'name',
            'mtype',
            'author',
            'description',
        ])

    def set_option(self, key, val):

        self.option[key] = val

    def set_options(self, options):

        self.options = options

    def validate(self):

        for ra in self._required_attrs:
            check_attr(self, ra)

    def required_attrs(self, attrs):

        if hasattr(self, '_required_attrs'):
            self._required_attrs += attrs
        else:
            self._required_attrs = attrs

    def __str__(self):
        return f'{self.mtype} - {self.name}'

    def __getitem__(self, key):

        for k,v in self.options.items():
            if k.lower() == key.lower():
                return self.options[k]['Value']

    def __setitem__(self, key, value):

        for k,v in self.options.items():
            if k.lower() == key.lower():
                self.options[k]['Value'] = value
