import csv

class CsvReader:
    @classmethod
    def __init__(self, filename):
        self.filename = filename
        

    @classmethod
    def read_file(self):
        separador = ";"
    
        with open(self.filename,encoding = "utf-8") as archivo:

            next(archivo)

            votos = []

            for i in archivo:

                i = i.rstrip("\n")
                columnas = i.split(separador)
                nro_region = int(columnas[0])
                region = columnas[1]
                provincia = columnas[2]
                circunscripcion_senatorial = int(columnas[3])
                distrito = int(columnas[4])
                comuna = columnas[5]
                circunscripcion_electoral = columnas[6]
                local = columnas[7]
                nro_mesa = int(columnas[8])
                tipo_de_mesa = columnas[9]
                mesas_fusionadas = columnas[10]
                electores = int(columnas[11])
                nro_en_voto = int(columnas[12])
                candidato = columnas[13]
                votos_tricel = int(columnas[14])   

                votos.append({
                    "nro. region": nro_region, 
                    "region": region,
                    "provincia":  provincia,
                    "circunscripcion senatorial": circunscripcion_senatorial,
                    "distrito": distrito, 
                    "comuna": comuna, 
                    "circunscripcion electoral": circunscripcion_electoral, 
                    "local": local, "nro. mesa": nro_mesa, 
                    "tipo de mesa": tipo_de_mesa,
                    "mesas fusionadas": mesas_fusionadas,
                    "electores": electores, 
                    "nro. en voto": nro_en_voto,
                    "candidato": candidato, 
                    "votos tricel": votos_tricel
                    })
                
        
        return votos
    

    

        



    


      
