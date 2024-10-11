from fpdf import FPDF
class Skills():
    def ab_os(self,pdf):
        pdf.cell(0,10, txt='9. SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS', align='L')
        pdf.cell(w=110,h=6,txt="SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS", border=1, align='L', fill=True)
        pdf.cell(w=30,h=6,txt="YES", border=1, align='C', fill=True)
        pdf.cell(w=30,h=6,txt="NO", border=1, align='C',ln=1, fill=True)

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
        column_widths = [110, 30, 30]  # Ancho de cada columna (Título, YES, NO)
        cell_height = 7  # Altura estándar de la celda

        for line in data_storage:
            # Dividimos el texto en varias líneas si es necesario
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
            pdf.cell(w=column_widths[1], h=adjusted_height, txt="", border=1, align='C', ln=0)  # Celda "YES"
            pdf.cell(w=column_widths[2], h=adjusted_height, txt="", border=1, align='C', ln=1) 

    def fitter():
        pass
    def officer():
        pass