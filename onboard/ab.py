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

class Onboard:
    def ab(self, pdf, database, uid):
        pdf.ln(40)
        pdf.cell(0, 10, txt='3. WORK EXPERIENCE ONBOARD', align="L")
        pdf.ln(10)

        anchuras_columnas = [25, 25, 32, 25, 18, 15, 30, 28]
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
        anchuras = [25, 25, 32, 25, 18, 15, 30, 28]
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
            tipo_barco = fila.get('typeOfVessel', [{}])[0].get('name', '') if fila.get('typeOfVessel') else ''
            posicion = fila.get('rank/position', '')

            # Calcular el número de líneas necesarias en cada celda para multi_cells
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

            # Dibujar cada celda de la fila con el ancho y altura ajustada
            pdf.set_xy(x_inicial, y_inicial)
            pdf.cell(anchuras[0], altura_fila, fecha_ingreso, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0], y_inicial)

            pdf.cell(anchuras[1], altura_fila, fecha_salida, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1], y_inicial)

            # Utilizar multi_cell para nombre_empresa ajustado a la altura máxima
            pdf.multi_cell(anchuras[2], cell_height, nombre_empresa, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2], y_inicial)

            # Utilizar multi_cell para nombre_barco ajustado a la altura máxima
            pdf.multi_cell(anchuras[3], cell_height, nombre_barco, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_inicial)

            # Utilizar cell para imo_numero
            pdf.cell(anchuras[4], altura_fila, imo_numero, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4], y_inicial)

            # Utilizar cell para gt_hp
            pdf.cell(anchuras[5], altura_fila, gt_hp, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4] + anchuras[5], y_inicial)

            # Utilizar multi_cell para tipo_barco ajustado a la altura máxima
            pdf.multi_cell(anchuras[6], cell_height, tipo_barco, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4] + anchuras[5] + anchuras[6], y_inicial)

            # Utilizar cell para posicion
            pdf.cell(anchuras[7], altura_fila, posicion, border=1, align='C')

            # Ajustar la posición y para la siguiente fila, considerando la altura máxima calculada
            pdf.set_y(y_inicial + altura_fila)
