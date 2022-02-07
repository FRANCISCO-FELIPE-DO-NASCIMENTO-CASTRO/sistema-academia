class Aluno:
    def __init__(self, codigo, nome) -> None:
        self.codigo = codigo
        self.nome = nome

    def __str__(self) -> str:
        return self.nome



class Matricula:
    def __init__(self, matricula) -> None:
        
        self.matricula = matricula
        self.aluno = []


    def adiciona(self, aluno):
        self.aluno.append(aluno)

    def lista(self):
        for a in self.aluno:
            print(self.matricula, " _ ", a.nome)



a = Aluno(1, "Elicarlos")
a1 = Aluno(12, "Isaaac")

m1= Matricula(1)

m2= Matricula(2)
m2.adiciona(a)
m2.adiciona(a)
m2.adiciona(a)
m1.adiciona(a)
m1.adiciona(a1)

print(a)
m1.lista()
m2.lista()
