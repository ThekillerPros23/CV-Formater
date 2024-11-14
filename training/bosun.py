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
        course = BosunCourses()
        courses = course.courses()
        # Agregar las celdas con los cursos

        pdf.set_font("calibri","",9)
        column_widths = [40, 40, 50, 30, 30]
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
        column_widths =  [40, 40, 50, 30, 30]
        
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
            # Obtener las líneas y alturas de las celdas de `course_name` y `number`
            # Obtener las líneas y alturas de las celdas de `course_name` y `number`
# Obtener las# Definir una altura mínima para `number`
            # Definir una altura mínima para `number`
           # Definir una altura mínima para `number`
            min_height_number = 2 * cell_height  # Ajuste mínimo en función del tamaño del texto

            # Generar las líneas para `course_name` y `number`
            lines_course_name = pdf.multi_cell(column_widths[0], cell_height, course_name, border=0, align='L', split_only=True)
            lines_number = pdf.multi_cell(column_widths[2], cell_height, number, border=0, align='C', split_only=True)

            # Calcular la altura de cada celda
            height_course_name = len(lines_course_name) * cell_height if course_name else cell_height
            # Ajustar `height_number` para que sea idéntico a `height_course_name`
            height_number = height_course_name  # `number` recibe la misma altura que `course_name`

            # Determinar la altura ajustada final
            adjusted_height = max(height_course_name, height_number, cell_height)

            # Verificar si es necesario un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Posición inicial de `x` e `y` para esta fila
            x_start = pdf.get_x()
            y_start = pdf.get_y()

            # Dibujar cada celda con la altura ajustada
            # Celda de Course Name
            pdf.set_xy(x_start, y_start)
            if course_name:
                pdf.multi_cell(column_widths[0], cell_height, course_name, border=1, align='L', fill=True)
            else:
                pdf.cell(column_widths[0], adjusted_height, '', border=1, align='L', fill=True)

            # Celda de Country
            pdf.set_xy(x_start + column_widths[0], y_start)
            if country:
                pdf.cell(column_widths[1], adjusted_height, country, border=1, align='C')
            else:
                pdf.cell(column_widths[1], adjusted_height, '', border=1, align='C')

            # Celda de Number (ahora con la misma altura que `course_name`)
            pdf.set_xy(x_start + column_widths[0] + column_widths[1], y_start)
            if number:
                pdf.multi_cell(column_widths[2], adjusted_height, number, border=1, align='C')
            else:
                pdf.cell(column_widths[2], adjusted_height, '', border=1, align='C')

            # Celda de Issue Date
            pdf.set_xy(x_start + column_widths[0] + column_widths[1] + column_widths[2], y_start)
            if issue_date:
                pdf.cell(column_widths[3], adjusted_height, issue_date, border=1, align='C')
            else:
                pdf.cell(column_widths[3], adjusted_height, '', border=1, align='C')

            # Celda de Expiry Date
            pdf.set_xy(x_start + column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], y_start)
            if expiry_date:
                pdf.cell(column_widths[4], adjusted_height, expiry_date, border=1, align='C', ln=1)
            else:
                pdf.cell(column_widths[4], adjusted_height, '', border=1, align='C', ln=1)

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
              # Obtener las líneas y alturas de las celdas de `course_name` y `number`
                # Obtener las líneas y alturas de las celdas de `course_name` y `number`
               # Obtener las líneas y alturas de las celdas de `course_name` y `number`
                # Definir una altura mínima para `number`
                   # Definir una altura mínima para `number`
# Definir una altura mínima para `number`
                min_height_number = 2 * cell_height  # Ajuste mínimo en función del tamaño del texto

                # Generar las líneas para `course_name` y `number`
                lines_course_name = pdf.multi_cell(column_widths[0], cell_height, course_name, border=0, align='L', split_only=True)
                lines_number = pdf.multi_cell(column_widths[2], cell_height, number, border=0, align='C', split_only=True)

                # Calcular la altura de cada celda
                height_course_name = len(lines_course_name) * cell_height if course_name else cell_height
                # Ajustar `height_number` para que sea idéntico a `height_course_name`
                height_number = height_course_name  # `number` recibe la misma altura que `course_name`

                # Determinar la altura ajustada final
                adjusted_height = max(height_course_name, height_number, cell_height)

                # Verificar si es necesario un salto de página
                if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                    pdf.add_page()

                # Posición inicial de `x` e `y` para esta fila
                x_start = pdf.get_x()
                y_start = pdf.get_y()

                # Dibujar cada celda con la altura ajustada
                # Celda de Course Name
                pdf.set_xy(x_start, y_start)
                if course_name:
                    pdf.multi_cell(column_widths[0], cell_height, course_name, border=1, align='L', fill=True)
                else:
                    pdf.cell(column_widths[0], adjusted_height, '', border=1, align='L', fill=True)

                # Celda de Country
                pdf.set_xy(x_start + column_widths[0], y_start)
                if country:
                    pdf.cell(column_widths[1], adjusted_height, country, border=1, align='C')
                else:
                    pdf.cell(column_widths[1], adjusted_height, '', border=1, align='C')

                # Celda de Number (ahora con la misma altura que `course_name`)
                pdf.set_xy(x_start + column_widths[0] + column_widths[1], y_start)
                if number:
                    pdf.multi_cell(column_widths[2], adjusted_height, number, border=1, align='C')
                else:
                    pdf.cell(column_widths[2], adjusted_height, '', border=1, align='C')

                # Celda de Issue Date
                pdf.set_xy(x_start + column_widths[0] + column_widths[1] + column_widths[2], y_start)
                if issue_date:
                    pdf.cell(column_widths[3], adjusted_height, issue_date, border=1, align='C')
                else:
                    pdf.cell(column_widths[3], adjusted_height, '', border=1, align='C')

                # Celda de Expiry Date
                pdf.set_xy(x_start + column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], y_start)
                if expiry_date:
                    pdf.cell(column_widths[4], adjusted_height, expiry_date, border=1, align='C', ln=1)
                else:
                    pdf.cell(column_widths[4], adjusted_height, '', border=1, align='C', ln=1)
