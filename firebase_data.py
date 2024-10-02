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

    def get_documents(self):
        # Cada vez que se llame a esta función, se crea un nuevo stream de documentos
        users_ref = self.db.collection('applications')
        return users_ref.stream()
        
    def marine_name(self):   
        name = []
        docs = self.get_documents()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            for datos in doc_data['versions']:
                name.append(datos['applicationProfile']['profile']['firstName'])
        new_name = name[0].split()
        return new_name[0]
        
    def marine_secondName(self):  # He cambiado el nombre de esta segunda función para evitar conflicto
        name = []
        docs = self.get_documents()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            for datos in doc_data['versions']:
                name.append(datos['applicationProfile']['profile']['firstName'])
        new_name = name[0].split()
        return new_name[1]
    def marine_lastname(self):  # He cambiado el nombre de esta segunda función para evitar conflicto
        name = []
        docs = self.get_documents()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            for datos in doc_data['versions']:
                name.append(datos['applicationProfile']['profile']['lastName'])
        new_name = name[0].split()
        return new_name[0]
    def marine_secondLastname(self):  # He cambiado el nombre de esta segunda función para evitar conflicto
        name = []
        docs = self.get_documents()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            for datos in doc_data['versions']:
                name.append(datos['applicationProfile']['profile']['lastName'])
        new_name = name[0].split()
        return new_name[1]
    def marine_dateOfBirth(self):
        dates = []
        docs = self.get_documents()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            for datos in doc_data['versions']:
                dates.append(datos['applicationProfile']['profile']['dateBirth'])

        return dates[0]
    def marine_nationality(self):
        nationality = []
        docs = self.get_documents()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            for datos in doc_data['versions']:
                nationality.append(datos['applicationProfile']['profile']["countryResidency"]["CountryName"])

        return nationality[0]
    def marine_gender(self):
        gender = []
        docs = self.get_documents()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            for datos in doc_data['versions']:
                gender.append(datos['applicationProfile']['profile']["gender"]["name"])

        return gender[0][0]
    def marine_marital(self):
        marital = []
        docs = self.get_documents()  # Obtén un nuevo stream cada vez que llames a la función
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            # nombre de los aplicantes
            for datos in doc_data['versions']:
                marital.append(datos['applicationProfile']['profile']["maritalStatus"]["name"])

        return marital[0]