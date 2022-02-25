# Importa bibliotecas necessárias
import zipfile
import requests
from io import BytesIO
import os
from subprocess import PIPE, Popen

 # Cria um diretório para armazenar o conteúdo
os.makedirs('./bike_sharing', exist_ok=True)


# Define a url
url = "https://www.kaggle.com/joseguilhermelopes/bike-sharing-system-in-brasilia-brazil/download"

# Faz download do conteúdo
filebytes = BytesIO(
    requests.get(url).content
)

# Extrai o conteúdo do zipfile
myzip = zipfile.ZipFile(filebytes)
myzip.extractall("./bike_sharing")

# Transfere para o HDFS
def save_in_hdfs(dir_input, dir_output, filename_output):
    put = Popen(["hadoop", "fs", "-put", "-f", dir_input + filename_output, dir_output + filename_output], stdin=PIPE, bufsize=-1)
    put.communicate()
    
filename = "df_rides.csv"
save_in_hdfs("/home/leandro/Documents/projetos/ETL-Hadoop_Hive_Sqoop_SQL/bike_sharing/","/data/usuarios_bike/", filename)

filename = "df_stations.csv"
save_in_hdfs("/home/leandro/Documents/projetos/ETL-Hadoop_Hive_Sqoop_SQL/bike_sharing/","/data/estacoes_bike/", filename)