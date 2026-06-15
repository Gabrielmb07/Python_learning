class Pessoa:
    def __init__(self,nome:str,cpf:str,idade:int,cidade:str):
        self._nome=nome
        self._cpf=cpf
        self._idade=idade
        self._cidade=cidade
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self,cpf:str):
        self._cpf=cpf
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome:str):
        self._nome=nome
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self,idade:int):
        self._idade=idade
    @property
    def cidade(self):
        return self._cidade
    @cidade.setter
    def cidade(self,cidade:str):
        self._cidade=cidade
