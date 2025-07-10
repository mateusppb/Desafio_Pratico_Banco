# Desafio Prático: Sistema Bancário Simplificado

Seu objetivo é criar um sistema bancário simples utilizando conceitos de **Programação Orientada a Objetos (POO)** em Python. Você definirá classes para representar **Contas Bancárias** (com diferentes tipos) e **Clientes**, e a lógica para realizar operações bancárias básicas.

---

## Requisitos da Classe Base `ContaBancaria`:

Esta será uma classe abstrata ou base para outros tipos de conta.

1.  **Atributos:**
    * `numero_conta` (string, único para cada conta)
    * `saldo` (float, inicializado com 0 ou um valor fornecido)
    * `titular` (objeto `Cliente`, associando a conta a um cliente)
2.  **Métodos:**
    * `__init__(self, numero_conta, titular, saldo_inicial=0.0)`: Construtor que inicializa os atributos.
    * `depositar(self, valor)`:
        * Adiciona `valor` ao `saldo`.
        * O `valor` deve ser positivo.
        * Retorna `True` se o depósito for bem-sucedido, `False` caso contrário.
    * `sacar(self, valor)`:
        * **Este método deve ser abstrato ou implementado com uma verificação básica e sobrescrito pelas subclasses.**
        * Verifica se o `valor` é positivo e se há saldo suficiente.
        * Se sim, subtrai `valor` do `saldo` e retorna `True`.
        * Se não, retorna `False`.
    * `get_saldo(self)`: Retorna o saldo atual da conta.
    * `__str__(self)`: Retorna uma representação em string da conta (ex: "Conta: [Numero] - Titular: [Nome do Titular] - Saldo: R$[Saldo]").

---

## Requisitos da Classe `ContaCorrente` (Herda de `ContaBancaria`):

1.  **Atributos Adicionais:**
    * `limite_cheque_especial` (float, ex: R$ 500.00)
2.  **Métodos Sobrescritos/Adicionais:**
    * `__init__(self, numero_conta, titular, saldo_inicial=0.0, limite_cheque_especial=500.00)`: Chame o construtor da classe base e inicialize o novo atributo.
    * `sacar(self, valor)`:
        * Sobrescreva o método `sacar` da classe base.
        * O saque é permitido se o `saldo` atual mais o `limite_cheque_especial` for maior ou igual ao `valor` a ser sacado.
        * Se o saque utilizar o cheque especial, o saldo pode ficar negativo.
        * Retorna `True` para sucesso, `False` para falha (valor inválido ou limite excedido).
    * `__str__(self)`: Inclua informações do limite na string de representação.

---

## Requisitos da Classe `ContaPoupanca` (Herda de `ContaBancaria`):

1.  **Atributos Adicionais:**
    * `taxa_rendimento` (float, ex: 0.005 para 0.5% ao mês)
2.  **Métodos Sobrescritos/Adicionais:**
    * `__init__(self, numero_conta, titular, saldo_inicial=0.0, taxa_rendimento=0.005)`: Chame o construtor da classe base e inicialize o novo atributo.
    * `sacar(self, valor)`:
        * Sobrescreva o método `sacar` da classe base.
        * O saque só é permitido se o `saldo` for suficiente (não pode usar cheque especial, saldo não pode ficar negativo).
        * Retorna `True` para sucesso, `False` para falha.
    * `aplicar_rendimento(self)`:
        * Calcula o rendimento (`saldo * taxa_rendimento`) e o adiciona ao `saldo`.
        * Retorna o valor do rendimento aplicado.
    * `__str__(self)`: Inclua informações da taxa de rendimento na string de representação.

---

## Requisitos da Classe `Cliente`:

1.  **Atributos:**
    * `nome` (string)
    * `cpf` (string, único para cada cliente)
    * `contas` (lista de objetos `ContaBancaria` associadas a este cliente)
2.  **Métodos:**
    * `__init__(self, nome, cpf)`: Construtor.
    * `adicionar_conta(self, conta)`: Adiciona um objeto `ContaBancaria` à lista `contas` do cliente.
    * `remover_conta(self, numero_conta)`: Remove uma conta da lista do cliente pelo número da conta. Retorna `True` se removida, `False` caso contrário.
    * `get_contas(self)`: Retorna a lista de contas do cliente.
    * `__str__(self)`: Retorna uma representação em string do cliente (ex: "Cliente: [Nome] (CPF: [CPF])").

---

## Cenário de Teste (Exemplo de Uso):

No seu script principal (`main.py` ou diretamente no arquivo das classes), crie instâncias e simule as operações:

1.  Crie um ou dois objetos `Cliente`.
2.  Crie algumas `ContaCorrente` e `ContaPoupanca`, associando-as aos clientes.
3.  Simule depósitos e saques em diferentes tipos de conta, testando os limites e regras de cada uma.
4.  Tente sacar mais do que o permitido.
5.  Aplique rendimento a uma conta poupança.
6.  Imprima os saldos e as informações das contas e clientes para verificar se as operações foram bem-sucedidas e os estados estão corretos.

---

## Dicas e Considerações:

* **Herança:** Preste atenção em como `ContaCorrente` e `ContaPoupanca` herdam de `ContaBancaria` e sobrescrevem seus métodos.
* **Encapsulamento:** Mantenha os atributos privados (prefixando com `_` ou `__` em Python) e acesse-os através de métodos (getters/setters, se necessário, ou diretamente via métodos que operam neles).
* **Tratamento de Entrada:** No cenário de teste, você pode simular a entrada do usuário ou apenas chamar os métodos diretamente.
* **Polimorfismo:** Observe como o mesmo método `sacar()` se comporta de maneira diferente para `ContaCorrente` e `ContaPoupanca` devido à sobrescrita.

---

## Como o Avaliador Verá seu Trabalho:

* **Modelagem POO:** A correta identificação e implementação de classes, atributos e métodos.
* **Herança e Polimorfismo:** A aplicação eficaz desses conceitos para criar tipos de contas especializados.
* **Lógica de Negócio:** A implementação precisa das regras de depósito, saque e rendimento para cada tipo de conta.
* **Relacionamento entre Objetos:** Como clientes e contas estão associados.
* **Organização e Legibilidade:** Código Python bem estruturado, claro e fácil de entender.
