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
        if self.saldo - valor < self._limite_conta(): 
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
            print('Você sacou {}. Seu saldo atual é de R${:,.2f}'.format(valor, self.saldo))
            # self.consultar_saldo()

#o underline indica que tal método é usada apenas na parte da classe e não pode ser utilizado na seção de programa - método privado

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def consultar_limite_cheque_especial(self):
        print('Seu limite de cheque especial é de R${:,.2f}'.format(self._limite_conta())) 


#programa

conta_vinicius = ContaCorrente("Marcus Vinicius", 15311742720)
# print(conta_vinicius.nome, conta_vinicius.cpf, conta_vinicius.saldo)

print(conta_vinicius.depositar(100))
print(conta_vinicius.sacar(1100))
conta_vinicius.consultar_limite_cheque_especial()

