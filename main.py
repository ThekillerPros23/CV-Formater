from fpdf import FPDF
from flask import Flask, jsonify, request
from datetime import datetime

class PDF(FPDF):
    def header(self):
        # Solo agregar el encabezado en la primera página
        if self.page_no() == 1:  
            self.image("LOGISTIC-SinFondo.png", 160, 8, 33)  # Alineado a la derecha
    def footer(self):
        # Posiciona el pie de página a 15 mm desde el final
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        
        # Añadir el código, revisión, fecha, y paginación
        page_info = f"Código: F-PMSSA-01-E  |  Revisión: 00  |  Fecha: 17 de mayo de 2022"
        page_number = f"Página {self.page_no()} de {{nb}}"
        
        # Escribir el texto alineado a la derecha
        self.cell(0, 10, page_info + '  ' + page_number, 0, 0, 'R')
app = Flask(__name__)

@app.route('/pdf_render', methods=['GET'])
def pdf_render():
    # Obtener datos de la solicitud
    name = request.args.get('name')
    second_name = request.args.get('second_name')
    lastname = request.args.get('lastname')
    second_lastname = request.args.get('second_lastname')
    date = request.args.get('date')
    nationality = request.args.get('nationality')
    sex = request.args.get('sex')
    civil_status = request.args.get('civil_status')
    
    # Formatear la fecha
    timestamp_obj = datetime.fromtimestamp(int(date))
    formatted_timestamp = timestamp_obj.strftime("%Y-%b-%d")

    # Crear PDF
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # Agregar contenido al PDF
    pdf.set_xy(0, 20)  # Ajustar la posición para el título
    pdf.set_font('helvetica', '', 22)
    pdf.cell(0, 10, 'SEAFARER APPLICATION FORM', align='C')

    pdf.set_xy(55, 30)  # Ajustar la posición para el siguiente texto
    pdf.set_font('Arial', '', 12)
    pdf.cell(30, 10, 'POSITION APPLYING FOR RANK: ')
    
    pdf.set_xy(124, 30)
    pdf.set_font('Arial', 'BU', 12)
    pdf.cell(60, 10, 'MESSMAN')

    pdf.set_xy(55, 40)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(55, 10, '1. PERSONAL INFORMATION')


    pdf.set_font('Arial', '', 12) 
    pdf.set_xy(50, 50)

    # Definir anchos para alineación
    cell_width = 50
    big_cell_width = 100
    height = 7

    # Encabezado para Nombres
    pdf.cell(w=cell_width, h=height, txt='NAME', border=1, align='L')
    pdf.cell(w=cell_width, h=height, txt=str(name), border=1, align='C')
    pdf.cell(w=cell_width, h=height, txt=str(second_name), border=1, align='C', ln=1)

    # Encabezado para Apellidos
    pdf.set_xy(50, 57)  
    pdf.cell(w=cell_width, h=height, txt='SURNAMES', border=1, align='L')
    pdf.cell(w=cell_width, h=height, txt=str(lastname), border=1, align='C')
    pdf.cell(w=cell_width, h=height, txt=str(second_lastname), border=1, align='C', ln=1)

    # Fecha de nacimiento
    pdf.set_xy(50, 64)  
    pdf.multi_cell(w=cell_width, h=7.5, txt='DATE OF BIRTH\n(YYYY-MM-DD)', border=1, align='C')

    # Llenar la fecha de nacimiento
    pdf.set_xy(100, 64) 
    pdf.cell(w=big_cell_width, h=15, txt=str(formatted_timestamp), border=1, align='C', ln=1)

    # Nacionalidad
    pdf.set_xy(50, 79)  
    pdf.cell(w=cell_width, h=height, txt='NATIONALITY', border=1, align='L')
    pdf.cell(w=big_cell_width, h=height, txt=str(nationality), border=1, align='C', ln=1)

    # Sexo y Estado Civil
    pdf.set_xy(50, 86)  
    pdf.cell(w=cell_width, h=7, txt='SEX', border=1, align='L')
    pdf.cell(w=20, h=7, txt=str(sex), border=1, align='C')
    pdf.cell(w=45, h=7, txt='CIVIL STATUS', border=1, align='L')
    pdf.cell(w=35, h=7, txt=str(civil_status), border=1, align='C', ln=1)
    
    # Espaciado y otras celdas
    pdf.set_xy(50, 93)
    pdf.cell(w=30, h=7, txt='HEIGHT (Ft/in)', border=1, align='L')
    pdf.cell(w=20, h=7, txt=str(sex), border=1, align='C')
    pdf.cell(w=30, h=7, txt='WEIGHT (Lb)', border=1, align='L')
    pdf.cell(w=20, h=7, txt=str(civil_status), border=1, align='C')
    pdf.cell(w=20, h=7, txt='BMI', border=1, align='L')
    pdf.cell(w=30, h=7, txt=str(civil_status), border=1, align='C', ln=1)

    pdf.ln(5)
    
    pdf.multi_cell(w=40, h=7, txt="COMPLETE HOME ADDRESS", border=1, align="L")
    pdf.set_xy(50, 105)
    pdf.cell(w=50, h=14, txt="", border=1, align="C")
    pdf.cell(w=50, h=14, txt="NEARLY AIRPORT", border=1, align="L")
    pdf.cell(w=50, h=14, txt="", border=1, align="C", ln=1)
    pdf.cell(w=30, h=7, txt="PHONE/CELL", border=1, align="C")
    pdf.cell(w=30, h=7, txt="", border=1, align="L")
    pdf.cell(w=30, h=7, txt="WHATSAPP", border=1, align="C")
    pdf.cell(w=30, h=7, txt="", border=1, align="C")
    pdf.cell(w=20, h=7, txt="E-MAIL", border=1, align="L")
    pdf.cell(w=50, h=7, txt="", border=1, align="C", ln=1)
    pdf.cell(w=30, h=7, txt="LANGUAGES", border=1, align="C")
    pdf.cell(w=30, h=7, txt="SPANISH", border=1, align="L")
    pdf.cell(w=30, h=7, txt=""+"%", border=1, align="R")
    pdf.cell(w=30, h=7, txt="ENGLISH", border=1, align="L")
    pdf.cell(w=20, h=7, txt=""+"%", border=1, align="R")
    pdf.cell(w=20, h=7, txt="OTHERS", border=1, align="L")
    pdf.cell(w=30, h=7, txt=""+"%", border=1, align="R", ln=1)
    pdf.ln(5)

    pdf.cell(w=0, h=7, txt="MARLINS / LANGUAGE -TEST", border=1, align="C",ln=1)
    pdf.cell(w=60, h=7, txt="TOTAL %", border=1, align="C")
    pdf.cell(w=60, h=7, txt="ISSUE DATE", border=1, align="C")
    pdf.cell(w=70, h=7, txt="PLACE OF ISSUE", border=1, align="C",ln=1)
    pdf.cell(w=60, h=7, txt="", border=1, align="C")
    pdf.cell(w=60, h=7, txt="", border=1, align="C")
    pdf.cell(w=70, h=7, txt="", border=1, align="C",ln=1)
    
    
    
    # Guardar el PDF generado
    pdf.output('hoja.pdf')

    return jsonify({"message": "PDF generated successfully!"})

if __name__ == "__main__":
    app.run(host='localhost', port=4000)
