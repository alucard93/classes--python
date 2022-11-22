from contas_banco import ContaCorrente, CartaoCredito

#programa

conta_vinicius = ContaCorrente("Marcus Vinicius", 15311742720, 2784, 40083234)
cartao_vinicius = CartaoCredito('Vinicius', conta_vinicius)
# print(cartao_vinicius.titular)
# print(cartao_vinicius.conta_corrente._num_conta) 
# print(conta_vinicius.cartoes[0].numero)
# print(cartao_vinicius.validade)
# print(cartao_vinicius.numero)
print(conta_vinicius.__dict__)
print(cartao_vinicius.__dict__)

# print(conta_vinicius.depositar(10000))

# # print(conta_vinicius.sacar(1100))

# print('-' * 39)

# conta_vinicius.consultar_historico_transacoes()

# print('-' * 39)

# conta_mae_vinicius = ContaCorrente('Dalva', '00505802765', 2134, 4112346)
# conta_vinicius.transferir(500, conta_mae_vinicius)
# conta_vinicius.consultar_saldo()
# conta_mae_vinicius.consultar_saldo()

# conta_vinicius.consultar_historico_transacoes()
# conta_mae_vinicius.consultar_historico_transacoes()

#o underline antes do parametro indica para a pessoa que abrir o meu código que para ela alterar aquele determinado dado possui uma função um metódo para ela utilizar para realizar a mudança.
