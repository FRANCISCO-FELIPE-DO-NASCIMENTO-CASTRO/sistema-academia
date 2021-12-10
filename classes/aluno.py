class Aluno:
    def __init__(self, 
    nome,endereco, bairro, cep,
    cidade, estado, fone, celular,
    sexo, cpf, nascimento, email,
    estadoCivil, profissao, empresa,
    objetivo, debito, matriculado ):
        self.__nome = nome
        self.__endereco = endereco
        self.__bairro = bairro
        self.__cep = cep
        self.__cidade = cidade
        self.__estado = estado
        self.__fone = fone
        self.__celular = celular
        self.__sexo = sexo
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__email = email
        self.__estadoCivil = estadoCivil
        self.__profissao = profissao
        self.__empresa = empresa
        self.__objetivo = objetivo
        self.__debito = debito
        self.__matriculado = matriculado   

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def bairro(self):
        return self.__bairro
    
    @property
    def cep(self):
        return self.__cep


    @property
    def cidade(self):
        return self.__cidade
       
    @property
    def estado(self):
        return self.__estado

    @property
    def fone(self):
        return self.__fone

    @property
    def celular(self):
        return self.__celular

    @property
    def sexo(self):
        return self.__sexo

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nascimento(self):
        return self.__nascimento

    @property
    def email(self):
        return self.__email

    @property
    def estadoCivil(self):
        return self.__estadoCivil


    @property
    def profissao(self):
        return self.__profissao


    @property
    def empresa(self):
        return self.__empresa

    @property
    def objetivo(self):
        return self.__objetivo


    @property
    def debito(self):
        return self.__debito

    @property
    def matriculado(self):
        return self.__matriculado

    def __str__(self) -> str:
        return self.__nome
        

    
    