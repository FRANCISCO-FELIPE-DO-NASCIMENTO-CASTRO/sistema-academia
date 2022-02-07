from typing import Type

# from classes.bandeira import Bandeira



# from classes.bandeira import Bandeira

class Cartao:
    # def __init__(self, descricao, bandeira: Type[Bandeira]):
    #     self.descricao = descricao
    #     self.bandeira = bandeira

    # def __str__(self) -> str:
    #     return f"Cartao {self.descricao} - bandeira: {self.bandeira.descricao} "
    def __init__(self, descricao) -> None:
        self.descricao = descricao
        self.bandeira = None


    
    # def adiciona_bandeira(self, bandeira: Type[Bandeira]):
    #     self.bandeira = bandeira

    def dadosCartao(self):
        print(f"Cartao:  {self.descricao} bandeira {self.bandeira.descricao}")

    def __str__(self) -> str:
        return self.descricao
        

