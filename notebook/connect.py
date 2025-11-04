from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

#cargar variables entorno
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI_ATLAS")
DB_NAME_ATLAS = os.getenv("MONGODB_DATABASE")

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME_ATLAS]
    print("Conexion exitosa a Atlas")
    colecciones = db.list_collection_names()
    print('Conectado Mongo DB Atlas: Base de Datos', (DB_NAME_ATLAS))
    print('Colecciones: ',(colecciones))

except errors.ServerSelectionTimeoutError as e:
    print("No se pudo conectar al servidor", e)

except errors.OperationFailure as e:
    print("Error de autenticacion", e)

except Exception as e:
    print('No se que pasó',e)