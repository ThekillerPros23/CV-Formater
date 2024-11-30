from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin

class FirebaseDataApplication():
    
    def __init__(self):
        self.cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
        self.app = firebase_admin.initialize_app(self.cred, name='application')
        self.db = firestore.client(self.app)
    
    def get_document_by_uid(self, id, version):
        # Filtra el documento por UID directamente en la consulta
        users_ref = self.db.collection('applications').where('uid', '==', id).limit(1)
        docs = list(users_ref.stream())
        if docs:
            doc_data = docs[0].to_dict()
            # Extrae el primer elemento de 'versions' si existe
            version_data = doc_data.get('versions', [{}])[0]
            doc_data['version'] = version_data  # Añade 'version' directamente al documento
            return doc_data
        return None

    def marine_image_seafarers(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data.get('photoURL') if doc_data and doc_data.get('photoURL') else "https://static.vecteezy.com/system/resources/previews/005/545/335/non_2x/user-sign-icon-person-symbol-human-avatar-isolated-on-white-backogrund-vector.jpg"

    def marine_firstname_seafarers(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['applicationProfile']['profile'].get('firstName') if doc_data else None

    def marine_lastname_seafarers(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['applicationProfile']['profile'].get('lastName') if doc_data else ""

    def marine_dateOfBirthSeafarers(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['applicationProfile']['profile'].get('dateBirth') if doc_data else ""

    def marine_contact(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['applicationProfile']['contacts'].get('contact') if doc_data else ""

    def marine_onland(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['skills'].get('onland') if doc_data else {}

    def marine_onboard(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['skills'].get('onboard') if doc_data else {}

    def marine_nationality(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['applicationProfile']['profile']['countryBirth'].get('CountryName') if doc_data else ""

    def marine_cellphone(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['applicationProfile']['profile']["phone"].get("value") if doc_data else ""

    def marine_gender(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['applicationProfile']['profile']['gender'].get('name') if doc_data else ""

    def marine_vaccines(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['applicationProfile'].get('vaccines') if doc_data else {}

    def marine_marital(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['applicationProfile']['profile']['maritalStatus'].get('name') if doc_data else ""

    def marine_home_address(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['applicationProfile']['profile'].get('address') if doc_data else ""

    def marine_airport(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version']['applicationProfile']['profile'].get('airport') if doc_data else ""

    def marine_email(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data.get('email') if doc_data else ""

    def marine_personaldocumention(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version'].get('seafarerDocument') if doc_data else {}

    def marine_certificates(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data['version'].get('seafarerCertificates') if doc_data else {}

    def marine_lang_engl(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data.get("version", {}).get("lang", {}).get("ENGLISH", {}).get("PercentageSpeak", "")

    def marine_lang_span(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data.get("version", {}).get("lang", {}).get("SPANISH", {}).get("PercentageSpeak", "") 

    def marine_weight(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data.get("version", {}).get("profile", {}).get("weight", {}).get("lb", {})

    def marine_height(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data.get("version", {}).get("profile", {}).get("height", {}).get("format", {})

    def marine_bmi(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data.get("version", {}).get("profile", {}).get("bmi", {})

    def marine_marlins(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data.get("version", {}).get("lang", {}).get("marlins", {}) 

    def marine_skills(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data.get("version", {}).get("skills", {}).get("skill", {})

    def marine_otherskills(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data.get("version", {}).get("additionalCertificates", {})

    def marine_position(self, id, version, ):
        doc_data = self.get_document_by_uid(id, version)
        return doc_data.get("version", {}).get("startApplication", {}).get("position", {})
