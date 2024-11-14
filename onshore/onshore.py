from datetime import datetime

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

class Onshore:
    def ab(self, pdf, database, uid):
        pdf.ln(60)
        pdf.cell(0, 10, txt='6. WORK EXPERIENCE ONSHORE', align="L")
        pdf.ln(10)

        anchuras_columnas =     [22, 22, 27, 27, 27, 25, 40]
        titulos_columnas = [
            'DATE ON(MM/DD/YYYY)',
            'DATE OFF(MM/DD/YYYY)',
            'COMPANY NAME',
            'DUTIES OR RESPONSIBILITIES',
            'RANK / POSITION',
            'REASON FOR LEAVING',
            'NAME OF CONTACT PERSON & TELEPHONE NUMBER',
           
        ]
        align_type = ['C', 'C', 'C', 'L', 'C', 'L', 'C', 'C']
          # Altura personalizada para cada celda de título
        margen_inferior = 10  # Margen inferior para evitar que el contenido se corte

        pdf.set_font('calibri', '', 9)
       # Definir las alturas específicas para cada grupo de columnas
        height_first_columns = 8
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
        anchuras = [22, 22, 27, 27, 27, 25, 40]
        cell_height = 7

        for fila in onland:
            # Obtener valores de cada campo y formatear fechas
            fecha_ingreso = fila.get('dateOn', '')
            fecha_salida = fila.get('dateOff', '')

            fecha_ingreso = datetime.strptime(fecha_ingreso, '%Y-%m-%d').strftime('%m-%d-%Y') if fecha_ingreso else ''
            fecha_salida = datetime.strptime(fecha_salida, '%Y-%m-%d').strftime('%m-%d-%Y') if fecha_salida else ''

            # Otros datos
            nombre_empresa = fila.get('companyName', '')
            nombre_barco = fila.get('dutiesOrResponsibilities', '')
            imo_numero = fila.get('rank/position', '')
            gt_hp = fila.get('reasonForLeaving', '')
            tipo_barco = fila.get('NAME OF CONTACT PERSON & TELEPHONE NUMBER', "")

            # Calcular el número de líneas necesarias para cada campo
            nombre_empresa_lineas = pdf.multi_cell(anchuras[2], cell_height, nombre_empresa, border=0, align='L', split_only=True)
            nombre_barco_lineas = pdf.multi_cell(anchuras[3], cell_height, nombre_barco, border=0, align='L', split_only=True)
            tipo_barco_lineas = pdf.multi_cell(anchuras[6], cell_height, tipo_barco, border=0, align='L', split_only=True)

            # Determinar la altura de la fila según la máxima cantidad de líneas en cualquier multi_cell
            max_lineas = max(len(nombre_empresa_lineas), len(nombre_barco_lineas), len(tipo_barco_lineas))
            altura_fila = cell_height * max_lineas

            # Añadir una nueva página si la altura sobrepasa el límite
            if pdf.get_y() + altura_fila > pdf.page_break_trigger:
                pdf.add_page()

            # Guardar posición inicial Y
            y_inicial = pdf.get_y()
            x_inicial = pdf.get_x()  # Posición X para la primera columna

            # Dibujar cada celda de la fila con la altura máxima
            pdf.set_xy(x_inicial, y_inicial)
            pdf.cell(anchuras[0], altura_fila, fecha_ingreso, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0], y_inicial)

            pdf.cell(anchuras[1], altura_fila, fecha_salida, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1], y_inicial)

            pdf.multi_cell(anchuras[2], cell_height, nombre_empresa, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2], y_inicial)

            pdf.multi_cell(anchuras[3], cell_height, nombre_barco, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_inicial)

            pdf.cell(anchuras[4], altura_fila, imo_numero, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4], y_inicial)

            pdf.cell(anchuras[5], altura_fila, gt_hp, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4] + anchuras[5], y_inicial)

            pdf.multi_cell(anchuras[6], cell_height, tipo_barco, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4] + anchuras[5] + anchuras[6], y_inicial)

            # Ajustar la posición y para la siguiente fila
            pdf.set_y(y_inicial + altura_fila)
