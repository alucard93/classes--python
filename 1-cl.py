import os 
os.system('cls')

#__init__ - quando eu chamar a class Tv automaticamente ele vai chamar a função do metodo

class Tv:
    
#self.atributo igual ao valor inicial
    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 10

#realizando a criação de uma instância da classe Tv - Herença//Reaproveitamento de código
tv_sala = Tv()
tv_quarto = Tv()

print(tv_sala.cor)