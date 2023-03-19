from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding


class Usuario:
    def __init__(self):
        self.chave_privada = rsa.generate_private_key(public_exponent=65537,
                                                      key_size=2048)
        self.chave_publica = self.chave_privada.public_key()

    def assinar(self, msg_):
        assinatura_ = self.chave_privada.sign(msg_,
                                              padding.PSS(
                                                  mgf=padding.MGF1(hashes.SHA256()),
                                                  salt_length=padding.PSS.MAX_LENGTH
                                              ),
                                              hashes.SHA256())
        return assinatura_

    def decriptografar(self, msg_criptografada_):
        mensagem_plana_ = self.chave_privada.decrypt(msg_criptografada_,
                                                     padding.OAEP(
                                                         mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                         algorithm=hashes.SHA256(),
                                                         label=None))
        return mensagem_plana_

    @staticmethod
    def verificar(assinatura_, msg_, chave_publica):
        try:
            chave_publica.verify(assinatura_,
                                 msg_,
                                 padding.PSS(
                                     mgf=padding.MGF1(hashes.SHA256()),
                                     salt_length=padding.PSS.MAX_LENGTH
                                 ),
                                 hashes.SHA256())
            return True
        except InvalidSignature:
            return False

    @staticmethod
    def criptografar(msg_plana_, chave_publica):
        msg_cifrada_ = chave_publica.encrypt(msg_plana_,
                                             padding.OAEP(
                                                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                 algorithm=hashes.SHA256(),
                                                 label=None))
        return msg_cifrada_


if __name__ == '__main__':
    # Criando um usuário com chaves publica e privada
    hugo = Usuario()

    # Criando uma mensagem que precisa ser assinada
    mensagem = b"Uma mensagem que precisa ser assinada"

    # Usuário hugo assinando a mensagem

    # Verificando a assinatura

    # Criptografando uma mensagem secreta

    # Decifrando a mensagem secreta
