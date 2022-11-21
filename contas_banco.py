import os
os.system('cls')

class ContaCorrente():
    #o atributo nome da classe - vai ser o nome passado na criação
    def __init__(self, nome, cpf) -> None:
        self.nome   = nome
        self.cpf    = cpf
        self.saldo  = 0
        self.limite = None # ou 0
    
    def consultar_saldo (self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo)) 
    
    def depositar (self, valor):
        self.saldo += valor
        print('Você depositou {}. Seu saldo atual é de R${:,.2f}'.format(valor, self.saldo)) 
    
    def sacar (self, valor):
        if self.saldo - valor < self.limite_conta(): 
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
            print('Você sacou {}. Seu saldo atual é de R${:,.2f}'.format(valor, self.saldo))
            # self.consultar_saldo()

    def limite_conta(self):
        self.limite = -1000
        return self.limite


#programa

conta_vinicius = ContaCorrente("Marcus Vinicius", 15311742720)
# print(conta_vinicius.nome, conta_vinicius.cpf, conta_vinicius.saldo)

print(conta_vinicius.depositar(100))
print(conta_vinicius.sacar(1100))

