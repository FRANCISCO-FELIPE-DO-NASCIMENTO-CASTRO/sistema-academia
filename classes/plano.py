class Plano:
    def __init__(self, plano, descricao, preco) -> None:
        self.__plano = plano
        self.__descricao = descricao
        self.__preco = preco
        self.__alunos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def plano(self):
        return self.__plano

    def matricular_aluno(self, aluno):
        self.__alunos.append(aluno)
        print(f'Aluno: {aluno.nome} cadastrado no curso {self.__plano}')
        

    def remover_aluno(self, aluno):
        self.__alunos.remove(aluno)
        print(f'Aluno: {aluno.nome} removido com sucessso!') 

    def __str__(self):
        s1 = (f'Aluno matriculados no {self.plano}\n')
        s2 = ""
        for i in range(len(self.__alunos)):
            s2 = s2 + " - " + self.__alunos[i].nome + "\n"

        return s1 + s2            