from pessoa import Pessoa
class Funcionario (Pessoa):
    def __init__(self,id_agencia:int,salario:int,cargo:str,nome:str,cpf:str,idade:int,cidade:str):
        super().__init__(nome,cpf,idade,cidade)
        self._salario=salario
        self._cargo=cargo
        self._id=id_agencia
    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self,salario:int):
        self._salario=salario
    @property
    def cargo(self):
        return self._cargo
    @cargo.setter
    def cargo(self,cargo:str):
        self._cargo=cargo
    @property
    def id_agencia(self):
        return self._id_agencia
    @id_agencia.setter
    def id_agencia(self,id_agencia:int):
        self._id_agencia=id_agencia