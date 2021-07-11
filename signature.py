from hashlib import blake2b
from hmac import compare_digest

class criptsignature():

    __SECRET_KEY = b'0g0e0n0e0r0a0t0e0d00s0e0r0v0e0r0s0e0c0r0e0t0k0e0y0'
    __SECRET_KEY_3SHA256 = "34d856eda9e72cc4d8b5a673d2edae2940064417ea7db5cf98e083e6b588df6b"
    __AUTH_SIZE = 64
    __total_contas = 0
    

    def __encrypekey(self):

        secret = list(str(self.__SECRET_KEY))
        secret_sha256 = list(self.__SECRET_KEY_3SHA256)
        hassh = secret+secret_sha256
        secret_sha256.extend(hassh)
        del secret_sha256[0:120]
        datakey =(secret_sha256)
        datakey = ''.join(datakey)
        key = datakey.encode("utf8")
        return key


    def signature(self,msg):
        """[summary]

        Args:
            msg ([type]): [description]

        Returns:
            [bytes]: [description]
        """
        key= self.__encrypekey()
        calcule = blake2b(digest_size=self.__AUTH_SIZE, key=key)
        calcule.update(msg)
        return calcule.hexdigest().encode('utf-8')


    def verify_signature(self,msg, sig):
        """[Verify]

        Args:
            msg ([bytes]): [description]
            sig ([bytes]): [description]

        Returns:
            [bool]: [description]
        """
        msg_sig = self.signature(msg)
        return compare_digest(msg_sig,sig)

if __name__ == '__main__':
    
    msg= b"Mensagem para assinatura RSA"
    tess = criptsignature()
    tes =tess.signature(msg)
    
    msgg= b"Mensagem para assinatura RSA"
    v = tess.verify_signature(msgg,tes)
    print(v)