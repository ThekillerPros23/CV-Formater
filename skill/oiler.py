class Skills():
    def oiler(self,pdf,database,uid):
        skill = database.marine_skills(uid)

      # Lista de textos para cada fila
        textos = [
     "For: Oiler",
    "Mark the following skills / responsibilities / learning experience / achievements if you have knowledge, competence, and experience about:",
    "I have contributed, supported, and performed all machinery space watches always following company´s procedures, rules, and regulations as motorman / oiler.",
    "I was also responsible for the inspection, operation, and testing, as required, of all machinery and equipment under my responsibility, also assisting engineers during the machinery maintenance schedule.",
    "Hard working team player and quick to learn individual.",
    "I was also responsible for helping the EWO or Engineer advised regarding the status of the vessel and assigned equipment, always in compliance with the company´s environmental policies and be committed to safeguarding the environmental.",
    "For: Wiper",
    "Highly motivated and keen to learn from superiors.",
    "As wiper always keeping all the machinery spaces clean, tidy, and sanitized at all times.",
    "Also participating in maintenance work, under supervision. Washing and rinsing the floors on a daily basis, and painting at all times.",
    "In the event something went wrong, it was reported immediately to the EOW. Ensures that relevant signs are posted, and advance notice was given when maintenance, repair, or cleaning operations.",
    "Performed all related duties and worn the proper PPE as required at all times.",
    "I have carried out the procedures and supported all engine planned maintenance including:",
    "Main engine",
    "Purifiers room",
    "Auxiliary Engine and Generators",
    "I.G. Fans",
    "Central Coolers",
    "Main Engine Air Coolers",
    "Painting & Cleaning Engine room and tanks",
    "Assisting on transferring and sounding fuel / oil / sludge",
    "Assisting overhauling pumps, valves, and others.",
    "Engine inventory and storing",
    "Loading and unloading",
    "Taking all readings on main engine and generators, and auxiliary equipment",
    "Always followed all working routines and procedures associated with entering and working in confined spaces, and donning hard helmets, safety belts, and other PPE.",
    "Exceptional quality of work with outstanding results:",
    "Time management",
    "Team Worker",
    "Good Leader",
    "Honest and hardworking",
    "Can you work effectively on a team or independently?",
    "Neat and well organized",
    "Can effectively perform with less or without supervision.",
    "Respect and good treatment towards my other colleagues.",
    "Have you ever been nominated employee of the month?"      ]

        anchuras = [130, 30, 30]
        cell_height = 6

        # Índices de las filas que deben tener fill=True, "YES" en la segunda columna y "NO" en la tercera
        special_rows = [0, 1, 6, 12, 26]  # Nota: los índices en Python comienzan en 0

        # Dibujar cada fila de datos
        for index, fila in enumerate(textos):
            # Valores de las columnas según el índice
            nombre_completo = fila
            telefono = "YES" if index in special_rows else "YES"  # Todas las filas tienen "YES" en la segunda columna
            direccion = "NO" if index in special_rows else ""     # Solo las filas en `special_rows` tienen "NO" en la tercera columna

            # Calcular el número de líneas necesarias en la primera columna
            nombre_lineas = pdf.multi_cell(anchuras[0], cell_height, nombre_completo, border=0, align='L', split_only=True)
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
            pdf.multi_cell(anchuras[0], cell_height, nombre_completo, border=1, align='L', fill=fill)

            # Columna de "YES"
            pdf.set_xy(x_inicial + anchuras[0], y_inicial)
            pdf.cell(anchuras[1], altura_fila, telefono, border=1, align='C', fill=fill)

            # Columna de "NO" solo en las filas especiales
            pdf.set_xy(x_inicial + anchuras[0] + anchuras[1], y_inicial)
            pdf.cell(anchuras[2], altura_fila, direccion, border=1, align='C', fill=fill)

            # Ajustar la posición y para la siguiente fila, considerando la altura máxima calculada
            pdf.set_y(y_inicial + altura_fila)