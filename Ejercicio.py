import matplotlib.pyplot as plt



vivienda = pd.read_csv("USA_Housing.csv")

# Sustituimos los nombres a español

vivienda.rename(columnas = {'Avg. Area Income': 'Ingresos medios de la zona', 'Avg. Area House Age': 'Edad media de la casa', 'Avg. Area Number of Rooms': 'Media de habitaciones', 'Avg. Area Number of Bedrooms ': 'Media de dormitorios', 'Area Population' :'Poblacion en la zona', 'Price':'Precio', 'Adress':'Direccion'}, inplace = True)