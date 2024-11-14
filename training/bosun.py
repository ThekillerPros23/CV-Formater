from fpdf import FPDF


from courses.bosun import *
from datetime import datetime



class Training():
    def bosun(self,pdf,database,uid):
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
        course = BosunCourses()
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
            lines_country = [country]  # Celda de país no usa `multi_cell`, así que es solo una línea
            lines_number = pdf.multi_cell(column_widths[2], cell_height, number, border=0, align='C', split_only=True)
            lines_issue_date = [issue_date]  # Fecha de emisión es solo una línea
            lines_expiry_date = [expiry_date]  # Fecha de expiración es solo una línea

            # Determinar la altura máxima de la fila en función del contenido más alto
            num_lines = max(len(lines_course_name), len(lines_country), len(lines_number), len(lines_issue_date), len(lines_expiry_date))
            adjusted_height = max(cell_height * num_lines, cell_height)

            # Verificar si es necesario un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Posición inicial de `x` e `y` para esta fila
            x_start = pdf.get_x()
            y_start = pdf.get_y()

            # Paso 2: Dibujar cada celda con la altura máxima de la fila
            # Celda de Course Name
            pdf.set_xy(x_start, y_start)
            pdf.multi_cell(column_widths[0], cell_height, course_name, border=1, align='L', fill=True)
            
            # Celda de Country (compartiendo `adjusted_height`)
            pdf.set_xy(x_start + column_widths[0], y_start)
            pdf.cell(w=column_widths[1], h=adjusted_height, txt=country, border=1, align='C')

            # Celda de Number (compartiendo `adjusted_height`)
            pdf.set_xy(x_start + column_widths[0] + column_widths[1], y_start)
            pdf.multi_cell(column_widths[2], cell_height, number, border=1, align='C', fill=True)
            
            # Celda de Issue Date (compartiendo `adjusted_height`)
            pdf.set_xy(x_start + column_widths[0] + column_widths[1] + column_widths[2], y_start)
            pdf.cell(w=column_widths[3], h=adjusted_height, txt=issue_date, border=1, align='C')

            # Celda de Expiry Date (compartiendo `adjusted_height`)
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
                lines_country = [country]  # Celda de país no usa `multi_cell`, así que es solo una línea
                lines_number = pdf.multi_cell(column_widths[2], cell_height, number, border=0, align='C', split_only=True)
                lines_issue_date = [issue_date]  # Fecha de emisión es solo una línea
                lines_expiry_date = [expiry_date]  # Fecha de expiración es solo una línea

                # Determinar la altura máxima de la fila en función del contenido más alto
                num_lines = max(len(lines_course_name), len(lines_country), len(lines_number), len(lines_issue_date), len(lines_expiry_date))
                adjusted_height = max(cell_height * num_lines, cell_height)

                # Verificar si es necesario un salto de página
                if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                    pdf.add_page()

                # Posición inicial de `x` e `y` para esta fila
                x_start = pdf.get_x()
                y_start = pdf.get_y()

                # Paso 2: Dibujar cada celda con la altura máxima de la fila
                # Celda de Course Name
                pdf.set_xy(x_start, y_start)
                pdf.multi_cell(column_widths[0], cell_height, course_name, border=1, align='L', fill=True)
                
                # Celda de Country (compartiendo `adjusted_height`)
                pdf.set_xy(x_start + column_widths[0], y_start)
                pdf.cell(w=column_widths[1], h=adjusted_height, txt=country, border=1, align='C')

                # Celda de Number (compartiendo `adjusted_height`)
                pdf.set_xy(x_start + column_widths[0] + column_widths[1], y_start)
                pdf.multi_cell(column_widths[2], cell_height, number, border=1, align='C', fill=True)
                
                # Celda de Issue Date (compartiendo `adjusted_height`)
                pdf.set_xy(x_start + column_widths[0] + column_widths[1] + column_widths[2], y_start)
                pdf.cell(w=column_widths[3], h=adjusted_height, txt=issue_date, border=1, align='C')

                # Celda de Expiry Date (compartiendo `adjusted_height`)
                pdf.set_xy(x_start + column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], y_start)
                pdf.cell(w=column_widths[4], h=adjusted_height, txt=expiry_date, border=1, align='C', ln=1)