import matplotlib.pyplot as plt



vivienda = pd.read_csv("USA_Housing.csv")

# Sustituimos los nombres a español

vivienda.rename(columnas = {'Avg. Area Income': 'Ingresos medios de la zona', 'Avg. Area House Age': 'Edad media de la casa', 'Avg. Area Number of Rooms': 'Media de habitaciones', 'Avg. Area Number of Bedrooms ': 'Media de dormitorios', 'Area Population' :'Poblacion en la zona', 'Price':'Precio', 'Adress':'Direccion'}, inplace = True)

# Valores innecesarios que hemos limpiado

viviendas = viviendas.dropna(subset = ["Precio"])

print("Este es el nuevo dataset: ")
print(viviendas)

columnas = Columnas(viviendas)
columnas.count()

filas = Filas(viviendas)
filas.count()

max = Max(viviendas, "Precios")
max.calculo()

min = Min(viviendas, "Precios")
min.calculo()

suma_precios_viviendas = sum(precios)
media_precios_viviendas = suma_precios_viviendas/10001
print("La media de precios es {}".format(media__mates))
