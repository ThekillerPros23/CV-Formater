from datetime import datetime
def draw_text_in_cell(pdf, x, y, width, height, text, font_size=10):
    """
    Función para escribir texto ajustado dentro de una celda.
    """
    pdf.set_xy(x, y)
    pdf.set_font("Arial", size=font_size)
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
        
def sanitize_text(text):
    """Reemplaza caracteres no soportados por equivalentes en latin1."""
    if not text:
        return ""
    try:
        return text.encode("latin1").decode("latin1")  # Verifica si es compatible con latin1
    except UnicodeEncodeError:
        # Reemplazar caracteres no compatibles con '?' o eliminarlos
        return text.encode("latin1", errors="replace").decode("latin1")

class Education():
    def educations(self,pdf,database,uid):
        pdf.cell(0,10, txt='7. HIGHEST LEVEL OF EDUCATION / OTHER TRAINING OR CERTIFICATE', align='L')
        pdf.ln(5)
        
        pdf.cell(w=0, h=7,txt='HIGHEST LEVEL OF EDUCATION / OTHER TRAINING OR CERTIFICATE', align='C', border=1, ln=1, fill=True)
        anchuras_columnas  = [60,40,30,30,30]
        titulos_columnas = [
                'NAME OF EDUCATION INSTITUTION / TECHNICAL INSTITUTE / UNIVERSITY',
                'OBTAINED TITLE OR GRADE',
                'COUNTRY OF ISSUE',
                'DATE ON\n(MM/DD/YYYY)',
                'DATE OFF\n(MM/DD/YYYY)',
            ]
        align_type = ['C', 'C', 'C', 'L', 'C', 'L', 'C', 'C']
          # Altura personalizada para cada celda de título
        margen_inferior = 10  # Margen inferior para evitar que el contenido se corte

        pdf.set_font('calibri', '', 9)
        
        height_first_columns = 12
        height_large_columns = 24
        height_other_columns = 12
        height_second_column  = 24
        for i, titulo in enumerate(titulos_columnas):
            # Determinar la altura para cada columna
            if i  == 0:
                cell_height = height_first_columns 
            elif i ==1:
                cell_height = height_second_column # Altura para las primeras dos columnas
            elif i == 2 :
                cell_height = height_large_columns
             # Altura para las columnas 3 y 5
            else:
                cell_height = height_other_columns  # Altura para las columnas restantes (4 y 6)

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

            # Mover el cursor hacia la siguiente posición en la fila
            pdf.set_xy(x_start + anchuras_columnas[i], y_start)  

        # Mover el cursor hacia abajo después de dibujar todos los títulos
        pdf.ln(max(height_first_columns, height_large_columns, height_other_columns))

        education = database.marine_otherskills(uid)
        print(education)
     
        anchuras  = [60,40,30,30,30]
        # Añadir los datos
# Populate the table with data from the Firestore `education` document
        for record in education:
            institution = sanitize_text(record.get('educationInstitution', ''))
            title = sanitize_text(record.get('certificateName', ''))
            country_data = record.get('certificateCountry', '').get('value',"")
            if isinstance(country_data, str):
                country = sanitize_text(country_data)
            else:
                country = ""

            # Convertir fechas al formato MM-DD-YYYY
            start_date = record.get('startDate', '')
            end_date = record.get('endDate', '')

            try:
                if start_date:
                    start_date = datetime.strptime(start_date, "%Y-%m-%d").strftime("%m-%d-%Y")
            except ValueError:
                pass  # Si la fecha tiene un formato inesperado, se deja tal cual

            try:
                if end_date:
                    end_date = datetime.strptime(end_date, "%Y-%m-%d").strftime("%m-%d-%Y")
            except ValueError:
                pass

            # Imprimir celdas con el formato de fecha actualizado
           # Generar las líneas para cada celda
            lines_institution = pdf.multi_cell(anchuras[0], cell_height, institution, border=0, align='L', split_only=True)
            lines_title = pdf.multi_cell(anchuras[1], cell_height, title, border=0, align='L', split_only=True)
            lines_country = pdf.multi_cell(anchuras[2], cell_height, country, border=0, align='L', split_only=True)
            lines_start_date = pdf.multi_cell(anchuras[3], cell_height, start_date, border=0, align='L', split_only=True)
            lines_end_date = pdf.multi_cell(anchuras[4], cell_height, end_date, border=0, align='L', split_only=True)

            # Calcular la altura de cada celda
            height_institution = len(lines_institution) * cell_height if institution else cell_height
            height_title = len(lines_title) * cell_height if title else cell_height
            height_country = len(lines_country) * cell_height if country else cell_height
            height_start_date = len(lines_start_date) * cell_height if start_date else cell_height
            height_end_date = len(lines_end_date) * cell_height if end_date else cell_height

            # Ajustar las alturas para que todas sean iguales a la mayor
            adjusted_height = max(height_institution, height_title, height_country, height_start_date, height_end_date)

            # Verificar si es necesario un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Posición inicial de `x` e `y` para esta fila
            x_start = pdf.get_x()
            y_start = pdf.get_y()

            # Dibujar cada celda con la altura ajustada
            pdf.set_xy(x_start, y_start)
            pdf.cell(anchuras[0], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start, y_start, anchuras[0], adjusted_height, institution)

            pdf.set_xy(x_start + anchuras[0], y_start)
            pdf.cell(anchuras[1], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0], y_start, anchuras[1], adjusted_height, title)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1], y_start)
            pdf.cell(anchuras[2], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1], y_start, anchuras[2], adjusted_height, country)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2], y_start)
            pdf.cell(anchuras[3], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2], y_start, anchuras[3], adjusted_height, start_date)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_start)
            pdf.cell(anchuras[4], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_start, anchuras[4], adjusted_height, end_date)

            pdf.ln()