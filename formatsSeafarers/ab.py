from fpdf import FPDF
from skills import *
import requests
from io import BytesIO
from PIL import Image
from courses.ab import *
from datetime import datetime

def descargar_imagen_firebase(url):
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception(f"Error al descargar la imagen: {response.status_code}")

# Guardar la imagen localmente
def guardar_imagen_para_fpdf(imagen, nombre_archivo):
    imagen.save(nombre_archivo, format='PNG')  # O 'JPEG' si prefieres JPG


def dividir_texto(texto, pdf, ancho_celda):
    # Dividir el texto en palabras
    palabras = texto.split(' ')
    lineas = []
    linea_actual = ''
    
    for palabra in palabras:
        # Probar si la palabra cabe en la línea actual
        if pdf.get_string_width(linea_actual + palabra) < ancho_celda:
            linea_actual += palabra + ' '
        else:
            # Si no cabe, agregar la línea actual a la lista y comenzar una nueva
            lineas.append(linea_actual.strip())
            linea_actual = palabra + ' '
    
    # Agregar la última línea
    if linea_actual:
        lineas.append(linea_actual.strip())
    
    return lineas



class Ab_OsSeafarers():
    def format_ab_os(self, pdf, database, uid):
        
        pdf.set_fill_color(142,170,219)
        anchuras = [40, 50, 60, 40]
        pdf.add_page()

        pdf.alias_nb_pages()
        # Agregar contenido al PDF
        
       
        # Título del formulario
        pdf.set_xy(0, 30)
        pdf.set_font('calibri', '', 22)
        pdf.cell(0, 10, 'SEAFARER APPLICATION FORM', align='C')

        pdf.set_xy(70, 40)  # Ajustar la posición para el siguiente texto
        pdf.set_font('calibri', '', 14)
        pdf.cell(20, 10, 'POSITION APPLYING FOR RANK: ' )
        pdf.set_font('calibri', 'BU', 14)
        pdf.set_xy(135, 40)
        pdf.cell(6,10, 'AB')

        image = database.marine_image_seafarers(uid)
        imagen = descargar_imagen_firebase(image)
        guardar_imagen_para_fpdf(imagen, "imagen_descargada.png")
       # Agregar imagen al PDF con tamaño ajustado
        pdf.set_xy(30, 60)
        pdf.image("imagen_descargada.png", x=20, y=60, w=50, h=50)

        pdf.set_xy(20, 50)
        pdf.set_font('calibri', '', 12)
        pdf.cell(55, 10, '1. PERSONAL INFORMATION')

        pdf.set_font('calibri', '', 9) 
        pdf.set_xy(80, 55)

        # Definir anchos para alineación
        cell_width = 50
        big_cell_width = 100
        height = 7
        pdf.set_font('calibri', '', 9) 
        # Encabezado para Nombres

        fullnames = database.marine_firstname_seafarers(uid)
        fullLastname = database.marine_lastname_seafarers(uid)
        # Obtener un solo nombre y apellido de la base de datos

        # Altura de la celda
        height = 7

        # Dividir el nombre en primer y segundo nombre si existe
        nombres = fullnames.split(' ', 1)  # Divide en el primer espacio
        primer_nombre = nombres[0]  # Primer nombre
        segundo_nombre = nombres[1] if len(nombres) > 1 else ''  # Segundo nombre (si existe)

        # Dividir los apellidos en primer y segundo apellido si existe
        apellidos = fullLastname.split(' ', 1)  # Divide en el primer espacio
        primer_apellido = apellidos[0]  # Primer apellido
        segundo_apellido = apellidos[1] if len(apellidos) > 1 else ''  # Segundo apellido (si existe)

            # Nombre y apellidos
        pdf.cell(w=40, h=height, txt='NAME', border=1, align='L', fill=True)  # Etiqueta de "NAME"
        pdf.cell(w=40, h=height, txt=primer_nombre, border=1, align='C')  # Primer nombre
        pdf.cell(w=40, h=height, txt=segundo_nombre, border=1, align='C', ln=1)  # Segundo nombre (si existe)
        pdf.set_font('calibri', '', 9)

        # Dibujar la celda de "SURNAMES" con primer y segundo apellido
        pdf.set_xy(80, 62)  # Ajustar la posición para los apellidos
        pdf.cell(w=40, h=height, txt='SURNAMES', border=1, align='L', fill=True)  # Etiqueta de "SURNAMES"
        pdf.cell(w=40, h=height, txt=primer_apellido, border=1, align='C')  # Primer apellido
        pdf.cell(w=40, h=height, txt=segundo_apellido, border=1, align='C', ln=1)  # Segundo apellido (si existe)
        pdf.set_font('calibri', '', 9)

        # Fecha de nacimiento
        pdf.set_xy(80, 69)
        pdf.multi_cell(w=40, h=6.5, txt='DATE OF BIRTH\n(YYYY-MM-DD)', border=1, align='L', fill=True)
        date = database.marine_dateOfBirthSeafarers(uid) or ""
        pdf.set_xy(120, 69)
        pdf.cell(w=80, h=13, txt=date, border=1, align='C', ln=1)

        # Número de identificación
        pdf.set_xy(80, 82)
        pdf.multi_cell(w=40, h=14, txt='IDENTIFICATION NUMBER', border=1, align='L', fill=True)
        identification_data = database.marine_identification(uid) or []

        # Busca primero "Identification (ID, NID, etc.)", si no existe, busca "Passport"
        identification_number = next(
            (doc['data']['documentNumber'] for doc in identification_data
            if doc.get('data', {}).get('documentName', {}).get('name') == "Identification (ID, NID, etc.)"),
            None
        )

        # Si no se encontró identificación, intenta con "Passport"
        if identification_number is None:
            identification_number = next(
                (doc['data']['documentNumber'] for doc in identification_data
                if doc.get('data', {}).get('documentName', {}).get('name') == "Passport"),
                ""
            )

        print(identification_number)
        pdf.set_xy(120, 82)
        pdf.cell(w=80, h=9, txt=identification_number, border=1, align='C', ln=1)
        # Nacionalidad
        nationality = database.marine_nationality(uid)
        pdf.set_xy(80, 91)
        pdf.cell(w=40, h=height, txt='NATIONALITY', border=1, align='L', fill=True)
        pdf.cell(w=80, h=height, txt=nationality, border=1, align='C', ln=1)

        # Sexo y Estado Civil
        gender = database.marine_gender(uid)
        pdf.set_xy(80, 98)
        pdf.cell(w=40, h=7, txt='SEX', border=1, align='L', fill=True)
        pdf.cell(w=20, h=7, txt=gender, border=1, align='C')
        marital = database.marine_marital(uid)
        pdf.cell(w=30, h=7, txt='CIVIL STATUS', border=1, align='L', fill=True)
        pdf.cell(w=30, h=7, txt=marital, border=1, align='C', ln=1)

        # Altura, peso y BMI
        pdf.set_xy(80, 105)
        height = database.marine_height(uid)
        pdf.cell(w=25, h=7, txt='HEIGHT (Ft/in)', border=1, align='L', fill=True)
        pdf.cell(w=20, h=7, txt=height, border=1, align='C')
        weight = database.marine_weight(uid)
        pdf.cell(w=22, h=7, txt='WEIGHT (Lb)', border=1, align='L', fill=True)
        pdf.cell(w=18, h=7, txt=weight, border=1, align='C')
        pdf.cell(w=15, h=7, txt='BMI', border=1, align='L', fill=True)
        bmi = database.marine_bmi(uid)
        pdf.cell(w=20, h=7, txt=str(bmi), border=1, align='C', ln=1)

        # Configuración inicial
        pdf.ln(5)
        pdf.set_font('calibri', '', 9)

       # Save initial position
       # Guardar la posición inicial
      # Posición inicial
        x_inicial = pdf.get_x()
        y_inicial = pdf.get_y()

        # Calcular alturas sin dibujar aún, para determinar la altura máxima
        pdf.set_xy(x_inicial, y_inicial)
        pdf.multi_cell(w=40, h=7, txt="COMPLETE HOME ADDRESS", border=0)  # Sin border para solo medir altura
        height_complete_home = pdf.get_y() - y_inicial

        home = database.marine_home_address(uid) or ""
        pdf.set_xy(x_inicial + 40, y_inicial)
        pdf.multi_cell(w=50, h=7, txt=home, border=0)
        height_home_address = pdf.get_y() - y_inicial

        pdf.set_xy(x_inicial + 90, y_inicial)
        pdf.multi_cell(w=50, h=7, txt="NEARLY AIRPORT", border=0)
        height_nearly_airport = pdf.get_y() - y_inicial

        airport = database.marine_airport(uid) or ""
        pdf.set_xy(x_inicial + 140, y_inicial)
        pdf.multi_cell(w=50, h=7, txt=airport, border=0)
        height_airport = pdf.get_y() - y_inicial

        # Obtener la altura máxima para todas las celdas
        max_height = max(height_complete_home, height_home_address, height_nearly_airport, height_airport)

        # Dibujar cada celda de la fila con la altura máxima calculada
        pdf.set_xy(x_inicial, y_inicial)
        pdf.multi_cell(w=40, h=max_height, txt="COMPLETE HOME ADDRESS", border=1, align="L", fill=True)

        pdf.set_xy(x_inicial + 40, y_inicial)
        pdf.multi_cell(w=50, h=max_height, txt="", border=1, align="C")

        pdf.set_xy(x_inicial + 90, y_inicial)
        pdf.multi_cell(w=50, h=max_height, txt="NEARLY AIRPORT", border=1, align="L", fill=True)

        pdf.set_xy(x_inicial + 140, y_inicial)
        pdf.multi_cell(w=50, h=max_height, txt="", border=1, align="C")

        # Mover el cursor a la siguiente posición para continuar el flujo
        pdf.set_xy(x_inicial, y_inicial + max_height)



        # Segunda fila con "PHONE/CELL" y demás datos
        email = database.marine_email(uid,)
        
        pdf.cell(w=30, h=7, txt="PHONE/CELL", border=1, align="C", fill=True)
        cell = database.marine_cellphone(uid)
        
        pdf.cell(w=30, h=7, txt=cell, border=1, align="L")
        
        pdf.cell(w=30, h=7, txt="WHATSAPP", border=1, align="C", fill=True)
        
        pdf.cell(w=30, h=7, txt=cell, border=1, align="C")
        
        pdf.cell(w=20, h=7, txt="E-MAIL", border=1, align="L", fill=True)
        
        pdf.cell(w=50, h=7, txt=email, border=1, align="C", ln=1)

        # Tercera fila con "LANGUAGES"
        
        pdf.cell(w=30, h=7, txt="LANGUAGES", border=1, align="C",fill=True)
        
        pdf.cell(w=30, h=7, txt="SPANISH", border=1, align="L", fill=True)
        spanish = database.marine_lang_span(uid) or ""
        pdf.cell(w=30, h=7, txt=str(spanish) + "%", border=1, align="R")
        pdf.cell(w=30, h=7, txt="ENGLISH", border=1, align="L",fill=True)
        english = database.marine_lang_engl(uid)
        pdf.cell(w=20, h=7, txt=str(english) + "%", border=1, align="R")
        
        pdf.cell(w=20, h=7, txt="OTHERS", border=1, align="L", fill= True)
        
        pdf.cell(w=30, h=7, txt="%", border=1, align="R", ln=1)

        pdf.ln(5)
        pdf.set_font('calibri','',9)
        marlin = database.marine_marlins(uid) or []

        if isinstance(marlin, list) and marlin:
            marlins = marlin[0]  # Accede al primer elemento si la lista no está vacía
        else:
            # Si `marlin` está vacío o no es una lista, usa un diccionario vacío con campos predeterminados
            marlins = {
                'PercentageTotal': "",
                'IssueDate': "",
                'PlaceIssue': "",
                'PercentageListening': "",
                'PercentageGrammar': "",
                'PercentageVocabulary': "",
                'PercentageNumbers': "",
                'PercentageReading': ""
            }

        # Continúa con la lógica de creación del PDF
        pdf.cell(w=0, h=7, txt="MARLINS / LANGUAGE -TEST", border=1, align="C", ln=1, fill=True)

        # Encabezados de columnas principales
        pdf.cell(w=60, h=7, txt="TOTAL %", border=1, align="C", fill=True)
        pdf.cell(w=60, h=7, txt="ISSUE DATE", border=1, align="C", fill=True)
        pdf.cell(w=70, h=7, txt="PLACE OF ISSUE", border=1, align="C", ln=1, fill=True)

        # Datos principales
        pdf.cell(w=60, h=7, txt=str(marlins['PercentageTotal']) + "%", border=1, align="R")
        pdf.cell(w=60, h=7, txt=marlins['IssueDate'], border=1, align="C")
        pdf.cell(w=70, h=7, txt=marlins['PlaceIssue'], border=1, align="C", ln=1)

        # Encabezados de secciones de habilidades
        pdf.cell(w=30, h=7, txt='LISTENING', border=1, align='L', fill=True)
        pdf.cell(w=40, h=7, txt='GRAMMAR', border=1, align='L', fill=True)
        pdf.cell(w=40, h=7, txt='VOCABULARY', border=1, align='L', fill=True)
        pdf.cell(w=40, h=7, txt='TIME AND NUMBERS', border=1, align='C', fill=True)
        pdf.cell(w=40, h=7, txt='READING', border=1, align='L', ln=1, fill=True)

        # Datos de habilidades individuales
        pdf.cell(w=30, h=7, txt=str(marlins['PercentageListening']) + '%', border=1, align='R')
        pdf.cell(w=40, h=7, txt=str(marlins['PercentageGrammar']) + '%', border=1, align='R')
        pdf.cell(w=40, h=7, txt=str(marlins['PercentageVocabulary']) + '%', border=1, align='R')
        pdf.cell(w=40, h=7, txt=str(marlins['PercentageNumbers']) + '%', border=1, align='R')
        pdf.cell(w=40, h=7, txt=str(marlins['PercentageReading']) + '%', border=1, align='R')
        pdf.ln(10)
        pdf.set_font('calibri','',9)
        pdf.cell(0,10,txt="2. EMERGENCY CONTACT / NEXT OF KIN", border=0, align='L')
        pdf.ln(10)
 
        datos = database.marine_contact(uid,)
        # Dibujar cada fila de datos
        cell_height = 7  # Altura base para cada línea de texto

        # Anchos específicos para cada columna
        anchuras = [40, 50, 60, 40]

        # Dibujar encabezado
        pdf.cell(w=anchuras[0], h=cell_height, txt="RELATIONSHIP", border=1, align='C', fill=True)
        pdf.cell(w=anchuras[1], h=cell_height, txt="COMPLETE NAME", border=1, align='C', fill=True)
        pdf.cell(w=anchuras[2], h=cell_height, txt="TELEPHONE NUMBER / MOBILE", border=1, align='C', fill=True)
        pdf.cell(w=anchuras[3], h=cell_height, txt="ADDRESS", border=1, align='C', ln=1, fill=True)

        # Dibujar cada fila de datos
        for fila in datos:
            # Obtener valores de cada campo
            nombre_completo = f"{fila.get('firstNames', '')} {fila.get('lastNames', '')}"
            telefono = fila.get('phone', {}).get('value', '')
            direccion = fila.get('address', '')
            relacion = fila.get('relationship', '')

            # Calcular el número de líneas necesarias en cada celda
            relacion_lineas = pdf.multi_cell(anchuras[0], cell_height, relacion, border=0, align='L', split_only=True)
            nombre_lineas = pdf.multi_cell(anchuras[1], cell_height, nombre_completo, border=0, align='L', split_only=True)
            telefono_lineas = pdf.multi_cell(anchuras[2], cell_height, telefono, border=0, align='L', split_only=True)
            direccion_lineas = pdf.multi_cell(anchuras[3], cell_height, direccion, border=0, align='L', split_only=True)

            # Determinar la altura de la fila según la máxima cantidad de líneas en cualquier celda
            max_lineas = max(len(relacion_lineas), len(nombre_lineas), len(telefono_lineas), len(direccion_lineas))
            altura_fila = cell_height * max_lineas

            # Añadir una nueva página si la altura sobrepasa el límite
            if pdf.get_y() + altura_fila > pdf.page_break_trigger:
                pdf.add_page()

            # Guardar posición inicial Y
            y_inicial = pdf.get_y()
            x_inicial = pdf.get_x()  # Posición X para la primera columna

            # Dibujar cada celda de la fila con el ancho y altura ajustada
            pdf.set_xy(x_inicial, y_inicial)
            pdf.cell(anchuras[0], altura_fila, relacion, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0], y_inicial)

            pdf.cell(anchuras[1], altura_fila, nombre_completo, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1], y_inicial)

            pdf.cell(anchuras[2], altura_fila, telefono, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2], y_inicial)

            # Celda para la dirección con multi_cell para permitir el salto de línea automático
            pdf.multi_cell(anchuras[3], cell_height, direccion, border=1, align='C')

            # Ajustar la posición y para la siguiente fila, considerando la altura máxima calculada
            pdf.set_y(y_inicial + altura_fila)
            
        pdf.ln(10)

        pdf.cell(0, 10, txt='3.WORK EXPERIENCE ONBOARD', align="L",)
        pdf.ln(10)

        
        anchuras_columnas = [25, 25, 32, 20, 18, 18, 23, 25]  
        altura_fila = [7,7,14,7,14,14,14,14]

        titulos_columnas = [
        'DATE ON  (MM/DD/YYYY)',
        'DATE OFF (MM/DD/YYYY)',
        'COMPANY NAME',
        'VESSEL NAME',
        'IMO #',
        'GT / HP',
        'TYPE OF VESSEL',
        'RANK/POSITION'
        ]
        x_inicial = pdf.get_x()
        y_inicial = pdf.get_y()
        align_type = ['C', 'C', 'C', 'L', 'C', 'L', 'C', 'C']
        pdf.set_xy(x_inicial, y_inicial)
        pdf.set_font('calibri','', 9)
        for i in range(len(titulos_columnas)):
            pdf.set_xy(x_inicial, y_inicial)
            
            # Si estás usando una lista para la altura de fila, usa el índice i para acceder a cada altura
            if isinstance(altura_fila, list):
                altura_actual = altura_fila[i]
            else:
                altura_actual = altura_fila

            # Dividir el texto del título si es necesario
            lines = pdf.multi_cell(anchuras_columnas[i], altura_actual / 2, titulos_columnas[i], border=0, align=align_type[i], split_only=True, fill=True)
            num_lines = len(lines)

            # Ajustar la altura de la celda según el número de líneas
            adjusted_height = max(altura_actual, altura_actual / 2 * num_lines)
            
            # Verificar si se necesita un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()
                pdf.set_xy(x_inicial, y_inicial)

            # Imprimir la celda del título
            pdf.multi_cell(anchuras_columnas[i], altura_actual / 2, titulos_columnas[i], border=1, align=align_type[i], fill=True)

            # Actualizar la posición x para la siguiente celda
            x_inicial += anchuras_columnas[i]
        
       # Retrieve and sort data by 'dateOn' in descending order
        onboard = sorted(database.marine_onboard(uid), key=lambda x: x.get('dateOn', ''), reverse=True)

        nuevaaltura_fila = 7  # Uniform row height

        for fila in onboard:
            # Extract vessel type or default to an empty string if not available
            tipo_vessel = fila.get('typeOfVessel', [{}])[0].get('name', '') if fila.get('typeOfVessel') else ''

            # List of column data in the correct order
            columnas = [
                fila.get('dateOn', ''),               # Start date
                fila.get('dateOff', ''),              # End date
                fila.get('companyName', ''),          # Company name
                fila.get('vesselName', ''),           # Vessel name
                fila.get('imo#', ''),                 # IMO number
                fila.get('gt/hp', ''),                # GT/HP
                tipo_vessel,                          # Vessel type
                fila.get('rank/position', '')         # Rank/position
            ]

            x_inicial = pdf.get_x()  # Initial X position before printing the row
            max_height = nuevaaltura_fila  # Default row height

            # Draw each cell in the row
            for i, valor in enumerate(columnas):
                pdf.cell(w=anchuras_columnas[i], h=max_height, txt=valor, align='C', border=1)
                x_inicial += anchuras_columnas[i]
                pdf.set_x(x_inicial)

            # Move to the next line after completing the row
            pdf.ln(max_height)



        # Salto de línea adicional después de cada grupo de filas
        pdf.ln(40)
        pdf.cell(0, 10, txt='4. Personal Documentation / Seafarer Documentation', align='L',ln=1)


            
        pdf.cell(w=0, h=7, txt='PERSONAL DOCUMENTATION / SEAFARER DOCUMENTATION', align='C', border=1, ln=1,fill=True)
        pdf.set_font('Calibri', '', 9)
       # Títulos de las columnas
        titulos_columnas = [
            "TYPE OF DOCUMENT / ID",
            "COUNTRY OF ISSUE",
            "NO.",
            "ISSUED AT (PLACE)",
            "DATE OF ISSUE (MM / DD / YYYY)",
            "VALID UNTIL (MM / DD / YYYY)"
        ]

        # Definir las anchuras de las columnas
        anchuras_columnas = [40, 30, 30, 30, 30, 30]

        # Altura de la fila
        altura_fila = 7
        
        # Imprimir los encabezados de la tabla
        for i, titulo in enumerate(titulos_columnas):
            pdf.cell(w=anchuras_columnas[i], h=altura_fila, txt=titulo, border=1, align='C', fill=True)
        pdf.ln(altura_fila)

        # Obtener los documentos
        personalDocuments = database.marine_personaldocumention(uid)
      
# Lista de documentos solo en la primera columna de la primera fila
       ## Lista de documentos predeterminada
# Lista de documentos predeterminada
# Lista de documentos predeterminada
        documents = [
            "COC II/5",
            "COC II/4",
            "B1/ B2",
            "FLAG CERTIFICATES",
            "FLAG SEAMANBOOK",
            "MCV",
            "PASSPORT",
            "SEAMAN'S BOOK (NATIONAL)",
            "US VISA C1-D"
        ]

        # Recorre toda la lista de documentos y muestra 8 filas siempre
        for document_name in documents:
            # Guardar posición inicial
            x_inicial = pdf.get_x()
            y_inicial = pdf.get_y()

            # Inicializar valores vacíos
            country = ""
            document_number = ""
            issued_at = ""
            date_of_issue = ""
            valid_until = ""

            # Buscar en `personalDocuments` el documento correspondiente al nombre actual
            for document in personalDocuments:
                doc_name = document.get('data', {}).get('documentName', {}).get('name', '').upper()
                
                # Comparar el nombre actual de `documents` con el nombre en `personalDocuments`
                if doc_name == document_name.upper():
                    country = document.get('data', {}).get('country', {}).get('value', '')
                    document_number = document.get('data', {}).get('documentNumber', '')
                    issued_at = document.get('data', {}).get('placeIssue', '')
                    date_of_issue = document.get('data', {}).get('issueDate', '')
                    valid_until = document.get('data', {}).get('expirationDate', '')
                    break  # Detener la búsqueda una vez encontrado el documento correspondiente

            # Contenido de cada columna en la fila actual
            columnas = [document_name, country, document_number, issued_at, date_of_issue, valid_until]

            # Calcular la altura máxima de la fila
            alturas = [pdf.get_string_width(valor) / anchuras_columnas[i] * altura_fila for i, valor in enumerate(columnas)]
            max_altura = max(altura_fila, *alturas)

            # Imprimir la primera columna con fondo (fill)
             # Color de fondo (puedes ajustar este valor)
            pdf.cell(w=anchuras_columnas[0], h=max_altura, txt=str(columnas[0]), border=1, align='C', fill=True)

            # Imprimir las demás celdas sin fondo
            for i in range(1, len(columnas)):
                pdf.cell(w=anchuras_columnas[i], h=max_altura, txt=str(columnas[i]), border=1, align='C', fill=False)

            # Mover a la siguiente línea
            pdf.ln(max_altura)



        pdf.ln(20)
        pdf.set_font('calibri', '',9)

        pdf.cell(0, 10, txt='5. TRAINING AND CERTIFICATION.', align='L')
        pdf.ln(10)
        
        pdf.cell(w=0, h=7, txt='STCW CERTIFICATES', align='C', border=1, ln=1, fill=True)

        # Definir los títulos de las columnas
        titulos_columnas = [
            "DESCRIPTION OF CERT / COURSE",
            "COUNTRY OF ISSUE",
            "NUMBER",
            "DATE OF ISSUE (MM/DD/YYYY)",
            "DATE OF EXPIRY (MM/DD/YYYY)"
        ]

        # Definir las anchuras de las columnas
        anchuras_columnas = [40, 30, 20, 50, 50]

        # Definir la altura de la fila
        altura_fila = [7,14,14,14,14,14]  # Si tienes diferentes alturas, podrías cambiar esto a una lista

        # Alineación por columna (en este caso se alinean al centro, puedes modificar si es necesario)
        align_type = ['C', 'C', 'C', 'C', 'C']

        # Coordenadas iniciales para comenzar a escribir
        x_inicial = pdf.get_x()
        y_inicial = pdf.get_y()

        # Imprimir los encabezados
        for i in range(len(titulos_columnas)):
            pdf.set_xy(x_inicial, y_inicial)
            
            # Si la altura de la fila es una lista, selecciona la altura específica
            if isinstance(altura_fila, list):
                altura_actual = altura_fila[i]
            else:
                altura_actual = altura_fila

            # Dividir el texto del título si es necesario (sin imprimir aún)
            lines = pdf.multi_cell(anchuras_columnas[i], altura_actual / 2, titulos_columnas[i], border=0, align=align_type[i], split_only=True, fill=True)
            num_lines = len(lines)

            # Ajustar la altura de la celda según el número de líneas
            adjusted_height = max(altura_actual, altura_actual / 2 * num_lines)

            # Verificar si se necesita un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()
                pdf.set_xy(x_inicial, y_inicial)

            # Imprimir la celda del título con el ajuste de altura
            pdf.multi_cell(anchuras_columnas[i], altura_actual / 2, titulos_columnas[i], border=1, align=align_type[i], fill=True)

            # Actualizar la posición x para la siguiente celda
            x_inicial += anchuras_columnas[i]

        # Mover a la siguiente línea después de completar la fila de encabezados

        """""courses = [
        "Basic Safety Maritime Training Course (BST)",
        "Proficiency in personal Survival Techniques 1.19",
        "Fire prevention and firefighting 1.20",
        "Elementary First Aid 1.13",
        "Personal Safety and Social Responsibilities 1.21",
        "Security Awareness Training for All Seafarers Course 3.27",
        "Security Awareness Training for All Seafarers with Designated Security Duties Course 3.26",
        "Safety Training for Personnel Providing Direct Services to Passengers in Passenger Spaces 1.44",
        "Passenger Ship Crowd Management Training 1.41",
        "Passenger Ship Crisis Management Training 1.42",
        "Passenger Safety, Cargo Safety and Hull Integrity Training 1.29",
        "Proficiency in the Management of Survival Crafts and Rescue Boats Course 1.23",
        "Basic Cargo Training Operations for Oil and Chemical Tanker Course 1.01",
        "Advanced Fire Fighting 2.03",
        "Engine Rating Course / WER",
        "Able Engine Course",

        ]
        """""
        course = AbCourses()
        courses = course.courses()
        # Agregar las celdas con los cursos

        pdf.set_font("calibri","",9)
        column_widths = [40, 30, 20, 50, 50]
        cell_height = 7 
        
        # Retrieve certificates from the database
        # Retrieve certificates from the database
        certificates = database.marine_certificates(uid)
        print(certificates)

        for i, course in enumerate(courses):
            # Check if there's a matching certificate for the course
            if i < len(certificates):
                certificate_data = certificates[i].get('data', {})
                
                # Retrieve specific fields from each certificate data and format dates
                country = certificate_data.get('country', {}).get('countryName', "")
                number = certificate_data.get('certificateNumber', "")
                
                # Format issue_date to MM/DD/YYYY
                issue_date = certificate_data.get('issueDate', "")
                if issue_date:
                    issue_date = datetime.strptime(issue_date, '%Y-%m-%d').strftime('%m/%d/%Y')
                
                # Format expiry_date to MM/DD/YYYY
                expiry_date = certificate_data.get('expirationDate', "")
                if expiry_date:
                    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').strftime('%m/%d/%Y')
            else:
                # Default values if no corresponding certificate data
                country, number, issue_date, expiry_date = "", "", "", ""

            # Split course name into lines if needed
            lines = pdf.multi_cell(column_widths[0], cell_height, course, border=0, align='L', split_only=True, fill=True)
            num_lines = len(lines)
            adjusted_height = max(cell_height * num_lines, cell_height)

            # Page break check
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Course cell
            pdf.multi_cell(column_widths[0], cell_height, course, border=1, align='L', fill=True)

            # Set X position for the rest of the columns
            pdf.set_xy(pdf.get_x() + column_widths[0], pdf.get_y() - adjusted_height)

            # Fill remaining columns with data from certificates
            pdf.cell(w=column_widths[1], h=adjusted_height, txt=country, border=1, align='C', ln=0)
            pdf.cell(w=column_widths[2], h=adjusted_height, txt=number, border=1, align='C', ln=0)
            pdf.cell(w=column_widths[3], h=adjusted_height, txt=issue_date, border=1, align='C', ln=0)
            pdf.cell(w=column_widths[4], h=adjusted_height, txt=expiry_date, border=1, align='C', ln=1)

        
        pdf.set_font('calibri', '', 9)
        pdf.cell(0,10, txt='6. WORK EXPERIENCE ONSHORE', align='L')
        pdf.ln(10)
        
        encabezados = [
        'DATE ON (MM/DD/YYYY)', 'DATE OFF (MM/DD/YYYY)', 'COMPANY NAME / SHIP-OWNER', 
        'DUTIES OR RESPONSABILITIES', 'RANK/POSITION', 'REASON FOR LEAVING', 
        'NAME OF CONTACT \nPERSON & TELEPHONE NUMBER'
        ]
        # Definir las anchuras de las celdas
        ancho_celdas = [22, 22, 27, 27, 27, 25, 40]

        # Definir la altura de las celdas
        altura_fila = [14, 14, 14, 14, 28, 14,9.3]

        # Definir la alineación de cada columna (esto faltaba)
        align_type = ['C', 'C', 'C', 'C', 'C', 'C', 'C']

        # Coordenadas iniciales para comenzar a escribir
        x_inicial = pdf.get_x()
        y_inicial = pdf.get_y()

        # Verificar que todas las listas tienen la misma longitud
        if not (len(encabezados) == len(ancho_celdas) == len(altura_fila) == len(align_type)):
            raise ValueError("Las listas encabezados, ancho_celdas, altura_fila y align_type deben tener la misma longitud.")

        # Imprimir los encabezados
        for i in range(len(encabezados)):
            pdf.set_xy(x_inicial, y_inicial)
            
            # Si la altura de la fila es una lista, selecciona la altura específica
            altura_actual = altura_fila[i]

            # Dividir el texto del encabezado si es necesario (sin imprimir aún)
            lines = pdf.multi_cell(ancho_celdas[i], altura_actual / 2, encabezados[i], border=0, align=align_type[i], split_only=True,fill=True)
            num_lines = len(lines)

            # Ajustar la altura de la celda según el número de líneas
            adjusted_height = max(altura_actual, altura_actual / 2 * num_lines)

            # Verificar si se necesita un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()
                pdf.set_xy(x_inicial, y_inicial)

            # Imprimir la celda del encabezado con el ajuste de altura
            pdf.multi_cell(ancho_celdas[i], altura_actual / 2, encabezados[i], border=1, align=align_type[i],fill=True)

            # Actualizar la posición x para la fsiguiente celda
            x_inicial += ancho_celdas[i]
        altura_fila = [14, 14, 14, 7, 14, 14,14]
        onland = database.marine_onland(uid,)
        
        for data in onland:
            # Reset initial x and y coordinates for each new row
            x_inicial = pdf.get_x()
            y_inicial = pdf.get_y()
            
            # Print each piece of data in a single line using cell
            pdf.set_xy(x_inicial, y_inicial)
            pdf.cell(ancho_celdas[0], altura_fila[0], txt=data.get('dateOn', ''), border=1, align='C')
            
            x_inicial += ancho_celdas[0]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.cell(ancho_celdas[1], altura_fila[1], txt=data.get('dateOff', ''), border=1, align='C')

            x_inicial += ancho_celdas[1]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.cell(ancho_celdas[2], altura_fila[2], txt=data.get('companyName', ''), border=1, align='C')

            x_inicial += ancho_celdas[2]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.cell(ancho_celdas[3], altura_fila[3], txt=data.get('dutiesOrResponsibilities', ''), border=1, align='C')

            x_inicial += ancho_celdas[3]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.cell(ancho_celdas[4], altura_fila[4], txt=data.get('rank/position', ''), border=1, align='C')

            x_inicial += ancho_celdas[4]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.cell(ancho_celdas[5], altura_fila[5], txt=data.get('reasonForLeaving', ''), border=1, align='C')

            x_inicial += ancho_celdas[5]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.cell(ancho_celdas[6], altura_fila[6], txt=data.get('nameOfContactPersonAndTelephoneNumber', ''), border=1, align='C')
            
            pdf.ln(altura_fila[0])  # Move to the next row

 

        pdf.cell(0,10, txt='7. HIGHEST LEVEL OF EDUCATION / OTHER TRAINING OR CERTIFICATE', align='L')
        pdf.ln(10)
        
        pdf.cell(w=0, h=7,txt='HIGHEST LEVEL OF EDUCATION / OTHER TRAINING OR CERTIFICATE', align='C', border=1, ln=1, fill=True)
        pdf.cell(w=90,h=7,txt='NAME OF EDUCATION INSTITUTION/TECHNICAL INSTITUTE/UNIVERSITY', align='C', border=1, fill=True)
        pdf.cell(w=40,h=7,txt='OBTAINED TITLE OR GRADE', align='C', border=1, fill=True)
        pdf.cell(w=30,h=7,txt='COUNTRY OF ISSUE', align='C', border=1, fill=True)
        pdf.cell(w=30,h=7,txt='DATE ON(MM/DD/YYYY)', align='C', border=1, fill=True)
        pdf.cell(w=30,h=7,txt='DATE OFF(MM/DD/YYYY)', align='C', border=1, fill=True)
        
        datos_educacion = [


        ]
        pdf.ln(7)
        # Añadir los datos
        for fila in datos_educacion:
            pdf.cell(w=90, h=7, txt=fila[0], align='C', border=1)
            pdf.cell(w=40, h=7, txt=fila[1], align='C', border=1)
            pdf.cell(w=30, h=7, txt=fila[2], align='C', border=1)
            pdf.cell(w=30, h=7, txt=fila[3], align='C', border=1)
            pdf.ln(7)
            

        pdf.ln(5)

        pdf.cell(0,10, txt='8. VACCINATION BOOK', align='L')
        pdf.ln(10)
        
        pdf.cell(w=0, h=6,txt='VACCINATION BOOK', align='C', border=1,ln=1,fill=True)

        pdf.set_font('calibri','',9)

        # Assuming `vaccines` is populated from the database
        vaccines = database.marine_vaccines(uid) or {}

        # Setting up the PDF structure
        pdf.cell(w=40, h=6, txt="TYPE OF VACCINE", border=1, align='C', fill=True)
        pdf.cell(w=40, h=6, txt="COUNTRY", border=1, align='C', fill=True)
        pdf.cell(w=40, h=6, txt="DOZE", border=1, align='C', fill=True)
        pdf.cell(w=40, h=6, txt='DATE OF ISSUE (MM / DD / YYYY)', align='C', border=1, fill=True)
        pdf.cell(w=30, h=6, txt='VACCINATION MARK', align='C', border=1, ln=1, fill=True)

        # Fill COVID vaccine data
        for card in vaccines.get('covid', {}).get('cards', []):
            pdf.cell(w=40, h=6, txt="COVID BOOK", border=1, align='C', fill=True)
            pdf.cell(w=40, h=6, txt=card.get('CountryIssue', {}).get('CountryName', ''), border=1, align='C')
            pdf.cell(w=40, h=6, txt=card.get('Doze', ''), border=1, align='C', fill=True)
            
            # Format IssueDate directly
            issue_date = card.get('IssueDate', '')
            formatted_issue_date = datetime.strptime(issue_date, '%Y-%m-%d').strftime('%m/%d/%Y') if issue_date else ''
            
            pdf.cell(w=40, h=6, txt=formatted_issue_date, border=1, align='C')
            pdf.cell(w=30, h=6, txt=card.get('VaccineBrand', {}).get('name', ''), align='C', border=1, ln=1)

        # Fill Yellow Fever vaccine data
        for card in vaccines.get('yellowFever', {}).get('cards', []):
            pdf.cell(w=40, h=6, txt="YELLOW FEVER", border=1, align='C', fill=True)
            pdf.cell(w=40, h=6, txt=card.get('CountryIssue', {}).get('CountryName', ''), border=1, align='C')
            pdf.cell(w=40, h=6, txt=card.get('Doze', ''), border=1, align='C', fill=True)
            
            # Format IssueDate directly
            issue_date = card.get('IssueDate', '')
            formatted_issue_date = datetime.strptime(issue_date, '%Y-%m-%d').strftime('%m/%d/%Y') if issue_date else ''
            
            pdf.cell(w=40, h=6, txt=formatted_issue_date, border=1, align='C')
            pdf.cell(w=30, h=6, txt=card.get('VaccineBrand', {}).get('name', ''), align='C', border=1, ln=1)
                        
        skills = Skills()
        skills.ab_os(pdf, database,uid)
        #skills.messman(pdf)
        pdf.ln(10)
   


