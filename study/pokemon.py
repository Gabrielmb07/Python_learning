class Pokemon:
    def __init__(self,nome:str,tipo:str,evolucao:int,treinador:str):
        self.nome=nome
        self.tipo=tipo
        self.evolucao=evolucao
        self.treinador=treinador
    def atacando(self):
        print(f'{self.nome} esta atacando')

pokemons=[]
while True:
    ver_ou_inserir=int(input("Deseja inserir um pokemon,1, ou visualizar um pokemon,2? "))
    if ver_ou_inserir==1:
        nome=input("Digite o nome do seu pokemon: ")
        tipo=input("Digite o tipo de seu pokemon: ")
        evolucao=int(input("Digite a evolucao de seu pokemon: "))
        treinador=input("Digite o treinador desse pokemon: ")
        pokemon=Pokemon (nome,tipo,evolucao,treinador)
        pokemons.append (pokemon)

    elif ver_ou_inserir ==2:
        for pok in pokemons:
            pok.atacando()