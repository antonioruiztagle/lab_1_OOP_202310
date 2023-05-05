class GeneralResultsExporter:

    def __init__(self, data, filename):
        self.data = data
        self.filename = filename


    def export(self):
        
        candidatos = []
        for element in self.data:
            if element["candidato"] not in candidatos:
                candidatos.append(element["candidato"])

        lista_nueva = []
        for candidato in candidatos:
            contador = 0
            for dato in self.data:
                if dato["candidato"] == candidato:
                    contador += dato["votos tricel"]
            lista_nueva.append([candidato,contador])
            
        with open(self.filename,"w",encoding = "utf-8") as archivo:
            for linea in lista_nueva:
                archivo.write(linea[0])
                archivo.write(" ")
                archivo.write(str(linea[1]))
                archivo.write("\n")

        return archivo



        