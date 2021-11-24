class Funcao:
    def __init__(self, id, funcao):
        self.__id = id
        self.__funcao = funcao

    @property
    def funcao(self):
        return self.__funcao

        
    def __str__(self):
        return self.funcao