from parse_options import ParseOptions
from csv_reader import CsvReader
from general_results_exporter import GeneralResultsExporter
from tables_by_region_exporter import TablesByRegionExporter
from resluts_by_local_exporter import ResultsByLocalExporter


ParseOptions.display_menu()
# ParseOptions.get_option()
CsvReader.__init__("data.csv")

datos = CsvReader.read_file()


# mesas = TablesByRegionExporter(datos, "cantidad_mesas_por_region.csv")
# mesas.export()
# resultados = GeneralResultsExporter(datos, "ResultadosGenerales.csv")
# resultados.export()
# resultadolocal = ResultsByLocalExporter(datos, f"resultados_del_local_{nombrelocal}.csv", nombrelocal)
# resultadolocal.export()



opcion = ParseOptions.get_option()

if opcion == str(1):
    mesas = TablesByRegionExporter(datos, "cantidad_mesas_por_region.csv")
    mesas.export()
elif opcion == str(2):
    resultados = GeneralResultsExporter(datos, "ResultadosGenerales.csv")
    resultados.export()
elif opcion == str(3):
    nombrelocal = input("Elegir local: ")
    resultadolocal = ResultsByLocalExporter(datos, f"resultados_del_local_{nombrelocal}.csv", nombrelocal)
    resultadolocal.export()




















