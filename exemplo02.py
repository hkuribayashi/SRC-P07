import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def gerador_cifra(chave, modo="CBC"):
    iv = os.urandom(16)
    if modo == "CBC":
        cifra_ = Cipher(algorithms.AES(chave), modes.CBC(iv))
    elif modo == "ECB":
        cifra_ = Cipher(algorithms.AES(chave), modes.ECB())
    else:
        raise RuntimeError("Modo Inválido")
    return cifra_


def criptografa_arquivo(arquivo_, cifra_):
    encriptador = cifra_.encryptor()
    return encriptador.update(arquivo_)# + encriptador.finalize()


def decriptografa_arquivo(arquivo_criptografado_, cifra_):
    decriptador = cifra_.decryptor()
    return decriptador.update(arquivo_criptografado_) + decriptador.finalize()


if __name__ == '__main__':
    #  Abre o arquivo que será criptografado
    with open('arquivo.txt', 'rb') as f:
        arquivo = f.read()

    # Gera chave simétrica aleatória
    chave_simetrica = os.urandom(32)

    # Gera uma Cifra Simétrica do tipo ECB
    cifra = gerador_cifra(chave_simetrica, "ECB")

    # Criptografa o arquivo
    arquivo_criptografado = criptografa_arquivo(arquivo, cifra)

    # Salva o arquivo criptografado
    with open('arquivo.txt.encrypted', 'wb') as f:
        f.write(arquivo_criptografado)

    # Decriptografa o arquivo
    arquivo_plano = decriptografa_arquivo(arquivo_criptografado, cifra)

    # Salva novo arquivo gerado
    with open('novo_arquivo.txt', 'wb') as f:
        f.write(arquivo_plano)
