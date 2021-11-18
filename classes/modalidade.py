class Modalidade:
    def __init__(self, id, modalidade, valor):
        self.__id = id
        self.__modalidade = modalidade
        self.__valor = valor

    @property
    def modalidade(self):
        return self.__modalidade

    
    def __str__(self):
        return self.modalidade