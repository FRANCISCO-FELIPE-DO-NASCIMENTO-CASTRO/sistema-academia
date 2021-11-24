class Matricula:
    def __init__(self, id): #dataAtual, plano, vencimento, desconto, valorFinal, situacao, dataFim, aluno=None):
        self.__id = id
        
        # self.__dataAtual = dataAtual
        # self.__plano = plano
        # self.__vencimento = vencimento
        # self.__desconto = desconto
        # self.__valorFinal = valorFinal
        # self.__situacao = situacao
        # self.__dataFim = dataFim
        # self.__aluno = aluno

    
    def gerar_comprovante(self):
        aluno = "Elicarlos Ferreira dos Santos "
        cpf = "014.7557.141-89"
        modalidade = 'Musculação'
        dia  = 18
        mes  = 'novembro'
        ano = 2021
        # Declaramos, para os devidos fins, que o(a) aluno(a)___ está devidamente matriculado(a) na modalidade _______
        # data
        from reportlab.pdfgen import canvas
        
        def comprovante(c):
            c.setFont("Helvetica", 20)
            c.drawString(160,800,'Comprovante de matricula')
            c.setFont("Helvetica", 12)
            c.drawString(20,740,f'Declaramos, para os devidos fins, que o(a) aluno(a) {aluno} cpf: {cpf}')
            c.drawString(20,720,f'está devidamente matriculado(a) na modalidade {modalidade}')
            c.drawString(150,620, '_______________________________________________')
            c.drawString(220,600,f'Teresina {dia} de {mes} de {ano}')


            c.setFont("Helvetica", 20)
            c.drawString(160,400, 'Comprovante de matricula')
            c.setFont("Helvetica", 12)
            c.drawString(20,340,f'Declaramos, para os devidos fins, que o(a) aluno(a) {aluno} cpf: {cpf}')
            c.drawString(20,320,f'está devidamente matriculado(a) na modalidade {modalidade}')
            c.drawString(150,220, '________________________________________________')
            c.drawString(220,200,f'Teresina {dia} de {mes} de {ano}')

            

        c = canvas.Canvas('comprovante-matricula.pdf')
        comprovante(c)
        c.showPage()
        c.save()



        