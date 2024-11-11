from fpdf import FPDF
from skills import *
class Skills():
    def ab_os(self,pdf,database, uid):
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
        pdf.cell(w=30,h=6,txt="es", border=1, align='C',ln=1)

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

    def cook():
        pass
    def bosun():
        pass
    def oiler():
        pass
    def messman(self,pdf):
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

    def fitter():
        pass
    