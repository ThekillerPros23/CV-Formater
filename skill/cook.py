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
    def cook(self, pdf, database, uid):
        skill = database.marine_skills(uid)
        ancho_columna_1 = 130  # Ancho de la primera columna
        ancho_columna_2 = 30   # Ancho de las columnas "YES" y "NO"
        altura_linea = 6       # Altura de cada línea de texto
        margen_inferior = 10   # Margen inferior para evitar que el contenido se corte

        # Lista de textos para cada fila
        textos = [
            "FOR COOK",
            "Mark the following skills /responsibilities / learning experience / achievements if you have knowledge, competence, and experience about:",
            "Do you have experience in the management and supervision of the kitchen personnel?",
            "Are you able to work with multicultural teams and assign tasks to them in the kitchen?",
            "Can you maintain order, follow the established galley cleaning schedule, and ensure discipline for the crew in charge after each service, while exercising proper methods to minimize equipment damage?",
            "Are you aware that everything related to overtime must be coordinated with the captain, who is responsible for its authorization?",
            "Do you know how to prepare the reports that you must present to the captain, related to the catering department, to determine product availability and current food costs?",
            "Do you understand that the cook position in no way states or implies that these are the only duties to be performed by the shipboard employee occupying this position? Shipboard employees will be required to perform any other job-related duties assigned by the master.",
            "Do you know about the established quality standards and company policies in order to supervise galley staff?",
            "Do you have experience keeping the galley, pantries, mess rooms and provision rooms clean and prepared for rough weather?",
            "PRACTICAL KITCHEN KNOWLEDGE",
            "Understands and follows recipes, has knowledge of nutrition, raw materials, preparation techniques, and applies these skills in menu planning.",
            "Understand the importance of the daily/weekly menus and organize and prepare these menus",
            "Understand the interaction between meals and the pace of daily work on board and its importance for the practical aspects of food and snack service",
            "Do you have experience planning and preparing provision orders while keeping food allowance in mind?",
            "FOOD HYGIENE AND PERSONAL",
            "Maintains good personal hygiene, understands the importance of frequent hand washing and how to perform it thoroughly, knows what kind of clothes to wear in the kitchen, and is aware of the factors that can put the health of others at risk.",
            "Do you know of how to break the chain of foodborne diseases?",
            "Understands the importance of and knows how to clean and disinfect kitchens, dining rooms, and pantries, and why it is important to do so.",
            "Do you have knowledge of how to handle refrigerated and frozen products?",
            "Organizes and applies appropriate working methods that ensure the correct flow of products, as well as continuous cleaning, to avoid cross-contamination of food.",
            "Maintains adequate control to ensure the safety of food when refrigerating leftovers, especially the importance of putting date in food for reuse",
            "Are you aware of the causes of allergies, how to prevent skin infections, and how to prevent skin allergies derived from food consumption, as well as how to identify the symptoms?",
            "Know the importance of keeping proper maintenance control for drinking water equipment to prevent the proliferation of bacteria in the system",
            "STORAGE OF FOOD",
            "Do you have knowledge of how to store highly perishable foods, perishables, and their shelf life?",
            "Procedure for storing food safely and safely, especially once the container is opened.",
            "Ensure the handling of food products at the time of delivery and how to place them on the shelves (first come, first out system) is carried out according to procedures",
            "MANAGEMENT OF RESERVATIONS",
            "Are you aware that the food products to be bought, according to the composition of the menu plan, is according to the use of raw materials and the financial established?",
            "Do you have experience in preparing and submitting a monthly stock of provisions and a galley consumables equipment inventory?",
            "Do you have the ability to calculate figures and amounts such as discounts, interest, commissions, tips, proportions, percentages?",
            "Can you maintain adequate control of the quantity of provisions according to the number of crew members and the duration and nature of the voyages?",
            "Do you Know the importance of food supply, and maintains control through systematization and periodic reviews to monitor the quantity and quality of food?",
            "Are you able to draw up a menu plan for an extended period?",
            "It supplies enough water to drink and prepare food.",
            "ENVIRONMENTAL PROTECTION",
            "Experience in how to manage the waste on board the ship in accordance with the provisions of Annex V of the MARPOL Convention, on waste management plans, kitchen waste should be handled and stored separately from provisions for food, raw materials and drinking water.",
            "SAFETY AND HEALTH OF FONDA SERVICE",
            "Maintain security in the storage of provisions during strong surges, while avoiding unnecessary physical exertion.",
            "Are you familiar with the IGS Code and safety management systems?",
            "Are you capable of providing first aid, particularly for kitchen-related accidents, such as fires, machine-related injuries, cuts, scalds, caustic burns, and crush injuries?",
            "Do you know of how to deal with fires in kitchens, and the use of firefighting equipment?"
        ]

        anchuras = [130, 30, 30]
        cell_height = 6

        # Índices de las filas que deben tener fill=True, "YES" en la segunda columna y "NO" en la tercera
        special_rows = [0, 1, 10, 15, 24, 28, 36, 38]  # Nota: los índices en Python comienzan en 0

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