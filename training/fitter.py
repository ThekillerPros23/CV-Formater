from fpdf import FPDF
from courses.fitter import *
from datetime import datetime



class Training():
    def fitter(self,pdf,database,uid):
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
        course = FitterCourses()
        courses = course.courses()
        # Agregar las celdas con los cursos

        pdf.set_font("calibri","",9)
        column_widths = [40, 30, 20, 50, 50]
        cell_height = 7 
        
        # Retrieve certificates from the database
        # Retrieve certificates from the database
        certificates = database.marine_certificates(uid)
  
        print(certificates)
        certificates_dict = {
        int(cert['documentName']['id']): cert['data']
        for cert in certificates if 'data' in cert and 'documentName' in cert
    }

    # Configuración de las fuentes y ajustes en el PDF
        pdf.set_font("calibri", "", 9)
        column_widths = [40, 30, 20, 50, 50]
        
        cell_height = 7
        
        
        
        for course_id, course_name in courses.items():
    # Buscar si existe un certificado para el ID del curso
            certificate_data = certificates_dict.get(course_id, None)

            # Asignar valores del certificado o dejarlos en blanco si no hay coincidencia
            if certificate_data:
                country = certificate_data.get('country', {}).get('countryName', "")
                number = certificate_data.get('certificateNumber', "")
                issue_date = certificate_data.get('issueDate', "")
                expiry_date = certificate_data.get('expirationDate', "")
            else:
                country, number, issue_date, expiry_date = "", "", "", ""

            # Formatear las fechas si existen
            if issue_date:
                issue_date = datetime.strptime(issue_date, '%Y-%m-%d').strftime('%m/%d/%Y')
            if expiry_date:
                expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').strftime('%m/%d/%Y')

            # Ajuste de altura de la celda basado en el texto del curso
      # Ajuste de altura de la celda basado en el texto del número del certificado
            # Paso 1: Calcular el número de líneas para cada celda y determinar la altura máxima de la fila
            lines_course_name = pdf.multi_cell(column_widths[0], cell_height, course_name, border=0, align='L', split_only=True)
            lines_number = pdf.multi_cell(column_widths[2], cell_height, number, border=0, align='C', split_only=True)

            # Calcular la altura en función del número de líneas en `course_name` y `number`
            height_course_name = len(lines_course_name) * cell_height
            height_number = len(lines_number) * cell_height

            # Determinar la altura ajustada en función de las celdas que lo necesiten
            if height_number < height_course_name:
                adjusted_height = height_course_name  # Ajustar `number` a la altura de `course_name`
            else:
                adjusted_height = height_number  # Si `number` es mayor, usamos su altura

            # Comparar con otras celdas fijas (country, issue_date, expiry_date) que solo tienen una línea
            min_cell_height = cell_height
            if adjusted_height < min_cell_height:
                adjusted_height = min_cell_height  # Asegura un mínimo de una línea de altura

            # Verificar si es necesario un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Posición inicial de `x` e `y` para esta fila
            x_start = pdf.get_x()
            y_start = pdf.get_y()

            # Dibujar cada celda con la altura ajustada
            # Celda de Course Name
            pdf.set_xy(x_start, y_start)
            pdf.multi_cell(column_widths[0], cell_height, course_name, border=1, align='L', fill=True)

            # Celda de Country (ajustada)
            pdf.set_xy(x_start + column_widths[0], y_start)
            pdf.cell(w=column_widths[1], h=adjusted_height, txt=country, border=1, align='C')

            # Celda de Number (ajustada a la altura de `course_name` si es necesario)
            pdf.set_xy(x_start + column_widths[0] + column_widths[1], y_start)
            pdf.multi_cell(w=column_widths[2], h=adjusted_height, txt=number, border=1, align='C', )

            # Celda de Issue Date (ajustada)
            pdf.set_xy(x_start + column_widths[0] + column_widths[1] + column_widths[2], y_start)
            pdf.cell(w=column_widths[3], h=adjusted_height, txt=issue_date, border=1, align='C')

            # Celda de Expiry Date (ajustada)
            pdf.set_xy(x_start + column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], y_start)
            pdf.cell(w=column_widths[4], h=adjusted_height, txt=expiry_date, border=1, align='C', ln=1)
            
        for course_id, certificate_data in certificates_dict.items():
            # Si el curso no está en la lista de cursos de referencia, agregarlo
            if course_id not in courses:
                course_name = certificate_data.get('documentName', {}).get('name', "Curso Desconocido")
                country = certificate_data.get('country', {}).get('countryName', "")
                number = certificate_data.get('certificateNumber', "")
                issue_date = certificate_data.get('issueDate', "")
                expiry_date = certificate_data.get('expirationDate', "")

                # Formatear las fechas si existen
                if issue_date:
                    issue_date = datetime.strptime(issue_date, '%Y-%m-%d').strftime('%m/%d/%Y')
                if expiry_date:
                    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').strftime('%m/%d/%Y')

                # Ajuste de altura de la celda basado en el texto del curso
    # Ajuste de altura de la celda basado en el texto del número del certificado
            # Paso 1: Calcular el número de líneas para cada celda y determinar la altura máxima de la fila
                lines_course_name = pdf.multi_cell(column_widths[0], cell_height, course_name, border=0, align='L', split_only=True)
                lines_number = pdf.multi_cell(column_widths[2], cell_height, number, border=0, align='C', split_only=True)

                # Calcular la altura en función del número de líneas en `course_name` y `number`
                height_course_name = len(lines_course_name) * cell_height
                height_number = len(lines_number) * cell_height

                # Determinar la altura ajustada en función de las celdas que lo necesiten
                if height_number < height_course_name:
                    adjusted_height = height_course_name  # Ajustar `number` a la altura de `course_name`
                else:
                    adjusted_height = height_number  # Si `number` es mayor, usamos su altura

                # Comparar con otras celdas fijas (country, issue_date, expiry_date) que solo tienen una línea
                min_cell_height = cell_height
                if adjusted_height < min_cell_height:
                    adjusted_height = min_cell_height  # Asegura un mínimo de una línea de altura

                # Verificar si es necesario un salto de página
                if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                    pdf.add_page()

                # Posición inicial de `x` e `y` para esta fila
                x_start = pdf.get_x()
                y_start = pdf.get_y()

                # Dibujar cada celda con la altura ajustada
                # Celda de Course Name
                pdf.set_xy(x_start, y_start)
                pdf.multi_cell(column_widths[0], cell_height, course_name, border=1, align='L', fill=True)

                # Celda de Country (ajustada)
                pdf.set_xy(x_start + column_widths[0], y_start)
                pdf.cell(w=column_widths[1], h=adjusted_height, txt=country, border=1, align='C')

                # Celda de Number (ajustada a la altura de `course_name` si es necesario)
                pdf.set_xy(x_start + column_widths[0] + column_widths[1], y_start)
                pdf.multi_cell(w=column_widths[2], h=adjusted_height, txt=number, border=1, align='C', )

                # Celda de Issue Date (ajustada)
                pdf.set_xy(x_start + column_widths[0] + column_widths[1] + column_widths[2], y_start)
                pdf.cell(w=column_widths[3], h=adjusted_height, txt=issue_date, border=1, align='C')

                # Celda de Expiry Date (ajustada)
                pdf.set_xy(x_start + column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], y_start)
                pdf.cell(w=column_widths[4], h=adjusted_height, txt=expiry_date, border=1, align='C', ln=1)