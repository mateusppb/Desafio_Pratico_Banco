# Sistema Bancário Simplificado - Desafio Prático

Projeto desenvolvido para o desafio de Programação Orientada a Objetos (POO) em Python.  
O sistema simula operações básicas de um banco, com clientes e diferentes tipos de contas bancárias.

---

## Descrição do Projeto

Este projeto implementa um sistema bancário simples que utiliza conceitos de POO para modelar:

- Contas Bancárias (conta corrente e poupança)
- Clientes vinculados a suas contas
- Operações de depósito, saque, e aplicação de rendimento (para poupança)

Uso de herança, polimorfismo, encapsulamento e lógica de negócio.

---

## Requisitos das Classes

### Classe Base `ContaBancaria`

- **Atributos:**
  - `numero_conta` (string, único para cada conta)
  - `saldo` (float)
  - `titular` (objeto Cliente)
- **Métodos:**
  - `__init__(self, numero_conta, titular, saldo_inicial=0.0)`
  - `depositar(self, valor)`
  - `sacar(self, valor)` (método base a ser sobrescrito)
  - `get_saldo(self)`
  - `__str__(self)`

### Classe `ContaCorrente` (herda de `ContaBancaria`)

- **Atributos adicionais:**
  - `limite_cheque_especial` (ex: R$ 500,00)
- **Métodos sobrescritos:**
  - `sacar(self, valor)` permite usar cheque especial (saldo pode ficar negativo até o limite)
  - `__str__(self)` inclui limite na exibição

### Classe `ContaPoupanca` (herda de `ContaBancaria`)

- **Atributos adicionais:**
  - `taxa_rendimento` (ex: 0.005 para 0,5%)
- **Métodos sobrescritos:**
  - `sacar(self, valor)` não permite saldo negativo
  - `aplicar_rendimento(self)` calcula e adiciona rendimento ao saldo
  - `__str__(self)` inclui taxa de rendimento

### Classe `Cliente`

- **Atributos:**
  - `nome` (string)
  - `cpf` (string)
  - `contas` (lista de contas associadas)
- **Métodos:**
  - `adicionar_conta(self, conta)`
  - `remover_conta(self, numero_conta)`
  - `get_contas(self)`
  - `__str__(self)`

---

## Cenário de Teste (Exemplo de Uso)

No script principal (`main.py`):

1. Criação de clientes
2. Criação e associação de contas correntes e poupança
3. Depósitos e saques com regras específicas para cada tipo de conta
4. Testes para saque indevido
5. Aplicação de rendimento na poupança
6. Impressão de informações para verificação

---

## Como Rodar

1. Clone o repositório  
   `git clone https://github.com/mateusppb/Desafio_Pratico_Banco.git`

2. Navegue até a pasta do projeto  
   `cd Desafio_Pratico_Banco`

3. Execute o script principal  
   `python main.py`

---

## Autor

Mateus Pimenta
