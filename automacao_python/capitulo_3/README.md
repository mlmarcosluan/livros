# Projeto: Sequência de Collatz

![Python](https://img.shields.io/badge/Python-3.12-red)

Este repositório contém a implementação de um programa Python que explora a **Sequência de Collatz**, também conhecida como "o mais simples problema matemático impossível". O programa permite que o usuário insira um número inteiro e observe a sequência até que o valor chegue a 1.

Além disso, o projeto inclui validação de entrada para garantir que o usuário insira apenas números inteiros válidos.

---

## Índice
- [Sobre o Projeto](#-sobre-o-projeto)
- [Conceitos Abordados](#-conceitos-abordados)
- [Como Usar o Programa](#-como-usar-o-programa)
- [Exemplo de Saída](#️-exemplo-de-saída)
- [Validação de Dados de Entrada](#-validação-de-dados-de-entrada)

---

## 📚 Sobre o Projeto

O programa implementa a **Sequência de Collatz**, que funciona da seguinte maneira:
- Se o número for **par**, divida-o por 2.
- Se o número for **ímpar**, multiplique-o por 3 e some 1.
- Repita o processo até que o número chegue a 1.

Esse comportamento é surpreendente porque, independentemente do número inicial, a sequência sempre termina em 1. Apesar de sua simplicidade, os matemáticos ainda não têm uma prova formal de por que isso acontece.

O programa também inclui validação de entrada para garantir que o usuário insira apenas números inteiros válidos.

---

## 📂 Conceitos Abordados

Este projeto explora os seguintes conceitos em Python:
1. **Funções**: Implementação da função `collatz()` para calcular a sequência.
2. **Condicionais**: Uso de `if` e `else` para verificar se um número é par ou ímpar.
3. **Laços de Repetição**: Uso de um loop `while` para continuar a sequência até chegar a 1.
4. **Tratamento de Exceções**: Uso de `try` e `except` para capturar erros de entrada inválida (por exemplo, quando o usuário insere uma string que não pode ser convertida para inteiro).
5. **Conversão de Tipos**: Conversão de strings para inteiros usando `int()`.

---

## 💻 Como Usar o Programa

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
2. **Execute o Programa** :
    Certifique-se de ter o Python instalado na sua máquina. Execute o programa com o seguinte comando:
    ```bash
    python collatz.py
    ```
3. **Insira um Número Inteiro** :
    O programa solicitará que você insira um número inteiro.
    Ele exibirá a sequência de Collatz até que o número chegue a 1.


## 🖥️ Exemplo de Saída
Aqui está um exemplo de como o programa funciona:
```bash
Digite um número:
3
10
5
16
8
4
2
1
```

## 🔒 Validação de Dados de Entrada
O programa inclui tratamento de exceções para evitar falhas quando o usuário insere dados inválidos. Por exemplo:

- Se o usuário inserir uma string que não pode ser convertida para inteiro (como 'puppy'), o programa exibirá uma mensagem de erro amigável:
```bash
Por favor, digite um número inteiro.
```
Isso é feito usando as cláusulas `try` e `except`:
```bash
try:
    number = int(input("Digite um número:\n"))
except ValueError:
    print("Por favor, digite um número inteiro.")
```