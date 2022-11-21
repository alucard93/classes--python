# # class Computador:
# #     def __init__(self, marca, memoria_ram, placa_de_video) -> None:
# #         self.marca          = marca
# #         self.memoria_ram    = memoria_ram
# #         self.placa_de_video = placa_de_video


# #     def Ligar(self):
# #         print('estou ligando')

# #     def Desligar(self):
# #         print('estou desligando')

# #     def ExibirInformacoesDesteComputador(self):
# #         print(self.marca, self.memoria_ram, self.placa_de_video)

# # computador1 = Computador('Asus', '6gb', 'Nvidia')
# # computador1.Ligar()
# # computador1.Desligar()
# # computador1.ExibirInformacoesDesteComputador()


# # # print(Computador1.marca)

# # # print(computador1.marca, computador1.memoria_ram , computador1.placa_de_video)
# # # print(computador2.marca, computador2.memoria_ram , computador2.placa_de_video)
# # # print(computador3.marca, computador3.memoria_ram , computador3.placa_de_video)

# # # computador1 = Computador('Asus', '8gb', 'Nvidia' )
# # # computador2 = Computador('Dell', '10gb', 'GeForce')
# # # computador3 = Computador('Acer', '16gb', 'ATM')

# # class Cachorro:
# #     quantidade_banho_geral = 0
# #     # (...)

# #     def tomar_banho(self):
# #         self.quantidade_banho_geral += 1

# # fred = Cachorro()
# # bili = Cachorro()
# # dudu = Cachorro()

# # fred.tomar_banho()
# # print(fred.quantidade_banho_geral)
# # # 1
# # bili.tomar_banho()
# # print(bili.quantidade_banho_geral)
# # # 1
# # dudu.tomar_banho()
# # print(dudu.quantidade_banho_geral)
# # # 1
# # print(Cachorro.quantidade_banho_geral)
# # # 0

# class Cachorro:
#     # (...)

#     def tomar_banho(self):
#         # Ao invés de incrementar o valor de "quantidade_banho_geral"
#         # de cada instância utilizando self, chamamos direto a classe
#         # Cachorro para modificarmos seu atributo geral
#         Cachorro.quantidade_banho_geral += 1

# fred.tomar_banho()
# print(fred.quantidade_banho_geral)
# # 1
# bili.tomar_banho()
# print(bili.quantidade_banho_geral)
# # 2
# dudu.tomar_banho()
# print(dudu.quantidade_banho_geral)
# # 3
# print(Cachorro.quantidade_banho_geral)
# # 3 

class Cachorro:
    ...
    def __init__(self, nome):
        self.nome = nome # atributo de instância
    ...
fred = Cachorro('fred')
bili = Cachorro('bili')

print(fred.nome)
# fred
print(bili.nome)
# bili

class Cachorro:
    nome_cientifico = 'canis lupus familiaris'
    quantidade_banho_geral = 0
    dias_para_passear = set()

    def __init__(self, nome):
      self.nome = nome

    def tomar_banho(self):
      Cachorro.quantidade_banho_geral += 1

    def passear(self, *args):
      for dia in args:
        self.dias_para_passear.add(dia)
		  # Ou
        self.dias_para_passear.update(args)

fred = Cachorro('fred')
bili = Cachorro('bili')

fred.passear('seg', 'qua', 'sex')
print(fred.dias_para_passear)
# {'sex', 'seg', 'qua'}

bili.passear('ter', 'qui', 'dom')
print(bili.dias_para_passear)
# {'seg', 'dom', 'qua', 'qui', 'sex', 'ter'}

class Cachorro:
    # Compartilhado com todas as instâncias
    nome_cientifico = 'canis lupus familiaris'
    quantidade_banho_geral = 0

    def __init__(self, nome):
      self.nome = nome
      self.dias_para_passear = set()

    def tomar_banho(self):
      Cachorro.quantidade_banho += 1

    def passear(self, *args):
      for dia in args:
        self.dias_para_passear.add(dia)
		  # Ou
        self.dias_para_passear.update(args)

fred = Cachorro('fred')
bili = Cachorro('bili')

fred.passear('seg', 'qua', 'sex')
print(fred.dias_para_passear)
# {'seg', 'qua', 'sex'}

bili.passear('ter', 'qui', 'dom')
print(bili.dias_para_passear)
# {'qui', 'ter', 'dom'}