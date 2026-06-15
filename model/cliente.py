from pessoa import Pessoa
class Cliente (Pessoa):
    def __init__(self,score:int,tipo:str,nome:str,cpf:str,idade:int,cidade:str):
        super().__init__ (nome,cpf,idade,cidade)
        self._score=score
        self._tipo=tipo
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,score:int):
        self._score=score
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,tipo:str):
        self._tipo=tipo