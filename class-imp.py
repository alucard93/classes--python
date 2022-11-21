import os
os.system('cls')

class Tv():
    #atributos
    cor = 'preta'
    tamanho = 55
    canal = 10
    volume = 50
    ############

    #métodos
    def mudar_canal(self):
        pass

    def mudar_volume(self):
        pass

    def ligar_desligar(self):
        pass

print(Tv.canal)
print(Tv.cor)


## vantagem da orientação a objeto com relação a estruturada
# Reaproveitando de código sem precisar refazer/copiar tudo
# Encapsulamento -> proteção a mudanças indesejadas - os metodos utilizados estarão todo contidos dentro da classe 
# Herança -> Instâncias do objeto tem as mesmas caracteristicas, apesar de ter valores diferentes - recebe de alguem alguma informação ja criada
# Polimorfismo -> Um mesmo método pode ter várias "formas" em diferentes classes (ou subclasses) - ex: Animais -> Gatos x Cachorros   