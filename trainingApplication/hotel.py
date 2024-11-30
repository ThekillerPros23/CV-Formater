from fpdf import FPDF
from courses.hotel_staff import *
from datetime import datetime

def draw_text_in_cell(pdf, x, y, width, height, text, font_size=9):
    """
    Función para escribir texto ajustado dentro de una celda.
    """
    pdf.set_xy(x, y)
    pdf.set_font("calibri", size=font_size)
    line_height = pdf.font_size + 1
    max_lines = int(height // line_height)

    # Dividir el texto en palabras
    words = text.split()
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
        


class Training():
    def hotel_staff(self,pdf,database,uid,version):
        if pdf.get_y() + 80 > pdf.page_break_trigger:  # Verificar si hay espacio suficiente para el título
            pdf.add_page()
        pdf.set_font('calibri', '',9)

        pdf.cell(0, 10, txt='5. TRAINING AND CERTIFICATION.', align='L')
        pdf.ln(10)
        
        pdf.cell(w=0, h=7, txt='STCW CERTIFICATES', align='C', border=1, ln=1, fill=True)

        # Definir los títulos de las columnas
        titulos_columnas = [
            "DESCRIPTION OF CERT / COURSE",
            "COUNTRY OF ISSUE",
            "NUMBER",
            "DATE OF ISSUE \n(MM/DD/YYYY)",
            "DATE OF EXPIRY \n(MM/DD/YYYY)"
        ]
        # Definir las anchuras de las columnas
        anchuras_columnas =  [40, 40, 50, 30, 30]

        # Definir la altura de la fila
          # Si tienes diferentes alturas, podrías cambiar esto a una lista

        # Alineación por columna (en este caso se alinean al centro, puedes modificar si es necesario)
        align_type = ['C', 'C', 'C', 'C', 'C']

        # Coordenadas iniciales para comenzar a escribir
        x_inicial = pdf.get_x()
        y_inicial = pdf.get_y()
        
          # Altura personalizada para cada celda de título
        margen_inferior = 10  # Margen inferior para evitar que el contenido se corte
  # Margen inferior para evitar que el contenido se corte
        height_first_columns = 8
        height_second_column = 15
        height_other_columns = 15
        height_last_columns = 7.5
        pdf.set_font('calibri', 'B', 9)  # Fuente para los títulos

        # Paso 1: Dibujar los títulos de las columnas
        for i, titulo in enumerate(titulos_columnas):
            # Determinar la altura para el título dependiendo de la columna
            if i == 0 :
                cell_height = height_first_columns 
            elif i == 2:
                cell_height = height_other_columns  # Primera y tercera columna con altura 12
            elif i == 1:
                cell_height = height_second_column  # Segunda columna con altura 15
            else:
                cell_height = height_last_columns  # Últimas columnas con altura 6

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
            pdf.set_xy(x_start + anchuras_columnas[i], y_start)  # Mover el cursor hacia abajo después de los títulos
            
        # Salto de línea para avanzar al contenido siguiente
        pdf.ln(max(height_first_columns, height_other_columns, height_second_column))


        # Mover a la siguiente línea después de completar la fila de encabezados
        course = HotelStaffCourses()
        courses = course.courses()
        # Agregar las celdas con los cursos

        pdf.set_font("calibri","",9)
        column_widths = [40, 40, 50, 30, 30]
        cell_height = 7 
        
        # Retrieve certificates from the database
        # Retrieve certificates from the database
        certificates = database.marine_certificates(uid,version)
  
        print(certificates)
        certificates_dict = {
        int(cert['documentName']['id']): cert['data']
        for cert in certificates if 'data' in cert and 'documentName' in cert
    }

    # Configuración de las fuentes y ajustes en el PDF
        pdf.set_font("calibri", "", 9)
        anchuras =  [40, 40, 50, 30, 30]
        
        cell_height = 7
        
        
        
        for course_id, course_name in courses.items():
    # Buscar si existe un certificado para el ID del curso
            certificate_data = certificates_dict.get(course_id, None)

            # Asignar valores del certificado o dejarlos en blanco si no hay coincidencia
            if certificate_data:
                country = certificate_data.get('country', {}).get('value', "")
                number = certificate_data.get('certificateNumber', "")
                issue_date = certificate_data.get('issueDate', "")
                expiry_date = certificate_data.get('expirationDate', "")
            else:
                country, number, issue_date, expiry_date = "", "", "", ""
            country = "" if country == "N/A" else country
            number = "" if number == "N/A" else number
            issue_date = "" if issue_date == "N/A" else issue_date
            expiry_date = "" if expiry_date == "N/A" else expiry_date

            # Formatear las fechas si existen
            if issue_date:
                issue_date = datetime.strptime(issue_date, '%Y-%m-%d').strftime('%m/%d/%Y')
            if expiry_date:
                expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').strftime('%m/%d/%Y')

            # Ajuste de altura de la celda basado en el texto del curso
      # Ajuste de altura de la celda basado en el texto del número del certificado
            # Paso 1: Calcular el número de líneas para cada celda y determinar la altura máxima de la fila
            # Obtener las líneas y alturas de las celdas de `course_name` y `number`
            # Obtener las líneas y alturas de las celdas de `course_name` y `number`
# Obtener las# Definir una altura mínima para `number`
            # Definir una altura mínima para `number`
           # Definir una altura mínima para `number`
            lines_course_name = pdf.multi_cell(anchuras[0], cell_height, course_name, border=0, align='L', split_only=True)
            lines_country = pdf.multi_cell(anchuras[1], cell_height, country, border=0, align='L', split_only=True)
            lines_number = pdf.multi_cell(anchuras[2], cell_height, number, border=0, align='L', split_only=True)
            lines_issue_date = pdf.multi_cell(anchuras[3], cell_height, issue_date, border=0, align='L', split_only=True)
            lines_expiry_date = pdf.multi_cell(anchuras[4], cell_height, expiry_date, border=0, align='L', split_only=True)

            # Calcular la altura de cada celda
            height_course_name = len(lines_course_name) * cell_height if course_name else cell_height
            height_country = len(lines_country) * cell_height if country else cell_height
            height_number = len(lines_number) * cell_height if number else cell_height
            height_issue_date = len(lines_issue_date) * cell_height if issue_date else cell_height
            height_expiry_date = len(lines_expiry_date) * cell_height if expiry_date else cell_height

            # Ajustar las alturas para que todas sean iguales a la mayor
            adjusted_height = max(height_course_name, height_country, height_number, height_issue_date, height_expiry_date)

            # Verificar si es necesario un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Posición inicial de `x` e `y` para esta fila
            x_start = pdf.get_x()
            y_start = pdf.get_y()

            # Dibujar la columna de cursos con color
            # Color azul claro
            pdf.set_xy(x_start, y_start)
            pdf.cell(anchuras[0], adjusted_height, border=1, fill=True)
            draw_text_in_cell(pdf, x_start, y_start, anchuras[0], adjusted_height, course_name)

            # Dibujar las demás columnas sin color
        # Color blanco (sin relleno)
            pdf.set_xy(x_start + anchuras[0], y_start)
            pdf.cell(anchuras[1], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0], y_start, anchuras[1], adjusted_height, country)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1], y_start)
            pdf.cell(anchuras[2], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1], y_start, anchuras[2], adjusted_height, number)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2], y_start)
            pdf.cell(anchuras[3], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2], y_start, anchuras[3], adjusted_height, issue_date)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_start)
            pdf.cell(anchuras[4], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_start, anchuras[4], adjusted_height, expiry_date)

            pdf.ln()

        for course_id, certificate_data in certificates_dict.items():
            # Si el curso no está en la lista de cursos de referencia, agregarlo
            if course_id not in courses:
                course_name = certificate_data.get('documentName', {}).get('name', "Curso Desconocido")
                country = certificate_data.get('country', {}).get('value', "")
                number = certificate_data.get('certificateNumber', "")
                issue_date = certificate_data.get('issueDate', "")
                expiry_date = certificate_data.get('expirationDate', "")
                country = "" if country == "N/A" else country
                number = "" if number == "N/A" else number
                issue_date = "" if issue_date == "N/A" else issue_date
                expiry_date = "" if expiry_date == "N/A" else expiry_date

                # Formatear las fechas si existen
                if issue_date:
                    issue_date = datetime.strptime(issue_date, '%Y-%m-%d').strftime('%m/%d/%Y')
                if expiry_date:
                    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').strftime('%m/%d/%Y')

                # Ajuste de altura de la celda basado en el texto del curso
    # Ajuste de altura de la celda basado en el texto del número del certificado
            # Paso 1: Calcular el número de líneas para cada celda y determinar la altura máxima de la fila
              # Obtener las líneas y alturas de las celdas de `course_name` y `number`
                # Obtener las líneas y alturas de las celdas de `course_name` y `number`
               # Obtener las líneas y alturas de las celdas de `course_name` y `number`
                # Definir una altura mínima para `number`
                   # Definir una altura mínima para `number`
# Definir una altura mínima para `number`
                lines_course_name = pdf.multi_cell(anchuras[0], cell_height, course_name, border=0, align='L', split_only=True)
                lines_country = pdf.multi_cell(anchuras[1], cell_height, country, border=0, align='L', split_only=True)
                lines_number = pdf.multi_cell(anchuras[2], cell_height, number, border=0, align='L', split_only=True)
                lines_issue_date = pdf.multi_cell(anchuras[3], cell_height, issue_date, border=0, align='L', split_only=True)
                lines_expiry_date = pdf.multi_cell(anchuras[4], cell_height, expiry_date, border=0, align='L', split_only=True)

                # Calcular la altura de cada celda
                height_course_name = len(lines_course_name) * cell_height if course_name else cell_height
                height_country = len(lines_country) * cell_height if country else cell_height
                height_number = len(lines_number) * cell_height if number else cell_height
                height_issue_date = len(lines_issue_date) * cell_height if issue_date else cell_height
                height_expiry_date = len(lines_expiry_date) * cell_height if expiry_date else cell_height

                # Ajustar las alturas para que todas sean iguales a la mayor
                adjusted_height = max(height_course_name, height_country, height_number, height_issue_date, height_expiry_date)

                # Verificar si es necesario un salto de página
                if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                    pdf.add_page()

                # Posición inicial de `x` e `y` para esta fila
                x_start = pdf.get_x()
                y_start = pdf.get_y()

                # Dibujar la columna de cursos con color
                # Color azul claro
                pdf.set_xy(x_start, y_start)
                pdf.cell(anchuras[0], adjusted_height, border=1, fill=True)
                draw_text_in_cell(pdf, x_start, y_start, anchuras[0], adjusted_height, course_name)

                # Dibujar las demás columnas sin color
            # Color blanco (sin relleno)
                pdf.set_xy(x_start + anchuras[0], y_start)
                pdf.cell(anchuras[1], adjusted_height, border=1)
                draw_text_in_cell(pdf, x_start + anchuras[0], y_start, anchuras[1], adjusted_height, country)

                pdf.set_xy(x_start + anchuras[0] + anchuras[1], y_start)
                pdf.cell(anchuras[2], adjusted_height, border=1)
                draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1], y_start, anchuras[2], adjusted_height, number)

                pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2], y_start)
                pdf.cell(anchuras[3], adjusted_height, border=1)
                draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2], y_start, anchuras[3], adjusted_height, issue_date)

                pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_start)
                pdf.cell(anchuras[4], adjusted_height, border=1)
                draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_start, anchuras[4], adjusted_height, expiry_date)

                pdf.ln()