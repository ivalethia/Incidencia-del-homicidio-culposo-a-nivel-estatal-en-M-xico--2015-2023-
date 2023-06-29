# %%

# Importar la biblioteca pandas con el alias pd.
import pandas as pd
# Importar la función unidecode desde la biblioteca unidecode.
from unidecode import unidecode
# Importar la biblioteca geopandas con el alias gpd.
import geopandas as gpd
# Importar el módulo pyplot de la biblioteca matplotlib con el alias plt.
import matplotlib.pyplot as plt
# Importar el módulo cm de la biblioteca matplotlib con el alias cm.
import matplotlib.cm as cm

# Leer el archivo CSV y almacenar los datos en el DataFrame df.
df = pd.read_csv("C:\ws\DATOS_INC_DELICT\IDEFC_NM_may23.csv", encoding='Windows-1252')

# Crear una condición de filtrado basada en los valores de las columnas 'Tipo de delito' y 'Subtipo de delito'.
filtro = (df['Tipo de delito'] == 'Homicidio') & (df['Subtipo de delito'] == 'Homicidio doloso')

# Filtrar el DataFrame df usando la condición filtro y almacenar los resultados en el DataFrame df_filtrado1.
df_filtrado1 = df.loc[filtro]

# Convertir las columnas de meses del DataFrame df_filtrado1 al tipo de dato float64.
df_filtrado1['Enero']=df_filtrado1['Enero'].astype('float64')
df_filtrado1['Febrero']=df_filtrado1['Febrero'].astype('float64')
df_filtrado1['Marzo']=df_filtrado1['Marzo'].astype('float64')
df_filtrado1['Abril']=df_filtrado1['Abril'].astype('float64')
df_filtrado1['Mayo']=df_filtrado1['Mayo'].astype('float64')
df_filtrado1['Junio']=df_filtrado1['Junio'].astype('float64')
df_filtrado1['Julio']=df_filtrado1['Julio'].astype('float64')
df_filtrado1['Agosto']=df_filtrado1['Agosto'].astype('float64')
df_filtrado1['Septiembre']=df_filtrado1['Septiembre'].astype('float64')
df_filtrado1['Octubre']=df_filtrado1['Octubre'].astype('float64')
df_filtrado1['Noviembre']=df_filtrado1['Noviembre'].astype('float64')
df_filtrado1['Diciembre']=df_filtrado1['Diciembre'].astype('float64')

# Reemplazar los nombres de las entidades por su versión en mayúsculas y sin acentos.
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Aguascalientes','AGUASCALIENTES')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Baja California','BAJA CALIFORNIA')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Baja California Sur','BAJA CALIFORNIA SUR')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Campeche','CAMPECHE')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Coahuila de Zaragoza','COAHUILA DE ZARAGOZA')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Colima','COLIMA')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Chiapas','CHIAPAS')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Chihuahua','CHIHUAHUA')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Ciudad de M�xico','CIUDAD DE MEXICO')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Durango','DURANGO')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Guanajuato','GUANAJUATO')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Guerrero','GUERRERO')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Hidalgo','HIDALGO')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Jalisco','JALISCO')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('M�xico','MEXICO')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Michoac�n de Ocampo','MICHOACAN DE OCAMPO')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Morelos','MORELOS')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Nayarit','NAYARIT')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Nuevo Le�n','NUEVO LEON')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Oaxaca','OAXACA')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Puebla','PUEBLA')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Quer�taro','QUERETARO')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Quintana Roo','QUINTANA ROO')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('San Luis Potos�','SAN LUIS POTOSI')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Sinaloa','SINALOA')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Sonora','SONORA')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Tabasco','TABASCO')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Tamaulipas','TAMAULIPAS')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Tlaxcala','TLAXCALA')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Veracruz de Ignacio de la Llave','VERACRUZ DE IGNACIO DE LA LLAVE')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Yucat�n','YUCATAN')
df_filtrado1['Entidad'] = df_filtrado1['Entidad'].replace('Zacatecas','ZACATECAS')

# Crea una lista con las entidades.
cols_a_modificar = ['Entidad']

# Aplicar la conversión de mayúsculas y eliminación de acentos a las entidades.
for col in cols_a_modificar:
    df_filtrado1[col] = df_filtrado1[col].apply(lambda x: unidecode(str(x).upper()))
    
# Seleccionar las columnas que se van a utilizar en archivos finales y el orden nuevo.
cols_a_mantener = ['Año', 'Clave_Ent', 'Entidad', 'Tipo de delito', 'Subtipo de delito', 'Modalidad', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Crea un nuevo DataFrame llamado df_filtrado11 a partir del DataFrame df_filtrado1. Selecciona todas las filas (:) y solo las columnas especificadas en la lista cols_a_mantener. Esto implica mantener únicamente las columnas que se encuentran en la lista cols_a_mantener y descartar el resto de las columnas.
df_filtrado11 = df_filtrado1.loc[:, cols_a_mantener]

# Guarda el DataFrame df_filtrado11 en un archivo CSV ubicado en la ruta especificada. El parámetro index=False indica que no se debe incluir la columna de índice en el archivo CSV resultante.
df_filtrado11.to_csv("C:/ws/DATOS_INC_DELICT/incidencia_hom_dol_2015_2023_desagregado.csv", index=False)

# Sumar el total de delitos por mes.
dataframe_agrupado = df_filtrado11.groupby(['Entidad', 'Año', 'Clave_Ent'], as_index=False).sum()

# Guarda el DataFrame dataframe_agrupado en un archivo CSV sin incluir el índice y con la ruta especificada.
dataframe_agrupado.to_csv("C:/ws/DATOS_INC_DELICT/incidencia_hom_dol_15_23_total.csv", index=False)

# Carga los datos del segundo dataframe de las poblaciones estatales proyectadas.
df2 = pd.read_csv('C:\ws\DATOS_INC_DELICT\proyecciones_poblacion_estatal.csv', encoding='Windows-1252')

# Crea una segunda lista con las entidades.
cols_a_modificar2 = ['Entidad']

# Aplicar la conversión de mayúsculas y eliminación de acentos a las entidades.
for col in cols_a_modificar2:
    df2[col] = df2[col].apply(lambda x: unidecode(str(x).upper()))

# Reemplazar los nombres de las entidades por su versión en mayúsculas, sin simbolos ni acentos.
df2['Entidad'] = df2['Entidad'].replace('COAHUILA','COAHUILA DE ZARAGOZA')
df2['Entidad'] = df2['Entidad'].replace('CIUDAD DE M?XICO','CIUDAD DE MEXICO')
df2['Entidad'] = df2['Entidad'].replace('M?XICO','MEXICO')
df2['Entidad'] = df2['Entidad'].replace('MICHOAC?N','MICHOACAN DE OCAMPO')
df2['Entidad'] = df2['Entidad'].replace('NUEVO LE?N','NUEVO LEON')
df2['Entidad'] = df2['Entidad'].replace('QUER?TARO','QUERETARO')
df2['Entidad'] = df2['Entidad'].replace('SAN LUIS POTOS?','SAN LUIS POTOSI')
df2['Entidad'] = df2['Entidad'].replace('VERACRUZ','VERACRUZ DE IGNACIO DE LA LLAVE')
df2['Entidad'] = df2['Entidad'].replace('YUCAT?N','YUCATAN')

# Renombra la columna "Ao" del DataFrame df2 a "Año".
df2 = df2.rename(columns={'Ao': 'Año'})

# Convertir las columnas de Año, Clave_Ent y Poblacion del DataFrame df2 al tipo de dato int6 y float64, respectivamente.
df2['Año']=df2['Año'].astype('int64')
df2['Clave_Ent']=df2['Clave_Ent'].astype('int64')
df2['Poblacion']=df2['Poblacion'].astype('float64')

# Seleccionar las columnas que se van a utilizar en archivos finales y el orden nuevo.
cols_a_mantener2 = ['Año','Entidad','Clave_Ent','Poblacion']

# Crea un nuevo DataFrame llamado df_filtrado21 a partir del DataFrame df2. Selecciona todas las filas (:) y solo las columnas especificadas en la lista cols_a_mantener. Esto implica mantener únicamente las columnas que se encuentran en la lista cols_a_mantener2 y descartar el resto de las columnas.
df_filtrado21 = df2.loc[:, cols_a_mantener2]
df_filtrado21.to_csv("C:/ws/DATOS_INC_DELICT/proyecciones_poblacion_estatal_formateado.csv", index=False)

# Combina dos DataFrames, dataframe_agrupado y df_filtrado21, utilizando las columnas "Año", "Entidad" y "Clave_Ent" como claves de unión. El parámetro how='inner' especifica que se realice una intersección entre los conjuntos de datos, es decir, solo se incluirán las filas que tengan valores coincidentes en las columnas de unión en ambos DataFrames.
df_combinado = pd.merge(dataframe_agrupado, df_filtrado21, on=['Año', 'Entidad', 'Clave_Ent',], how='inner')

# Se define una función llamada calcular_division que recibe una fila (row) y un mes (mes). La función verifica si los valores en la columna correspondiente al mes y en la columna 'Poblacion' no son None. Si ambos valores existen, se calcula la división y se devuelve el resultado. De lo contrario, se devuelve None.
def calcular_division(row, mes):
    if row[mes] is not None and row['Poblacion'] is not None:
        return row[mes] / row['Poblacion']
    else:
        return None

# Se itera sobre una lista de meses y se agrega una nueva columna a df_combinado para cada mes. El nombre de cada columna se forma concatenando el nombre del mes con '_percapita'. Para cada fila en df_combinado, se aplica la función calcular_division utilizando el valor del mes actual y se asigna el resultado a la columna correspondiente.
for mes in ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']:
    df_combinado[mes + '_percapita'] = df_combinado.apply(lambda row: calcular_division(row, mes), axis=1)

# El DataFrame df_combinado se guarda en un archivo CSV con el nombre "incidencia_hom_dol_15_23_total_percapita.csv". El parámetro index=False se utiliza para evitar que se agregue una columna adicional con los índices del DataFrame.
df_combinado.to_csv("C:/ws/DATOS_INC_DELICT/incidencia_hom_dol_15_23_total_percapita.csv", index=False)

# Se lee un archivo shapefile llamado "00ent.shp" utilizando la función gpd.read_file de la librería GeoPandas. El DataFrame resultante se asigna a la variable estados. A continuación, se aplica la proyección EPSG:4326 a los datos geoespaciales utilizando el método to_crs.
estados = gpd.read_file('C:\ws\DATOS_INC_DELICT\\00ent.shp')
estados = estados.to_crs("EPSG:4326")

# Se renombran las columnas 'CVE_ENT' y 'NOMGEO' del DataFrame estados a 'Clave_Ent' y 'Entidad', respectivamente, utilizando el método rename. Además, se convierte la columna 'Clave_Ent' al tipo de dato 'int64' utilizando el método astype.
estados = estados.rename(columns={'CVE_ENT': 'Clave_Ent'})
estados = estados.rename(columns={'NOMGEO': 'Entidad'})
estados['Clave_Ent']=estados['Clave_Ent'].astype('int64')

# Se define una lista llamada cols_a_modificar3 que contiene el nombre de la columna 'Entidad'. Luego, se itera sobre esta lista y se aplica una función lambda a cada valor en la columna 'Entidad' del DataFrame estados. La función convierte el valor a una cadena de texto, lo pasa a mayúsculas y elimina cualquier acento utilizando la función unidecode de la librería unidecode.
cols_a_modificar3 = ['Entidad']
for col in cols_a_modificar3:
    estados[col] = estados[col].apply(lambda x: unidecode(str(x).upper()))

# Se combina el DataFrame estados con df_combinado utilizando la columna 'Clave_Ent' como clave de unión. La unión se realiza utilizando un inner join, lo que significa que solo se conservarán las filas que tengan coincidencias en ambas tablas.
df_homicidios_geometry_estados = pd.merge(estados, df_combinado, on=['Clave_Ent'], how='inner')

# El DataFrame df_homicidios_geometry_estados se guarda en un archivo CSV con el nombre "df_homicidios_geometry_estados.csv". El parámetro index=False se utiliza para evitar que se agregue una columna adicional con los índices del DataFrame.
df_homicidios_geometry_estados.to_csv("C:/ws/DATOS_INC_DELICT/df_homicidios_geometry_estados.csv", index=False)

# Se define la función plot_homicide_incidence que toma como argumentos un año y un mes. La función filtra los datos en df_homicidios_geometry_estados para obtener solo las filas correspondientes al año proporcionado. Luego, se define un diccionario month_names que mapea los códigos de mes ('01', '02', etc.) a los nombres de los meses en español. El nombre del mes se determina mediante la consulta al diccionario month_names utilizando el código del mes proporcionado. Se configuran las opciones de color para el mapa y se crea una figura y un eje utilizando plt.subplots. A continuación, se realiza el trazado del mapa utilizando la columna correspondiente al mes per cápita, se dibujan los límites de los estados y se guarda la figura en un archivo PNG.
def plot_homicide_incidence(year, month):
    datos = df_homicidios_geometry_estados[df_homicidios_geometry_estados['Año'] == year]

    month_names = {
        '01': 'Enero',
        '02': 'Febrero',
        '03': 'Marzo',
        '04': 'Abril',
        '05': 'Mayo',
        '06': 'Junio',
        '07': 'Julio',
        '08': 'Agosto',
        '09': 'Septiembre',
        '10': 'Octubre',
        '11': 'Noviembre',
        '12': 'Diciembre'
    }
    month_name = month_names[month]
    cmap = cm.get_cmap('hot')
    cmap_inverted = cmap.reversed()

    fig, ax = plt.subplots(figsize=(10,6), dpi=250)

    datos.plot(f'{month_name}_percapita', ax=ax, edgecolor='#d3d3d3', linewidth=0.2, legend=True, colormap=cmap_inverted, vmin=0.0000, vmax=0.00013).set_title(f'Incidencia de homicidios culposos (corregido\n per capita) en {month_name} del {year}')
    estados.plot(ax=ax, color='none', edgecolor='black', linewidth=0.5)
    # Guardar el mapa en formato PNG
    fig.savefig(f'C:\ws\DATOS_INC_DELICT\mapa_estados_percapita_{year}_{month}.png', dpi=500)
    plt.show()
estados
plot_homicide_incidence(2015, '01')
plot_homicide_incidence(2015, '02')
plot_homicide_incidence(2015, '03')
plot_homicide_incidence(2015, '04')
plot_homicide_incidence(2015, '05')
plot_homicide_incidence(2015, '06')
plot_homicide_incidence(2015, '07')
plot_homicide_incidence(2015, '08')
plot_homicide_incidence(2015, '09')
plot_homicide_incidence(2015, '10')
plot_homicide_incidence(2015, '11')
plot_homicide_incidence(2015, '12')
plot_homicide_incidence(2016, '01')
plot_homicide_incidence(2016, '02')
plot_homicide_incidence(2016, '03')
plot_homicide_incidence(2016, '04')
plot_homicide_incidence(2016, '05')
plot_homicide_incidence(2016, '06')
plot_homicide_incidence(2016, '07')
plot_homicide_incidence(2016, '08')
plot_homicide_incidence(2016, '09')
plot_homicide_incidence(2016, '10')
plot_homicide_incidence(2016, '11')
plot_homicide_incidence(2016, '12')
plot_homicide_incidence(2017, '01')
plot_homicide_incidence(2017, '02')
plot_homicide_incidence(2017, '03')
plot_homicide_incidence(2017, '04')
plot_homicide_incidence(2017, '05')
plot_homicide_incidence(2017, '06')
plot_homicide_incidence(2017, '07')
plot_homicide_incidence(2017, '08')
plot_homicide_incidence(2017, '09')
plot_homicide_incidence(2017, '10')
plot_homicide_incidence(2017, '11')
plot_homicide_incidence(2017, '12')
plot_homicide_incidence(2018, '01')
plot_homicide_incidence(2018, '02')
plot_homicide_incidence(2018, '03')
plot_homicide_incidence(2018, '04')
plot_homicide_incidence(2018, '05')
plot_homicide_incidence(2018, '06')
plot_homicide_incidence(2018, '07')
plot_homicide_incidence(2018, '08')
plot_homicide_incidence(2018, '09')
plot_homicide_incidence(2018, '10')
plot_homicide_incidence(2018, '11')
plot_homicide_incidence(2018, '12')
plot_homicide_incidence(2019, '01')
plot_homicide_incidence(2019, '02')
plot_homicide_incidence(2019, '03')
plot_homicide_incidence(2019, '04')
plot_homicide_incidence(2019, '05')
plot_homicide_incidence(2019, '06')
plot_homicide_incidence(2019, '07')
plot_homicide_incidence(2019, '08')
plot_homicide_incidence(2019, '09')
plot_homicide_incidence(2019, '10')
plot_homicide_incidence(2019, '11')
plot_homicide_incidence(2019, '12')
plot_homicide_incidence(2020, '01')
plot_homicide_incidence(2020, '02')
plot_homicide_incidence(2020, '03')
plot_homicide_incidence(2020, '04')
plot_homicide_incidence(2020, '05')
plot_homicide_incidence(2020, '06')
plot_homicide_incidence(2020, '07')
plot_homicide_incidence(2020, '08')
plot_homicide_incidence(2020, '09')
plot_homicide_incidence(2020, '10')
plot_homicide_incidence(2020, '11')
plot_homicide_incidence(2020, '12')
plot_homicide_incidence(2021, '01')
plot_homicide_incidence(2021, '02')
plot_homicide_incidence(2021, '03')
plot_homicide_incidence(2021, '04')
plot_homicide_incidence(2021, '05')
plot_homicide_incidence(2021, '06')
plot_homicide_incidence(2021, '07')
plot_homicide_incidence(2021, '08')
plot_homicide_incidence(2021, '09')
plot_homicide_incidence(2021, '10')
plot_homicide_incidence(2021, '11')
plot_homicide_incidence(2021, '12')
plot_homicide_incidence(2022, '01')
plot_homicide_incidence(2022, '02')
plot_homicide_incidence(2022, '03')
plot_homicide_incidence(2022, '04')
plot_homicide_incidence(2022, '05')
plot_homicide_incidence(2022, '06')
plot_homicide_incidence(2022, '07')
plot_homicide_incidence(2022, '08')
plot_homicide_incidence(2022, '09')
plot_homicide_incidence(2022, '10')
plot_homicide_incidence(2022, '11')
plot_homicide_incidence(2022, '12')
plot_homicide_incidence(2023, '01')
plot_homicide_incidence(2023, '02')
plot_homicide_incidence(2023, '03')
plot_homicide_incidence(2023, '04')
plot_homicide_incidence(2023, '05')


# %%

# Se define la función plot_homicide_incidence2 que toma como argumentos un año y un mes. Dentro de la función, se filtran los datos en df_homicidios_geometry_estados para obtener solo las filas correspondientes al año proporcionado y se asignan a la variable datos.
def plot_homicide_incidence2(year, month):
    datos = df_homicidios_geometry_estados[df_homicidios_geometry_estados['Año'] == year]

# Se define un diccionario month_names que mapea los códigos de mes ('01', '02', etc.) a los nombres de los meses en español. El nombre del mes se determina mediante la consulta al diccionario month_names utilizando el código del mes proporcionado.
    month_names = {
        '01': 'Enero',
        '02': 'Febrero',
        '03': 'Marzo',
        '04': 'Abril',
        '05': 'Mayo',
        '06': 'Junio',
        '07': 'Julio',
        '08': 'Agosto',
        '09': 'Septiembre',
        '10': 'Octubre',
        '11': 'Noviembre',
        '12': 'Diciembre'
    }
    month_name = month_names[month]

# Se obtiene el mapa de colores 'hot' utilizando la función cm.get_cmap de matplotlib. Luego, se invierte el mapa de colores utilizando el método reversed. A continuación, se crea una figura y un eje utilizando plt.subplots con un tamaño de figura de 10x6 pulgadas y una resolución de 250 puntos por pulgada.
    cmap = cm.get_cmap('hot')
    cmap_inverted = cmap.reversed()
    fig, ax = plt.subplots(figsize=(10,6), dpi=250)

# Se traza el mapa utilizando la columna correspondiente al mes de datos, donde el nombre de la columna se obtiene mediante f-strings y se pasa a datos.plot. Se especifican los parámetros de estilo, como el color de borde, el ancho de línea y la escala de colores invertida. También se establecen los límites mínimo (vmin) y máximo (vmax) para el colorbar. A continuación, se dibujan los límites de los estados en el mismo eje utilizando estados.plot.
    datos.plot(f'{month_name}', ax=ax, edgecolor='#d3d3d3', linewidth=0.2, legend=True, colormap=cmap_inverted, vmin=0.0, vmax=325.0).set_title(f'Incidencia de homicidios culposos\n (número de casos) en {month_name} del {year}')
    estados.plot(ax=ax, color='none', edgecolor='black', linewidth=0.5)

# Se guarda la figura en un archivo PNG utilizando el método savefig. El archivo se guarda en la ubicación especificada en la ruta con nombres que contienen el año y el mes. Luego, se muestra el gráfico utilizando plt.show().
    fig.savefig(f'C:\ws\DATOS_INC_DELICT\mapa_estados_casos_{year}_{month}.png', dpi=500)
    plt.show()

plot_homicide_incidence2(2015, '01')
plot_homicide_incidence2(2015, '02')
plot_homicide_incidence2(2015, '03')
plot_homicide_incidence2(2015, '04')
plot_homicide_incidence2(2015, '05')
plot_homicide_incidence2(2015, '06')
plot_homicide_incidence2(2015, '07')
plot_homicide_incidence2(2015, '08')
plot_homicide_incidence2(2015, '09')
plot_homicide_incidence2(2015, '10')
plot_homicide_incidence2(2015, '11')
plot_homicide_incidence2(2015, '12')
plot_homicide_incidence2(2016, '01')
plot_homicide_incidence2(2016, '02')
plot_homicide_incidence2(2016, '03')
plot_homicide_incidence2(2016, '04')
plot_homicide_incidence2(2016, '05')
plot_homicide_incidence2(2016, '06')
plot_homicide_incidence2(2016, '07')
plot_homicide_incidence2(2016, '08')
plot_homicide_incidence2(2016, '09')
plot_homicide_incidence2(2016, '10')
plot_homicide_incidence2(2016, '11')
plot_homicide_incidence2(2016, '12')
plot_homicide_incidence2(2017, '01')
plot_homicide_incidence2(2017, '02')
plot_homicide_incidence2(2017, '03')
plot_homicide_incidence2(2017, '04')
plot_homicide_incidence2(2017, '05')
plot_homicide_incidence2(2017, '06')
plot_homicide_incidence2(2017, '07')
plot_homicide_incidence2(2017, '08')
plot_homicide_incidence2(2017, '09')
plot_homicide_incidence2(2017, '10')
plot_homicide_incidence2(2017, '11')
plot_homicide_incidence2(2017, '12')
plot_homicide_incidence2(2018, '01')
plot_homicide_incidence2(2018, '02')
plot_homicide_incidence2(2018, '03')
plot_homicide_incidence2(2018, '04')
plot_homicide_incidence2(2018, '05')
plot_homicide_incidence2(2018, '06')
plot_homicide_incidence2(2018, '07')
plot_homicide_incidence2(2018, '08')
plot_homicide_incidence2(2018, '09')
plot_homicide_incidence2(2018, '10')
plot_homicide_incidence2(2018, '11')
plot_homicide_incidence2(2018, '12')
plot_homicide_incidence2(2019, '01')
plot_homicide_incidence2(2019, '02')
plot_homicide_incidence2(2019, '03')
plot_homicide_incidence2(2019, '04')
plot_homicide_incidence2(2019, '05')
plot_homicide_incidence2(2019, '06')
plot_homicide_incidence2(2019, '07')
plot_homicide_incidence2(2019, '08')
plot_homicide_incidence2(2019, '09')
plot_homicide_incidence2(2019, '10')
plot_homicide_incidence2(2019, '11')
plot_homicide_incidence2(2019, '12')
plot_homicide_incidence2(2020, '01')
plot_homicide_incidence2(2020, '02')
plot_homicide_incidence2(2020, '03')
plot_homicide_incidence2(2020, '04')
plot_homicide_incidence2(2020, '05')
plot_homicide_incidence2(2020, '06')
plot_homicide_incidence2(2020, '07')
plot_homicide_incidence2(2020, '08')
plot_homicide_incidence2(2020, '09')
plot_homicide_incidence2(2020, '10')
plot_homicide_incidence2(2020, '11')
plot_homicide_incidence2(2020, '12')
plot_homicide_incidence2(2021, '01')
plot_homicide_incidence2(2021, '02')
plot_homicide_incidence2(2021, '03')
plot_homicide_incidence2(2021, '04')
plot_homicide_incidence2(2021, '05')
plot_homicide_incidence2(2021, '06')
plot_homicide_incidence2(2021, '07')
plot_homicide_incidence2(2021, '08')
plot_homicide_incidence2(2021, '09')
plot_homicide_incidence2(2021, '10')
plot_homicide_incidence2(2021, '11')
plot_homicide_incidence2(2021, '12')
plot_homicide_incidence2(2022, '01')
plot_homicide_incidence2(2022, '02')
plot_homicide_incidence2(2022, '03')
plot_homicide_incidence2(2022, '04')
plot_homicide_incidence2(2022, '05')
plot_homicide_incidence2(2022, '06')
plot_homicide_incidence2(2022, '07')
plot_homicide_incidence2(2022, '08')
plot_homicide_incidence2(2022, '09')
plot_homicide_incidence2(2022, '10')
plot_homicide_incidence2(2022, '11')
plot_homicide_incidence2(2022, '12')
plot_homicide_incidence2(2023, '01')
plot_homicide_incidence2(2023, '02')
plot_homicide_incidence2(2023, '03')
plot_homicide_incidence2(2023, '04')
plot_homicide_incidence2(2023, '05')

# %%

# Se importan los módulos imageio y os necesarios para el código.
import imageio
import os

# Se define la función create_gif_mapa_estados_percapita que toma como argumento el nombre de archivo de salida para el GIF animado.
def create_gif_mapa_estados_percapita(output_filename):

# Se obtiene una lista de archivos en el directorio actual que comienzan con "mapa_estados_percapita_" y terminan con ".png". Luego, se ordenan los archivos alfabéticamente en orden ascendente.
    files = [filename for filename in os.listdir('.') if filename.startswith('mapa_estados_percapita_') and filename.endswith('.png')]
    sorted_files = sorted(files)
    #print(sorted_files)
    
# Se crea una lista vacía images. Luego, se itera sobre cada archivo en sorted_files y se lee la imagen utilizando imageio.imread. Cada imagen se agrega a la lista images.            
    images = []

    for filename in sorted_files:
        images.append(imageio.imread(filename))

# Se guarda la lista de imágenes en un archivo GIF utilizando imageio.mimsave. Se especifica el nombre de archivo de salida, la lista de imágenes, el formato como GIF y la duración de cada imagen en milisegundos. Luego, se muestra un mensaje indicando que se ha creado el archivo GIF animado.
    imageio.mimsave(output_filename, images, format='gif', duration=250)
    print(f'Archivo GIF animado creado: {output_filename}')

    #print(sorted_files)

create_gif_mapa_estados_percapita('inc_hom_culp_mex_percapita.gif')

# %%
import imageio
import os

def create_gif_mapa_estados_casos(output_filename):

    files = [filename for filename in os.listdir('.') if filename.startswith('mapa_estados_casos_') and filename.endswith('.png')]
    sorted_files = sorted(files)
    #print(sorted_files)
    
    images = []

    for filename in sorted_files:
        images.append(imageio.imread(filename))
            
    imageio.mimsave(output_filename, images, format='gif', duration=250)
    print(f'Archivo GIF animado creado: {output_filename}')

    #print(sorted_files)

create_gif_mapa_estados_casos('inc_hom_culp_mex_casos.gif')

# %%

# Se importan los módulos cv2 y os necesarios para el código.
import cv2
import os

# Se define la función create_avi_mapa_estados_percapita que toma como argumento el nombre de archivo de salida para el video AVI.
def create_avi_mapa_estados_percapita(output_filename):

# Se obtiene una lista de archivos en el directorio actual que comienzan con "mapa_estados_percapita_" y terminan con ".png". Luego, se ordenan los archivos alfabéticamente en orden ascendente. La lista ordenada se imprime en la consola.
    files = [filename for filename in os.listdir('.') if filename.startswith('mapa_estados_percapita_') and filename.endswith('.png')]
    sorted_files = sorted(files)
    print(sorted_files)

#Se lee la primera imagen de la lista ordenada de archivos y se obtienen las dimensiones de la imagen (alto, ancho y número de canales).
    frame = cv2.imread(sorted_files[0])
    height, width, layers = frame.shape

# Se crea un objeto VideoWriter de OpenCV para escribir el video. Se especifica el nombre de archivo de salida, el códec de compresión ('MJPG'), la tasa de cuadros por segundo (3 en este caso) y las dimensiones del video (ancho y alto).
    video = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'MJPG'), 3, (width, height))

# Se itera sobre cada archivo en sorted_files, se lee la imagen correspondiente y se escribe en el objeto VideoWriter.
    for filename in sorted_files:
        image = cv2.imread(filename)
        video.write(image)

# Se cierran todas las ventanas abiertas por OpenCV y se libera el objeto VideoWriter.
    cv2.destroyAllWindows()
    video.release()

# Se muestra un mensaje indicando que se ha creado el archivo de video AVI.
    print(f'Archivo de video AVI creado: {output_filename}')

create_avi_mapa_estados_percapita('inc_hom_culp_mex_percapita.avi')

# %%
import cv2
import os

def create_avi_mapa_estados_casos(output_filename):

    files = [filename for filename in os.listdir('.') if filename.startswith('mapa_estados_casos_') and filename.endswith('.png')]
    sorted_files = sorted(files)
    print(sorted_files)

    frame = cv2.imread(sorted_files[0])
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'MJPG'), 3, (width, height))

    for filename in sorted_files:
        image = cv2.imread(filename)
        video.write(image)

    cv2.destroyAllWindows()
    video.release()

    print(f'Archivo de video AVI creado: {output_filename}')

create_avi_mapa_estados_casos('inc_hom_culp_mex_casos.avi')

# %%

