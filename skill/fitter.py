class Skills():
    def fitter(self,pdf,database, uid):
        skill = database.marine_skills(uid)
        pdf.cell(0,10, txt='9. SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS', align='L')
        pdf.ln()
      # Lista de textos para cada fila
        textos = [
      "Mark the following skills / responsibilities / learning experience / achievements if you have knowledge, competence, and experience about:",
    "Have you contributed, supported, and performed all machinery space watches always following company´s procedures, rules, and regulations as fitter?",
    "Do you have knowledge and experience in equipment maintenance?",
    "Do you have a welding certificate by one of the following LR, ABS, DNV?",
    "Do you have knowledge and experience in welding, including TIG and MIG?",
    "Do you have knowledge in the handling and storage of the equipment used on board?",
    "Have you worked under the supervision of various departments, for example the deck and engine department?",
    "Are you aware that all overtime performed must be authorized and reported to the officer in charge, depending on the area and nature of the work performed?",
    "Do you always follow all working routines and procedures associated with safety & environmental procedures?",
    "Have you worked with supervisors and subordinates to understand and comply with the company´s environmental policies and be committed to safeguarding the environment?",
    "Are you aware of the mechanisms to inform your superior about any situation on board that puts the environment at risk or the environmental system does not function properly onboard?",
    "Are you aware that it is your responsibility to keep the equipment and tools in good working order?",
    "I have carried out the procedures and supported all engine-planned maintenance including:",
    "Do you have knowledge in overhauling of pumps?",
    "Do you have knowledge in operating lathe machine?",
    "Do you have knowledge in carrying out must steelwork, including stainless steel?",
    "Do you have knowledge in pipe installation and fitting?",
    "Do you have experience assisting with overhauling of diesel engines and auxiliary systems?",
    "Do you have experience taking all readings on main engine and generators, and auxiliary equipment?",
    "Do you always follow up on all working routines and procedures associated with entering and working in confined spaces, and donning hard helmets, safety belts, and other PPE?",
    "Exceptional quality of work with outstanding results:",
    "Time management",
    "Team Worker",
    "Good Leader",
    "Honest and hardworking",
    "Can you work effectively on a team or independently?",
    "Neat and well organized",
    "Can effectively perform with less or without supervision",
    "Respect and good treatment towards my other colleagues.",
    "Have you ever been nominated employee of the month?"        ]

        anchuras = [130, 30, 30]
        cell_height = 6

        # Índices de las filas que deben tener fill=True, "YES" en la segunda columna y "NO" en la tercera
        special_rows = [0, 8,  12, 20]  # Nota: los índices en Python comienzan en 0

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