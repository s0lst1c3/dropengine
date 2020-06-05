import random
import string

from codecs import getencoder
from Crypto.Util import Padding

GLOBAL_KEYSPACE = ''.join([
    string.ascii_letters,
    string.digits,
    '{}!@#$^&()*&[]|,./?',
])

def rot13(pt):

    encoder = getencoder('rot-13')
    ct = encoder(pt)[0]
    return ct


def random_string(keyspace=None, length=None, min_len=8, max_len=16, exclude=[]):

    if keyspace is None:
        keyspace = GLOBAL_KEYSPACE

    if length is None:
        length = random.randrange(min_len, max_len)

    while True:

        retval = ''.join(random.choice(keyspace) for _ in range(length))
        if retval not in exclude:
            return retval

def random_pad_char():

    return random.choice(GLOBAL_KEYSPACE).encode()

def encryption_padding(padme, pad_char):

    return Padding.pad(padme, 16);

def random_bytes(length=None):

    if length is None:
        length = random.randrange(8,16)
    return ''.join(random.choice(string.ascii_letters) for _ in range(length)).encode()

def random_key(length=256):

    #print(length)

    return ''.join(random.choice(GLOBAL_KEYSPACE) for _ in range(length)).encode()

def print_ciphertext(ct):


    print('{\n    0x', end='')
    split_chars = ct.hex(' ').split()
    for i,c in enumerate(split_chars[:len(split_chars)-1]):

        if i % 10 == 9:
            print('{},\n    0x'.format(c), end='')
        else:
            print('{}, 0x'.format(c), end='')
    if (i+1) % 10 == 9:
        print('{}'.format(split_chars[i+1]))
    else:
        print('{}'.format(split_chars[i+1]), end='')

    print('};')
