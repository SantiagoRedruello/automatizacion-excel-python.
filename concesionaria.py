import csv
from bs4 import BeautifulSoup

print("Iniciando el robot extractor...")

# 1. Simulación de la página web de la concesionaria
contenido_web = """
<html>
    <body>
        <span class="auto">Fiat Cronos - $5.000.000</span>
        <span class="auto">Toyota Hilux - $15.000.000</span>
        <span class="auto">Ford Fiesta - $3.500.000</span>
    </body>
</html>
"""

sopa = BeautifulSoup(contenido_web, 'html.parser')
autos_limpios = sopa.find_all('span', class_='auto')

print("Guardando los datos directamente en Excel...")

# 2. Creamos el archivo Excel (.csv)
with open("lista_autos_cliente.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Vehículo y Precio extraídos por el Robot"])
    
    for auto in autos_limpios:
        escritor.writerow([auto.text])

print("¡ÉXITO TOTAL! El archivo fue creado con éxito.")



