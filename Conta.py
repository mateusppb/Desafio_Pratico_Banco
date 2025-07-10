from Cliente import Cliente

class ContaBancaria:
    def __init__(self,numero_conta: str,titular: Cliente):
        self._numero_conta = numero_conta
        self._saldo = 0.0
        self._titular = titular
    
    def depositar(self, valor:float):
        if valor > 0:
            self._saldo += valor
            return True
        else:
            return False
    
    def sacar(self, valor) -> bool:
        return False #abstrato para subclasses sobrescreverem
    
    def get_saldo(self):
        return self._saldo
    

    
    def __str__(self):
        return f'Conta: [{self._numero_conta}] - Titular: [{self._titular}] - Saldo: R$[\033[32m{self._saldo}\033[0m]'
        

class ContaCorrente(ContaBancaria):
    def __init__(self,numero_conta: str,titular: Cliente):
        super().__init__(numero_conta, titular)
        self.__limite_cheque_especial = 500.00

    def sacar(self, valor):
        if valor < 0:
            print('Valor de saque inválido.')
            return False
        elif valor > self._saldo + self.__limite_cheque_especial:
            print('Saldo insuficiente.')
            return False
        self._saldo -= valor
        return True
    
    def __str__(self):
        if self._saldo >= 0:
            return f'Conta: [{self._numero_conta}] - Titular: [{self._titular}] - Saldo: R$[\033[32m{self._saldo}\033[0m] - Limite do cheque especial: [{self.__limite_cheque_especial}]'
        else:
            return f'Conta: [{self._numero_conta}] - Titular: [{self._titular}] - Saldo: R$[\033[31m{self._saldo}\033[0m] - Limite do cheque especial: [{self.__limite_cheque_especial}]'
        



class ContaPoupanca(ContaBancaria):
    def __init__(self,numero_conta: str,titular: Cliente):
        super().__init__(numero_conta, titular)
        self.__taxa_rendimento = 0.005
    
    def sacar(self, valor):
        if valor < 0:
            print('Valor de saque inválido.')
            return False
        elif valor > self._saldo:
            print('Saldo insuficiente.')
            return False
        self._saldo -= valor
        return True
    
    def aplicar_rendimento(self): 
        rendimento = self._saldo * self.__taxa_rendimento
        self._saldo += rendimento
        return rendimento
    
    def __str__(self):
        return f'Conta: [{self._numero_conta}] - Titular: [{self._titular}] - Saldo: R$[\033[32m{self._saldo}\033[0m] - Taxa de rendimento: [{self.__taxa_rendimento}]'

