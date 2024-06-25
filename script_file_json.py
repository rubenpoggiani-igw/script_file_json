import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  

db = client['esercizio1']  
collection = db['1']  

url = 'https://run.mocky.io/v3/1ac3fe6c-2178-45c5-8bd9-b6710e243b6a'

try:
    
    response = requests.get(url)
    data = response.json()

    collection.insert_many(data)

    print("Dati inseriti con successo nel database.")
except Exception as e:
    print(f"Si è verificato un errore: {e}")
