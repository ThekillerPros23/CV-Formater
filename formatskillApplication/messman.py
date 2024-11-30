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


class Skills():
    def messman(self,pdf,database,uid,version):
        skill = database.marine_skills(uid,version)
        pdf.cell(0,10, txt='9. SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS', align='L')
        pdf.ln()
      # Lista de textos para cada fila
        textos = [
            "SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS",
            "Hard working",
            "Well organized and effective support skills, being able to take the initiative with jobs at hand. Proper cleaning techniques and chemical handling",
            "Ability to work positively and cooperatively in a diverse team environment to meet the entire housekeeping operation.",
            "Demonstrated aptitude and monitors at all times company’s OPP procedures for sanitation and cleanliness.",
            "Always in compliance with the company’s environmental policies and committed to safeguarding the environment, performing all related duties and wearing the proper PPE as required at all times.",
            "Active worker and responsible seaman, able to adjust to a variety of activities such as: cleaning and sanitizing cabins, uploading and downloading provisions, manipulating laundry equipment, handling cleaning machines (e.g., scrubbing machine, suction machine, shampooing machine, steaming machine), dealing with chemicals, performing fogging, delivering food in quarantine areas, etc.",
            "Friendly, open-minded, organized, and effective in providing support, with the ability to take initiative with tasks at hand. Proficient in proper cleaning techniques and chemical handling.",
            "Ability to work cooperatively every day, using common sense in a multicultural environment to meet the demands of the entire housekeeping operation."
        ]

        anchuras = [130, 30, 30]
        cell_height = 6
        special_rows = [0] 
        # Dibujar cada fila de datos
        for index, fila in enumerate(textos):
            # Valores de las columnas según el índice
            nombre_completo = fila
            telefono = "YES" if index in special_rows else "YES"  # Todas las filas tienen "YES" en la segunda columna
            direccion = "NO" if index in special_rows else ""     # Solo las filas en `special_rows` tienen "NO" en la tercera columna

            # Calcular el número de líneas necesarias en la primera columna
            align = 'C' if index in special_rows else 'L'
            nombre_lineas = pdf.multi_cell(anchuras[0], cell_height, nombre_completo, border=0, align=align, split_only=True)
            max_lineas = len(nombre_lineas)
            altura_fila = cell_height * max_lineas

            # Añadir una nueva página si la altura sobrepasa el límite
            if pdf.get_y() + altura_fila > pdf.page_break_trigger:
                pdf.add_page()

            # Guardar posición inicial Y
            y_inicial = pdf.get_y()
            x_inicial = pdf.get_x()  # Posición X para la primera columna

            # Definir si se aplica relleno a las columnas
            fill = True if index in special_rows else False

            # Columna de skills
            pdf.set_xy(x_inicial, y_inicial)
            pdf.multi_cell(anchuras[0], cell_height, nombre_completo, border=1, align=align, fill=fill)

            # Columna de "YES"
            pdf.set_xy(x_inicial + anchuras[0], y_inicial)
            pdf.cell(anchuras[1], altura_fila, telefono, border=1, align='C', fill=fill)

            # Columna de "NO" solo en las filas especiales
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1], y_inicial)
            pdf.cell(anchuras[2], altura_fila, direccion, border=1, align='C', fill=fill)

            # Ajustar la posición y para la siguiente fila, considerando la altura máxima calculada
            pdf.set_y(y_inicial + altura_fila)
