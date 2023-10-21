"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    df = pd.read_fwf('clusters_report.txt', index_col = False, header = None, skiprows = 4 ,
                 names = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave','principales_palabras_clave'])
    
    
    columns_fill = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave']
    df[columns_fill] = df[columns_fill].fillna(method='ffill')
    df=df.groupby(columns_fill)['principales_palabras_clave'].agg(list).reset_index()
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].replace({' %':''}, regex=True).replace({',':'.'}, regex=True).astype(float)
    df['cluster'] = df['cluster'].astype(int)
    df['principales_palabras_clave']=df['principales_palabras_clave'].apply(lambda x: ' '.join(x))
    df['principales_palabras_clave'] = [item.replace('.', '').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ') for item in df['principales_palabras_clave']]

    return df