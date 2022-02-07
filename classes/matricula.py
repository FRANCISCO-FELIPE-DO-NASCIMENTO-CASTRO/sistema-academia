from typing import Type
from datetime import datetime
from classes.plano import Plano
from classes.aluno import Aluno
from classes.mensalidade import Mensalidade




class Matricula:
    def __init__(self, aluno: Type[Aluno], plano: Type[Plano], diaVencimento, dataFinal): #dataAtual, plano, vencimento, desconto, valorFinal, situacao, dataFim, aluno=None):
        # Associação com a classe aluno
        self.aluno = []
        # Associação com a classe Plano      
        self.plano = plano
        self.dataVigencia = datetime.now()
        self.diaVencimento = diaVencimento
        self.dataFim = dataFinal
        self.desconto = 0
        self.valorFinal = self.valor_final()

      
        # self.__FOREIGN KEY(id_empresa) REFERENCES Empresa(id),'\
        # self.__FOREIGN KEY(id_aluno) REFERENCES Aluno(id),'\
        # self.__FOREIGN KEY(id_modalidade) REFERENCES Modalidade(id))'


    def matriculaAluno(self, aluno):
        self.aluno.append(aluno)

    def valor_final(self):
        self.valorFinal = self.plano.mensalidade + self.plano.adesao + self.plano.taxaManutencao
        return self.valorFinal

    def gerarMensalidade(self):
        print("estou em mensalidade")
        mensalidades = []
               
        cont = 1
        mensalidade = Mensalidade(self.aluno.nome ,cont, self.diaVencimento, self.plano.mensalidade)
        mensalidade.statusPendente()
        print(mensalidade.dadosMensalidade())
        mensalidades.append(mensalidade)

        total = self.plano.mensalidade + ((self.plano.adesao + self.plano.taxaManutencao) / 11)
        cont = 2
        while cont <= 12:
            mensalidade = Mensalidade(self.aluno.nome ,cont, self.diaVencimento, total)
            mensalidade.statusPendente()
            mensalidades.append(mensalidade)
            print(mensalidade.dadosMensalidade())
            cont += 1
        print("Valor final:  ", self.valorFinal)

        soma = 0
        for mensalidade in mensalidades:
            soma += mensalidade.valor
        self.aluno.debito = soma
        print("Soma gerar >>>>>>>>>>>>> ",self.aluno.debito)


        for m in mensalidades:
            self.aluno.adicionaMensalidade(m)

       
       
    def dados_matricula(self):
        print(f"Aluno: {self.aluno.nome} {self.dataVigencia} matriculado plano {self.plano.descricao} Valor: {self.valorFinal}")
       
    


        
       
                   
    
    # def gerar_comprovante(self):
    #     aluno = "Elicarlos Ferreira dos Santos "
    #     cpf = "014.7557.141-89"
    #     modalidade = 'Musculação'
    #     dia  = 18
    #     mes  = 'novembro'
    #     ano = 2021
    #     # Declaramos, para os devidos fins, que o(a) aluno(a)___ está devidamente matriculado(a) na modalidade _______
    #     # data
    #     from reportlab.pdfgen import canvas
        
    #     def comprovante(c):
    #         c.setFont("Helvetica", 20)
    #         c.drawString(160,800,'Comprovante de matricula')
    #         c.setFont("Helvetica", 12)
    #         c.drawString(20,740,f'Declaramos, para os devidos fins, que o(a) aluno(a) {aluno} cpf: {cpf}')
    #         c.drawString(20,720,f'está devidamente matriculado(a) na modalidade {modalidade}')
    #         c.drawString(150,620, '_______________________________________________')
    #         c.drawString(220,600,f'Teresina {dia} de {mes} de {ano}')


    #         c.setFont("Helvetica", 20)
    #         c.drawString(160,400, 'Comprovante de matricula')
    #         c.setFont("Helvetica", 12)
    #         c.drawString(20,340,f'Declaramos, para os devidos fins, que o(a) aluno(a) {aluno} cpf: {cpf}')
    #         c.drawString(20,320,f'está devidamente matriculado(a) na modalidade {modalidade}')
    #         c.drawString(150,220, '________________________________________________')
    #         c.drawString(220,200,f'Teresina {dia} de {mes} de {ano}')

            

    #     c = canvas.Canvas('comprovante-matricula.pdf')
    #     comprovante(c)
    #     c.showPage()
    #     c.save()



        