import os 
os.system('cls')

#__init__ - quando eu chamar a class Tv automaticamente ele vai chamar a função do metodo
# sempre que vc estiver dentro de uma classe e quiser referenciar a classe pode usar o 'self'
#ex: self.cor = 'preta'  pode-se ler que é uma variavel cor da classe Tv // parametro cor da classe Tv
#metódo é uma função dentro de uma classe
# () - indica que é um metódo, se n tiver é um atributo
# class Tv:

# #self.atributo igual ao valor inicial
#     def __init__(self):
#         # atributo da classe Tv = variavel
#         self.cor = 'preta'
#         self.ligada = False
#         self.tamanho = 55
#         self.canal = 'Netflix'
#         self.volume = 10

#     # def mudar_canal(self):
#     #     self.canal = 'Disney+'

#     #Encapsulamento//Polimorfismo//Reaproveitamento
#     def mudar_canal(self, novo_canal):
#         self.canal = novo_canal
#         # print('Canal foi alterado para {}'.format(novo_canal))


# #realizando a criação de uma instância da classe Tv - Herença//Reaproveitamento de código
# tv_sala = Tv()
# tv_quarto = Tv()

# # print(tv_sala.cor)
# tv_sala.mudar_canal('Globo')
# print(tv_sala.canal)

class Tv:
#atributo de classe
    cor = 'preta'

    # todos os atributos que são de instância vão ter o self na frente
    def __init__(self, tamanho):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = 'Netflix'
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

tv_sala = Tv(55)
tv_quarto = Tv(70)

print(tv_sala.tamanho)

#atributo da classe muda todas as instâncias // não é recomendo fazer isso
Tv.cor = 'branca'

print(tv_sala.cor)
print(tv_quarto.cor)
