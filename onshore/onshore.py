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
        pdf.ln(40)
        pdf.cell(0, 10, txt='6. WORK EXPIRENCE ONSHORE', align="L")
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
        altura_linea = [8, 8, 24, 12, 24, 12, 12, 6]  # Altura personalizada para cada celda de título
        margen_inferior = 10  # Margen inferior para evitar que el contenido se corte

        pdf.set_font('calibri', '', 9)

        # Calcular el número de líneas para cada título
        alturas_titulos = [
            pdf.multi_cell(anchuras_columnas[i], altura_linea[i], titulos_columnas[i], border=0, align=align_type[i], split_only=True)
            for i in range(len(titulos_columnas))
        ]

        # Obtener el número de líneas en cada título y calcular la altura final para cada uno
        alturas_finales_titulos = [len(lineas) * altura_linea[i] for i, lineas in enumerate(alturas_titulos)]

        # Dibujar los encabezados de las columnas con alturas personalizadas
        x_inicial = pdf.get_x()  # Posición inicial en X
        y_inicial = pdf.get_y()  # Posición inicial en Y

        # Dibujar cada título de columna en su respectiva celda
        for i, titulo in enumerate(titulos_columnas):
            pdf.set_xy(x_inicial + sum(anchuras_columnas[:i]), y_inicial)
            
            # Usar la altura específica calculada para cada título
            pdf.multi_cell(anchuras_columnas[i], altura_linea[i], titulo, border=1, align=align_type[i], fill=True)

        # Mover el cursor hacia abajo después de los títulos, usando la altura máxima entre todas las celdas
        
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
