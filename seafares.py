import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Usar una cuenta de servicio.
class FirebaseDataSeafarers():
    
    def __init__(self):
        
        self.cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
        self.app = firebase_admin.initialize_app(self.cred,name='seafarers')
        self.db = firestore.client(self.app)
    def get_documents_seafarer(self):
        users_ref = self.db.collection('usersData')
        return users_ref.stream()
    def marine_image_seafarers(self,id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados
        seafarer_documents = []
        img = None
        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                img =  doc_data['photoURL']
        return img
    def marine_firstname_seafarers(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados
        seafarer_documents = []

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                    seafarer_documents = doc_data['seafarerData']['seafarerProfile']['profile'].get('firstName', None)
                    break  # Deja de iterar una vez que se encuentra el documento

        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_marlins_total(self,id):
        docs = self.get_documents_seafarer()

        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                seafarer_documents = doc_data['seafarerData']['seafarerProfile']['lang']['marlins']['PercentageTotal']
        return seafarer_documents
    
    def marine_lastname_seafarers(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados
        seafarer_documents = []

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                    seafarer_documents = doc_data['seafarerData']['seafarerProfile']['profile'].get('lastName', None)
                    break  # Deja de iterar una vez que se encuentra el documento

        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_dateOfBirthSeafarers(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                    seafarer_documents = doc_data['seafarerData']['seafarerProfile']['profile'].get('dateBirth', None)
                    
        
        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_contact(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                if 'seafarerData' in doc_data and 'seafarerDocument' in doc_data['seafarerData']:
                    seafarer_documents = doc_data['seafarerData']['seafarerProfile']['contacts'].get('contact', None)
                    
        
        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_onland(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                    seafarer_documents = doc_data['seafarerData']['skills']['onland']                    
        
        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_onboard(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                    seafarer_documents = doc_data['seafarerData']['skills']['onboard']                    
        
        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_nationality(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                if 'seafarerData' in doc_data and 'seafarerDocument' in doc_data['seafarerData']:
                    seafarer_documents = doc_data['seafarerData']['seafarerProfile']['profile']['countryBirth'].get('CountryName', None)
                    
        
        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_cellphone(self,id):
        docs = self.get_documents_seafarer()

        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                seafarer_documents = doc_data['seafarerData']['seafarerProfile']['lang']['marlins']['PercentageTotal']
        return seafarer_documents
    def marine_gender(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                if 'seafarerData' in doc_data and 'seafarerDocument' in doc_data['seafarerData']:
                    seafarer_documents = doc_data['seafarerData']['seafarerProfile']['profile']['gender'].get('name', None)
                    
        
        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_vaccines(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                seafarer_documents = doc_data["seafarerData"]['applicationProfile']['profile'].get('vaccines', None)
                    
        
        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_marital(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                if 'seafarerData' in doc_data and 'seafarerDocument' in doc_data['seafarerData']:
                    seafarer_documents = doc_data['seafarerData']['seafarerProfile']['profile']['maritalStatus'].get('name', None)
                    
        
        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_home_address(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                if 'seafarerData' in doc_data and 'seafarerDocument' in doc_data['seafarerData']:
                    seafarer_documents = doc_data['seafarerData']['seafarerProfile']['profile'].get('address', None)
                    
        
        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_airport(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                if 'seafarerData' in doc_data and 'seafarerDocument' in doc_data['seafarerData']:
                    seafarer_documents = doc_data['seafarerData']['seafarerProfile']['profile'].get('airport', None)
                    
        
        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_email(self, id):
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                email =  doc_data['email']

        
        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return email
    def marine_personaldocumention(self, id):
        # Obtiene un nuevo stream de documentos
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados
        seafarer_documents = []

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                if 'seafarerData' in doc_data and 'seafarerDocument' in doc_data['seafarerData']:
                    seafarer_documents = doc_data['seafarerData']['seafarerDocument']
                    break  # Deja de iterar una vez que se encuentra el documento

        # Retorna la lista de documentos, o una lista vacía si no se encuentra nada
        return seafarer_documents
    def marine_certificates(self, id):
        # Get all seafarer documents
        docs = self.get_documents_seafarer()

        # Loop through each document
        for doc in docs:
            doc_data = doc.to_dict()

            # Check if the UID matches the provided ID
            if doc_data.get('uid') == id:
                # Check if 'seafarerData' and 'seafarerCertificates' exist
                if 'seafarerData' in doc_data and 'seafarerCertificates' in doc_data['seafarerData']:
                    return doc_data['seafarerData']['seafarerCertificates']