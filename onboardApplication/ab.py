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
        
# Función para ajustar el texto a la altura especificada dentro de una celda
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

class Onboard:
    def ab(self, pdf, database, uid):
        if pdf.get_y() + 40 > pdf.page_break_trigger:  # Verificar si hay espacio suficiente para el título
            pdf.add_page()
        pdf.cell(0, 10, txt='3. WORK EXPERIENCE ONBOARD', align="L")
        pdf.ln(10)

        anchuras_columnas = [25, 25, 32, 25, 18, 20, 25, 28]
        titulos_columnas = [
            'DATE ON (MM/DD/YYYY)',
            'DATE OFF (MM/DD/YYYY)',
            'COMPANY NAME',
            'VESSEL NAME',
            'IMO #',
            'GT / HP',
            'TYPE OF VESSEL',
            'RANK/POSITION'
        ]
        align_type = ['C', 'C', 'C', 'L', 'C', 'L', 'C', 'C']
          # Altura personalizada para cada celda de título
        margen_inferior = 10  # Margen inferior para evitar que el contenido se corte

        margen_inferior = 10  # Margen inferior para evitar que el contenido se corte
        height_first_columns = 6
        height_other_columns = 12
        pdf.set_font('calibri', 'B', 9)  # Fuente para los títulos

        # Paso 1: Dibujar los títulos de las columnas
        for i, titulo in enumerate(titulos_columnas):
            # Determinar la altura para el título dependiendo de la columna
            cell_height = height_first_columns if i < 2 else height_other_columns

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
        
        pdf.ln(max(height_first_columns, height_other_columns))
                # Cargar y ordenar datos
        onboard = sorted(database.marine_onboard(uid), key=lambda x: x.get('dateOn', ''), reverse=True)
        print(onboard)
        anchuras =  [25, 25, 32, 25, 18, 20, 25, 28]
        cell_height = 7
        for fila in onboard:
        # Obtener valores de cada campo y formatear las fechas
            fecha_ingreso_raw = fila.get('dateOn', '')
            fecha_salida_raw = fila.get('dateOff', '')

            # Convertir las fechas al formato MM/DD/YYYY si están en formato YYYY-MM-DD
            fecha_ingreso = (
                f"{fecha_ingreso_raw[5:7]}/{fecha_ingreso_raw[8:10]}/{fecha_ingreso_raw[:4]}"
                if len(fecha_ingreso_raw) == 10 else fecha_ingreso_raw
            )
            fecha_salida = (
                f"{fecha_salida_raw[5:7]}/{fecha_salida_raw[8:10]}/{fecha_salida_raw[:4]}"
                if len(fecha_salida_raw) == 10 else fecha_salida_raw
            )

            nombre_empresa = fila.get('companyName', '')
            nombre_barco = fila.get('vesselName', '')
            imo_numero = fila.get('imo#', '')
            gt_hp = fila.get('gt/hp', '')
            tipo_barco = fila.get('typeOfVessel', [])
            tipo_barco = tipo_barco[0].get('name', '') if isinstance(tipo_barco, list) and tipo_barco else ''

            posicion = fila.get('rank/position', '')

            # Calcular el número de líneas necesarias en cada celda para multi_cells
            lines_fecha_ingreso = pdf.multi_cell(anchuras[0], cell_height, fecha_ingreso, border=0, align='L', split_only=True)
            lines_fecha_salida = pdf.multi_cell(anchuras[1], cell_height, fecha_salida, border=0, align='L', split_only=True)
            lines_nombre_empresa = pdf.multi_cell(anchuras[2], cell_height, nombre_empresa, border=0, align='L', split_only=True)
            lines_nombre_barco = pdf.multi_cell(anchuras[3], cell_height, nombre_barco, border=0, align='L', split_only=True)
            lines_imo_numero = pdf.multi_cell(anchuras[4], cell_height, imo_numero, border=0, align='L', split_only=True)
            lines_gt_hp = pdf.multi_cell(anchuras[5], cell_height, gt_hp, border=0, align='L', split_only=True)
            lines_tipo_barco = pdf.multi_cell(anchuras[6], cell_height, tipo_barco, border=0, align='L', split_only=True)
            lines_posicion = pdf.multi_cell(anchuras[7], cell_height, posicion, border=0, align='L', split_only=True)

            # Calcular la altura de cada celda
            height_fecha_ingreso = len(lines_fecha_ingreso) * cell_height if fecha_ingreso else cell_height
            height_fecha_salida = len(lines_fecha_salida) * cell_height if fecha_salida else cell_height
            height_nombre_empresa = len(lines_nombre_empresa) * cell_height if nombre_empresa else cell_height
            height_nombre_barco = len(lines_nombre_barco) * cell_height if nombre_barco else cell_height
            height_imo_numero = len(lines_imo_numero) * cell_height if imo_numero else cell_height
            height_gt_hp = len(lines_gt_hp) * cell_height if gt_hp else cell_height
            height_tipo_barco = len(lines_tipo_barco) * cell_height if tipo_barco else cell_height
            height_posicion = len(lines_posicion) * cell_height if posicion else cell_height

            # Ajustar las alturas para que todas sean iguales a la mayor
            adjusted_height = max(height_fecha_ingreso, height_fecha_salida, height_nombre_empresa,
                                height_nombre_barco, height_imo_numero, height_gt_hp,
                                height_tipo_barco, height_posicion)

            # Verificar si es necesario un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Posición inicial de `x` e `y` para esta fila
            x_start = pdf.get_x()
            y_start = pdf.get_y()

            # Dibujar cada celda con la altura ajustada
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

            pdf.set_xy(x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4] + anchuras[5] + anchuras[6], y_start)
            pdf.cell(anchuras[7], adjusted_height, border=1)
            draw_text_in_cell(pdf, x_start + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4] + anchuras[5] + anchuras[6], y_start, anchuras[7], adjusted_height, posicion)

            pdf.ln()