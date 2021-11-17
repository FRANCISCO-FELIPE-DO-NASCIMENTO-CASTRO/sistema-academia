class Empresa:
    def __init__(self, cnpj, razao_social, fantasia, cep, rua, numero, casa, cidade, estado):
        self.__cnpj = cnpj
        self.__razao_social = razao_social
        self.__fantasia = fantasia
        self.__cep = cep
        self.__rua = rua
        self.__numero = numero
        self.__casa = casa
        self.__cidade =  cidade
        self.__estado = estado


    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def fantasia(self):
        return self.__fantasia

    @property
    def cep (self):
        return self.__cep

    @property
    def rua (self):
        return self.__rua

    @property
    def numero (self):
        return self.__numero

    @property
    def casa(self):
        return self.__casa

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    def __str__(self) -> str:
        return f'Cnpf: {self.cnpj} Razão Social: {self.razao_social}'
    
    



    