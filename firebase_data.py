import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Usar una cuenta de servicio.
class FirebaseData():
    
    def __init__(self):
        
        self.cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def get_documents_applications(self):
        
        users_ref = self.db.collection('applications')
        return users_ref.stream()
    
    def get_documents_seafarer(self):
        users_ref = self.db.collection('usersData')
        return users_ref.stream()
    
    def marine_name(self,id):   
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
    def marine_email(self, id):
        docs = self.get_documents_seafarer()  # Obtiene un nuevo stream de documentos
        email = None  # Inicializa la variable email

        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario
            if doc_data.get('uid') == id:  # Verifica si el UID coincide
                email = doc_data.get('email', None)  # Extrae el email si existe
                break  # Sale del bucle una vez que encuentra el email

        return email  # Retorna el email encontrado o None si no existe
        
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
    def marine_personaldocumention(self, id):
        # Obtiene un nuevo stream de documentos
        docs = self.get_documents_seafarer()

        # Inicializa una variable para almacenar los documentos encontrados
        seafarer_documents = None

        # Itera sobre los documentos para encontrar el ID coincidente
        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario

            # Verifica si el UID del documento coincide con el ID proporcionado
            if doc_data.get('uid') == id:
                # Verifica que 'seafarerData' y 'seafarerDocument' existan en el documento
                if 'seafarerData' in doc_data and 'seafarerDocument' in doc_data['seafarerData']:
                    seafarer_documents = doc_data['seafarerData']['seafarerDocument']
                    
                    # Itera sobre cada documento dentro de 'seafarerDocument'
                    for document in seafarer_documents:
                        # Aquí puedes trabajar con cada documento individualmente
                        print(document)  # O procesa el documento de la forma que desees
                else:
                    print("No se encontró seafarerData o seafarerDocument en los datos.")
                break  # Sale del bucle una vez que encuentra el documento correcto

        # Retorna el contenido de seafarerDocument, o None si no se encuentra
        return seafarer_documents
    def marine_certificates(self,uid):
        
