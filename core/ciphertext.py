class Ciphertext():

    def __init__(self,
                 etype='',
                 pt='',
                 ct='',
                 ekey='',
                 padded_pt='',
                 iv='',
                 pad_char='',
                 pad_len=None,
                 oformat=None):

        self.etype = etype
        self.pt = pt
        self.ct = ct
        self.ct_len = len(ct)
        self.ekey = ekey
        self.ekey_len = len(ekey)
        self.padded_pt = padded_pt
        self.iv = iv
        self.pad_char = pad_char
        self.pad_len = pad_len

        assert oformat is not None

        self.oformat = oformat

    def __str__(self):

        return_me = []

        #if self.pt is not None:

        #    return_me.append('\n'.join([
        #        'plaintext:',
        #        '',
        #        self.oformat.render(self.pt),
        #        '',
        #    ]))


        if self.pad_len is not None:

            return_me.append('\n'.join([
                'pad length',
                '',
                str(hex(self.pad_len)),
                '',
            ]))



        if self.ct_len is not None:

            return_me.append('\n'.join([
                'ct length',
                '',
                str(hex(self.ct_len)),
                '',
            ]))

        if self.ekey_len is not None:

            return_me.append('\n'.join([
                'ekey length',
                '',
                str(hex(self.ekey_len)),
                '',
            ]))

        if self.iv is not None:

            return_me.append('\n'.join([
                'byte[] iv =',
                '',
                self.oformat.render(self.iv),
                '',
            ]))

        if self.ekey is not None:

            return_me.append('\n'.join([
                'byte[] ekey =',
                '',
                self.oformat.render(self.ekey),
                '',
            ]))

        if self.ct is not None:

            return_me.append('\n'.join([
                'byte[] shellcode = ',
                '',
                self.oformat.render(self.ct),
                '',
            ]))

        #if self.padded_pt is not None:

        #    return_me.append('\n'.join([
        #        'padded plaintext:',
        #        '',
        #        self.oformat.render(self.padded_pt),
        #        '',
        #    ]))


        #if self.pad_char is not None:

        #    return_me.append('\n'.join([
        #        'pad char:',
        #        '',
        #        self.oformat.render(self.pad_char),
        #        '',
        #    ]))

        return '\n'.join(return_me)
