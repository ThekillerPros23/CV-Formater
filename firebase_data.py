import firebase_admin
from firebase_admin import credentials, firestore

class Firebase:
    def firebase_data(self):
        self.cred = credentials.Certificate("")
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

database = Firebase()