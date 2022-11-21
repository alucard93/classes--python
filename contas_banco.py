import os
os.system('cls')

class ContaCorrente():
    #o atributo nome da classe - vai ser o nome passado na criação
    def __init__(self, nome, cpf) -> None:
        self.nome  = nome
        self.cpf   = cpf
        self.saldo = 0


#programa

conta_vinicius = ContaCorrente("Marcus Vinicius", 15311742720)
print(conta_vinicius.nome, conta_vinicius.cpf, conta_vinicius.saldo)
