

from classes.aluno import Aluno
from classes.bandeira import Bandeira
from classes.cartoes import Cartao
# from classes.pagamento import Pagamento
from classes.plano import Plano
from classes.modalidade import Modalidade

from classes.instrutor import Instrutor
from classes.matricula import Matricula
# from controllers.controller import Controller
from controllers.databasecontroller import DataBaseController
from models.banco_academia import DataBase
from telaPrincipal import TelaPrincipal


# # musculacao = Especialidade('Musculação')

# # instrutor = Instrutor('Paulo Cintura', '014.545.788-78', 2500)
# # instrutor.adicionar_especialidade(musculacao)

# # print(instrutor)

# # modalidade = Modalidade('Musculação', 500.00)

# # modalidade2 = Modalidade('CrossFit', 500.00)

# aluno = Aluno('Francisco dos Anzois', 'Q C', 'Vila Maria', '64060-115','Teresina','Piaui', '869998444', '86 9880045474','M', '01761432389', '11-03-1985','fra@hotmail.com','casado','estudante', 'Solution', 'Emagrecer', 0.0, False)
# # aluno2 = Aluno('Isaac Nunes dos Santos', '016.514.000-99', 'M','64060-115', 'Q C', '50',' Vila Maria', 'Teresina', 'Piaui', '86-98841-7874', 'isaac@hotmail.com', '12221')
# # aluno3 = Aluno('Maria Rosa', '017.514.894-78', 'F','64060-115', 'Q C', '50',' Vila Maria', 'Teresina', 'Piaui', '86-98841-7874', 'francisco@hotmail.com', '1212121')

# # plano_smart = Plano('Plano Smart',
# #  'Treine o quanto quiser na sua unidade, sem taxa de cancelamento.',79.90)

# # matricula = Matricula(1)
# # matricula.gerar_comprovante()

# # plano_smart.matricular_aluno(aluno)
# # plano_smart.matricular_aluno(aluno2)
# # plano_smart.matricular_aluno(aluno3)


# # print(plano_smart)




# def main():
#     banco = DataBaseController()
#     banco.criar_banco()
#     banco.criar_tabelas()
#     controller = Controller()
#     # controller.adiciona_modalidade(modalidade)
#     # controller.adiciona_modalidade(modalidade2)
#     # matricula = Matricula()
#     # matricula.fazer_matricula(
#     #     'Elicarlos Ferreira', modalidade, 11-12-2021, 'Treino', 11-12-2022, 0, 0, 'Ativo', 11-12-2022)

#     controller.adiciona_aluno(aluno)

   

    
    

   
#     # Uma Forma de implementar
#     # nubank = Cartao("Nubank", master)
#     # hiper = Cartao("Hiper card", master)
#     # cea = Cartao("Cea", visa)


#     # Manutenção anual:
#     plano = Plano("PLANO SMART",0, 79.90, 0)

#     plano2 = Plano("PLANO BLACK",0 , 119.90, 0 )
#     aluno2 = Aluno('Elicarlos Ferreira', 'Q C', 'Vila Maria', '64060-115','Teresina','Piaui', '869998444', '86 9880045474','M', '01761432389', '11-03-1985','fra@hotmail.com','casado','estudante', 'Solution', 'Emagrecer', 0.0, False)
    
#     plano2 = Plano("PLANO BLACK",0 , 119.90, 0 )
#     aluno3 = Aluno('Pedro Gonzales', 'Q C', 'Vila Maria', '64060-115','Teresina','Piaui', '869998444', '86 9880045474','M', '01761432389', '11-03-1985','fra@hotmail.com','casado','estudante', 'Solution', 'Emagrecer', 0.0, False)



#     matricula = Matricula(aluno, plano,  20, "12-12-2022")
#     matricula2 = Matricula(aluno2, plano2,  20, "12-12-2022")
#     matricula3 = Matricula(aluno3, plano2, 20, "15-12-2021")

#     matricula.dados_matricula()
#     matricula2.dados_matricula()
#     matricula3.dados_matricula()

#     matricula.gerarMensalidade()
#     matricula2.gerarMensalidade()
#     matricula3.gerarMensalidade()

#     print("Debito do aluno 1")
#     print(aluno.debito)
  
#     hiper = Cartao("Hiper")
#     nubank = Cartao("Nubank")
#     credishop = Cartao("credishop")
#     # credishop = Cartao("credishop")
#     # picpay = Cartao("picpay")
#     # losango = Cartao("losango")
#     # nubank = Cartao("Nubank")

#     visa = Bandeira("Visa")
#     visa.adicionaCartao(nubank)
#     credishop = Bandeira("credishop")
#     credishop.adicionaCartao(credishop)
    
    

#     visa.adicionaCartao(hiper)
    
#     print("Lista de cartao credishop")
#     credishop.listaCartao()
#     print("Lista de cartao Visa")
#     visa.listaCartao()



#     print("Numero de mensalidade aluno 1")
#     aluno.listaMensalidade()
#     print("Numero de mensalidade aluno 2")
#     aluno2.listaMensalidade()

#     print("Numero de mensalidade aluno 3")
#     aluno3.listaMensalidade()
#     # master = Bandeira("Master")


#     # nubank.adiciona_bandeira(master)
#     # nubank.dadosCartao()
#     # hiper.adiciona_bandeira(visa)
#     # hiper.dadosCartao()

#     print("__________________________")
#     # print("_____", nubank)
#     # print("_____", cea)
#     # controller.adiciona_aluno(aluno2)
#     # controller.adiciona_aluno(aluno3)
#     # controller.deletar(1)
#     # controller.buscar_aluno_por_id(10)
#     # controller.listar_aluno()
def main():
    tela = TelaPrincipal()
    tela.principal()
    

if __name__ == '__main__':
    main()
    
