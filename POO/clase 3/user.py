class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password


    def show_username(self, pwd):
        if pwd == self.__password:
            return self.__username
        return "no te puedo mostrar el nombre de usuario"
    

    def show_password(self, username):
        if username == self.__username:
            return self.__password
        return "No te puesdo mostrar la password"
    
    
    def change_passwrod(self, pwd, new_value):
        if pwd == self.__password:
            self.__password = new_value
            return "cambio existoso"
        return "cambio fallido" 

