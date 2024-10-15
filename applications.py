import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Usar una cuenta de servicio.
class FirebaseDataApplication():
    
    def __init__(self):
        
        self.cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
        self.app = firebase_admin.initialize_app(self.cred, name= 'application')
        self.db = firestore.client(self.app)

    def get_documents_applications(self):
        
        users_ref = self.db.collection('applications')
        return users_ref.stream()
    
    def get_documents_seafarer(self):
        users_ref = self.db.collection('usersData')
        return users_ref.stream()

    def marine_position(self, id):
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        position = None  # Inicializar la variable position como None por defecto
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            
            # Verificar si el uid coincide con el id proporcionado
            if doc_data.get('uid') == id:
                for version in doc_data['versions']:
                    # Extraer el nombre del perfil dentro de la versión
                    if 'startApplication' in version and 'position' in version['startApplication']:
                        # 'position' es una lista, así que debes iterar sobre ella
                        for pos in version['startApplication']['position']:
                            position = pos.get('id', None)  # Acceder al id dentro de cada posición
                            break  # Si solo necesitas la primera posición, puedes romper el bucle aquí
        
        return position
    def marine_image(self, id):
        # Get all seafarer documents
        docs = self.get_documents_seafarer()

        # Loop through each document
        for doc in docs:
            doc_data = doc.to_dict()

            # Check if the UID matches the provided ID
            if doc_data.get('uid') == id:
                # Check if 'seafarerData' and 'seafarerCertificates' exist
                if 'seafarerData' in doc_data and 'photoURL' in doc_data['seafarerData']:
                    return doc_data['seafarerData']['photoURL']
        
        # Return an empty list if no matching certificate is found
        return []
    
    def marine_image_application(self,id, version):   
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            
            # Verificar si el uid coincide con el id proporcionado
            if doc_data.get('uid') == id:
                for version in doc_data['versions']:
                    urlImage = version['photoURL']
        return urlImage
    def marine_name(self,id, version):   
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
        
    
        
    def marine_lastname(self,id, version):  # He cambiado el nombre de esta segunda función para evitar conflicto
        
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            if doc_data.get('uid') == id:
                for version in doc_data['versions']:
                    if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                        lastname = version['applicationProfile']['profile'].get('lastName', None)
        return lastname
    def marine_dateOfBirth(self,id,version):
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            if doc_data.get('uid') == id:
                for version in doc_data['versions']:
                    if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                        birth = version['applicationProfile']['profile'].get('dateBirth', None)
        return birth
    def marine_nationality(self,id, version):
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            if doc_data.get('uid') == id:
                for version in doc_data['versions']:
                    if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                        nationality = version['applicationProfile']['profile']['countryBirth'].get('CountryName', None)
        return nationality
    def marine_gender(self,id, version):
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            if doc_data.get('uid') == id:
                    for version in doc_data['versions']:
                        if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                            gender = version['applicationProfile']['profile']['gender'].get('name', None)
        return gender[0]
    def marine_marital(self,id, version):
        marital = []
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            if doc_data.get('uid') == id:
                    for version in doc_data['versions']:
                        if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                            marital = version['applicationProfile']['profile']['maritalStatus'].get('name', None)
        return marital
    def marine_home_address(self,id,version):
        marital = []
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            if doc_data.get('uid') == id:
                    for version in doc_data['versions']:
                        if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                            airport = version['applicationProfile']['profile'].get('address', None)
        return airport
    def marine_airport(self,id, version):
        airport = []
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            if doc_data.get('uid') == id:
                    for version in doc_data['versions']:
                        if 'applicationProfile' in version and 'profile' in version['applicationProfile']:
                            airport = version['applicationProfile']['profile'].get('airport', None)
        return airport
    def marine_email(self, id, version):
        docs = self.get_documents_seafarer()  # Obtiene un nuevo stream de documentos
        email = None  # Inicializa la variable email

        for doc in docs:
            doc_data = doc.to_dict()  # Convierte el documento en un diccionario
            if doc_data.get('uid') == id:  # Verifica si el UID coincide
                email = doc_data.get('email', None)  # Extrae el email si existe
                break  # Sale del bucle una vez que encuentra el email

        return email  # Retorna el email encontrado o None si no existe
        
    def marine_contact(self,id, version):   
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
    def marine_onboard(self,id, version):
        docs = self.get_documents_applications()  
        for doc in docs:
            doc_data = doc.to_dict()  
            if doc_data.get('uid') == id:
                    for version in doc_data['versions']:
                        if 'skills' in version and 'onboard' in version['skills']:
                            onboard = version['skills'].get('onboard', None)
        return onboard
    def marine_onland(self,id, version):
     
        docs = self.get_documents_applications()  
        for doc in docs:
            doc_data = doc.to_dict()  
            if doc_data.get('uid') == id:
                for version in doc_data['versions']:
                    if 'skills' in version and 'onland' in version['skills']:
                        onland = version['skills'].get('onland', None)
        return onland
    
        
        # Return an empty list if no matching certificate is found
        return []
    def marine_vaccines(self,id, version):
        contact = []
        docs = self.get_documents_applications()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            if doc_data.get('uid') == id:
                    for version in doc_data['versions']:
                        if 'applicationProfile' in version and 'vaccines' in version['applicationProfile']:
                            vaccines = version['applicationProfile'].get('vaccines', None)
        return vaccines
