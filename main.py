from Conta import *
from Cliente import Cliente
#criação de cliente
cliente1 = Cliente("Mateus", "12345678900")
cliente2 = Cliente("Fulano", "00011122233")
print(cliente1)

#criação de contas
c1 = ContaCorrente("000",cliente1)
c2 = ContaCorrente("001",cliente2)
c3 = ContaPoupanca("002",cliente1)
c4 = ContaPoupanca("003",cliente2)
#teste da exceção (número de conta duplicado)
c5 = ContaCorrente("000",cliente1)

#depósito negativo
print("depósito de -100 reais:")
if not c1.depositar(-100):
    print("Valor inválido\n")

#depósito regular
print("depósito de 100 reais:")
if c1.depositar(100):
    print("Depósito realizado com sucesso!\n")

#depósitos para fins de teste
c2.depositar(100)
c3.depositar(100)
c4.depositar(100)

#teste de saque
print("Funcionamento do saque:")
print(f"pré saque de R$50,00:\n{c2}\n")
c2.sacar(50)
saldo_Atual = c2.get_saldo()
print(f"pós saque de R$50,00:\n{c2}\n")

#exibição de saldo negativo na conta corrente
c1.sacar(200)
print(f"Exemplo saldo negativo conta corrente:\n{c1}\n")

#teste saque indevido
print("Exemplo de saque acima do saldo:")
c3.sacar(200)
print("\n")

#teste de rendimento
print(f"pré rendimento:\n{c3}\n")
rendimento = c3.aplicar_rendimento()
print(f"pós rendimento de {rendimento}:\n{c3}")

#lisatr as contas de um cliente
cliente1.get_contas()

#teste de duplicação de cpf
#lançamento de erro
cliente3 = Cliente("Ciclano", "12345678900")




    
