# Demonstração de uso de Criptografia e Hash em Python

Este projeto é uma demonstração reproduzível dos conceitos
de criptografia (simétrica e assimétrica) e hash criptográfico 
(dispersão/digest), implementados na linguagem Python.

Este projeto é para alunos da disciplina SI01033 (Segurança em 
Redes de Computadores) do Curso de Sistemas de Informação da 
Unifesspa, que querem testar ferramentas de criptografia 
e/ou implementar tais ferramentas em seus cógigos/aplicações reais, 
e assim reproduzir os próprios resultados ou brincar com o conceito, 
para criar variações dos resultados a serem obtidos.

## Hash Criptográfico

Começamos com o arquivo `exemplo01.py`. Este arquivo apresenta uma
demonstração do conceito de hash criptográfico, contextualizado no 
exemplo de um processo de autenticação (login) de um usuário.

Dentro do arquivo `exemplo01.py` é implementada uma classe Usuario, 
que possui 02 (dois) atributos: username e senha, além de um conjunto
de métodos de instância e de classe necessários ao funcionamento da classe.

O que deve ser modificado/implementado?
1. O valor do atributo senha deve ser salvo em formato hash (SHA256); 
2. O método login deve ser implementado de forma a comparar uma senha informada com a senha salva no atributo senha; 
3. Deve ser implementado um método para aplicar um salt na senha; 
4. Modificar o método login( ) para usar o método implementado no item anterior.

## Criptogrfia Simétrica

Agora utilizaremos o arquivo `exemplo02.py`.

## Criptogrfia Assimétrica
  
## Conclusão

O objetivo deste projeto é simplesmente para propósitos educacionais, 
para permitir ao discente, entender as diferenças entre os modos *ECB* e *CBC*.
