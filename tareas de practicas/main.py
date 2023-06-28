from persona import Persona
from hermano import Hermano

persona = Persona()

persona.establecer_nombre(str(input("nombre: ")))
persona.establecer_apellido(str(input("apellido: ")))
persona.establecer_edad(int(input("edad: ")))



persona.mostrar()
if persona.esMayorDeEdad():
    print("Es mayor de edad")
else:
    print("es un pendejo ql")


hermano = Hermano()

hermano.creanombre(str(input("nombre supuesto hermano: ")))
hermano.creaapellido(str(input("apellido supuesto hermano: ")))
hermano.creaedad(int(input("edad supuesto hermano: ")))
hermano.mostrarhermano()


if hermano.MayorDeEdad():
    print("Tambien es mayor de edad")

else:
    print("tambien es un pendejo ql")

if hermano.creaapellido == persona.establecer_apellido:
    print("Efectivamente son hermanos")

else: 
    print("No son hermanos estos wnes")




