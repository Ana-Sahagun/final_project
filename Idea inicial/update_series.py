import requests
import json
import pandas as pd
from opnieuw import retry
from requests.exceptions import HTTPError, ConnectionError
import time
from tinydb import TinyDB, Query


# Get data from a series
@retry(
    retry_on_exceptions=(ConnectionError, HTTPError),
    max_calls_total=4,
    retry_window_after_first_call_in_seconds=60,
)
def get_series(cod, nult=100):
    url = f"https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/{cod}?nult={nult}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    time.sleep(10)
    if response.status_code == 200:
        return response.json()
    

codigos=["CNE2444"]
for codigo in codigos: 
    db=TinyDB(r"C:\Users\anasa\Desktop\Ana\IRONHACK\Proyecto final/series.json")
    series_table=db.table("series")
    Serie=Query()
    for i in range(0, 5):
        try:
            print(f'Obteniendo datos de {codigo}. iteracion {i+1}')
            response=get_series(codigo)
            if response:
                if response.get('Data', []):
                    series_table.upsert(response, Serie.codigo==response["COD"])
                    break
        except:
            continue