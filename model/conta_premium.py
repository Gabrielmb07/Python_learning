from contas import Conta
class Conta_premium:
    def __init__(self,pontos:int,saldo:int,id:int,id_agencia:str):
        super().__init__(saldo,id,id_agencia)
        self._pontos=pontos
    @property
    def pontos(self):
        return self._pontos
    @pontos.setter
    def pontos(self,pontos:int):
        self._pontos=pontos