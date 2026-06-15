from contas import Conta
class Conta_corrente:
    def __init__(self,salario:int,saldo:int,id:int,id_agencia:str):
        super().__init__(saldo,id,id_agencia)
        self._salario=salario
    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self,salario:int):
        self._salario=salario