class Animal:
    def __init__(self,nome:str):
        self.nome=nome
    def speak(self):
        pass

class Dog (Animal):
    def speak(self):
        print(f'{self.nome} esta latindo')
class Cat (Animal):
    def speak(self):
        print(f'{self.nome} esta miando')
class Vaca (Animal):
    def speak(self):
        print(f'{self.nome} esta mugindo')

fala=[]
while True:
    inserir_ou_ver=int(input("Voce quer inserir um novo animal,1, ou ver todos os animais falando,2: "))
    if inserir_ou_ver==1:
        nome=input("Qual o nome do animal voce deseja inserir? ")
        tipo=input("Qual o tipo de animal e esse? ")
        if tipo=="Dog":
            dog=Dog (nome)
            fala.append(dog)
        elif tipo=="Cat":
            cat=Cat (nome)
            fala.append(cat)
        elif tipo=="Vaca":
            vaca=Vaca (nome)
            fala.append(vaca)

    elif inserir_ou_ver==2:
        for fal in fala:
            fal.speak()