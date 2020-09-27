import base64
import hashlib
import config
import core.helpers.crypto

from base.input.crypter.crypter import Crypter

from Crypto.Cipher import AES

# TODO: NEED TO FILL OUT DKEY FUNCTIONS / TEMPLATE RENDERING BECAUSE I FORGOT

class MCrypter(Crypter):

    def __init__(self):

        if config.debug:
            print('calling MCrypter.__init__()')

        super().__init__()

        self.name = '{{ name }}'
        self.mtype = 'crypter'
        self.author = '{{ author }}'
        self.description = '{{ description }}'

        self.compatible_interfaces = [

            {% for c in compatible_interfaces %}
            '{{ c }}',
            {% endfor %}
        ]

        self.compatible_omodules = [

            {% for c in compatible_xmodules %}
            '{{ c }}',
            {% endfor %}
        ]

    def add_arguments(self):
        #self.parser.add_argument(...
        pass

    def encrypt(self, pt, ekey_val):

        if type(pt) != bytes:
            pt = pt.encode()

        # encryption happens here
        return {

            'pt' : pt,
            'ekey' : ekey_val,
            #'ct' : ct,
            'options' : self.args.__dict__,
        }
