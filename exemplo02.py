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
    return encriptador.update(arquivo_)


def decriptografa_arquivo(arquivo_criptografado_, cifra_):
    decriptador = cifra_.decryptor()
    return decriptador.update(arquivo_criptografado_) + decriptador.finalize()


if __name__ == '__main__':
    #  Abre o arquivo que será criptografado
    with open('arquivo.txt', 'rb') as f:
        arquivo = f.read()

    # Gera chave simétrica aleatória
    chave_simetrica = os.urandom(32)
    with open('chave_simetrica.txt', 'wb') as f:
        f.write(chave_simetrica)

    # Gera uma Cifra Simétrica do tipo ECB
    cifra = gerador_cifra(chave_simetrica, "ECB")

    # Criptografa o arquivo
    arquivo_cifrado = criptografa_arquivo(arquivo, cifra)

    # Salva o arquivo criptografado
    with open('arquivo.txt.encriptado', 'wb') as f:
        f.write(arquivo_cifrado)

    # Decriptografa o arquivo
    with open('arquivo.txt.encriptado', 'rb') as f:
        novo_arquivo = f.read()
    arquivo_plano = decriptografa_arquivo(novo_arquivo, cifra)

    # Salva novo arquivo gerado
    with open('novo_arquivo.txt', 'wb') as f:
        f.write(arquivo_plano)
