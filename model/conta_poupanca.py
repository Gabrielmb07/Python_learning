from contas import Conta
class Conta_poupanca:
    def __init__(self,rendimento:int,saldo:int,id:int,id_agencia:str):
        super().__init__(saldo,id,id_agencia)
        self._rendimento=rendimento
    @property
    def rendimento(self):
        return self._rendimento
    @rendimento.setter
    def rendimento(self,rendimento:int):
        self._rendimento=rendimento
