import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()
user_references = db.collection("applications")
data = user_references.stream()
all_data = []
for datos in data:
    data_user = datos.to_dict()
    all_data.append(data_user)
with open("data.json", "a") as file:
        json.dump(all_data, file, indent=4)