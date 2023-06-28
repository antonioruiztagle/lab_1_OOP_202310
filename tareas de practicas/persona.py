class Persona:

    def __init__(self, nombre = "", edad = "", apellido=""):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

    def establecer_nombre(self, nombre):
         self.nombre = nombre
    def obtener_nombre(self):
        return self.nombre
    
    def establecer_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad tiene que ser un numero positivo")

    def obtener_edad(self):
        return self.edad 

    def establecer_apellido(self, apellido):
        self.apellido = apellido

    def obtener_apellido(self):
        return self.apellido
    
    def mostrar(self):
        
        self.nombre
        self.edad
        self.apellido

    def esMayorDeEdad(self):
        return self.edad >= 18
    


