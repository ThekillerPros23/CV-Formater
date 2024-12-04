from fpdf import FPDF
from formatskill.fitter import *
import requests
from io import BytesIO
from PIL import Image
from courses.fitter import *
from datetime import datetime
from onboard.ab import *
from onshore.onshore import *
from training.fitter import *
from number import *
import phonenumbers
from phonenumbers import PhoneNumberFormat, NumberParseException
import re
from education.archivo import *

number = Number()
country_abbreviations = number.number()


formatted_pattern = re.compile(r"^\+\w{2} \(\+\d{1,3}\) \d+")
def draw_text_in_cell(pdf, x, y, width, height, text, font_size=9):
    """
    Función para escribir texto ajustado dentro de una celda, manejando palabras largas y saltos de línea.
    """
    pdf.set_xy(x, y)
    pdf.set_font("calibri", size=font_size)
    line_height = pdf.font_size + 1
    max_lines = int(height // line_height)

    # Dividir el texto en palabras o fragmentos si son demasiado largas
    words = []
    for word in text.split():
        while pdf.get_string_width(word) > width - 2:  # Si la palabra es demasiado larga, dividirla
            words.append(word[:len(word)//2])
            word = word[len(word)//2:]
        words.append(word)

    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word
        if pdf.get_string_width(test_line) <= width - 2:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
        if len(lines) == max_lines:
            break

    if current_line:
        lines.append(current_line)

    # Dibujar las líneas dentro de la celda
    for i, line in enumerate(lines):
        if i < max_lines:
            pdf.text(x + 1, y + 3 + i * line_height, line)
def format_phone_number(number):
    try:
        # Verifica si el número ya está en el formato deseado
        if formatted_pattern.match(number):
            return number  # Devuelve el número tal cual si ya está formateado

        # Asegúrate de que el número tenga el prefijo "+"
        if not number.startswith("+"):
            number = f"+{number}"

        # Parsear el número para detectar país y detalles
        parsed_number = phonenumbers.parse(number, None)
        country_code = parsed_number.country_code
        national_number = phonenumbers.format_number(parsed_number, PhoneNumberFormat.NATIONAL)

        # Obtener la abreviatura del país
        country_abbr = country_abbreviations.get(country_code, "Unknown")

        # Formatear como "+SV (+503) número"
        formatted_number = f"+{country_abbr} (+{country_code}) {national_number}"
        return formatted_number

    except NumberParseException:
        return "Número inválido"



def descargar_imagen_firebase(url):
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception(f"Error al descargar la imagen: {response.status_code}")

# Guardar la imagen localmente
def guardar_imagen_para_fpdf(imagen, nombre_archivo):
    imagen.save(nombre_archivo, format='PNG')  # O 'JPEG' si prefieres JPG


def ajustar_texto_a_altura(texto, ancho_maximo, pdf):
    palabras = texto.split()
    linea_actual = ""
    lineas = []

    for palabra in palabras:
        prueba_linea = f"{linea_actual} {palabra}".strip()
        if pdf.get_string_width(prueba_linea) <= ancho_maximo:
            linea_actual = prueba_linea
        else:
            lineas.append(linea_actual)
            linea_actual = palabra

    if linea_actual:
        lineas.append(linea_actual)

    return lineas


class FitterSeafarers():
    def format_fitter(self, pdf, database, uid):
   
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
        
        
        pdf.set_xy(70, 50)
        position = database.marine_position(uid)
        position_name = position[0].get('name', "") if position else ""

        # Centrar dinámicamente la posición en X para position_name
        text_width = pdf.get_string_width(position_name)
        pdf.set_xy((210 - text_width) / 2, 50)
        pdf.cell(0, 5, position_name)

        image = database.marine_image_seafarers(uid)
        imagen = descargar_imagen_firebase(image)
        guardar_imagen_para_fpdf(imagen, "imagen_descargada.png")
        # Agregar imagen al PDF con tamaño ajustado
        pdf.set_xy(30, 60)
        pdf.image("imagen_descargada.png", x=20, y=70, w=50, h=50)

        pdf.set_xy(20, 58)
        pdf.set_font('calibri', '', 12)
        pdf.cell(55, 10, '1. PERSONAL INFORMATION')

        pdf.set_font('calibri', '', 9)
        pdf.set_xy(80, 66)

        # Definir anchos para alineación
        cell_width = 50
        big_cell_width = 100
        height = 7
        pdf.set_font('calibri', '', 9)

        # Encabezado para Nombres
        fullnames = database.marine_firstname_seafarers(uid)
        fullLastname = database.marine_lastname_seafarers(uid)

        # Dividir el nombre en primer y segundo nombre si existe
        nombres = fullnames.split(' ', 1)
        primer_nombre = nombres[0]
        segundo_nombre = nombres[1] if len(nombres) > 1 else ''

        # Dividir los apellidos en primer y segundo apellido si existe
        apellidos = fullLastname.split(' ', 1)
        primer_apellido = apellidos[0]
        segundo_apellido = apellidos[1] if len(apellidos) > 1 else ''

        # Nombre y apellidos
        pdf.cell(w=40, h=height, txt='NAME', border=1, align='L', fill=True)
        pdf.cell(w=40, h=height, txt=primer_nombre, border=1, align='C')
        pdf.cell(w=40, h=height, txt=segundo_nombre, border=1, align='C', ln=1)

        pdf.set_xy(80, 73)
        pdf.cell(w=40, h=height, txt='SURNAMES', border=1, align='L', fill=True)
        pdf.cell(w=40, h=height, txt=primer_apellido, border=1, align='C')
        pdf.cell(w=40, h=height, txt=segundo_apellido, border=1, align='C', ln=1)

        # Fecha de nacimiento
        pdf.set_xy(80, 80)
        pdf.multi_cell(w=40, h=6.5, txt='DATE OF BIRTH\n(MM-DD-YYY)', border=1, align='L', fill=True)

        date = database.marine_dateOfBirthSeafarers(uid) or ""
        if date:
            try:
                formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%m-%d-%Y")
            except ValueError:
                formatted_date = date
        else:
            formatted_date = ""

        pdf.set_xy(120, 80)
        pdf.cell(w=80, h=13, txt=formatted_date, border=1, align='C', ln=1)

        # Número de identificación
        pdf.set_xy(80, 93)
        pdf.multi_cell(w=40, h=14, txt='IDENTIFICATION NUMBER', border=1, align='L', fill=True)
        identification_data = database.marine_identification(uid) or []

        identification_number = next(
            (doc['data']['documentNumber'] for doc in identification_data
            if doc.get('data', {}).get('documentName', {}).get('name') == "Identification (ID, NID, etc.)"),
            None
        )

        if identification_number is None:
            identification_number = next(
                (doc['data']['documentNumber'] for doc in identification_data
                if doc.get('data', {}).get('documentName', {}).get('name') == "Passport"),
                ""
            )

        pdf.set_xy(120, 93)
        pdf.cell(w=80, h=14, txt=identification_number, border=1, align='C', ln=1)

        # Nacionalidad
        nationality = database.marine_nationality(uid) or ""
        pdf.set_xy(80, 107)
        pdf.cell(w=40, h=height, txt='NATIONALITY', border=1, align='L', fill=True)
        pdf.cell(w=80, h=height, txt=nationality, border=1, align='C', ln=1)

        # Sexo y Estado Civil
        gender = database.marine_gender(uid)
        pdf.set_xy(80, 114)
        pdf.cell(w=40, h=7, txt='SEX', border=1, align='L', fill=True)
        pdf.cell(w=20, h=7, txt=gender, border=1, align='C')
        marital = database.marine_marital(uid)
        pdf.cell(w=30, h=7, txt='CIVIL STATUS', border=1, align='L', fill=True)
        pdf.cell(w=30, h=7, txt=marital, border=1, align='C', ln=1)

        # Altura, peso y BMI
        pdf.set_xy(80, 121)
        height = database.marine_height(uid)
        if height == "0' 0''" or height == "nan":
            height = ""
        pdf.cell(w=25, h=7, txt='HEIGHT (Ft/in)', border=1, align='L', fill=True)
        pdf.cell(w=20, h=7, txt=height, border=1, align='C')

        weight = database.marine_weight(uid)
        if weight == "0" or weight == "nan":
            weight = ""
        pdf.cell(w=22, h=7, txt='WEIGHT (Lb)', border=1, align='L', fill=True)
        pdf.cell(w=18, h=7, txt=weight, border=1, align='C')

        pdf.cell(w=15, h=7, txt='BMI', border=1, align='L', fill=True)
        bmi = database.marine_bmi(uid)
        if str(bmi) == "0" or str(bmi) == "nan":
            bmi = ""
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
        
        pdf.cell(w=18, h=7, txt="PHONE/CELL", border=1, align="C", fill=True)
        cell = database.marine_cellphone(uid)
        formatted_cell = format_phone_number(cell)

        pdf.cell(w=45, h=7, txt=formatted_cell, border=1, align="L")

        pdf.cell(w=18, h=7, txt="WHATSAPP", border=1, align="C", fill=True)
        pdf.cell(w=45, h=7, txt=formatted_cell, border=1, align="L")      
        pdf.cell(w=12, h=7, txt="E-MAIL", border=1, align="L", fill=True)
        
        pdf.cell(w=52, h=7, txt=email, border=1, align="C", ln=1)

        # Tercera fila con "LANGUAGES"
        
        pdf.cell(w=30, h=7, txt="LANGUAGES", border=1, align="C",fill=True)
        
        pdf.cell(w=30, h=7, txt="ENGLISH", border=1, align="L",fill=True)
        english = database.marine_lang_engl(uid)
        pdf.cell(w=20, h=7, txt=str(english) + "%", border=1, align="R")
        
        pdf.cell(w=30, h=7, txt="SPANISH", border=1, align="L", fill=True)
        spanish = database.marine_lang_span(uid) or ""
        pdf.cell(w=30, h=7, txt=str(spanish) + "%", border=1, align="R")

        
        
        others_lang = database.marine_lang_other(uid) or []
        highest_percentage = 0  # Valor inicial para comparar

        # Iterar sobre los datos para encontrar el porcentaje más alto
        for data in others_lang:
            # Obtener el valor del porcentaje, ajustando si es un diccionario
            percentage = data.get("PercentageSpeak", 0)  # Reemplazar con 0 si no está definido
            if isinstance(percentage, dict):  # Si es un diccionario, extraer el valor correcto
                percentage = percentage.get("value", 0)  # Ajusta "value" según el formato de tus datos
            if percentage > highest_percentage:
                highest_percentage = percentage

        # Agregar la información al PDF
        pdf.cell(w=20, h=7, txt="OTHERS", border=1, align="L", fill=True)

        pdf.cell(w=30, h=7, txt=str(highest_percentage) + "%", border=1, align="R", ln=1)

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
        pdf.cell(w=60, h=7, txt=str(marlins.get('PercentageTotal', "")) + "%", border=1, align="R")
        pdf.cell(w=60, h=7, txt=marlins.get('IssueDate', ""), border=1, align="C")
        pdf.cell(w=70, h=7, txt=marlins.get('PlaceIssue', ""), border=1, align="C", ln=1)

        # Encabezados de secciones de habilidades
        pdf.cell(w=30, h=7, txt='LISTENING', border=1, align='L', fill=True)
        pdf.cell(w=40, h=7, txt='GRAMMAR', border=1, align='L', fill=True)
        pdf.cell(w=40, h=7, txt='VOCABULARY', border=1, align='L', fill=True)
        pdf.cell(w=40, h=7, txt='TIME AND NUMBERS', border=1, align='C', fill=True)
        pdf.cell(w=40, h=7, txt='READING', border=1, align='L', ln=1, fill=True)

        # Datos de habilidades individuales
        pdf.cell(w=30, h=7, txt=str(marlins.get('PercentageListening', "")) + '%', border=1, align='R')
        pdf.cell(w=40, h=7, txt=str(marlins.get('PercentageGrammar', "")) + '%', border=1, align='R')
        pdf.cell(w=40, h=7, txt=str(marlins.get('PercentageVocabulary', "")) + '%', border=1, align='R')
        pdf.cell(w=40, h=7, txt=str(marlins.get('PercentageNumbers', "")) + '%', border=1, align='R')
        pdf.cell(w=40, h=7, txt=str(marlins.get('PercentageReading', "")) + '%', border=1, align='R')
        pdf.ln(10)
        pdf.set_font('calibri','',9)
        pdf.cell(0,10,txt="2. EMERGENCY CONTACT / NEXT OF KIN", border=0, align='L')
        pdf.ln(10)
 
        datos = database.marine_contact(uid,)
        # Dibujar cada fila de datos
        cell_height = 7  # Altura base para cada línea de texto

        # Anchos específicos para cada columna
        anchuras = [30, 60, 50, 55]

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
            
        pdf.ln(5)

        onboard = Onboard()
        onboard.ab(pdf,database,uid)

        # Salto de línea adicional después de cada grupo de filas
        pdf.ln(30)
        pdf.cell(0, 10, txt='4. PERSONAL DOCUMENTATION / SEAFARER DOCUMENTATION', align='L',ln=1)


            
        pdf.cell(w=0, h=7, txt='PERSONAL DOCUMENTATION / SEAFARER DOCUMENTATION', align='C', border=1, ln=1,fill=True)
        pdf.set_font('Calibri', '', 9)
       # Títulos de las columnas
        titulos_columnas = [
           "TYPE OF DOCUMENT / ID",
            "COUNTRY OF ISSUE",
            "NO.",
            "ISSUED AT (PLACE)",
            "DATE OF ISSUE \n(MM / DD / YYYY)",
            "VALID UNTIL \n(MM / DD / YYYY)"
        ]

        height_first_columns = 12
        height_other_columns = 12
        height_last_columns = 6  # Altura para las últimas dos columnas

        # Definir las anchuras de las columnas
        anchuras_columnas = [40, 30, 30, 30, 30, 30]
        align_type = ['C', 'C', 'C', 'L', 'C', 'C']

        # Altura de la fila
        altura_fila = 7

        # Paso 1: Dibujar los títulos de las columnas
        for i, titulo in enumerate(titulos_columnas):
            # Determinar la altura para el título dependiendo de la columna
            if i < len(anchuras_columnas) - 2:  # Las primeras columnas excepto las últimas dos
                cell_height = height_first_columns if i < 2 else height_other_columns
            else:  # Últimas dos columnas
                cell_height = height_last_columns

            # Obtener el número de líneas necesarias para el título y ajustar la altura
            lines = pdf.multi_cell(anchuras_columnas[i], cell_height, titulo, border=0, align=align_type[i], split_only=True)
            num_lines = len(lines)
            adjusted_height = max(cell_height * num_lines, cell_height)  # Ajustar altura en base a las líneas necesarias

            # Verificar si es necesario un salto de página antes de dibujar el título
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Establecer la posición inicial de cada título de columna
            x_start = pdf.get_x()
            y_start = pdf.get_y()
            pdf.set_xy(x_start, y_start)

            # Dibujar cada título de columna con su altura ajustada y alineación
            pdf.multi_cell(anchuras_columnas[i], cell_height, titulo, border=1, align=align_type[i], fill=True)
            pdf.set_xy(x_start + anchuras_columnas[i], y_start)  # Mover el cursor hacia abajo después de los títulos, usando la altura máxima entre todas las celdas

        # Agregar un salto de línea para moverse al siguiente contenido
        pdf.ln(max(height_first_columns, height_other_columns, height_last_columns))


        # Obtener los documentos
        personalDocuments = database.marine_personaldocumention(uid)
      
# Lista de documentos solo en la primera columna de la primera fila
       ## Lista de documentos predeterminada
# Lista de documentos predeterminada
# Lista de documentos predeterminada
        documents = [
            "COC III/5",
            "COC III/4",
            "B1/ B2",
            "FLAG CERTIFICATES",
            "FLAG SEAMANBOOK",
            "MCV",
            "PASSPORT",
            "SEAMAN'S BOOK (NATIONAL)",
            "US VISA C1-D"
        ]
        anchuras = [40, 30, 30, 30, 30, 30]
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

                    # Convertir las fechas a formato MM-DD-YYYY
                    date_of_issue = document.get('data', {}).get('issueDate', '')
                    valid_until = document.get('data', {}).get('expirationDate', '')

                    try:
                        if date_of_issue:
                            date_of_issue = datetime.strptime(date_of_issue, "%Y-%m-%d").strftime("%m-%d-%Y")
                    except ValueError:
                        pass  # Si el formato no es correcto, dejamos el valor tal cual

                    try:
                        if valid_until:
                            valid_until = datetime.strptime(valid_until, "%Y-%m-%d").strftime("%m-%d-%Y")
                    except ValueError:
                        pass

                    break  # Detener la búsqueda una vez encontrado el documento correspondiente

            lines_doc_name = pdf.multi_cell(anchuras[0], cell_height, document_name, border=0, align='L', split_only=True)
            lines_country = pdf.multi_cell(anchuras[1], cell_height, country, border=0, align='L', split_only=True)
            lines_number = pdf.multi_cell(anchuras[2], cell_height, document_number, border=0, align='L', split_only=True)
            lines_issued_at = pdf.multi_cell(anchuras[3], cell_height, issued_at, border=0, align='L', split_only=True)
            lines_issue_date = pdf.multi_cell(anchuras[4], cell_height, date_of_issue, border=0, align='L', split_only=True)
            lines_expiry_date = pdf.multi_cell(anchuras[5], cell_height, valid_until, border=0, align='L', split_only=True)

            # Calcular la altura de cada celda
            height_doc_name = len(lines_doc_name) * cell_height if document_name else cell_height
            height_country = len(lines_country) * cell_height if country else cell_height
            height_number = len(lines_number) * cell_height if document_number else cell_height
            height_issued_at = len(lines_issued_at) * cell_height if issued_at else cell_height
            height_issue_date = len(lines_issue_date) * cell_height if date_of_issue else cell_height
            height_expiry_date = len(lines_expiry_date) * cell_height if valid_until else cell_height

            # Ajustar las alturas para que todas sean iguales a la mayor
            adjusted_height = max(height_doc_name, height_country, height_number, height_issued_at, height_issue_date, height_expiry_date)

            # Verificar si es necesario un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Posición inicial de `x` e `y` para esta fila
            x_start = pdf.get_x()
            y_start = pdf.get_y()

            # Dibujar la columna de documentos con color
            # Color azul claro
            pdf.set_xy(x_start, y_start)
            pdf.cell(anchuras[0], adjusted_height, border=1, fill=True)
            draw_text_in_cell(pdf, x_start, y_start, anchuras[0], adjusted_height, document_name)

            # Dibujar las demás columnas sin color
            pdf.set_xy(x_start + anchuras[0], y_start)
            pdf.cell(anchuras[1], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0], y_start, anchuras[1], adjusted_height, country)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1], y_start)
            pdf.cell(anchuras[2], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1], y_start, anchuras[2], adjusted_height, document_number)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2], y_start)
            pdf.cell(anchuras[3], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2], y_start, anchuras[3], adjusted_height, issued_at)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_start)
            pdf.cell(anchuras[4], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_start, anchuras[4], adjusted_height, date_of_issue)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4], y_start)
            pdf.cell(anchuras[5], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4], y_start, anchuras[5], adjusted_height, valid_until)

            pdf.ln()


        training = Training()
        training.fitter(pdf,database,uid)
       
        onland = Onshore()
        onland.ab(pdf,database,uid)
        
        education = Education()
        education.educations(pdf,database,uid)


        pdf.ln(10)

        pdf.cell(0,10, txt='8. VACCINATION BOOK', align='L')
        pdf.ln(10)
        
        pdf.cell(w=0, h=6,txt='VACCINATION BOOK', align='C', border=1,ln=1,fill=True)

        pdf.set_font('calibri','',9)

        # Assuming `vaccines` is populated from the database
        vaccines = database.marine_vaccines(uid) or {}
        print(vaccines)
        # Setting up the PDF structure
        pdf.cell(w=40, h=6, txt="TYPE OF VACCINE", border=1, align='C', fill=True)
        pdf.cell(w=40, h=6, txt="COUNTRY", border=1, align='C', fill=True)
        pdf.cell(w=30, h=6, txt="DOZE", border=1, align='C', fill=True)
        pdf.cell(w=50, h=6, txt='DATE OF ISSUE (MM / DD / YYYY)', align='C', border=1, fill=True)
        pdf.cell(w=30, h=6, txt='VACCINATION MARK', align='C', border=1, ln=1, fill=True)

        for card in vaccines.get('covid', {}).get('cards', []):
            pdf.cell(w=40, h=6, txt="COVID BOOK", border=1, align='C', fill=True)
            country_issue = card.get('CountryIssue', {})
            if isinstance(country_issue, dict):
                value = country_issue.get('value', '')
            else:
                value = str(country_issue)
            pdf.cell(w=40, h=6, txt=value, border=1, align='C')
            pdf.cell(w=30, h=6, txt=card.get('Doze', ''), border=1, align='C', fill=True)

            # Formatear IssueDate con validación
            issue_date = card.get('IssueDate', '')
            try:
                formatted_issue_date = datetime.strptime(issue_date, '%Y-%m-%d').strftime('%m/%d/%Y') if issue_date else ''
            except ValueError:
                formatted_issue_date = ''
            
            pdf.cell(w=50, h=6, txt=formatted_issue_date, border=1, align='C')

            # Verificar que VaccineBrand es un diccionario antes de acceder a 'name'
            vaccine_brand = card.get('VaccineBrand', {})
            brand_name = vaccine_brand.get('name', '') if isinstance(vaccine_brand, dict) else ''
            
            pdf.cell(w=30, h=6, txt=brand_name, align='C', border=1, ln=1)

        # Llenar datos de fiebre amarilla
        yellow_fever_cards = vaccines.get('yellowFever', {}).get('cards', [])
        if not yellow_fever_cards:
            # Si no hay datos, imprime una fila en blanco con el título "YELLOW FEVER"
            pdf.cell(w=40, h=6, txt="YELLOW FEVER", border=1, align='C', fill=True)
            pdf.cell(w=40, h=6, txt="", border=1, align='C')  # País en blanco
            pdf.cell(w=30, h=6, txt="", border=1, align='C', fill=True)  # Dosis en blanco
            pdf.cell(w=50, h=6, txt="", border=1, align='C')  # Fecha en blanco
            pdf.cell(w=30, h=6, txt="", border=1, align='C', ln=1)  # Marca en blanco
        else:
            # Si hay datos, imprime cada tarjeta
            for card in yellow_fever_cards:
                pdf.cell(w=40, h=6, txt="YELLOW FEVER", border=1, align='C', fill=True)
                country_issue = card.get('CountryIssue', {})
                if isinstance(country_issue, dict):
                    value = country_issue.get('value', '')
                else:
                    value = str(country_issue)
                pdf.cell(w=40, h=6, txt=value, border=1, align='C')
                pdf.cell(w=30, h=6, txt=card.get('Doze', ''), border=1, align='C', fill=True)
                
                # Formatear IssueDate con validación
                issue_date = card.get('IssueDate', '')
                try:
                    formatted_issue_date = datetime.strptime(issue_date, '%Y-%m-%d').strftime('%m/%d/%Y') if issue_date else ''
                except ValueError:
                    formatted_issue_date = ''
                
                pdf.cell(w=50, h=6, txt=formatted_issue_date, border=1, align='C')

                # Verificar que VaccineBrand es un diccionario antes de acceder a 'name'
                vaccine_brand = card.get('VaccineBrand', {})
                brand_name = vaccine_brand.get('name', '') if isinstance(vaccine_brand, dict) else ''
                
                pdf.cell(w=30, h=6, txt=brand_name, align='C', border=1, ln=1)




        pdf.ln(10)
        skills = Skills()
        skills.fitter(pdf, database,uid)
        #skills.messman(pdf)
        pdf.ln(10)
   
