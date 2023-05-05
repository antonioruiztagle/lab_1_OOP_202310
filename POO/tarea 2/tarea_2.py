# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:07:38 2023

@author: anton
"""

def import_data(nombre_archivo):
    separador = ";"
    with open(nombre_archivo,encoding = "utf-8") as archivo:
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

def export_tables_by_region(data,filename):
    regiones = []
    for element in data:
        if element["region"] not in regiones:
            regiones.append(element["region"])
    listanueva=[]
    for region in regiones:
        contador = 0
        for elemento in data:
            if elemento["region"] == region:
                contador += 1
        conteo = contador/4
        listanueva.append([region,conteo])

    with open(filename,"w",encoding = "utf-8") as archivo:
        for line in listanueva:
            archivo.write(f"{line[0]} {int(line[1])}\n")


def export_general_results(data, filename):
    candidatos = []
    for element in data:
        if element["candidato"] not in candidatos:
            candidatos.append(element["candidato"])

    lista_nueva = []
    for candidato in candidatos:
        contador = 0
        for dato in data:
            if dato["candidato"] == candidato:
                contador += dato["votos tricel"]
        lista_nueva.append([candidato,contador])
        
    with open(filename,"w",encoding = "utf-8") as archivo:
        for linea in lista_nueva:
            archivo.write(linea[0])
            archivo.write(" ")
            archivo.write(str(linea[1]))
            archivo.write("\n")

def export_count_by_local(data,filename):
    local = input("ingrese el nombre del local: ")
    listanueva = []
    candidatos = []
    for element in data:
        if element["candidato"] not in candidatos:
            candidatos.append(element["candidato"])
    for candidato in candidatos:
        contador = 0
        for element in data:
            if element["local"] == local and element["candidato"] == candidato:
                contador += element["votos tricel"]
        listanueva.append([candidato,contador])
    with open(filename,"w",encoding = "utf-8") as archivo:
        for linea in listanueva:
            archivo.write(linea[0])
            archivo.write(" ")
            archivo.write(str(linea[1]))
            archivo.write("\n")

           

data = import_data("data.csv")
export_count_by_local(data,"candidatoslocal.csv")
export_general_results(data, "resultadosgenerales.csv")
export_tables_by_region(data, "tablasporregion.csv")



        
               
        
        