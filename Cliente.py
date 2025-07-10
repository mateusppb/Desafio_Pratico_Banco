class Cliente:
    def __init__(self,nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__contas = []
    
    def adicionar_conta(self, conta):
        from Conta import ContaBancaria
        if isinstance(conta, ContaBancaria):
            for c in self.__contas:
                if c.numero_conta == conta._numero_conta:
                    print(f"Conta de número {conta._numero_conta} já existente para esse cliente.")
                    return False
            
            self.__contas.append(conta)
            return True
        else:
            print("O objeto não é ContaBancaria.")
            return False

    def remover_conta(self, numero_conta):
        for conta in self.__contas:
            if conta.numero_conta == numero_conta:
                self.__contas.remove(conta)
                return True
        return False
        
    def get_contas(self):
        contas_cliente1 = self.__contas
        i = 1
        for c in contas_cliente1:
            print(f"Conta {i}: {c}")
            i += 1
        return True

    def __str__(self):
        return f'Cliente: [{self.__nome}] (CPF: [{self.__cpf}])'


