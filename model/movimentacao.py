class Movimentacao:
    def __init__ (self,movimentacao:str,tipo_movimentacao:str,id_movimentacao:int,id_conta:int):
        self._movimentacao=movimentacao
        self._tipo_movimentacao=tipo_movimentacao
        self._id_movimentacao=id_movimentacao
        self._id_conta=id_conta
    @property
    def movimentacao(self):
        return self._movimentacao
    @movimentacao.setter
    def movimentacao(self,movimentacao:int):
        self._movimentacao=movimentacao
    @property
    def tipo_movimentacao(self):
        return self._tipo_movimentacao
    @tipo_movimentacao.setter
    def tipo_movimentacao(self,tipo_movimentacao:int):
        self._tipo_movimentacao=tipo_movimentacao
    @property
    def id_movimentacao(self):
        return self._id_movimentacao
    @id_movimentacao.setter
    def id_movimentacao(self,id_movimentacao:int):
        self._id_movimentacao=id_movimentacao
    @property
    def id_conta(self):
        return self._id_conta
    @id_conta.setter
    def id_conta(self,id_conta:int):
        self._id_conta=id_conta