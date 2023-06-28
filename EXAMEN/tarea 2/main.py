import csv


def import_data():
    file_name = input("Ingrese el nombre del archivo con los datos a leer: ")
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)  # Leer el encabezado
        for row in reader:
            data.append(dict(zip(header, row)))
    return data


def export_tables_by_region(data, filename):
    tables_by_region = {}
    header = data[0].keys()  # Obtener el encabezado del primer diccionario en la lista
    
    region_key = None
    for key in header:
        if key.lower().replace('.', '') == 'region':
            region_key = key
            break
    
    if not region_key:
        print("No se encontró la clave 'Región' en el archivo.")
        return
    
    for row in data:
        region = row[region_key]
        if region in tables_by_region:
            tables_by_region[region] += 1
        else:
            tables_by_region[region] = 1
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Región', 'Cantidad de Mesas'])
        for region, count in tables_by_region.items():
            writer.writerow([region, count])


def export_general_results(data, filename):
    general_results = {}
    for row in data:
        candidate = row['Candidato']
        votes = row['Votos TRICEL']
        if candidate in general_results:
            general_results[candidate] += int(votes)
        else:
            general_results[candidate] = int(votes)
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Candidato', 'Votos'])
        for candidate, votes in general_results.items():
            writer.writerow([candidate, votes])


def export_count_by_local(data, filename):
    local = input("Ingrese el nombre del local que desea analizar: ")
    
    count_by_local = {}
    for row in data:
        if row['Local'] == local:
            candidate = row['Candidato']
            votes = row['Votos TRICEL']
            if candidate in count_by_local:
                count_by_local[candidate] += int(votes)
            else:
                count_by_local[candidate] = int(votes)
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Candidato', 'Votos'])
        for candidate, votes in count_by_local.items():
            writer.writerow([candidate, votes])


# Uso de las funciones
data = import_data()
export_tables_by_region(data, 'mesas_por_region.csv')
export_general_results(data, 'recuento_general.csv')
export_count_by_local(data, 'conteo_por_local.csv')
