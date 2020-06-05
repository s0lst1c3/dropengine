import config

from base.input.input_module.input_module import InputModule

class Crypter(InputModule):

    def __init__(self):

        if config.debug:
            print('calling Crypter.__init__()')
        super().__init__()

        self.ekey = None
        self.pt = None
        self.ct = None

    def validate(self):

        if not hasattr(self, 'compatible_decrypters'):
            raise Exception('Crypter modules requires attribute: self.compatible_decrypter')

        if not hasattr(self, 'encrypt'):
            raise Exception('Crypter modules requires method: self.encrypt')
        
        super().validate()

    def encrypt(self):
        raise Exception('encrypt method not implemented')


    def ekey(self, ekey=None):
        if ekey is not None:
            self.ekey = ekey
        return self.ekey

    def pt(self, pt=None):
        if pt is not None:
            self.pt = pt
        return self.pt

    def ct(self, ct=None):
        if ct is not None:
            self.ct = ct
        return self.ct

    def iv(self, iv=None):
        if iv is not None:
            self.iv = iv
        return self.iv
