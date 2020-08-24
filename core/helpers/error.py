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

def pnoselect(mtype):

    perror(f'No {mtype} selected.')
    print()
    perror(f'You must specify a module of type {mtype} using the --{mtype} flag.')
    print()
    perror(f'Run the following command for a list of available {mtype} modules:')
    print()
    if mtype in ['premodules', 'postmodules', 'ekeys', 'dkeys']:
        print(f'    python dropengine.py --list {mtype}')
    else:
        print(f'    python dropengine.py --list {mtype}s')
    print()
    pexit('Aborting.')

def picompat(mod1, mod2, mtype):
    print()
    perror(f'[!] Error: module "{mod1}" incompatible with interface "{mod2}"')
    print()
    perror(f'Run the following command for a list of modules compatible with interface "{mod2}":')
    print()
    print(f'    python dropengine.py --list --compatible --interface {mod2}')
    print()

    perror(f'Run the following command for a list of interfaces compatible with module "{mod1}":')
    print()
    print(f'    python dropengine.py --list interfaces --compatible --{mtype} {mod1}')
    print()
    pexit('Aborting.')

def pcompat(mod1, mod2, mtype):
    print()
    perror(f'[!] Error: module "{mod2}" incompatible with module "{mod1}"')
    print()
    perror(f'Run the following command for a list of modules compatible with module "{mod1}":')
    print()
    print(f'    python dropengine.py --list --compatible --{mtype} {mod1}')
    print()
    pexit('Aborting.')

def pmeth_missing(name, meth):
    pexit(f'Error: module {name} must have method: self.{meth}')

def check_attr(self, attr):
    if not hasattr(self, attr):
        pattr_missing(type(self).__name__, attr)
