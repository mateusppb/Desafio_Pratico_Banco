from Cliente import Cliente

#classe pai de contas
class ContaBancaria:
    def __init__(self,numero_conta: str,titular: Cliente):
        self._numero_conta = numero_conta
        self._saldo = 0.0
        self._titular = titular
    
    #realizar um depósito
    def depositar(self, valor:float):
        if valor > 0:
            self._saldo += valor
            return True
        else:
            return False
        
    #sacar um valor da conta
    def sacar(self, valor) -> bool:
        return False #abstrato para subclasses sobrescreverem
    
    #acessar o saldo da conta(protegido)
    def get_saldo(self):
        return self._saldo
    
    #impressão das infos da conta
    def __str__(self):
        return f'Conta: [{self._numero_conta}] - Titular: [{self._titular}] - Saldo: R$[\033[32m{self._saldo}\033[0m]'
        
#conta corrente filha de ContaBancaria
class ContaCorrente(ContaBancaria):
    def __init__(self,numero_conta: str,titular: Cliente):
        super().__init__(numero_conta, titular)
        self.__limite_cheque_especial = 500.00

    #sobreposição em relação a função sacar da classe pai
    #sacar um valor válido da conta
    def sacar(self, valor):
        if valor < 0:
            print('Valor de saque inválido.')
            return False
        elif valor > self._saldo + self.__limite_cheque_especial:
            print('Saldo insuficiente.')
            return False
        self._saldo -= valor
        return True
    
    #impressão das infos da conta
    def __str__(self):
        if self._saldo >= 0:
            return f'Conta: [{self._numero_conta}] - Titular: [{self._titular}] - Saldo: R$[\033[32m{self._saldo}\033[0m] - Limite do cheque especial: [{self.__limite_cheque_especial}]'
        else:
            return f'Conta: [{self._numero_conta}] - Titular: [{self._titular}] - Saldo: R$[\033[31m{self._saldo}\033[0m] - Limite do cheque especial: [{self.__limite_cheque_especial}]'
        
#conta poupança filha de ContaBancaria
class ContaPoupanca(ContaBancaria):
    def __init__(self,numero_conta: str,titular: Cliente):
        super().__init__(numero_conta, titular)
        self.__taxa_rendimento = 0.005
    
    #sobreposição em relação a função sacar da classe pai
    #sacar um valor válido da conta
    def sacar(self, valor):
        if valor < 0:
            print('Valor de saque inválido.')
            return False
        elif valor > self._saldo:
            print('Saldo insuficiente.')
            return False
        self._saldo -= valor
        return True
    
    #método para calcular e retornar um rendimento
    def aplicar_rendimento(self): 
        rendimento = self._saldo * self.__taxa_rendimento
        self._saldo += rendimento
        return rendimento
    
    #impressão das infos da conta
    def __str__(self):
        return f'Conta: [{self._numero_conta}] - Titular: [{self._titular}] - Saldo: R$[\033[32m{self._saldo}\033[0m] - Taxa de rendimento: [{self.__taxa_rendimento}]'

