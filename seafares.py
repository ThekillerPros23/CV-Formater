from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin

class FirebaseDataSeafarers():
    
    def __init__(self):
        self.cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
        self.app = firebase_admin.initialize_app(self.cred, name='seafarers')
        self.db = firestore.client(self.app)
    
    def get_document_by_uid(self, uid):
        # Filtra el documento por UID directamente en la consulta
        users_ref = self.db.collection('usersData').where('uid', '==', uid).limit(1)
        docs = list(users_ref.stream())
        return docs[0].to_dict() if docs else None
    def marine_image_seafarers(self, id):
        doc_data = self.get_document_by_uid(id)
        # Return photoURL if it exists; otherwise, return the fallback URL
        return doc_data.get('photoURL') if doc_data and doc_data.get('photoURL') else "https://static.vecteezy.com/system/resources/previews/005/545/335/non_2x/user-sign-icon-person-symbol-human-avatar-isolated-on-white-backogrund-vector.jpg"

    def marine_firstname_seafarers(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['seafarerProfile']['profile'].get('firstName') if doc_data else None

    # Aplica el mismo enfoque de filtrado a las otras funciones
    def marine_lastname_seafarers(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['seafarerProfile']['profile'].get('lastName') if doc_data else ""

    def marine_dateOfBirthSeafarers(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['seafarerProfile']['profile'].get('dateBirth') if doc_data else ""

    def marine_contact(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['seafarerProfile']['contacts'].get('contact') if doc_data else ""

    def marine_onland(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['skills'].get('onland') if doc_data else {}

    def marine_onboard(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['skills'].get('onboard') if doc_data else {}

    def marine_nationality(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['seafarerProfile']['profile']['countryBirth'].get('CountryName') if doc_data else ""

    def marine_cellphone(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['seafarerProfile']['profile']["phone"].get("value") if doc_data else ""

    def marine_gender(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['seafarerProfile']['profile']['gender'].get('name') if doc_data else ""

    def marine_vaccines(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['seafarerProfile'].get('vaccines') if doc_data else {}

    def marine_marital(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['seafarerProfile']['profile']['maritalStatus'].get('name') if doc_data else ""

    def marine_home_address(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['seafarerProfile']['profile'].get('address') if doc_data else ""

    def marine_airport(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData']['seafarerProfile']['profile'].get('airport') if doc_data else ""

    def marine_email(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data.get('email') if doc_data else ""

    def marine_personaldocumention(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData'].get('seafarerDocument') if doc_data else {}
    def marine_certificates(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data['seafarerData'].get('seafarerCertificates') if doc_data else { }
    def marine_lang_engl(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data.get("seafarerData", {}).get("seafarerProfile", {}).get("lang", {}).get("default", {}).get("ENGLISH", {}).get("PercentageSpeak", "")

    def marine_lang_span(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data.get("seafarerData", {}).get("seafarerProfile", {}).get("lang", {}).get("default", {}).get("SPANISH", {}).get("PercentageSpeak", "") 
    def marine_weight(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data.get("seafarerData", {}).get("seafarerProfile", {}).get("profile", {}).get("weight", {}).get("lb", {})
    
    def marine_height(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data.get("seafarerData", {}).get("seafarerProfile", {}).get("profile", {}).get("height", {}).get("format", {})

    def marine_bmi(self, id):
        doc_data = self.get_document_by_uid(id)
        return doc_data.get("seafarerData", {}).get("seafarerProfile", {}).get("profile", {}).get("bmi", {})

    def marine_certificates(self,id):
        doc_data = self.get_document_by_uid(id)
        return doc_data.get("seafarerData", {}).get("seafarerCertificates", {})