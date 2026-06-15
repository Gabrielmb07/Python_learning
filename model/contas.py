class Conta:
    def __init__(self,saldo:int,id:int,id_agencia:str):
        self._saldo=saldo
        self._id=id
        self._id_agencia=id_agencia
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,saldo:int):
        self._saldo=saldo
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id:int):
        self._id=id
    @property
    def id_agencia(self):
        return self._id_agencia
    @id_agencia.setter
    def id_agencia(self,id_agencia:int):
        self._id_agencia=id_agencia