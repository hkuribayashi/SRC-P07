# Demonstração de uso de Criptografia e Hash Criptográfico em Python

Este projeto é uma demonstração reproduzível dos conceitos
de criptografia (simétrica e assimétrica) e *hash* criptográfico 
(dispersão/*digest*), implementados na linguagem Python.

Este projeto é para alunos da disciplina SI01033 (Segurança em 
Redes de Computadores) do Curso de Sistemas de Informação da 
Unifesspa, que querem testar ferramentas de criptografia 
e/ou implementar tais ferramentas em seus cógigos/aplicações reais, 
e assim reproduzir os próprios resultados ou brincar com o conceito, 
para criar variações dos resultados a serem obtidos.

## Hash Criptográfico

Começamos com o arquivo `exemplo01.py`. Este arquivo apresenta uma
demonstração do conceito de *hash* criptográfico, contextualizado no 
exemplo de um processo de autenticação (login) de um usuário.

Dentro do arquivo `exemplo01.py` é implementada uma classe Usuario, 
que possui 02 (dois) atributos: username e senha, além de um conjunto
de métodos de instância e de classe necessários ao funcionamento da classe.

O que deve ser modificado/implementado?
1. O valor do atributo senha deve ser salvo em formato *hash* (SHA256); 
2. O método login( ) deve ser implementado de forma a comparar uma senha informada com a senha salva no atributo senha; 
3. Deve ser implementado um método para aplicar um *salt* na senha; 
4. Modificar o método login( ) para usar o método implementado no item anterior.

## Criptografia Simétrica

Agora utilizaremos o arquivo `exemplo02.py`. O objetivo deste exemplo
é testar métodos de criptografia simétrica. No exemplo em questão 
utilizamos o algoritmo Advanced Encryption Standard (AES). Neste exemplo 
é possível testar o uso do AES nos modos Electronic CodeBook (ECB) e 
Cipher Block Chaining (CBC).

O que deve ser implementado/modificado?

1. Realizar a criação de uma chave simétrica;
2. Criar uma cifra simétrica utilizando ECB ou CBC;
3. Criptografar o arquivo `arquivo.txt` e gerar um novo arquivo chamado `arquivo.txt.encrypted`;
4. Tentar decifrar o arquivo `arquivo.txt.encrypted` com a chave simétrica criada no item (1).

## Criptografia Assimétrica
  
Por fim, utilizaremos o arquivo `exemplo03.py`. O objetivo deste exemplo
é testar métodos de criptografia assimétrica. No exemplo em questão 
utilizamos o algoritmo Rivest–Shamir–Adleman (RSA). Neste exemplo, o objetivo 
é verificar o uso das chaves publica e privada, onde cada uma possui suas respectivas
funções. 

A chave pública é usada para criptografar um arquivo, que somente poderá decifrado
com a chave privada respectiva. Por outro lado, uma chave privada, por também assinar 
um arquivo, e esta assinatura poderá ser verificada através da chave pública correspondente.

No arquivo `exemplo03.py` uma outra classe Usuário é implementada. Esta classe possui
02 (dois) atributos de instância: chave_publica e chave_privada. Tais chaves são criadas
por meio do algoritmo RSA, com chaves de 2048 bits, criadas no método construtor da classe.
A classe ainda possui um conjunto de métodos de instância e estáticos, usados para implementar 
as funções de encriptar/desencriptar e assinar/verificar assinatura.

O que deve ser implementado/modificado?

1. Assinar uma mensagem qualquer com a chave privada de um usuário;
2. Verificar a assinatura do item (2) com a respectiva chave pública;
3. Criptografar uma mensagem secreta para um usuário, usando sua chave pública
4. Decifrar a mensagem secreta usando a chave privada do usuário

## Conclusão

O objetivo deste projeto é simplesmente para propósitos educacionais, 
para permitir ao discente, entender as diferenças entre os métodos de 
criptografia *simétrica* e *assimétrica*, além de entender os conceitos
de *hash* criptográfico e *salt*.
