import os
os.system('cls')

class Agencia:
    def __init__(self, telefone, cnpj, numero) -> None:
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa com nível abaixo do recomendado. Caixa atual: {}'.format(self.caixa))
        else:
            print('O valor de Caixa está ok. Caixa atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa.')
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


#problema
agencia1 = Agencia(22223333, 2000000000000, 4568)
agencia1.caixa = 1000000
agencia1.verificar_caixa()
agencia1.emprestar_dinheiro(1500, 153000000, 0.2)
print(agencia1.emprestimos)
agencia1.adicionar_cliente('nascimento', 1534455555, 10000)
print(agencia1.clientes)