from datetime import datetime

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

class Onboard():
    def ab(self, pdf, database, uid):
        pdf.cell(0, 10, txt='3.WORK EXPERIENCE ONBOARD', align="L")
        pdf.ln(10)

        # Configuración de columnas
        anchuras_columnas = [25, 25, 32, 20, 18, 18, 23, 25]
        titulos_columnas = [
            'DATE ON  (MM/DD/YYYY)',
            'DATE OFF (MM/DD/YYYY)',
            'COMPANY NAME',
            'VESSEL NAME',
            'IMO #',
            'GT / HP',
            'TYPE OF VESSEL',
            'RANK/POSITION'
        ]
        align_type = ['C', 'C', 'C', 'L', 'C', 'L', 'C', 'C']
        pdf.set_font('calibri', '', 9)
        altura_linea = 6
        margen_inferior = 10

        # Dibujar los encabezados
        for i, titulo in enumerate(titulos_columnas):
            lineas_texto = ajustar_texto_a_altura(titulo, anchuras_columnas[i], pdf)
            altura_total = altura_linea * len(lineas_texto)
            pdf.multi_cell(anchuras_columnas[i], altura_linea, "\n".join(lineas_texto), border=1, align=align_type[i], fill=True)
            pdf.set_xy(pdf.get_x() + anchuras_columnas[i], pdf.get_y() - altura_total)
        pdf.ln(altura_total)

        # Cargar y ordenar datos
        onboard = sorted(database.marine_onboard(uid), key=lambda x: x.get('dateOn', ''), reverse=True)

        # Generar filas con datos
        for fila in onboard:
            date_on = fila.get('dateOn', '')
            date_off = fila.get('dateOff', '')

            try:
                if date_on:
                    date_on = datetime.strptime(date_on, "%Y-%m-%d").strftime("%m-%d-%Y")
            except ValueError:
                pass

            try:
                if date_off:
                    date_off = datetime.strptime(date_off, "%Y-%m-%d").strftime("%m-%d-%Y")
            except ValueError:
                pass

            columnas = [
                date_on,
                date_off,
                fila.get('companyName', ''),
                fila.get('vesselName', ''),
                fila.get('imo#', ''),
                fila.get('gt/hp', ''),
                fila.get('typeOfVessel', [{}])[0].get('name', '') if fila.get('typeOfVessel') else '',
                fila.get('rank/position', '')
            ]

            # Ajuste de altura de cada columna en función de la cantidad de líneas necesarias
            alturas = [len(ajustar_texto_a_altura(valor, anchuras_columnas[i], pdf)) * altura_linea for i, valor in enumerate(columnas)]
            altura_fila = max(alturas)
            
            # Verificar si hay suficiente espacio en la página actual
            if pdf.get_y() + altura_fila + margen_inferior > pdf.page_break_trigger:
                pdf.add_page()

            # Dibujar cada celda en la fila
            y_inicial = pdf.get_y()
            for i, valor in enumerate(columnas):
                lineas_texto = ajustar_texto_a_altura(valor, anchuras_columnas[i], pdf)
                pdf.multi_cell(anchuras_columnas[i], altura_linea, "\n".join(lineas_texto), border=1, align=align_type[i])
                # Posicionar a la derecha de la celda actual
                pdf.set_xy(pdf.get_x() + anchuras_columnas[i], y_inicial)
            
            # Mover el cursor a la siguiente fila
            pdf.ln(altura_fila)
