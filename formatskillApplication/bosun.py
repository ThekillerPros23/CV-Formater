class Skills():
    def bosun(self,pdf, database, uid,version):
        skill = database.marine_skills(uid,version)
        ancho_columna_1 = 130  # Ancho de la primera columna
        ancho_columna_2 = 30   # Ancho de las columnas "YES" y "NO"
        altura_linea = 6       # Altura de cada línea de texto
        margen_inferior = 10   # Margen inferior para evitar que el contenido se corte

        # Lista de textos para cada fila
        pdf.cell(0,10, txt='9. SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS', align='L')
        pdf.ln()
        textos = [
    "Mark the following skills/ responsibilities/ learning experience / achievements if you have knowledge, competence, and experience about:",
    "Skilled professional sailor, responsible, reliable, proactive, and well-organized, with strong managerial and organizational skills in the maintenance and conservation of the vessel's decks and superstructures.",
    "Have you carried out the task on board related to the able bodied seaman (Abs) and ordinary Seaman (Oss) for work assignment?",
    "Do you consider yourself to have the leadership qualities necessary to manage a multicultural crew?",
    "Have you performed operations relevant to port cargo?",
    "Do you have Knowledge of inventory management and ensure that there are sufficient inventories of all supplies and tools used by the deck department?",
    "Do you have control of the operations carried out in the docking and undocking port have been supervised, including mooring ropes and/or anchor chains are properly fastened?",
    "Do you have full knowledge of all day-to-day deck operations related to maintenance and deck procedures including?",
    "• Anchor windlass, chains, and anchors",
    "• Mooring winches, ropes, and springs",
    "• Cranes, derricks and associated auxiliary equipment",
    "• Lifeboats, davits and associated auxiliary equipment.",
    "Supervises the crew to ensure that all deck-planned maintenance is carried out within the specified time periods given by deck Maintenance officer.",
    "Responsible for ensuring that all working routines and procedures associated with entering and working in confined spaces are strictly adhered to.",
    "Do you have knowledge on how to report and fill out accident/incident reports?",
    "Do you always follow all working routines and procedures associated with safety & environmental procedures?",
    "Do you understand the Company Safety & environmental protection quality management program and the responsibilities in the safety organization according to the emergency evacuation plan, as well as station bill?",
    "Have you collaborated in carrying out firefighting drills on board the ship?",
    "Do you have Knowledge of the responsibility that the crew in charge properly use the appropriate protective equipment?",
    "Have you ensured that crew is using at all times the proper safety and protection equipment in the daily deck operations and the critical working areas are appropriately and adequately isolated?",
    "Do you have knowledge of the care of hazardous material and chemicals and all areas where these areas are in use within the deck department?",
    "Have you known of the proper handling and storage of chemicals and hazards? (Including the correct storage of the paint)",
    "Exceptional quality of work with outstanding results",
    "Time management",
    "Team worker",
    "Good leader",
    "Honest and hardworking",
    "Can you work effectively on team or independently",
    "Neat and well organized",
    "Respect and good treatment towards my other colleagues.",
    "Have you ever been nominated employee of the month?",
    "Can effectively perform with less or without supervision"
]        

        anchuras = [130, 30, 30]
        cell_height = 6

        # Índices de las filas que deben tener fill=True, "YES" en la segunda columna y "NO" en la tercera
        special_rows = [0,7,15,18,22]  # Nota: los índices en Python comienzan en 0

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