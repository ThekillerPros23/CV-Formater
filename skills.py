import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Inicializa Firebase con las credenciales
cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
firebase_admin.initialize_app(cred)

# Conecta a Firestore
db = firestore.client()

# Recupera los datos de la colección 'usersData'
users_references = db.collection('usersData')
docs = users_references.stream()

# Iterar sobre cada documento y recuperar solo el campo 'seafarerDocument'
for docs_data in docs:
    data = docs_data.to_dict()
    
    # Navegar al campo 'seafarerDocument' dentro de 'seafarerData'
    if 'seafarerData' in data and 'seafarerDocument' in data['seafarerData']:
        seafarer_document = data['seafarerData']['seafarerDocument']
        
        # Convertir a formato JSON para imprimirlo más legible
        seafarer_document_json = json.dumps(seafarer_document, indent=4)
        print(seafarer_document_json)
