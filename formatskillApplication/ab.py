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
    def ab_os(self, pdf, database, uid,version):
        skill = database.marine_skills(uid,version)
        ancho_columna_1 = 130  # Ancho de la primera columna
        ancho_columna_2 = 30   # Ancho de las columnas "YES" y "NO"
        altura_linea = 6       # Altura de cada línea de texto
        margen_inferior = 10   # Margen inferior para evitar que el contenido se corte
        pdf.cell(0,10, txt='9. SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS', align='L')
        pdf.ln()
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
