class Agencia:
    def __init__(self,id:int,nome:str,cidade:str):
        self._id=id
        self._nome=nome
        self._cidade=cidade
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id:int):
        self._id=id
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome:str):
        self._nome=nome
    @property
    def cidade(self):
        return self._cidade
    @cidade.setter
    def cidade(self,cidade:str):
        self._cidade=cidade