class Usuario:
    def __init__(self, usuario, email, senha):
        self.__usuario = usuario
        self.__email = email
        self.__senha = senha

    @property
    def usuario(self):
        return self.__usuario

    @property
    def email(self):
        return self.__email


    def adicionar_usuario(self):
        pass

    def atualizar_usuario(self):
        pass

    def remove_usuario(self):
        pass


    def recuperar_senha(self):
        pass
        
    def __str__(self):
        return f'Usuario: { self.usuario } - email: {self.email}'