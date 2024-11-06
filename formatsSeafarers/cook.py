from fpdf import FPDF
from skills import *
from fpdf import FPDF
from skills import *
import requests
from io import BytesIO
from PIL import Image

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



class CookSeafarers():
    def format_cook(self, pdf, database, uid):
        
        pdf.set_fill_color(59,70,86)
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
        pdf.cell(6,10, 'COOK')

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

        pdf.set_text_color(255,255,255)
        pdf.cell(w=40, h=height, txt='NAME', border=1, align='L',fill=True)  # Etiqueta de "NAME"
        pdf.set_text_color(0,0,0)
        pdf.cell(w=40, h=height, txt=primer_nombre, border=1, align='C')  # Primer nombre
        pdf.cell(w=40, h=height, txt=segundo_nombre, border=1, align='C', ln=1)  # Segundo nombre (si existe)
        pdf.set_font('calibri', '', 9)

        # Dibujar la celda de "SURNAMES" con primer y segundo apellido
        pdf.set_xy(80, 57)  # Ajustar la posición para los apellidos

        pdf.set_text_color(255,255,255)
        pdf.cell(w=40, h=height, txt='SURNAMES', border=1, align='L', fill=True)  # Etiqueta de "SURNAMES"
        pdf.set_text_color(0,0,0)
        pdf.cell(w=40, h=height, txt=primer_apellido, border=1, align='C')  # Primer apellido
        pdf.cell(w=40, h=height, txt=segundo_apellido, border=1, align='C', ln=1)  # Segundo apellido (si existe)
        pdf.set_font('calibri', '', 9)
            


        pdf.set_xy(80, 64) 
        pdf.set_text_color(255,255,255) 
        pdf.multi_cell(w=40, h=6.5, txt='DATE OF BIRTH\n(YYYY-MM-DD)', border=1, align='L', fill=True)

        date = database.marine_dateOfBirthSeafarers(uid,)
        pdf.set_text_color(0,0,0)
        pdf.set_xy(120, 64) 
        pdf.cell(w=80, h=13, txt=date, border=1, align='C', ln=1)

        # Nacionalidad
        nationality = database.marine_nationality(uid,)
        pdf.set_xy(80, 77)  
        pdf.set_text_color(255,255,255)
        pdf.cell(w=40, h=height, txt='NATIONALITY', border=1, align='L', fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80, h=height, txt=nationality, border=1, align='C', ln=1)

        # Sexo y Estado Civil

        gender = database.marine_gender(uid)

        pdf.set_xy(80, 84)  
        pdf.set_text_color(255,255,255)
        pdf.cell(w=40, h=7, txt='SEX', border=1, align='L', fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=20, h=7, txt=gender, border=1, align='C')


        marital = database.marine_marital(uid,)
        pdf.set_text_color(255,255,255)
        pdf.cell(w=30, h=7, txt='CIVIL STATUS', border=1, align='L', fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=30, h=7, txt=marital, border=1, align='C', ln=1)

        # Espaciado y otras celdas
        pdf.set_xy(80, 91)

        pdf.set_text_color(255,255,255)
        pdf.cell(w=25, h=7, txt='HEIGHT (Ft/in)', border=1, align='L', fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=20, h=7, txt='', border=1, align='C')
        pdf.set_text_color(255,255,255)
        pdf.cell(w=22, h=7, txt='WEIGHT (Lb)', border=1, align='L', fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=18, h=7, txt='', border=1, align='C')
        pdf.set_text_color(255,255,255)
        pdf.cell(w=15, h=7, txt='BMI', border=1, align='L', fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=20, h=7, txt='', border=1, align='C', ln=1)

        # Configuración inicial
        pdf.ln(5)
        pdf.set_font('calibri', '', 9)

        # Guardar posición inicial
        x_inicial = pdf.get_x()
        y_inicial = pdf.get_y()

        # Primera celda "COMPLETE HOME ADDRESS" con multi_cell
        pdf.set_xy(x_inicial, y_inicial)
        pdf.set_text_color(255,255,255)
        pdf.multi_cell(w=40, h=7, txt="COMPLETE HOME ADDRESS", border=1, align="L", fill=True)
        height_complete_home = pdf.get_y() - y_inicial  # Altura ocupada por esta celda
        pdf.set_text_color(0,0,0)
        # Segunda celda "BARRIADA EL ALBA..."
        pdf.set_xy(x_inicial + 40, y_inicial)
        pdf.multi_cell(w=50, h=7, txt="", border=1, align="C")
        height_barrio = pdf.get_y() - y_inicial  # Altura ocupada por esta celda


        pdf.set_xy(x_inicial + 90, y_inicial)
        pdf.set_text_color(255,255,255)
        pdf.multi_cell(w=50, h=7, txt="NEARLY AIRPORT", border=1, align="L", fill=True)
        height_airport = pdf.get_y() - y_inicial  # Altura ocupada por esta celda

        airport = database.marine_airport(uid,)
        pdf.set_xy(x_inicial + 140, y_inicial)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=50, h=7, txt=airport, border=1, align="C")
        height_empty = pdf.get_y() - y_inicial  # Altura ocupada por esta celda (debería ser 7)

        # Obtener la altura máxima de la fila
        max_height = max(height_complete_home, height_barrio, height_airport, height_empty)

        # Rellenar celdas para que todas ocupen la misma altura
        # Si alguna celda es más pequeña, agregamos un espacio en blanco para que se ajuste a la altura máxima

        # Si la primera celda "COMPLETE HOME ADDRESS" es más pequeña, la rellenamos
        if height_complete_home < max_height:
            pdf.set_xy(x_inicial, y_inicial + height_complete_home)
            pdf.cell(w=40, h=max_height - height_complete_home, txt="", border=1)

        # Si la segunda celda es más pequeña, la rellenamos
        if height_barrio < max_height:
            pdf.set_xy(x_inicial + 40, y_inicial + height_barrio)
            pdf.cell(w=50, h=max_height - height_barrio, txt="", border=1)

        # Si la tercera celda es más pequeña, la rellenamos
        if height_airport < max_height:
            pdf.set_xy(x_inicial + 90, y_inicial + height_airport)
            pdf.cell(w=50, h=max_height - height_airport, txt="", border=1)

        # Si la cuarta celda es más pequeña, la rellenamos
        if height_empty < max_height:
            pdf.set_xy(x_inicial + 140, y_inicial + height_empty)
            pdf.cell(w=50, h=max_height - height_empty, txt="", border=1)

        # Mover a la siguiente línea después de ajustar todas las celdas
        pdf.set_xy(x_inicial, y_inicial + max_height)

        # Segunda fila con "PHONE/CELL" y demás datos
        email = database.marine_email(uid,)
        pdf.set_text_color(255,255,255)
        pdf.cell(w=30, h=7, txt="PHONE/CELL", border=1, align="C", fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=30, h=7, txt="", border=1, align="L")
        pdf.set_text_color(255,255,255)
        pdf.cell(w=30, h=7, txt="WHATSAPP", border=1, align="C", fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=30, h=7, txt="", border=1, align="C")
        pdf.set_text_color(255,255,255)
        pdf.cell(w=20, h=7, txt="E-MAIL", border=1, align="L", fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=50, h=7, txt=email, border=1, align="C", ln=1)

        # Tercera fila con "LANGUAGES"
        pdf.set_text_color(255,255,255)
        pdf.cell(w=30, h=7, txt="LANGUAGES", border=1, align="C",fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=30, h=7, txt="SPANISH", border=1, align="L")
        pdf.cell(w=30, h=7, txt="%", border=1, align="R")
        pdf.cell(w=30, h=7, txt="ENGLISH", border=1, align="L")
        pdf.cell(w=20, h=7, txt="%", border=1, align="R")
        pdf.set_text_color(255,255,255)
        pdf.cell(w=20, h=7, txt="OTHERS", border=1, align="L", fill= True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=30, h=7, txt="%", border=1, align="R", ln=1)

        pdf.ln(5)
        pdf.set_font('calibri','',9)
        pdf.set_text_color(255,255,255)
        pdf.cell(w=0, h=7, txt="MARLINS / LANGUAGE -TEST", border=1, align="C",ln=1 ,fill=True)

        pdf.cell(w=60, h=7, txt="TOTAL %", border=1, align="C", fill=True)
        pdf.cell(w=60, h=7, txt="ISSUE DATE", border=1, align="C", fill=True)
        pdf.cell(w=70, h=7, txt="PLACE OF ISSUE", border=1, align="C",ln=1, fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=60, h=7, txt="", border=1, align="R")
        pdf.cell(w=60, h=7, txt="", border=1, align="C")
        pdf.cell(w=70, h=7, txt="", border=1, align="C",ln=1)
        pdf.set_text_color(255,255,255)
        pdf.cell(w=30, h=7, txt='LISTENING', border=1, align='L', fill=True)
        pdf.cell(w=40, h=7, txt='GRAMMAR', border=1, align='L', fill=True)
        pdf.cell(w=40, h=7, txt='VOCABULARY', border=1, align='L', fill=True)
        pdf.cell(w=40, h=7, txt='TIME AND NUMBERS', border=1, align='C', fill=True)
        pdf.cell(w=40, h=7, txt='READING', border=1, align='L', ln=1, fill=True)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=30, h=7, txt='%', border=1, align='R')
        pdf.cell(w=40, h=7, txt='%', border=1, align='R')
        pdf.cell(w=40, h=7, txt='%', border=1, align='R')
        pdf.cell(w=40, h=7, txt='%', border=1, align='R')
        pdf.cell(w=40, h=7, txt='%', border=1, align='R')    


        pdf.ln(10)
        pdf.set_font('calibri','',9)
        pdf.cell(0,10,txt="2. EMERGENCY CONTACT / NEXT OF KIN0", border=0, align='L')
        pdf.ln(10)
        pdf.set_text_color(255,255,255)
        pdf.cell(w=0,h=7,txt="EMERGENCY CONTACT / NEXT OF KIN", border=1, align='C',ln=1,fill=True)
        pdf.cell(w=40,h=7,txt="RELATIONSHIP", border=1, align='C', fill=True)
        pdf.cell(w=50,h=7,txt="COMPLETE NAME", border=1, align='C',fill=True)
        pdf.cell(w=60,h=7,txt="TELEPHONE NUMBER / MOBILE", border=1, align='C', fill=True)
        pdf.cell(w=40, h=7, txt="ADDRESS", border=1, align='C', ln=1, fill=True)
        pdf.set_text_color(0,0,0)
        datos = database.marine_contact(uid,)

        # Dibujar la tabla con las celdas alineadas correctamente
        for fila in datos:
            nombre_completo = f"{fila['firstNames']} {fila['lastNames']}"
            telefono = fila['phone'].get('value', '') if fila['phone']['value'] else ''
            columnas = [fila['relationship'], nombre_completo, telefono, fila['address']]

            for i, valor in enumerate(columnas):
                pdf.cell(w=anchuras[i], h=8, txt=valor, border=1, align='C')
            
            pdf.ln(8)  # Saltar a la siguiente línea después de cada fil

        # Agregar el título "3.WORK EXPERIENCE ONBOARD"

        pdf.ln(5)

        pdf.cell(0, 10, txt='3.WORK EXPERIENCE ONBOARD', align="L",)
        pdf.ln(10)

        pdf.set_text_color(255,255,255)
        anchuras_columnas = [30, 30, 24, 17, 18, 18, 23, 30]  
        altura_fila = [7,7,7,7,14,14,14,14]

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
        pdf.set_text_color(0,0,0)
        onboard = database.marine_onboard(uid,)  # Obtener los datos de la base de datos
        nuevaaltura_fila = 7  # Altura uniforme para todas las filas

        for fila in onboard:
            # Obtener el nombre del tipo de buque o cadena vacía si no está disponible
            tipo_vessel = fila['typeOfVessel'][0]['name'] if fila['typeOfVessel'] else ''
            
            # Crear la lista de datos de cada columna en el orden correcto
            columnas = [
                fila['dateOn'],         # Fecha de inicio
                fila['dateOff'],        # Fecha de finalización
                fila['companyName'],    # Nombre de la compañía
                fila['vesselName'],     # Nombre del buque
                fila['imo#'],           # Número IMO
                fila['gt/hp'] if fila['gt/hp'] else '',  # GT/HP (vacío si no está disponible)
                tipo_vessel,            # Tipo de buque
                fila['rank/position']   # Rango/posición
            ]

            x_inicial = pdf.get_x()  # Posición X inicial antes de imprimir la fila
            max_height = nuevaaltura_fila  # Altura predeterminada para la fila

            # Dibujar cada celda de la fila
            for i in range(len(columnas)):
                # Imprimir una celda para cada valor en la columna
                pdf.cell(w=anchuras_columnas[i], h=max_height, txt=columnas[i], align='C', border=1)
                
                # Actualizar la posición X para la siguiente celda
                x_inicial += anchuras_columnas[i]
                pdf.set_x(x_inicial)

        # Saltar a la siguiente línea después de imprimir la fila completa
        pdf.ln(max_height)

        # Salto de línea adicional después de cada grupo de filas
        pdf.ln(5)
        pdf.cell(0, 10, txt='4. Personal Documentation / Seafarer Documentation', align='L')
        pdf.ln(10)  

        pdf.set_text_color(255,255,255)    
        pdf.cell(w=0, h=7, txt='PERSONAL DOCUMENTATION / SEAFARER DOCUMENTATION', align='C', border=1, ln=1,fill=True)
        pdf.set_font('Calibri', '', 9)

        # Definir los títulos de las columnas
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

        # Definir la altura de la fila
        altura_fila = [14,14,14,14,7,7]  # O podría ser una lista si varía por fila

        # Alineación por columna (en este caso se alinean al centro, puedes modificar si es necesario)
        align_type = ['C', 'C', 'C', 'C', 'C', 'C']

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

            # Dividir el texto del encabezado si es necesario (sin imprimir aún)
            lines = pdf.multi_cell(anchuras_columnas[i], altura_actual / 2, titulos_columnas[i], border=0, align='C', split_only=True, fill=True)
            num_lines = len(lines)

            # Ajustar la altura de la celda según el número de líneas
            adjusted_height = max(altura_actual, altura_actual / 2 * num_lines)

            # Verificar si se necesita un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()
                pdf.set_xy(x_inicial, y_inicial)

            # Imprimir la celda del encabezado con el ajuste de altura
            pdf.multi_cell(anchuras_columnas[i], altura_actual / 2, titulos_columnas[i], border=1, align='C', fill=True)

            # Actualizar la posición x para la siguiente celda
            x_inicial += anchuras_columnas[i]
            # Mover a la siguiente línea después de completar la fila de encabezados

        pdf.set_text_color(0,0,0)
        personalDocuments = database.marine_personaldocumention(uid)
        # Llenar los datos para cada fila
        # Asegúrate de que la altura de la fila sea un valor numérico
        altura_fila = 7  # O cualquier valor adecuado

        # Si necesitas manejar diferentes alturas para diferentes celdas
        # Define una lista de alturas y usa el valor adecuado para cada celda
        altura_fila_por_celda = [7, 7, 7, 7, 7, 7]  # Si es necesario, define diferentes alturas aquí

        # Verificar si personalDocuments es None o una lista vacía
        if personalDocuments:
            for document in personalDocuments:
                pdf.set_font('Calibri', '', 9)  # Restablecer el tamaño de la fuente para las filas de datos

                # Guardar la posición inicial para restablecer el cursor en cada celda
                x_inicial = pdf.get_x()
                y_inicial = pdf.get_y()

                # Obtener los datos del documento (Si no existen, dejar las celdas vacías)
                document_type = document['documentName']['name'] if 'documentName' in document else ''
                country = document['data']['country']['value'] if 'country' in document['data'] else ''
                document_number = document['data']['documentNumber'] if 'documentNumber' in document['data'] else ''
                issued_at = document['data']['placeIssue'] if 'placeIssue' in document['data'] else ''
                date_of_issue = document['data']['issueDate'] if 'issueDate' in document['data'] else ''
                valid_until = document['data']['expirationDate'] if 'expirationDate' in document['data'] else ''

                # Imprimir la celda del "document_type"
                pdf.multi_cell(w=40, h=altura_fila, txt=document_type, align='C', border=1)

                # Mover el cursor a la siguiente celda en la misma línea
                pdf.set_xy(x_inicial + 40, y_inicial)

                # Imprimir la celda del "country"
                pdf.multi_cell(w=30, h=altura_fila, txt=country, align='C', border=1)

                # Actualizar la posición x e y para la siguiente celda
                pdf.set_xy(x_inicial + 40 + 30, y_inicial)

                # Imprimir la celda del "document_number"
                pdf.multi_cell(w=30, h=altura_fila, txt=document_number, align='C', border=1)

                # Actualizar la posición para la siguiente celda
                pdf.set_xy(x_inicial + 40 + 30 + 30, y_inicial)

                # Imprimir la celda del "issued_at"
                pdf.multi_cell(w=30, h=altura_fila, txt=issued_at, align='C', border=1)

                # Actualizar la posición para la siguiente celda
                pdf.set_xy(x_inicial + 40 + 30 + 30 + 30, y_inicial)

                # Imprimir la celda del "date_of_issue"
                pdf.multi_cell(w=30, h=altura_fila, txt=date_of_issue, align='C', border=1)

                # Actualizar la posición para la siguiente celda
                pdf.set_xy(x_inicial + 40 + 30 + 30 + 30 + 30, y_inicial)

                # Imprimir la celda del "valid_until"
                pdf.multi_cell(w=30, h=altura_fila, txt=valid_until, align='C', border=1)
        else:
            # Si no hay documentos, imprimir una fila vacía
            pdf.set_font('Calibri', '', 9)

            # Guardar la posición inicial
            x_inicial = pdf.get_x()
            y_inicial = pdf.get_y()

            # Imprimir celdas vacías
            pdf.multi_cell(w=40, h=altura_fila, txt='', align='C', border=1)
            pdf.set_xy(x_inicial + 40, y_inicial)

            pdf.multi_cell(w=30, h=altura_fila, txt='', align='C', border=1)
            pdf.set_xy(x_inicial + 40 + 30, y_inicial)

            pdf.multi_cell(w=30, h=altura_fila, txt='', align='C', border=1)
            pdf.set_xy(x_inicial + 40 + 30 + 30, y_inicial)

            pdf.multi_cell(w=30, h=altura_fila, txt='', align='C', border=1)
            pdf.set_xy(x_inicial + 40 + 30 + 30 + 30, y_inicial)

            pdf.multi_cell(w=30, h=altura_fila, txt='', align='C', border=1)
            pdf.set_xy(x_inicial + 40 + 30 + 30 + 30 + 30, y_inicial)

            pdf.multi_cell(w=30, h=altura_fila, txt='', align='C', border=1)

        pdf.ln(20)
        pdf.set_font('calibri', '',9)

        pdf.cell(0, 10, txt='5. TRAINING AND CERTIFICATION.', align='L')
        pdf.ln(10)
        pdf.set_text_color(255,255,255)
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
        #print(database.marine_certificates(uid))
        for course in courses:
            pdf.set_text_color(255,255,255)
        # Dividir el texto del curso en múltiples líneas
            lines = pdf.multi_cell(column_widths[0], cell_height, course, border=0, align='L', split_only=True,fill=True)
            num_lines = len(lines)

            # Ajustar la altura de la celda de acuerdo al número de líneas
            adjusted_height = max(cell_height * num_lines, cell_height)

            # Verificar si se necesita un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Imprimir la celda del curso
            pdf.multi_cell(column_widths[0], cell_height, course, border=1, align='L', fill=True)

            # Rellenar las otras columnas con los datos estáticos, ajustando la altura
            pdf.set_text_color(0,0,0)
            pdf.set_xy(pdf.get_x() + column_widths[0], pdf.get_y() - adjusted_height)
            pdf.cell(w=column_widths[1], h=adjusted_height, txt="", border=1, align='C', ln=0)
            pdf.cell(w=column_widths[2], h=adjusted_height, txt="", border=1, align='C', ln=0)
            pdf.cell(w=column_widths[3], h=adjusted_height, txt="", border=1, align='C', ln=0)
            pdf.cell(w=column_widths[4], h=adjusted_height, txt="", border=1, align='C', ln=1)

        pdf.set_font('calibri', '', 9)
        pdf.cell(0,10, txt='6. WORK EXPERIENCE ONSHORE', align='L')
        pdf.ln(10)
        pdf.set_text_color(255,255,255)
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
        altura_fila = [14, 14, 7, 14, 14, 14,14]
        onland = database.marine_onland(uid,)
        pdf.set_text_color(0,0,0)
        for data in onland:
            # Reinicia las coordenadas x e y iniciales para cada nueva fila
            x_inicial = pdf.get_x()
            y_inicial = pdf.get_y()
            
            # Imprimir cada dato de la fila
            pdf.set_xy(x_inicial, y_inicial)
            pdf.multi_cell(ancho_celdas[0], altura_fila[0], txt=data.get('dateOn', ''), border=1, align='C')
            
            x_inicial += ancho_celdas[0]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.multi_cell(ancho_celdas[1], altura_fila[1], txt=data.get('dateOff', ''), border=1, align='C')

            x_inicial += ancho_celdas[1]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.multi_cell(ancho_celdas[2], altura_fila[2], txt=data.get('companyName', ''), border=1, align='C')

            x_inicial += ancho_celdas[2]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.multi_cell(ancho_celdas[3], altura_fila[3], txt=data.get('dutiesOrResponsibilities', ''), border=1, align='C')

            x_inicial += ancho_celdas[3]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.multi_cell(ancho_celdas[4], altura_fila[4], txt=data.get('rank/position', ''), border=1, align='C')

            x_inicial += ancho_celdas[4]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.multi_cell(ancho_celdas[5], altura_fila[5], txt=data.get('reasonForLeaving', ''), border=1, align='C')

            x_inicial += ancho_celdas[5]
            pdf.set_xy(x_inicial, y_inicial)
            pdf.multi_cell(ancho_celdas[6], altura_fila[6], txt=data.get('nameOfContactPersonAndTelephoneNumber', ''), border=1, align='C')
            
            pdf.ln(adjusted_height)  # Moverse 

        pdf.cell(0,10, txt='7. HIGHEST LEVEL OF EDUCATION / OTHER TRAINING OR CERTIFICATE', align='L')
        pdf.ln(10)
        pdf.set_text_color(255,255,255)
        pdf.cell(w=0, h=7,txt='HIGHEST LEVEL OF EDUCATION / OTHER TRAINING OR CERTIFICATE', align='C', border=1, ln=1, fill=True)
        pdf.cell(w=90,h=7,txt='NAME OF EDUCATION INSTITUTION/TECHNICAL INSTITUTE/UNIVERSITY', align='C', border=1, fill=True)
        pdf.cell(w=40,h=7,txt='OBTAINED TITLE OR GRADE', align='C', border=1, fill=True)
        pdf.cell(w=30,h=7,txt='COUNTRY OF ISSUE', align='C', border=1, fill=True)
        pdf.cell(w=30,h=7,txt='DATE ON(MM/DD/YYYY)', align='C', border=1, fill=True)
        pdf.cell(w=30,h=7,txt='DATE OFF(MM/DD/YYYY)', align='C', border=1, fill=True)
        pdf.set_text_color(0,0,0)
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
        pdf.set_text_color(255,255,255)
        pdf.cell(w=0, h=6,txt='VACCINATION BOOK', align='C', border=1,ln=1,fill=True)

        pdf.set_font('calibri','',9)

        vaccines =  database.marine_vaccines(uid) or {}

        pdf.cell(w=40,h=6,txt="TYPE OF VACCINE", border=1, align='C', fill=True)
        pdf.cell(w=40,h=6,txt="COUNTRY", border=1, align='C', fill=True)
        pdf.cell(w=40,h=6,txt="DOZE", border=1, align='C', fill=True)
        pdf.cell(w=40,h=6,txt='DATE OF ISSUE(MM / DD / YYYY)', align='C', border=1, fill=True)
        pdf.cell(w=30,h=6,txt='VACCINATION MARK', align='C', border=1,ln=1, fill=True)
        pdf.cell(w=40, h=24, txt='COVID BOOK', align='C', border=1, fill=True)
        pdf.set_text_color(0,0,0)
        # Manejo seguro para evitar KeyError y rellenar campos vacíos si los datos no existen
        if "covid" in vaccines and "cards" in vaccines["covid"]:
            for card in vaccines["covid"]["cards"]:
                # Usar get() para manejar valores faltantes
                country_name = card.get("CountryIssue", {}).get("CountryName", "N/A")
                doze = card.get("Doze", "N/A")
                issue_date = card.get("IssueDate", "N/A")
                vaccine_name = card.get("VaccineBrand", {}).get("name", "N/A")

                # Escribir valores en el PDF
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=40, h=6, txt=country_name, align='C', border=1)
                pdf.set_text_color(255, 255, 255)
                pdf.cell(w=40, h=6, txt=doze, align='C', border=1, fill=True)
                pdf.set_text_color(0, 0, 0)
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
        if "yellowFever" in data and "cards" in data["yellowFever"]:
            for card in data["yellowFever"]["cards"]:
                country_name = card.get("CountryIssue", {}).get("CountryName", "N/A")
                issue_date = card.get("IssueDate", "N/A")

                pdf.cell(w=40, h=6, txt='YELLOW FEVER', align='C', border=1)
                pdf.cell(w=40, h=6, txt=country_name, align='C', border=1)
                pdf.cell(w=40, h=6, txt='UNLIMITED', align='C', border=1,fill=True)
                pdf.cell(w=40, h=6, txt=issue_date, align='C', border=1)
                pdf.cell(w=30, h=6, txt='OTHER', align='C', border=1, ln=1)
        else:
            # Si no hay datos de 'yellowFever', rellenar con celdas vacías
            pdf.cell(w=40, h=6, txt='YELLOW FEVER', align='C', border=1, fill=True)
            pdf.cell(w=40, h=6, txt='No Data', align='C', border=1)
            pdf.cell(w=40, h=6, txt='UNLIMITED', align='C', border=1)
            pdf.cell(w=40, h=6, txt='N/A', align='C', border=1)
            pdf.cell(w=30, h=6, txt='OTHER', align='C', border=1, ln=1)

        pdf.ln(5)
        skills = Skills()
        skills.messman(pdf)
        #skills.messman(pdf)
        pdf.ln(10)
      