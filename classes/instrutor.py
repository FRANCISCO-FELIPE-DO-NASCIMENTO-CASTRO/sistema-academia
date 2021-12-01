
class Instrutor:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
        self.__especialidade = []

    @property
    def nome(self):
        return self.__nome

    
    def adicionar_especialidade(self, especialidade):
        self.__especialidade.append(especialidade)
        print('Especialidade adicionada com sucesso')

    def remove_especialidade(self, especialidade):
        self.__especialidade.remove(especialidade)
        print('Removida com sucesso')

    def __str__(self):
        nome = self.nome + '\n'
        s1 = ("ESPECIALIDADE\n")
        s = ""
        for i in range(len(self.__especialidade)):
            s = s + " _ " + self.__especialidade[i].especialidade

        return nome + s1 + s
            
    
        

    