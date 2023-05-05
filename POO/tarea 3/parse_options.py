class ParseOptions:
    # parse_options.py

    @classmethod
    def display_menu(self):

        
        print("MENU")
        print("1. Cantidad de mesas por region")
        print("2. Resultados generales")
        print("3. Resultados por local")


    
    @classmethod
    def get_option(self):

        opcion = input("elige una opcion: ")
        return opcion


