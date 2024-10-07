import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Inicializa Firebase
cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
firebase_admin.initialize_app(cred)

# Conecta a Firestore
db = firestore.client()

# Recupera los datos de la colección 'usersData'
users_references = db.collection('usersData')
docs = users_references.stream()

# Crea un diccionario para almacenar los datos
users_data = {}

# Recorre los documentos y agrégales el ID del documento
for doc in docs:
    users_data[doc.id] = doc.to_dict()

# Guarda los datos en un archivo .json
with open('users_data.json', 'w') as json_file:
    json.dump(users_data, json_file, indent=4)

print("Datos guardados en users_data.json")
