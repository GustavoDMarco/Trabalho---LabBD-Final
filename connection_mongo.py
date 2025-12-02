import os
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["lab-bd"]  # confirme o nome do banco no Atlas

vagas = db["vagas"]
curriculos = db["curriculos"]
