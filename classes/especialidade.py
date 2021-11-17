class Especialidade:
    def __init__(self, especialidade):
        self.__especialidade = especialidade

    @property
    def especialidade(self):
        return self.__especialidade

    def __str__(self):
        return self.especialidade