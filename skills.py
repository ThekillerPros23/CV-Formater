from fpdf import FPDF
from skills import *
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
    def ab_os(self, pdf, database, uid):
        skill = database.marine_skills(uid)
        ancho_columna_1 = 130  # Ancho de la primera columna
        ancho_columna_2 = 30   # Ancho de las columnas "YES" y "NO"
        altura_linea = 6       # Altura de cada línea de texto
        margen_inferior = 10   # Margen inferior para evitar que el contenido se corte

        # Lista de textos para cada fila
        textos = [
            "Mark the following skills/ responsibilities/ learning experience / achievements if you have knowledge, competence, and experience about:",
    "Skilled professional sailor, responsible, reliable, proactive, and well-organized, with strong managerial and organizational skills in the maintenance and conservation of the vessel's decks and superstructures.",
    "Perform operations relevant to port cargo.",
    "Performed a safe lookout.",
    "Stood wheel duty when required and followed helm orders from the master, watchkeeping officer or the pilot.",
    "Stood duties at port by the gangway following company´s security policy.",
    "I have experience with the procedures supported and carried out in all deck-planned maintenance, including:",
    "Anchor windlass, chains, and anchors.",
    "Mooring winches, ropes, and springs.",
    "Cranes, derricks and associated auxiliary equipment.",
    "Lifeboats, davits and associated auxiliary equipment.",
    "Cleaning and maintaining other lifesaving appliances.",
    "Outer deck railings, wires, superstructures, deck hull, fire lockers, life raft stations, paint locker, hazmat, and chemicals.",
    "Always followed all working routines and procedures associated with entering and working in confined spaces, and donning hard helmets, safety belts and other PPE.",
    "Deck Maintenance.",
    "Cut surface engrave.",
    "Loading and unloading.",
    "Painting.",
    "Fast Rescue boats Handling.",
    "Survival Craft Boat handling.",
    "Deck Inventory / Storing.",
    "Exceptional quality of work with outstanding results.",
    "Time management.",
    "Team worker.",
    "Good leader.",
    "Honest and hardworking.",
    "Can work effectively on team or independently.",
    "Neat and well organized.",
    "Respect and good treatment towards my other colleagues.",
    "Have you ever been nominated employee of the month.",
    "Can effectively perform with less or without supervision."
        ]

        # Procesa cada texto en la primera columna
        for idx, texto in enumerate(textos, start=1):
            # Determinar si la fila debe tener fondo
            tiene_fondo = idx in [1, 7, 14, 22]
            
            # Ajusta el texto para que se divida en líneas
            lineas_texto = ajustar_texto_a_altura(texto, ancho_columna_1, pdf)
            altura_total = altura_linea * len(lineas_texto)
            
            # Verificar si hay suficiente espacio en la página actual
            if pdf.get_y() + altura_total + margen_inferior > pdf.page_break_trigger:
                pdf.add_page()  # Hacer salto de página si no hay suficiente espacio

            # Guardar la posición inicial para alinear columnas
            x, y = pdf.get_x(), pdf.get_y()
            
            # Establecer el color de relleno si la fila requiere fondo
            # Color gris claro (opcional)
            
            # Primera columna con multi_cell para permitir saltos de línea
            pdf.multi_cell(w=ancho_columna_1, h=altura_linea, txt="\n".join(lineas_texto), border=1, align="C", fill=tiene_fondo)
            
            # Restaurar posición para las celdas "YES" y "NO"
            pdf.set_xy(x + ancho_columna_1, y)
            
            # Crear las celdas "YES" y "NO"
            if tiene_fondo:  # Si es una de las filas especificadas, añade "YES" y "NO"
                pdf.cell(w=ancho_columna_2, h=altura_total, txt="YES", border=1, align="C", fill=True)
                pdf.cell(w=ancho_columna_2, h=altura_total, txt="NO", border=1, align="C", ln=1, fill=True)
            else:
                # Para el resto, solo "YES" en la primera celda y vacío en la segunda
                pdf.cell(w=ancho_columna_2, h=altura_total, txt="YES", border=1, align="C", fill=False)
                pdf.cell(w=ancho_columna_2, h=altura_total, txt="", border=1, align="C", ln=1, fill=False)
    def bosun(self,pdf,database,uid):
        skill = database.marine_skills(uid)
        ancho_columna_1 = 130  # Ancho de la primera columna
        ancho_columna_2 = 30   # Ancho de las columnas "YES" y "NO"
        altura_linea = 6       # Altura de cada línea de texto
        margen_inferior = 10   # Margen inferior para evitar que el contenido se corte

        # Lista de textos para cada fila
        textos = [
            "Mark the following skills/ responsibilities/ learning experience / achievements if you have knowledge, competence, and experience about:",
            "Skilled professional sailor, responsible, reliable, proactive, and well-organized, with strong managerial and organizational skills in the maintenance and conservation of the vessel's decks and superstructures.",
            "Experience with tasks on board related to the able-bodied seaman (ABs) and ordinary seaman (OSs) for work assignments.",
            "Leadership qualities necessary to manage a multicultural crew.",
            "Experience with operations relevant to port cargo.",
            "Knowledge of inventory management and ensuring sufficient inventories of all supplies and tools used by the deck department.",
            "Supervision of docking and undocking operations, including ensuring mooring ropes and/or anchor chains are properly fastened.",
            "Full knowledge of all day-to-day deck operations related to maintenance and deck procedures, including:",
            "    • Anchor windlass, chains, and anchors",
            "    • Mooring winches, ropes, and springs",
            "    • Cranes, derricks and associated auxiliary equipment",
            "    • Lifeboats, davits and associated auxiliary equipment",
            "Supervision of the crew to ensure that all deck-planned maintenance is carried out within specified time periods given by the deck maintenance officer.",
            "Ensuring all working routines and procedures associated with entering and working in confined spaces are strictly adhered to.",
            "Knowledge on how to report and fill out accident/incident reports.",
            "Consistent adherence to all working routines and procedures associated with safety and environmental procedures.",
            "Understanding of the company safety and environmental protection quality management program and responsibilities within the safety organization according to the emergency evacuation plan, as well as station bill.",
            "Participation in firefighting drills on board the ship.",
            "Knowledge of the responsibility to ensure the crew properly uses the appropriate protective equipment.",
            "Ensuring that crew is using proper safety and protection equipment at all times during daily deck operations and that critical working areas are appropriately isolated.",
            "Knowledge of the care of hazardous materials and chemicals and awareness of areas where these materials are used within the deck department.",
            "Understanding of proper handling and storage of chemicals and hazardous materials, including correct paint storage.",
            "Exceptional quality of work with outstanding results.",
            "Time management.",
            "Teamwork skills.",
            "Leadership skills.",
            "Honesty and hardworking nature.",
            "Ability to work effectively in a team or independently.",
            "Neat and well-organized.",
            "Respect and good treatment toward colleagues.",
            "Previous nomination as employee of the month.",
            "Ability to perform effectively with little or no supervision."
        ]

        # Procesa cada texto en la primera columna
        for idx, texto in enumerate(textos, start=1):
            # Determinar si la fila debe tener fondo
            tiene_fondo = idx in [1, 8, 16, 19,23]
            
            # Ajusta el texto para que se divida en líneas
            lineas_texto = ajustar_texto_a_altura(texto, ancho_columna_1, pdf)
            altura_total = altura_linea * len(lineas_texto)
            
            # Verificar si hay suficiente espacio en la página actual
            if pdf.get_y() + altura_total + margen_inferior > pdf.page_break_trigger:
                pdf.add_page()  # Hacer salto de página si no hay suficiente espacio

            # Guardar la posición inicial para alinear columnas
            x, y = pdf.get_x(), pdf.get_y()
            
            # Establecer el color de relleno si la fila requiere fondo
              # Color gris claro

            # Primera columna con multi_cell para permitir saltos de línea
            pdf.multi_cell(w=ancho_columna_1, h=altura_linea, txt="\n".join(lineas_texto), border=1, align="C", fill=tiene_fondo)
            
            # Restaurar posición para las celdas "YES" y "NO"
            pdf.set_xy(x + ancho_columna_1, y)
            
            # Crear las celdas "YES" y "NO" con la misma altura total para que estén alineadas
            pdf.cell(w=ancho_columna_2, h=altura_total, txt="yes", border=1, align="C", fill=tiene_fondo)
            pdf.cell(w=ancho_columna_2, h=altura_total, txt="", border=1, align="C", ln=1, fill=tiene_fondo)

    def oiler(self,pdf,database,uid):
        skill = database.marine_skills(uid)
        pdf.cell(0,10, txt='9. SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS', align='L', ln=1)

        pdf.cell(130,7, txt = "Mark the following skills / responsibilities / learning experience / achievements if you have knowledge, competence, and experience about:", border=1, align="C", fill = True)
        pdf.cell(30,7,"YES", border=1, align="C", fill=True)
        pdf.cell(30,7,"NO", border=1, align="C", fill=True,ln=1)

        pdf.cell(w=130,h=6, txt="Skilled professional sailor, responsible, reliable, proactive, and well-organized, with strong managerial and organizational skills in the maintenance and conservation of the vessel's decks and superstructures.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
       
        pdf.cell(w=130,h=6, txt="Perform operations relevant to port cargo.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Performed a safe lookout.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Stood wheel duty when required and followed helm orders from the master, watchkeeping officer or the pilot", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Stood duties at port by the gangway following company´s security policy.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
       
        pdf.cell(130,7, txt = "I have experience with the procedures supported and carried out in all deck-planned maintenance, including:", border=1, align="C",  fill = True)
        pdf.cell(30,7,"YES", border=1, align="C", fill=True)
        pdf.cell(30,7,"NO", border=1, align="C", fill=True,ln=1)

        pdf.cell(w=130,h=6, txt="Anchor windlass, chains, and anchors", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
       
        pdf.cell(w=130,h=6, txt="Mooring winches, ropes, and springs", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Cranes, derricks and associated auxiliary equipment", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Lifeboats, davits and associated auxiliary equipment", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Cleaning and maintaining other lifesaving appliances", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Outer deck railings, wires, superstructures, deck hull, fire lockers, life raft stations, paint locker, hazmat, and chemicals.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        

        pdf.cell(130,7, txt = "Always followed all working routines and procedures associated with entering and working in confined spaces, and donning hard helmets, safety belts and other PPE.", border=1, align="L", fill = True)
        pdf.cell(30,7,"YES", border=1, align="C", fill=True)
        pdf.cell(30,7,"NO", border=1, align="C", fill=True,ln=1)


        pdf.cell(w=130,h=6, txt="Deck Maintenance", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
       
        pdf.cell(w=130,h=6, txt="Cut surface engrave", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Loading and unloading", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Painting", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Fast Rescue boats Handling", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Survival Craft Boat handling", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Deck Inventory / Storing", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(130,7, txt = "Exceptional quality of work with outstanding results", border=1, align="L", fill = True, )
        pdf.cell(30,7,"YES", border=1, align="C", fill=True)
        pdf.cell(30,7,"NO", border=1, align="C", fill=True,ln=1)

        pdf.cell(w=130,h=6, txt="Time management", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
       
        pdf.cell(w=130,h=6, txt="Team worker", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Good leader", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Honest and hardworking", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Can work effectively on team or independently", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Neat and well organized", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Respect and good treatment towards my other colleagues.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Have your ever been nominated employee of the month", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Can effectively perform with less or without supervision", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

    def messman(self,pdf,database,uid):
        pdf.cell(0,10, txt='9. SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS', align='L')
        pdf.ln(10)
        pdf.cell(w=110,h=6,txt="SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS", border=1, align='L', fill=True)
        pdf.cell(w=30,h=6,txt="YES", border=1, align='C', fill=True)
        pdf.cell(w=30,h=6,txt="NO", border=1, align='C',ln=1, fill=True)
        data_storage=[
                "Hard worked",
                "Well Organized and effective support skills, being able to take the initiative with jobs at hand. Proper cleaning techniques and chemical handling",
                "Ability to work positively and cooperatively in a diverse team environment to meet the entire housekeeping operation.",
                "Demonstrated aptitude and monitors at all times companys OPP procedures for sanitation and cleanliness. ",
                "Always in compliance with the companys environmental policies and be committed to safeguarding the environment and performed all related duties and worn the proper PPE as required at all times.",
                "Active worker and responsible Seaman able to adjust to a variety of activities such as: cleaning and sanitizing cabins, uploading and downloading provision, manipulate laundry equipment, handle cleaning machines, such as: Scrubbing machine, suction machine, shampooing machine, steaming machine, dealing with chemicals, doing the fogging, delivering food in quarantine areas, etc. ",
                "So friendly, open minded, organized and effective support skills, being able to take the initiative with jobs at hand. Proper cleaning techniques and chemical handling. ",
                "Ability to work every day cooperatively by using too much common sense in a multicultural environment to meet the entire housekeeping operation.",
                "Demonstrated aptitude and monitors at all times companys OPP procedures for sanitation and cleanliness. ",
            ]
        other_data = [
            "✔️",
            "❌"
        ]
        column_widths = [110, 30, 30]  # Ancho de cada columna (Título, YES, NO)
        cell_height = 7  # Altura estándar de la celda

        for line in data_storage:
            # Dividimos el texto en varias líneas si es necesario
            pdf.set_font("calibri", "", 9)
            lines = pdf.multi_cell(column_widths[0], cell_height, line, border=0, align='L', split_only=True )
            num_lines = len(lines)

            # Ajustamos la altura de la celda según el número de líneas
            adjusted_height = max(cell_height * num_lines, cell_height)

            # Verificamos si se necesita un salto de página
            if pdf.get_y() + adjusted_height > pdf.page_break_trigger:
                pdf.add_page()

            # Imprimimos la celda del título (texto del data_storage)
            pdf.multi_cell(column_widths[0], cell_height, line, border=1, align='L')

            # Ajustamos la posición de las celdas "YES" y "NO" de acuerdo a la altura ajustada
            pdf.set_xy(pdf.get_x() + column_widths[0], pdf.get_y() - adjusted_height)
            pdf.set_font("NotoEmoji", size=16)
            pdf.cell(w=column_widths[1], h=adjusted_height, txt="✔️", border=1, align='C', ln=0)  # Celda "YES"
            pdf.cell(w=column_widths[2], h=adjusted_height, txt="❌", border=1, align='C', ln=1) 

    def fitter(self,pdf,database,uid):
        skill = database.marine_skills(uid)
        pdf.cell(0,10, txt='9. SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS', align='L', ln=1)

        pdf.cell(130,7, txt = "Mark the following skills / responsibilities / learning experience / achievements if you have knowledge, competence, and experience about:", border=1, align="C", fill = True)
        pdf.cell(30,7,"YES", border=1, align="C", fill=True)
        pdf.cell(30,7,"NO", border=1, align="C", fill=True,ln=1)

        pdf.cell(w=130,h=6, txt="Skilled professional sailor, responsible, reliable, proactive, and well-organized, with strong managerial and organizational skills in the maintenance and conservation of the vessel's decks and superstructures.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
       
        pdf.cell(w=130,h=6, txt="Perform operations relevant to port cargo.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Performed a safe lookout.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Stood wheel duty when required and followed helm orders from the master, watchkeeping officer or the pilot", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Stood duties at port by the gangway following company´s security policy.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
       
        pdf.cell(130,7, txt = "I have experience with the procedures supported and carried out in all deck-planned maintenance, including:", border=1, align="C",  fill = True)
        pdf.cell(30,7,"YES", border=1, align="C", fill=True)
        pdf.cell(30,7,"NO", border=1, align="C", fill=True,ln=1)

        pdf.cell(w=130,h=6, txt="Anchor windlass, chains, and anchors", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
       
        pdf.cell(w=130,h=6, txt="Mooring winches, ropes, and springs", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Cranes, derricks and associated auxiliary equipment", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Lifeboats, davits and associated auxiliary equipment", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Cleaning and maintaining other lifesaving appliances", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Outer deck railings, wires, superstructures, deck hull, fire lockers, life raft stations, paint locker, hazmat, and chemicals.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        

        pdf.cell(130,7, txt = "Always followed all working routines and procedures associated with entering and working in confined spaces, and donning hard helmets, safety belts and other PPE.", border=1, align="L", fill = True)
        pdf.cell(30,7,"YES", border=1, align="C", fill=True)
        pdf.cell(30,7,"NO", border=1, align="C", fill=True,ln=1)


        pdf.cell(w=130,h=6, txt="Deck Maintenance", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
       
        pdf.cell(w=130,h=6, txt="Cut surface engrave", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Loading and unloading", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Painting", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Fast Rescue boats Handling", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Survival Craft Boat handling", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Deck Inventory / Storing", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(130,7, txt = "Exceptional quality of work with outstanding results", border=1, align="L", fill = True, )
        pdf.cell(30,7,"YES", border=1, align="C", fill=True)
        pdf.cell(30,7,"NO", border=1, align="C", fill=True,ln=1)

        pdf.cell(w=130,h=6, txt="Time management", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
       
        pdf.cell(w=130,h=6, txt="Team worker", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Good leader", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Honest and hardworking", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Can work effectively on team or independently", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Neat and well organized", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Respect and good treatment towards my other colleagues.", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)

        pdf.cell(w=130,h=6, txt="Have your ever been nominated employee of the month", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
        
        pdf.cell(w=130,h=6, txt="Can effectively perform with less or without supervision", align="C", border=1, )
        pdf.cell(w=30,h=6,txt="yes", border=1, align='C')
        pdf.cell(w=30,h=6,txt="", border=1, align='C',ln=1)
    def cook(self,pdf,database,uid):
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

        # Procesa cada texto en la primera columna
        for idx, texto in enumerate(textos, start=1):
            # Determinar si la fila debe tener fondo
            tiene_fondo = idx in [1, 7, 14, 22]
            
            # Ajusta el texto para que se divida en líneas
            lineas_texto = ajustar_texto_a_altura(texto, ancho_columna_1, pdf)
            altura_total = altura_linea * len(lineas_texto)
            
            # Verificar si hay suficiente espacio en la página actual
            if pdf.get_y() + altura_total + margen_inferior > pdf.page_break_trigger:
                pdf.add_page()  # Hacer salto de página si no hay suficiente espacio

            # Guardar la posición inicial para alinear columnas
            x, y = pdf.get_x(), pdf.get_y()
            
            # Establecer el color de relleno si la fila requiere fondo
            # Color gris claro (opcional)
            
            # Primera columna con multi_cell para permitir saltos de línea
            pdf.multi_cell(w=ancho_columna_1, h=altura_linea, txt="\n".join(lineas_texto), border=1, align="C", fill=tiene_fondo)
            
            # Restaurar posición para las celdas "YES" y "NO"
            pdf.set_xy(x + ancho_columna_1, y)
            
            # Crear las celdas "YES" y "NO"
            if tiene_fondo:  # Si es una de las filas especificadas, añade "YES" y "NO"
                pdf.cell(w=ancho_columna_2, h=altura_total, txt="YES", border=1, align="C", fill=True)
                pdf.cell(w=ancho_columna_2, h=altura_total, txt="NO", border=1, align="C", ln=1, fill=True)
            else:
                # Para el resto, solo "YES" en la primera celda y vacío en la segunda
                pdf.cell(w=ancho_columna_2, h=altura_total, txt="YES", border=1, align="C", fill=False)
                pdf.cell(w=ancho_columna_2, h=altura_total, txt="", border=1, align="C", ln=1, fill=False)
