import configparser

class SymbolINI(object):

    def __init__(self, input_file):

        self.symbols = configparser.ConfigParser(allow_no_value=True)
        self.symbols.optionxform = lambda optionstr: optionstr
        self.symbols.read(input_file)[0]
        self.input_file = input_file

    def vars(self):
        return list(self.symbols['vars'].keys())

    def method_names(self):
        return list(self.symbols['methods'].keys())

    def class_decls(self):
        return list(self.symbols['class_decls'].keys())

    def formal_params(self):
        return list(self.symbols['params'].keys())

    def delegates(self):
        return list(self.symbols['delegates'].keys())

    def imports(self):
        return list(self.symbols['imports'].keys())
