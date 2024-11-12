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
        altura_linea = 6  # Altura de cada línea de texto
        margen_inferior = 10  # Margen inferior para evitar que el contenido se corte
        pdf.set_font('calibri', '', 9)

        # Calcular la altura de los títulos en función de los saltos de línea
        alturas_titulos = [
            pdf.multi_cell(anchuras_columnas[i], 0, titulos_columnas[i], border=0, align=align_type[i], split_only=True)
            for i in range(len(titulos_columnas))
        ]

        # Obtener el máximo número de líneas entre los títulos
        max_lineas_titulo = max(len(lineas) for lineas in alturas_titulos)
        altura_titulo = altura_linea * max_lineas_titulo

        # Dibujar encabezados de la tabla con saltos de línea
        x_inicial = pdf.get_x()  # Posición inicial en X
        y_inicial = pdf.get_y()  # Posición inicial en Y

        # Dibujar los títulos de las columnas
        for i, titulo in enumerate(titulos_columnas):
            pdf.set_xy(x_inicial + sum(anchuras_columnas[:i]), y_inicial)
            
            # Dibujar cada título con su altura correspondiente
            pdf.multi_cell(anchuras_columnas[i], altura_titulo, titulo, border=1, align=align_type[i],fill=True)

        # Mover el cursor hacia abajo después de todos los títulos en una sola línea
        pdf.ln(altura_titulo)

        # Cargar y ordenar datos
        onboard = sorted(database.marine_onboard(uid), key=lambda x: x.get('dateOn', ''), reverse=True)
        anchuras = [25, 25, 32, 25, 18, 15, 30, 28]
        cell_height = 7
        for fila in onboard:
           
            fecha_ingreso = fila.get('dateOn', '')
            fecha_salida = fila.get('dateOff', '')
            nombre_empresa = fila.get('companyName', '')
            nombre_barco = fila.get('vesselName', '')
            imo_numero = fila.get('imo#', '')
            gt_hp = fila.get('gt/hp', '')
            tipo_barco = fila.get('typeOfVessel', [{}])[0].get('name', '') if fila.get('typeOfVessel') else ''
            posicion = fila.get('rank/position', '')

            # Calcular el número de líneas necesarias en cada celda
            fecha_ingreso_lineas = pdf.multi_cell(anchuras[0], cell_height, fecha_ingreso, border=0, align='L', split_only=True)
            fecha_salida_lineas = pdf.multi_cell(anchuras[1], cell_height, fecha_salida, border=0, align='L', split_only=True)
            nombre_empresa_lineas = pdf.multi_cell(anchuras[2], cell_height, nombre_empresa, border=0, align='L', split_only=True)
            nombre_barco_lineas = pdf.multi_cell(anchuras[3], cell_height, nombre_barco, border=0, align='L', split_only=True)
            imo_numero_lineas = pdf.multi_cell(anchuras[4], cell_height, imo_numero, border=0, align='L', split_only=True)
            gt_hp_lineas = pdf.multi_cell(anchuras[5], cell_height, gt_hp, border=0, align='L', split_only=True)
            tipo_barco_lineas = pdf.multi_cell(anchuras[6], cell_height, tipo_barco, border=0, align='L', split_only=True)
            posicion_lineas = pdf.multi_cell(anchuras[7], cell_height, posicion, border=0, align='L', split_only=True)

            # Determinar la altura de la fila según la máxima cantidad de líneas en cualquier celda
            max_lineas = max(len(fecha_ingreso_lineas), len(fecha_salida_lineas), len(nombre_empresa_lineas), 
                            len(nombre_barco_lineas), len(imo_numero_lineas), len(gt_hp_lineas), 
                            len(tipo_barco_lineas), len(posicion_lineas))
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

            pdf.multi_cell(anchuras[2], cell_height, nombre_empresa, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2], y_inicial)

            pdf.multi_cell(anchuras[3], cell_height, nombre_barco, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3], y_inicial)

            pdf.multi_cell(anchuras[4], cell_height, imo_numero, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4], y_inicial)

            pdf.multi_cell(anchuras[5], cell_height, gt_hp, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4] + anchuras[5], y_inicial)

            pdf.multi_cell(anchuras[6], cell_height, tipo_barco, border=1, align='C')
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1] + anchuras[2] + anchuras[3] + anchuras[4] + anchuras[5] + anchuras[6], y_inicial)

            pdf.multi_cell(anchuras[7], cell_height, posicion, border=1, align='C')

            # Ajustar la posición y para la siguiente fila, considerando la altura máxima calculada
            pdf.set_y(y_inicial + altura_fila)
