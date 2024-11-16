from datetime import datetime

# Función para ajustar el texto a la altura especificada dentro de una celda
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
        
class Onshore:
    def ab(self, pdf, database, uid):
        if pdf.get_y() +150  > pdf.page_break_trigger:  # Verificar si hay espacio suficiente para el título
            pdf.add_page()
        pdf.cell(0, 10, txt='6. WORK EXPERIENCE ONSHORE', align="L")
        pdf.ln(10)
        anchuras_columnas =     [22, 22, 27, 35, 27, 25, 40]
        titulos_columnas = [
            'DATE ON\n(MM/DD/YYYY)',
            'DATE OFF\n(MM/DD/YYYY)',
            'COMPANY NAME',
            'DUTIES OR RESPONSIBILITIES',
            'RANK /POSITION',
            'REASON FOR LEAVING',
            'NAME OF CONTACT PERSON & TELEPHONE NUMBER',
           
        ]
        align_type = ['C', 'C', 'C', 'L', 'C', 'L', 'C', 'C']
          # Altura personalizada para cada celda de título
        margen_inferior = 10  # Margen inferior para evitar que el contenido se corte

        pdf.set_font('calibri', '', 9)
       # Definir las alturas específicas para cada grupo de columnas
        height_first_columns = 12
        height_large_columns = 24
        height_other_columns = 12

        for i, titulo in enumerate(titulos_columnas):
            # Determinar la altura para cada columna
            if i < 2:
                cell_height = height_first_columns  # Altura para las primeras dos columnas
            elif i == 2 or i == 4:
                cell_height = height_large_columns  # Altura para las columnas 3 y 5
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

                # Cargar y ordenar datos
      # Ordenar los registros y definir anchuras y altura de celda
        onland = sorted(database.marine_onland(uid), key=lambda x: x.get('dateOn', ''), reverse=True)
        anchuras = [22, 22, 27, 35, 27, 25, 40]
        cell_height = 6

        for fila in onland:
            # Obtener valores de cada campo y formatear fechas
            fecha_ingreso = fila.get('dateOn', '')
            fecha_ingreso = '' if fecha_ingreso in ('NA', 'N/A') else fecha_ingreso
            fecha_ingreso = datetime.strptime(fecha_ingreso, '%Y-%m-%d').strftime('%m-%d-%Y') if fecha_ingreso else ''

            fecha_salida = fila.get('dateOff', '')
            fecha_salida = '' if fecha_salida in ('NA', 'N/A') else fecha_salida
            fecha_salida = datetime.strptime(fecha_salida, '%Y-%m-%d').strftime('%m-%d-%Y') if fecha_salida else ''

            # Otros datos
            nombre_empresa = fila.get('companyName', '')
            nombre_empresa = '' if nombre_empresa in ('NA', 'N/A') else nombre_empresa

            nombre_barco = fila.get('dutiesOrResponsibilities', '')
            nombre_barco = '' if nombre_barco in ('NA', 'N/A') else nombre_barco

            imo_numero = fila.get('rank/position', '')
            imo_numero = '' if imo_numero in ('NA', 'N/A') else imo_numero

            gt_hp = fila.get('reasonForLeaving', '')
            gt_hp = '' if gt_hp in ('NA', 'N/A') else gt_hp

            tipo_barco = fila.get('nameOfContactPersonAndTelephoneNumber', '')
            tipo_barco = '' if tipo_barco in ('NA', 'N/A') else tipo_barco

            # Generar las líneas para cada celda
            lines_fecha_ingreso = pdf.multi_cell(anchuras[0], cell_height, fecha_ingreso, border=0, align='L', split_only=True)
            lines_fecha_salida = pdf.multi_cell(anchuras[1], cell_height, fecha_salida, border=0, align='L', split_only=True)
            lines_nombre_empresa = pdf.multi_cell(anchuras[2], cell_height, nombre_empresa, border=0, align='L', split_only=True)
            lines_nombre_barco = pdf.multi_cell(anchuras[3], cell_height, nombre_barco, border=0, align='L', split_only=True)
            lines_imo_numero = pdf.multi_cell(anchuras[4], cell_height, imo_numero, border=0, align='L', split_only=True)
            lines_gt_hp = pdf.multi_cell(anchuras[5], cell_height, gt_hp, border=0, align='L', split_only=True)

            # Calcular la altura de cada celda
            height_fecha_ingreso = len(lines_fecha_ingreso) * cell_height if fecha_ingreso else cell_height
            height_fecha_salida = len(lines_fecha_salida) * cell_height if fecha_salida else cell_height
            height_nombre_empresa = len(lines_nombre_empresa) * cell_height if nombre_empresa else cell_height
            height_nombre_barco = len(lines_nombre_barco) * cell_height if nombre_barco else cell_height
            height_imo_numero = len(lines_imo_numero) * cell_height if imo_numero else cell_height
            height_gt_hp = len(lines_gt_hp) * cell_height if gt_hp else cell_height

            # Ajustar las alturas para que todas sean iguales a la mayor
            adjusted_height = max(height_fecha_ingreso, height_fecha_salida, height_nombre_empresa,
                                height_nombre_barco, height_imo_numero, height_gt_hp)

            # Verificar si es necesario un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Posición inicial de `x` e `y` para esta fila
            x_start = pdf.get_x()
            y_start = pdf.get_y()

            # Dibujar cada celda con la altura ajustada
            # Celda de Fecha de Ingreso
            pdf.set_xy(x_start, y_start)
            pdf.cell(anchuras[0], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start, y_start, anchuras[0], adjusted_height, fecha_ingreso)

            pdf.set_xy(x_start + anchuras[0], y_start)
            pdf.cell(anchuras[1], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0], y_start, anchuras[1], adjusted_height, fecha_salida)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1], y_start)
            pdf.cell(anchuras[2], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1], y_start, anchuras[2], adjusted_height, nombre_empresa)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2], y_start)
            pdf.cell(anchuras[3], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2], y_start, anchuras[3], adjusted_height, nombre_barco)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_start)
            pdf.cell(anchuras[4], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_start, anchuras[4], adjusted_height, imo_numero)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4], y_start)
            pdf.cell(anchuras[5], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4], y_start, anchuras[5], adjusted_height, gt_hp)

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4] + anchuras[5], y_start)
            pdf.cell(anchuras[6], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4] + anchuras[5], y_start, anchuras[6], adjusted_height, tipo_barco)

            pdf.ln()