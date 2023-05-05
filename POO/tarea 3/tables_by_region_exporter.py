class TablesByRegionExporter:
    

    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def export(self):

        regiones = []
        for element in self.data:
            if element["region"] not in regiones:
                regiones.append(element["region"])
        listanueva=[]
        for region in regiones:
            contador = 0
            for elemento in self.data:
                if elemento["region"] == region:
                    contador += 1
            conteo = contador/4
            listanueva.append([region,conteo])

        with open(self.filename,"w",encoding = "utf-8") as archivo:
            for line in listanueva:
                archivo.write(f"{line[0]} {int(line[1])}\n")  
                
        return archivo


