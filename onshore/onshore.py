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
        pdf.cell(0, 10, txt='6. WORK EXPIRENCE ONSHORE', align="L")
        pdf.ln(10)

        # Configuración de columnas para ajustarse al ancho total de la página
        anchuras_columnas = [22, 22, 27, 27, 27, 25, 40]
        titulos_columnas = [
            'DATE ON (MM/DD/YYYY)',
            'DATE OFF (MM/DD/YYYY)',
            'COMPANY NAME',
            'DUTIES OR RESPONSIBILITIES',
            'RANK / POSITION',
            'REASON FOR LEAVING',
            'NAME OF CONTACT PERSON & TELEPHONE NUMBER',
          
        ]
        align_type = ['C', 'C', 'C', 'L', 'C', 'L', 'C', 'C']
        altura_linea = 6  # Altura de cada línea de texto
        margen_inferior = 10  # Margen inferior para evitar que el contenido se corte
        pdf.set_font('calibri', '', 9)

        # Ajustar altura de los títulos en función de los saltos de línea
        alturas_titulos = [
            ajustar_texto_a_altura(titulo, anchuras_columnas[i], pdf) for i, titulo in enumerate(titulos_columnas)
        ]
        max_lineas_titulo = max(len(lineas) for lineas in alturas_titulos)
        altura_titulo = altura_linea * max_lineas_titulo

        # Dibujar encabezados de la tabla con saltos de línea
        x_inicial = pdf.get_x()  # Posición inicial en X
        y_inicial = pdf.get_y()  # Posición inicial en Y

        for i, lineas_titulo in enumerate(alturas_titulos):
            ancho_columna = anchuras_columnas[i]
            texto_multilinea = "\n".join(lineas_titulo)
            
            # Dibujar una celda para cada título, pero sin saltar a la siguiente línea
            pdf.multi_cell(w=ancho_columna, h=altura_linea, txt=texto_multilinea, border=1, align=align_type[i], fill=True)
            
            # Mover el cursor manualmente a la siguiente posición en X
            pdf.set_xy(x_inicial + ancho_columna, y_inicial)
            x_inicial += ancho_columna  # Incrementar X para la próxima celda

        # Mover el cursor hacia abajo después de todos los títulos en una sola línea
        pdf.ln(altura_titulo)

        # Cargar y ordenar datos
        onland = sorted(database.marine_onland(uid), key=lambda x: x.get('dateOn', ''), reverse=True)

        # Generar filas con datos
        for fila in onland:
            # Convertir fechas a formato MM-DD-YYYY
            date_on = fila.get('dateOn', '')
            date_off = fila.get('dateOff', '')

            try:
                if date_on:
                    date_on = datetime.strptime(date_on, "%Y-%m-%d").strftime("%m-%d-%Y")
            except ValueError:
                pass  # Si la fecha tiene un formato inesperado, se deja tal cual

            try:
                if date_off:
                    date_off = datetime.strptime(date_off, "%Y-%m-%d").strftime("%m-%d-%Y")
            except ValueError:
                pass

            # Crear las columnas de cada fila
            columnas = [
                date_on,
                date_off,
                fila.get('companyName', ''),
                fila.get('dutiesOrResponsibilities', ''),
                fila.get('rank/position', ''),
                fila.get('reasonForLeaving', ''),
                fila.get('nameOfContactPersonAndTelephoneNumber', ''),
                 
            ]

            # Calcular el número de líneas de texto en cada columna y obtener la altura máxima de la fila
            alturas_lineas = [
                ajustar_texto_a_altura(texto, anchuras_columnas[i], pdf) for i, texto in enumerate(columnas)
            ]
            max_lineas_fila = max(len(linea) for linea in alturas_lineas)
            altura_celda = altura_linea * max_lineas_fila  # Altura uniforme para toda la fila

            # Verificar si hay suficiente espacio en la página actual
            if pdf.get_y() + altura_celda + margen_inferior > pdf.page_break_trigger:
                pdf.add_page()  # Salto de página si no hay suficiente espacio

            # Guardar la posición inicial para alinear columnas
            x, y = pdf.get_x(), pdf.get_y()

            # Dibujar cada celda con la altura ajustada de la fila
            for i, lineas_texto in enumerate(alturas_lineas):
                ancho_columna = anchuras_columnas[i]
                
                # Unir las líneas de texto en una cadena con saltos de línea
                texto_multilinea = "\n".join(lineas_texto)
                
                # Dibujar celda con la altura uniforme para toda la fila
                pdf.set_xy(x, y)  # Mantener el cursor en el lugar correcto para cada columna
                pdf.multi_cell(w=ancho_columna, h=altura_celda / max_lineas_fila, txt=texto_multilinea, border=1, align=align_type[i])
                x += ancho_columna  # Mover la posición X para la próxima celda en la fila

            # Restablecer para la próxima fila
            pdf.ln(altura_celda)
