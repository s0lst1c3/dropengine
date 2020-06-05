class Format:

    def __init__(self):

        self.name = ''
        self.author = ''
        self.description = ''
        self.options = {}

    def __getitem__(self, key):

        for k,v in self.options.items():
            if k.lower() == key.lower():
                return self.options[k]['Value']

    def __setitem__(self, key, value):

        for k,v in self.options.items():
            if k.lower() == key.lower():
                self.options[k]['Value'] = value

    def __str__(self):

        return f'Format - {self.name} - {self.description}'

