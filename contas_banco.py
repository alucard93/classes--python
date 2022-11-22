from datetime import datetime
import pytz     #pip3 install pytz
import os
os.system('cls')


class ContaCorrente():

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta) -> None:
        self.nome   = nome
        self.cpf    = cpf
        self.saldo  = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
    
    def consultar_saldo (self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo)) 
    
    def depositar (self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
    
    def sacar (self, valor):
        if self.saldo - valor < self._limite_conta(): 
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
            print('Você sacou {}. Seu saldo atual é de R${:,.2f}'.format(valor, self.saldo))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def consultar_limite_cheque_especial(self):
        print('Seu limite de cheque especial é de R${:,.2f}'.format(self._limite_conta())) 

    def consultar_historico_transacoes(self):
        print('Histórico de transações: ')
        print('Valor, Saldo, Data e Hora')
        for transacoes in self.transacoes:
            print(transacoes)
    
    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((+valor, conta_destino.saldo, ContaCorrente._data_hora()))


#programa

conta_vinicius = ContaCorrente("Marcus Vinicius", 15311742720, 2784, 40083234)

print(conta_vinicius.depositar(10000))

# print(conta_vinicius.sacar(1100))

print('-' * 39)

conta_vinicius.consultar_historico_transacoes()

print('-' * 39)

conta_mae_vinicius = ContaCorrente('Dalva', '00505802765', 2134, 4112346)

conta_vinicius.transferir(500, conta_mae_vinicius)

conta_vinicius.consultar_saldo()
conta_mae_vinicius.consultar_saldo()

conta_vinicius.consultar_historico_transacoes()
conta_mae_vinicius.consultar_historico_transacoes()

