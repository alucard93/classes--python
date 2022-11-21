import os
os.system('cls')

class ContaCorrente():
    #o atributo nome da classe - vai ser o nome passado na criação
    def __init__(self, nome, cpf) -> None:
        self.nome  = nome
        self.cpf   = cpf
        self.saldo = 0
    
    def consultar_saldo (self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo)) 
    
    def depositar_ou_sacar (self, valor):
        self.saldo += valor
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo)) 


#programa

conta_vinicius = ContaCorrente("Marcus Vinicius", 15311742720)
# print(conta_vinicius.nome, conta_vinicius.cpf, conta_vinicius.saldo)
print(conta_vinicius.depositar_ou_sacar(100))
print(conta_vinicius.consultar_saldo())
# print(conta_vinicius.depositar_ou_sacar(-20))

# print(conta_vinicius.saldo)
