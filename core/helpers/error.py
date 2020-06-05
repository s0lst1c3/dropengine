import sys
import inspect
from termcolor import colored, cprint

def perror(msg):
    cprint(f'[!] {msg}', 'red', attrs=['bold'], file=sys.stderr)

def praise(msg):
    perror(msg)
    raise Exception(msg)

def pexit(msg):
    perror(msg)
    sys.exit(1)

def pattr_missing(name, attr):
    pexit(f'Error: module {name} must have attribute: self.{attr}')

def pmeth_missing(name, meth):
    pexit(f'Error: module {name} must have method: self.{meth}')

def check_attr(self, attr):
    if not hasattr(self, attr):
        pattr_missing(type(self).__name__, attr)
