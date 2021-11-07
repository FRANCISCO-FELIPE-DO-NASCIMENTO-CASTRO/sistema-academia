class Academia:
    def __init__(self, cnpj, nome):
        self.cnpj=cnpj
        self.nome=nome

    def __str__ (self):
        return "cnpj:{}\n nome:{}\n"\
            .format(self.cnpj,self.nome)

class Personal:
    def __init__(self,nome,especialidade):
        self.nome=nome
        self.especialidade=especialidade

    def __str__(self):
        return "nome:{}\n especialidade:{}\n"\
            .format(self.nome,self.especialidade)
         

class Aluno:
    def __init__ (self, nome, idade, peso, altura, matricula, tipo_treino, mensalidade):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
        self.matricula=matricula
        self.tipo_treino=tipo_treino
        self.mensalidade=mensalidade
        self.cadastrar=None


    def pagar_mensalidade(self):
        print('Mensalidade paga')

    def calcularImc (self):
        print ('O IMC de {} é: {}'.format(self.nome,self.peso/self.altura**2))
    
    def fazerMatricula(self,academia):
        if type(academia)==Academia:
            self.cadastrar=academia

    def __str__ (self):
        return "nome:{}\n idade:{}\n peso:{}\n altura:{}\n matricula:{}\n tipo_treino:{}\n mensalidade:{}\n cadastrar:{}\n"\
            .format(self.nome,self.idade,self.peso,self.altura,self.matricula,self.tipo_treino,self.mensalidade,self.cadastrar)

academia= Academia (14778536905,"training")
print(academia)
francisco= Aluno("Francisco", 21, 120, 1.88, 123456, "aerobica",100)
print(francisco)
francisco.pagar_mensalidade()
francisco.calcularImc()
francisco.fazerMatricula("training")
print(francisco)
