class Cliente:
    def __init__(self, nome, idade) -> None:
        self.__nome = nome   
        self.__idade = idade   

    def adiciona(self, cliente):
        clientes = []
        clientes.append(cliente)
    
    def __str__(self) -> str:
        return (self.__nome, self.__idade)

c = Cliente('Elicarlos', 15)
c.adiciona(c)

for c in c:
    print(c)
