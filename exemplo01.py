import hashlib
import string
import random


class Usuario:
    def __init__(self, username, senha):
        self.__user = username
        salt = Usuario.get_string_aleatoria()
        self.__senha = salt +":"+Usuario.get_hash(senha+salt)

    @staticmethod
    def get_string_aleatoria(length=8):
        letras = string.ascii_lowercase
        result_str = ''.join(random.choice(letras) for _ in range(length))
        return result_str

    @staticmethod
    def get_hash(password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def login(self, password):
        salt = self.__senha.split(":")
        hash_password = Usuario.get_hash(password+salt[0])
        return hash_password == salt[1]

    def __str__(self):
        return "User [username={}, password={}]".format(self.__user, self.__senha)


if __name__ == '__main__':
    # Cria e imprime um usuário
    hugo = Usuario("hkuribayashi", "123456")

    saida = hugo.login("123456")
    print(saida)

    print(hugo)

