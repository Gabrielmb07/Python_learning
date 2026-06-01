class Dog:
    def __init__(self,name:str):
        self.name=name
    def latir(self):
        print(f'{self.name} esta latindo')

dog1=Dog("Rex")
dog2=Dog("Brutus")
dog3=Dog("Bidu")

cachorros=[]
cachorros.append (dog1)
cachorros.append (dog2)
cachorros.append (dog3)

for cach in cachorros:
    cach.latir()