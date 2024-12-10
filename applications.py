from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
import os
from dotenv import *
load_dotenv()
class FirebaseDataApplication():
    
    def __init__(self):
        cred_data = {
            "type": os.getenv("FIREBASE_TYPE"),
            "project_id": os.getenv("FIREBASE_PROJECT_ID"),
            "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
            "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),  # Convertir saltos de línea
            "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
            "client_id": os.getenv("FIREBASE_CLIENT_ID"),
            "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
            "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_CERT_URL"),
            "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_CERT_URL"),
            "universe_domain":os.getenv("FIREBASE_DOMAIN")
        }
        self.cred = credentials.Certificate(cred_data)
        self.app = firebase_admin.initialize_app(self.cred, name='application')
        self.db = firestore.client(self.app)
    
    def get_document_by_uid(self, id, version_index):
        """
        Retrieves the document by UID and fetches the specified version.
        """
        # Asegúrate de que version_index sea un entero
        try:
            version_index = int(version_index)
        except ValueError:
            raise TypeError(f"Version index must be an integer, got {type(version_index).__name__}: {version_index}")

        users_ref = self.db.collection('applications').where('uid', '==', id).limit(1)
        docs = list(users_ref.stream())
        if docs:
            doc_data = docs[0].to_dict()
            # Ensure versions exist and fetch the desired version by index
            versions = doc_data.get('versions', [])
            if 0 <= version_index < len(versions):
                print(versions[version_index])
                return versions[version_index]
            else:
                raise IndexError(f"Version index {version_index} is out of range for available versions.")
        return None


    def marine_image_seafarers(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('photoURL', "https://static.vecteezy.com/system/resources/previews/005/545/335/non_2x/user-sign-icon-person-symbol-human-avatar-isolated-on-white-backogrund-vector.jpg")

    def marine_firstname_seafarers(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('firstName', "")

    def marine_lastname_seafarers(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('lastName', "")

    def marine_dateOfBirthSeafarers(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('dateBirth', "")

    def marine_contact(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('contacts', {}).get('contact', "")

    def marine_onland(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('skills', {}).get('onland', {})

    def marine_onboard(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('skills', {}).get('onboard', {})

    def marine_nationality(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('countryBirth', {}).get('CountryName', "")

    def marine_cellphone(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('phone', {}).get('value', "")

    def marine_gender(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('gender', {}).get('name', "")

    def marine_vaccines(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('vaccines', {})

    def marine_marital(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('maritalStatus', {}).get('name', "")

    def marine_home_address(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('address', "")

    def marine_airport(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('airport', "")

    def marine_email(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('email', "")

    def marine_personaldocumention(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationDocument', {})

    def marine_certificates(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationCertificates', {})

    def marine_lang_engl(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('lang', {}).get("default", {}).get('ENGLISH', {}).get('PercentageSpeak', "")

    def marine_lang_span(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('lang', {}).get("default", {}).get('SPANISH', {}).get('PercentageSpeak', "")

    def marine_weight(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('weight', {}).get('lb', "")

    def marine_height(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('height', {}).get('format', "")

    def marine_bmi(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('profile', {}).get('bmi', "")

    def marine_marlins(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationProfile', {}).get('lang', {}).get('marlins', "")

    def marine_skills(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('skills', {}).get('skill', "")

    def marine_otherskills(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('additionalCertificates', "")

    def marine_position(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('startApplication', {}).get('position', "")

    def marine_identification(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        return doc_data.get('applicationDocument', {})

    def marine_lang_other(self, id, version_index):
        doc_data = self.get_document_by_uid(id, version_index)
        print(doc_data.get("applicationProfile", {}).get("profile", {}).get("lang", {}).get("other", ""))
        return doc_data.get("applicationProfile", {}).get("profile", {}).get("lang", {}).get("other", "")
