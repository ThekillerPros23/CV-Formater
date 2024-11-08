from fpdf import FPDF
from skills import *
import requests
from io import BytesIO
from PIL import Image


class PDF(FPDF):
    def header(self):
        # Solo agregar el encabezado en la primera página
        if self.page_no() == 1:  
            self.image("LOGISTIC-SinFondo.png", 160, 8, 33)  # Alineado a la derecha
    def footer(self):
        self.set_text_color(0,0,0)
        self.set_y(-20)
        self.set_font('calibri', 'I', 9)

        # Código
        self.set_x(-60)
        self.cell(0, 3.5, 'Código: F-PMSSA-01-C', ln=True, align='R')

        # Revisión
        self.set_x(-60)
        self.cell(0, 3.5, 'Revisión: 00', ln=True, align='R')

        # Fecha
        self.set_x(-60)
        self.cell(0, 3, 'Fecha: 7 de octubre de 2024', ln=True, align='R')

        # Número de página
        self.set_x(-30)
        page_text = f'Página {self.page_no()} de {{nb}}'
        self.cell(0, 3, page_text, ln=True, align='R')


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
        
        pdf.set_fill_color(217,226,243)
        anchuras = [40, 50, 60, 40]
        pdf.add_page()
        pdf.alias_nb_pages()
        # Agregar contenido al PDF
        pdf.set_xy(0, 20)  # Ajustar la posición para el título
        pdf.set_font('calibri', '', 22)
        pdf.cell(0, 10, 'SEAFARER APPLICATION FORM', align='C')

        pdf.set_xy(80, 30)  # Ajustar la posición para el siguiente texto
        pdf.set_font('calibri', '', 9)
        pdf.cell(30, 10, 'POSITION APPLYING FOR RANK: ' )
        pdf.set_font('calibri', 'BU', 9)
        pdf.set_xy(123, 30)
        pdf.cell(6,10, 'AB')

        image = database.marine_image_seafarers(uid)
        imagen = descargar_imagen_firebase(image)
        guardar_imagen_para_fpdf(imagen, "imagen_descargada.png")
       # Agregar imagen al PDF con tamaño ajustado
        pdf.set_xy(30, 50)
        pdf.image("imagen_descargada.png", x=20, y=50, w=50, h=50)

        pdf.set_xy(80, 40)
        pdf.set_font('calibri', '', 9)
        pdf.cell(55, 10, '1. PERSONAL INFORMATION')


        pdf.set_font('calibri', '', 9) 
        pdf.set_xy(80, 50)

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

        
        pdf.cell(w=40, h=height, txt='NAME', border=1, align='L',fill=True)  # Etiqueta de "NAME"
        
        pdf.cell(w=40, h=height, txt=primer_nombre, border=1, align='C')  # Primer nombre
        pdf.cell(w=40, h=height, txt=segundo_nombre, border=1, align='C', ln=1)  # Segundo nombre (si existe)
        pdf.set_font('calibri', '', 9)

        # Dibujar la celda de "SURNAMES" con primer y segundo apellido
        pdf.set_xy(80, 57)  # Ajustar la posición para los apellidos

        
        pdf.cell(w=40, h=height, txt='SURNAMES', border=1, align='L', fill=True)  # Etiqueta de "SURNAMES"
        
        pdf.cell(w=40, h=height, txt=primer_apellido, border=1, align='C')  # Primer apellido
        pdf.cell(w=40, h=height, txt=segundo_apellido, border=1, align='C', ln=1)  # Segundo apellido (si existe)
        pdf.set_font('calibri', '', 9)
            


        pdf.set_xy(80, 64) 
         
        pdf.multi_cell(w=40, h=6.5, txt='DATE OF BIRTH\n(YYYY-MM-DD)', border=1, align='L', fill=True)

        date = database.marine_dateOfBirthSeafarers(uid,) or ""
        
        pdf.set_xy(120, 64) 
        pdf.cell(w=80, h=13, txt=date, border=1, align='C', ln=1)

        # Nacionalidad
        nationality = database.marine_nationality(uid,)
        pdf.set_xy(80, 77)  
        
        pdf.cell(w=40, h=height, txt='NATIONALITY', border=1, align='L', fill=True)
        
        pdf.cell(w=80, h=height, txt=nationality, border=1, align='C', ln=1)

        # Sexo y Estado Civil

        gender = database.marine_gender(uid)

        pdf.set_xy(80, 84)  
        
        pdf.cell(w=40, h=7, txt='SEX', border=1, align='L', fill=True)
        
        pdf.cell(w=20, h=7, txt=gender, border=1, align='C')


        marital = database.marine_marital(uid,)
        
        pdf.cell(w=30, h=7, txt='CIVIL STATUS', border=1, align='L', fill=True)
        
        pdf.cell(w=30, h=7, txt=marital, border=1, align='C', ln=1)

        # Espaciado y otras celdas
        pdf.set_xy(80, 91)

        
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
        x_inicial = pdf.get_x()
        y_inicial = pdf.get_y()

        # Columna 1: "COMPLETE HOME ADDRESS" con fondo
        pdf.set_xy(x_inicial, y_inicial)
        pdf.multi_cell(w=40, h=7, txt="COMPLETE HOME ADDRESS", border=1, align="L", fill=True)
        height_complete_home = pdf.get_y() - y_inicial  # Altura usada por esta celda

        # Columna 2: Dirección del hogar
        home = database.marine_home_address(uid) or ""
        pdf.set_xy(x_inicial + 40, y_inicial)
        pdf.multi_cell(w=50, h=7, txt=home, border=1, align="C")
        height_barrio = pdf.get_y() - y_inicial  # Altura usada por esta celda

        # Columna 3: "NEARLY AIRPORT" con fondo
        pdf.set_xy(x_inicial + 90, y_inicial)
        pdf.multi_cell(w=50, h=7, txt="NEARLY AIRPORT", border=1, align="L", fill=True)
        height_airport = pdf.get_y() - y_inicial  # Altura usada por esta celda

        # Columna 4: Datos del aeropuerto
        airport = database.marine_airport(uid) or ""
        pdf.set_xy(x_inicial + 140, y_inicial)
        pdf.multi_cell(w=50, h=7, txt=airport, border=1, align="C")
        height_empty = pdf.get_y() - y_inicial  # Altura usada por esta celda

        # Determinar la altura máxima entre las celdas
        max_height = max(height_complete_home, height_barrio, height_airport, height_empty)

        # Ajustar altura de la Columna 1 si es necesario
        pdf.set_xy(x_inicial, y_inicial)
        pdf.multi_cell(w=40, h=max_height, txt="COMPLETE HOME ADDRESS", border=1, align="L", fill=True)

        # Ajustar altura de la Columna 3 si es necesario
        pdf.set_xy(x_inicial + 90, y_inicial)
        pdf.multi_cell(w=50, h=max_height, txt="NEARLY AIRPORT", border=1, align="L", fill=True)

        # Mover a la siguiente posición para continuar
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
        
        pdf.cell(w=30, h=7, txt="SPANISH", border=1, align="L")
        spanish = database.marine_lang_span(uid) or ""
        pdf.cell(w=30, h=7, txt=str(spanish) + "%", border=1, align="R")
        pdf.cell(w=30, h=7, txt="ENGLISH", border=1, align="L")
        english = database.marine_lang_engl(uid)
        pdf.cell(w=20, h=7, txt=str(english) + "%", border=1, align="R")
        
        pdf.cell(w=20, h=7, txt="OTHERS", border=1, align="L", fill= True)
        
        pdf.cell(w=30, h=7, txt="%", border=1, align="R", ln=1)

        pdf.ln(5)
        pdf.set_font('calibri','',9)
        marlin = database.marine_marlins(uid) or []

        # Verifica si `marlin` contiene al menos un elemento antes de intentar acceder al índice
        if marlin:
            marlins = marlin[0]  # Accede al primer elemento
        else:
            # Maneja el caso en que `marlin` esté vacío o no se hayan encontrado datos
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
        
        pdf.cell(w=0,h=7,txt="EMERGENCY CONTACT / NEXT OF KIN", border=1, align='C',ln=1,fill=True)
        pdf.cell(w=40,h=7,txt="RELATIONSHIP", border=1, align='C', fill=True)
        pdf.cell(w=50,h=7,txt="COMPLETE NAME", border=1, align='C',fill=True)
        pdf.cell(w=60,h=7,txt="TELEPHONE NUMBER / MOBILE", border=1, align='C', fill=True)
        pdf.cell(w=40, h=7, txt="ADDRESS", border=1, align='C', ln=1, fill=True)
        
        datos = database.marine_contact(uid,)

        #anchuras = [30, 50, 30, 80]  # Ajusta los valores de anchura según sea necesario

# Dibujar la tabla con las celdas alineadas correctamente
        for fila in datos:
            # Usamos .get para cada campo y manejamos cuando el valor sea None o no esté definido.
            nombre_completo = f"{fila.get('firstNames', '')} {fila.get('lastNames', '')}"
            telefono = fila.get('phone', {}).get('value', '')  # Si 'phone' o 'value' no existen, será vacío.
            direccion = fila.get('address', '')  # Si 'address' no existe, será vacío.

            # Calcula la altura de cada celda
            alturas = [
                pdf.get_string_width(fila.get('relationship', '')) / anchuras[0] * 8,
                pdf.get_string_width(nombre_completo) / anchuras[1] * 8,
                pdf.get_string_width(telefono) / anchuras[2] * 8,
                pdf.get_string_width(direccion) / anchuras[3] * 8
            ]
            # La altura máxima de la fila
            max_altura = max(alturas)

            # Primera celda: relationship
            pdf.cell(w=anchuras[0], h=16, txt=fila.get('relationship', ''), border=1, align='C')

            # Segunda celda: nombre_completo
            pdf.cell(w=anchuras[1], h=16, txt=nombre_completo, border=1, align='C')

            # Tercera celda: telefono
            pdf.cell(w=anchuras[2], h=16, txt=telefono, border=1, align='C')

            # Cuarta celda: dirección con multi_cell
            x, y = pdf.get_x(), pdf.get_y()
            pdf.multi_cell(w=anchuras[3], h=8, txt=direccion, border=1, align='C')
            
            # Restaurar la posición x para mantener la alineación y mover hacia la siguiente fila
            pdf.set_xy(x + anchuras[3], y)
            pdf.ln(max_altura)
        # Agregar el título "3.WORK EXPERIENCE ONBOARD"

        pdf.ln(5)

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
            

        # Llenar los datos para cada fila
        if personalDocuments:
            for document in personalDocuments:
                # Guardar posición inicial
                x_inicial = pdf.get_x()
                y_inicial = pdf.get_y()

                # Extraer datos del documento
                document_type = document.get('documentName', {}).get('name', '')
                country = document.get('data', {}).get('country', {}).get('value', '')
                document_number = document.get('data', {}).get('documentNumber', '')
                issued_at = document.get('data', {}).get('placeIssue', '')
                date_of_issue = document.get('data', {}).get('issueDate', '')
                valid_until = document.get('data', {}).get('expirationDate', '')

                # Contenido de cada columna en la fila actual
                columnas = [document_type, country, document_number, issued_at, date_of_issue, valid_until]

                # Calcular la altura máxima de la fila
                alturas = [pdf.get_string_width(valor) / anchuras_columnas[i] * altura_fila for i, valor in enumerate(columnas)]
                max_altura = max(altura_fila, *alturas)

                # Imprimir cada celda en la fila actual
                for i, valor in enumerate(columnas):
                    pdf.cell(w=anchuras_columnas[i], h=max_altura, txt=valor, border=1, align='C')

                # Mover a la siguiente línea
                pdf.ln(max_altura)
        else:
            # Si no hay documentos, imprimir una fila vacía
            pdf.cell(w=sum(anchuras_columnas), h=altura_fila, txt="No documents available", border=1, align='C')
            pdf.ln(altura_fila)


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

        courses = [
        "Basic Safety Maritime Training Course (BST)",
        "Proficiency in Personal Survival Techniques 1.19",
        "Fire Prevention and Firefighting 1.20",
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
        # Agregar las celdas con los cursos

        pdf.set_font("calibri","",9)
        column_widths = [40, 30, 20, 50, 50]
        cell_height = 7 
        
        # Retrieve certificates from the database
        # Retrieve certificates from the database
        certificates = database.marine_certificates(uid)

        for i, course in enumerate(courses):
            # Check if there's a matching certificate for the course
            if i < len(certificates):
                certificate_data = certificates[i].get('data', {})
                
                # Retrieve specific fields from each certificate data
                country = certificate_data.get('country', {}).get('countryName', "")
                number = certificate_data.get('certificateNumber', "")
                issue_date = certificate_data.get('issueDate', "")
                expiry_date = certificate_data.get('expirationDate', "")
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

            # Actualizar la posición x para la siguiente celda
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

        vaccines =  database.marine_vaccines(uid) or {}
        print(vaccines)
        pdf.cell(w=40,h=6,txt="TYPE OF VACCINE", border=1, align='C', fill=True)
        pdf.cell(w=40,h=6,txt="COUNTRY", border=1, align='C', fill=True)
        pdf.cell(w=40,h=6,txt="DOZE", border=1, align='C', fill=True)
        pdf.cell(w=40,h=6,txt='DATE OF ISSUE(MM / DD / YYYY)', align='C', border=1, fill=True)
        pdf.cell(w=30,h=6,txt='VACCINATION MARK', align='C', border=1,ln=1, fill=True)
        pdf.cell(w=40, h=24, txt='COVID BOOK', align='C', border=1, fill=True)
        
        # Manejo seguro para evitar KeyError y rellenar campos vacíos si los datos no existen
        if "covid" in vaccines and "cards" in vaccines["covid"]:
            for card in vaccines["covid"]["cards"]:
                # Usar get() para manejar valores faltantes
                country_name = card.get("CountryIssue", {}).get("CountryName", "")
                doze = card.get("Doze", "")
                issue_date = card.get("IssueDate", "")
                vaccine_name = card.get("VaccineBrand", {}).get("name", "")

                # Escribir valores en el PDF
                
                pdf.cell(w=40, h=6, txt=country_name, align='C', border=1)
                
                pdf.cell(w=40, h=6, txt=doze, align='C', border=1, fill=True)
                
                pdf.cell(w=40, h=6, txt=issue_date, align='C', border=1)
                pdf.cell(w=30, h=6, txt=vaccine_name, align='C', border=1, ln=1)
                pdf.cell(w=40, h=6, txt='')  # Celda vacía si es necesario
            pdf.ln()
        else:
            # Si no hay datos de 'covid', rellenar con celdas vacías
            pdf.cell(w=40, h=6, txt='No Data', align='C', border=1)
            pdf.cell(w=40, h=6, txt='N/A', align='C', border=1)
            pdf.cell(w=40, h=6, txt='N/A', align='C', border=1)
            pdf.cell(w=30, h=6, txt='N/A', align='C', border=1, ln=1)
            pdf.cell(w=40, h=6, txt='')  # Celda vacía adicional si es necesario
            pdf.ln()
        # Manejo seguro para fiebre amarilla
       # Verificar si hay datos de 'yellowFever' y 'cards'
        
        if "yellowFever" in vaccines and "cards" in vaccines["yellowFever"]:
            for card in vaccines["yellowFever"]["cards"]:
                # Extraer información de 'CountryIssue' y 'IssueDate'
                country_name = card.get("CountryIssue", {}).get("CountryName", "N/A")
                issue_date = card.get("IssueDate", "N/A")
                
                # Agregar celdas con datos de fiebre amarilla
                pdf.cell(w=40, h=6, txt='YELLOW FEVER', align='C', border=1, fill=True)
                
                pdf.cell(w=40, h=6, txt=country_name, align='C', border=1)
                
                pdf.cell(w=40, h=6, txt='UNLIMITED', align='C', border=1, fill=True)
                
                pdf.cell(w=40, h=6, txt=issue_date, align='C', border=1)
                
                pdf.cell(w=30, h=6, txt='OTHER', align='C', border=1, ln=1,)
                
        else:
            # Si no hay datos, rellenar con celdas vacías
            pdf.cell(w=40, h=6, txt='YELLOW FEVER', align='C', border=1, fill=True)
            pdf.cell(w=40, h=6, txt='No Data', align='C', border=1)
            pdf.cell(w=40, h=6, txt='UNLIMITED', align='C', border=1)
            pdf.cell(w=40, h=6, txt='N/A', align='C', border=1)
            pdf.cell(w=30, h=6, txt='OTHER', align='C', border=1, ln=1)
        pdf.ln(5)
        
        skills = Skills()
        skills.ab_os(pdf, database,uid)
        #skills.messman(pdf)
        pdf.ln(10)
   


