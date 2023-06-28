class Cuenta:
    def __init__(self, titular, cuenta):
        
        self.titular = titular
        self.cuenta = cuenta
        self.cuenta = 0

    def get_titular(self):
        return self.titular
    
    def set_titular(self, titular):
       
        self.titular = titular

    def get_cuenta(self):
        return self.cuenta

    def set_cuenta(self, cuenta):
        
        self.cuenta = cuenta

    def mostrar(self):

        print(self.titular)
        print(self.cuenta)


    def ingresar(self, cuenta):

        if cuenta > 0:
            self.cuenta += cuenta
        else:
           return False
    
    def retirar(self, cuenta):

        if cuenta > 0:
            self.cuenta -= cuenta
        else:
           return False

    def mostraractual(self):
        print(self.titular)
        print(self.cuenta)
        
     

cuenta = Cuenta(titular = "", cuenta = "")


cuenta.set_titular(str(input("nombre titular: ")))
cuenta.set_cuenta(int(input("cuenta actual: ")))
cuenta.ingresar(int(input("ingrese monto a abonar: ")))
cuenta.mostraractual()
cuenta.retirar(int(input("ingrese monto a retirar: ")))
cuenta.mostraractual()











    