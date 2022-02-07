from typing import Type


class Cliente:
    def __init__(self, cpf, nome) -> None:
        self.cpf = cpf
        self.nome = nome  

    
    @property
    def cliente(self):
        return self.nome

    def __str__(self) -> str:
        return self.nome

class Produto:
    def __init__(self, codigo, descricao, preco) -> None:
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco

    # @property
    # def descricao(self):
    #     return self.descricao

    def __str__(self) -> str:
        return self.descricao

class ItemVendido:
    def __init__(self, produto: Type[Produto], quantidade ) -> None:
        
        self.quantidade = quantidade
    
        # Relacionando o item venda ao produto
        self.produto = produto

    def __str__ (self):
        return self.produto.codigo, " - ",self.produto.descricao, " - ", self.produto.preco, ' - ', self.quantidade, ' - ', self.valorUnitario

class Venda:
    def __init__(self, data, formaPagamento, cliente: Type[Cliente]) -> None:
        self.data = data
        self.total = 0
        self.formaPagamento = formaPagamento
        # Associação com cliente
        self.cliente = cliente        
        # Composicao 
        self.itens = []

    def additens(self, produto: Type[Produto], quantidade: int):
        item = ItemVendido(produto, quantidade)
        self.itens.append(item)
        

    def list_itens(self) -> None:
        
        for i in self.itens:            
            print(i.produto.descricao, i.produto.preco, 'quant ', i.quantidade, 'Vl. Unit: ', i.produto.preco, 'forma de Pag', self.formaPagamento)
            self.total += i.quantidade * i.produto.preco

        return f"Total: {self.total}"

  
    def __str__(self) -> str:
        return  f'Cliente: {self.cliente.nome}'

cliente = Cliente('01761433323', 'Elicarlos')
print("Cliente", cliente)

camisa = Produto('01414111','camisa', 250)
vestido = Produto('01414111','Vestido Azul', 75)

venda = Venda(12-12-2021, 'Cartao', cliente)

venda.additens(camisa, 2 )
venda.additens(vestido, 1 )





print(venda.list_itens())