import hashlib
import string
import random


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    @staticmethod
    def get_salt_aleatorio(length=8):
        letras = string.ascii_lowercase
        result_str = ''.join(random.choice(letras) for _ in range(length))
        return result_str

    @staticmethod
    def get_senha_salteada(password):
        salt = User.get_salt_aleatorio()
        password = password + salt
        return salt + ":" + hashlib.sha256(password.encode("utf-8")).hexdigest()

    def login(self, password):
        pass

    def __str__(self):
        return "User [username={}, password={}]".format(self.__username, self.__password)


if __name__ == '__main__':
    # Cria e imprime um usuário
    hugo = User("hkuribayashi", "123456")
    print(hugo)

    # Testar o login do Usuario
    # hugo.login("senha")
