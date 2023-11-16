import pickle
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding

from utils import save_key, load_key


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
    assinatura = hugo.assinar(mensagem)

    # Verificando a assinatura
    validacao = Usuario.verificar(assinatura, mensagem, hugo.chave_publica)
    print(validacao)

    with open('arquivo.txt', 'rb') as f:
        arquivo = f.read()

    # Criptografando uma mensagem secreta
    mensagem2 = b"Nova Mensagem"
    msg_cifrada = Usuario.criptografar(arquivo, hugo.chave_publica)

    with open('arquivo_cifrado.txt', 'wb') as k:
        k.write(msg_cifrada)

    chave_privada_hugo = 'chave_privada_hugo'
    save_key(hugo.chave_privada, chave_privada_hugo)

    hugo.chave_privada = load_key(chave_privada_hugo)
    hugo.chave_publica = hugo.chave_privada.public_key()

    # Decifrando a mensagem secreta
    with open('arquivo_cifrado.txt', 'rb') as l:
        arquivo_cifrado = l.read()

    msg_plana_ = hugo.decriptografar(arquivo_cifrado)
    print(msg_plana_.decode())
