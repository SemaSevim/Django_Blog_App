from datetime import datetime
from xmlrpc.client import DateTime
from django.db import connection
from .models import Soru

def execute_sql(sql:str):
    with connection.cursor() as cursor:
        cursor.execute(sql)

def insert_soru(soru:str,ayim_tarihi:datetime):
    try: #if else gibi
        sql=f"INSERT INTO anketler_soru(soru_metni,ayim_tarihi) VALUES( '{soru}','{ayim_tarihi}')"
        execute_sql(sql)
    except Exception as e: #istisna
        print(e)

def update_soru(id:int,soru:str,ayim_tarihi:datetime):
    try:
        sql=f"Update anketler_soru set soru_metni='{soru}',yayim_tarihi='{ayim_tarihi}' where id={id}"
        execute_sql(sql)
    except Exception as e:
        print(e)
def select_soru():
    return Soru.objects.raw('SELECT * FROM anketler_soru')

def delete_soru(id:int):
    try:
        sql=f"Delete anketler_soru where id={id}"
    except Exception as e:
        print(e)  