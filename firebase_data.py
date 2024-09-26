import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
class FirebaseData():
    def database(self, query):
        self.cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
        app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        users_ref = self.db.collection(query)
        docs = users_ref.stream()
        return self.docs
