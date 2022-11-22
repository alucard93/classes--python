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


class AgenciaVirtual(Agencia):
    pass


class AgenciaComum(Agencia):
    pass


class AgenciaPremium(Agencia):
    pass



