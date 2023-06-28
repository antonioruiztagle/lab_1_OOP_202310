class Hermano:
    def __init__(self, nombre = "", apellido = "", edad = ""):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def creanombre(self, nombre):
       
        self.nombre = nombre

    def obtennombre(self):

        return self.nombre
        
    def creaapellido(self, apellido):
        
        self.nombre = apellido

    def obtenapellido(self):

        return self.apellido
    
    def creaedad(self, edad):
        
        self.edad = edad

    def obtenedad(self):

        return self.edad
    
    def mostrarhermano(self):

        print(self.nombre) 
        print(self.apellido)
        print(self.edad)
    
    def MayorDeEdad(self):
        return  self.edad >= 18


        

    