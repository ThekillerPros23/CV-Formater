import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Usar una cuenta de servicio.
class FirebaseData():
    
    def __init__(self):
        # Inicializa la app de Firebase con las credenciales
        self.cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def get_documents_applications(self):
        # Cada vez que se llame a esta función, se crea un nuevo stream de documentos
        users_ref = self.db.collection('applications')
        return users_ref.stream()
    
    def get_documents_seafarer(self):
        users_ref = self.db.collection('usersData')
        return users_ref.stream()
    
    def marine_name(self,id):   
        name = []
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            
            # Verificar si el uid coincide con el id proporcionado
            if doc_data.get('uid') == id:
                for version in doc_data['versions']:
                    # Extraer el nombre del perfil dentro de la versión
                    if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                        first_name = version['applicationProfile']['profile'].get('firstName', None)
                        
        return first_name
        

        
    def marine_lastname(self,id):  # He cambiado el nombre de esta segunda función para evitar conflicto
        
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            if doc_data.get('uid') == id:
                for version in doc_data['versions']:
                    if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                        lastname = version['applicationProfile']['profile'].get('lastName', None)
        return lastname
    def marine_dateOfBirth(self,id):
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            if doc_data.get('uid') == id:
                for version in doc_data['versions']:
                    if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                        birth = version['applicationProfile']['profile'].get('dateBirth', None)
        return birth
    def marine_nationality(self,id):
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            if doc_data.get('uid') == id:
                for version in doc_data['versions']:
                    if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                        nationality = version['applicationProfile']['profile']['countryBirth'].get('CountryName', None)
        return nationality
    def marine_gender(self,id):
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            if doc_data.get('uid') == id:
                    for version in doc_data['versions']:
                        if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                            gender = version['applicationProfile']['profile']['gender'].get('name', None)
        return gender[0]
    def marine_marital(self,id):
        marital = []
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            if doc_data.get('uid') == id:
                    for version in doc_data['versions']:
                        if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                            marital = version['applicationProfile']['profile']['maritalStatus'].get('name', None)
        return marital
    def marine_home_address(self):
        marital = []
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            for datos in doc_data['versions']:
                marital.append(datos['applicationProfile']['profile']["maritalStatus"]["name"])
    def marine_airport(self,id):
        airport = []
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            if doc_data.get('uid') == id:
                    for version in doc_data['versions']:
                        if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                            airport = version['applicationProfile']['profile'].get('airport', None)
        return airport
    def marine_contact(self,id):   
        contact = []
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            if doc_data.get('uid') == id:
                    for version in doc_data['versions']:
                        if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                            contact = version['applicationProfile']['contacts'].get('contact', None)
        return contact
    def marine_onboard(self,id):
        docs = self.get_documents_applications()  
        for doc in docs:
            doc_data = doc.to_dict()  
            if doc_data.get('uid') == id:
                    for version in doc_data['versions']:
                        if 'skills' in version and 'onboard' in version['skills']:
                            onboard = version['skills'].get('onboard', None)
        return onboard
    def marine_onland(self,id):
     
        docs = self.get_documents_applications()  
        for doc in docs:
            doc_data = doc.to_dict()  
            if doc_data.get('uid') == id:
                for version in doc_data['versions']:
                    if 'skills' in version and 'onland' in version['skills']:
                        onland = version['skills'].get('onland', None)
        return onland
    def marine_personaldocumention(self):
        pass
    def marine_land(self):
        docs = self.get_documents_seafarer()
        for doc in docs:
            doc_data = doc.to_dict()
            return doc_data