import os 
os.system('cls')

#__init__ - quando eu chamar a class Tv automaticamente ele vai chamar a função do metodo
# sempre que vc estiver dentro de uma classe e quiser referenciar a classe pode usar o 'self'
#ex: self.cor = 'preta'  pode-se ler que é uma variavel cor da classe Tv // parametro cor da classe Tv
#metódo é uma função dentro de uma classe
# () - indica que é um metódo, se n tiver é um atributo
class Tv:

#self.atributo igual ao valor inicial
    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 10

    def mudar_canal(self):
        self.canal = 'Disney+'


#realizando a criação de uma instância da classe Tv - Herença//Reaproveitamento de código
tv_sala = Tv()
tv_quarto = Tv()

print(tv_sala.cor)
tv_sala.mudar_canal()
print(tv_sala.canal)