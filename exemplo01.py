import hashlib
import string
import random


class Usuario:
    def __init__(self, username, senha):
        self.__user = username
        self.__senha = senha

    @staticmethod
    def get_salt_aleatorio(length=8):
        letras = string.ascii_lowercase
        result_str = ''.join(random.choice(letras) for _ in range(length))
        return result_str

    @staticmethod
    def get_senha_salteada(password):
        salt = Usuario.get_salt_aleatorio()
        password = password + salt
        return salt + ":" + hashlib.sha256(password.encode("utf-8")).hexdigest()

    def login(self, password):
        pass

    def __str__(self):
        return "User [username={}, password={}]".format(self.__user, self.__senha)


if __name__ == '__main__':
    # Cria e imprime um usuário
    hugo = Usuario("hkuribayashi", "123456")
    print(hugo)

    # Testar o login do Usuario
    # hugo.login("senha")
