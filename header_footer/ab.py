from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        # Solo agregar el encabezado en la primera página
        if self.page_no() == 1:  
            self.image("LOGISTIC-SinFondo.png", 160, 8, 33)  # Alineado a la derecha
    def footer(self):
        self.set_text_color(0,0,0)
        self.set_y(-20)
        self.set_font('calibri', 'I', 9)

        # Código
        self.set_x(-60)
        self.cell(0, 3.5, 'Código: F-PMSSA-01-C', ln=True, align='R')

        # Revisión
        self.set_x(-60)
        self.cell(0, 3.5, 'Revisión: 02', ln=True, align='R')

        # Fecha
        self.set_x(-60)
        self.cell(0, 3, 'Fecha: 7 de noviembre de 2024', ln=True, align='R')

        # Número de página
        self.set_x(-30)
        page_text = f'Página {self.page_no()} de {{nb}}'
        self.cell(0, 3, page_text, ln=True, align='R')
