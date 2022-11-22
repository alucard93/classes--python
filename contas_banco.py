from datetime import datetime
import pytz     #pip3 install pytz
import os
os.system('cls')


class ContaCorrente():
    """ 
    Cria um obeto ContaCorrente para gerencar as contas dos clientes.
    
    Atributos:
        nome (str): Nome do Cliente
        cpf (str): CPF do Cliente. Deve ser inserido com pontos e traços.
        agencia: Agencia responsável pela conta do cliente
        num_conta: Número da conta corrente do cliente
        saldo: Saldo disponivel na conta do cliente
        limite: limite de cheque especial daquele cliente
        transacoes: histórico de transações do cliente.
    """
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta) -> None:
        self._nome   = nome
        self._cpf    = cpf
        self._saldo  = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
    
    def consultar_saldo (self):
        """
            Exibe o sado atual da conta do cliente.
            Não há parâmetros necessários.
        """
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo)) 
    
    def depositar (self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
    
    def sacar (self, valor):
        if self._saldo - valor < self._limite_conta(): 
            print('Saldo insuficiente')
        else:
            self._saldo -= valor
            print('Você sacou {}. Seu saldo atual é de R${:,.2f}'.format(valor, self._saldo))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def consultar_limite_cheque_especial(self):
        print('Seu limite de cheque especial é de R${:,.2f}'.format(self._limite_conta())) 

    def consultar_historico_transacoes(self):
        print('Histórico de transações: ')
        print('Valor, Saldo, Data e Hora')
        for transacoes in self._transacoes:
            print(transacoes)
    
    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((+valor, conta_destino._saldo, ContaCorrente._data_hora()))


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

#o underline antes do parametro indica para a pessoa que abrir o meu código que para ela alterar aquele determinado dado possui uma função um metódo para ela utilizar para realizar a mudança.

