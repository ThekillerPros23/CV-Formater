from fpdf import FPDF
from flask import Flask, jsonify, request
from datetime import datetime

class PDF(FPDF):
    def header(self):
        # Solo agregar el encabezado en la primera página
        if self.page_no() == 1:  
            self.image("LOGISTIC-SinFondo.png", 160, 8, 33)  # Alineado a la derecha
    def footer(self):
        self.set_y(-20)

        # Configuración de fuente para el footer
        self.set_font('calibri', 'I', 10)

        # Texto alineado a la derecha
        # Mover el cursor al borde derecho
        self.set_x(-60)  # Ajusta el valor para alinear mejor al borde derecho

        # Agregar las líneas de información del pie de página
        self.cell(0, 5, 'Código: F-PMSSA-01-E', ln=True, align='R')
        self.set_x(-60)  # Repetimos para alinear cada línea
        self.cell(0, 5, 'Revisión: 00', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 5, 'Fecha: 17 de mayo de 2022', ln=True, align='R')
        self.set_x(-80)

        # Número de página actual vs total de páginas
        page_text = f'Página {self.page_no()} de {{nb}}'
        self.cell(0, 5, page_text, ln=True, align='R')
   
app = Flask(__name__)

@app.route('/pdf_render', methods=['GET'])
def pdf_render():
   
    datos = [
    {"col1": "Dato1", "col2": "Dato2", "col3": "Dato3", "col4": "Dato4"},
    {"col1": "Dato5", "col2": "Dato6", "col3": "Dato7", "col4": "Dato8"}, 
      {"col1": "Dato1", "col2": "Dato2", "col3": "Dato3", "col4": "Dato4"},
    {"col1": "Dato5", "col2": "Dato6", "col3": "Dato7", "col4": "Dato8"},
      {"col1": "Dato1", "col2": "Dato2", "col3": "Dato3", "col4": "Dato4"},
    {"col1": "Dato5", "col2": "Dato6", "col3": "Dato7", "col4": "Dato8"},  
      {"col1": "Dato1", "col2": "Dato2", "col3": "Dato3", "col4": "Dato4"},
    {"col1": "Dato5", "col2": "Dato6", "col3": "Dato7", "col4": "Dato8"}, 
      {"col1": "Dato1", "col2": "Dato2", "col3": "Dato3", "col4": "Dato4"},
    {"col1": "Dato5", "col2": "Dato6", "col3": "Dato7", "col4": "Dato8"}, 
]

    anchuras = [40, 50, 60, 40]
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
    pdf.add_font('calibri', '', 'calibri.ttf', uni=True)
    pdf.add_font('calibri', 'I','calibrii.ttf',uni=True)
    pdf.add_page()
    pdf.alias_nb_pages()
    # Agregar contenido al PDF
    pdf.set_xy(0, 20)  # Ajustar la posición para el título
    pdf.set_font('helvetica', '', 22)
    pdf.cell(0, 10, 'SEAFARER APPLICATION FORM', align='C')

    pdf.set_xy(55, 30)  # Ajustar la posición para el siguiente texto
    pdf.set_font('Arial', '', 11)
    pdf.cell(30, 10, 'POSITION APPLYING FOR RANK: ')
    
    pdf.set_xy(124, 30)
    pdf.set_font('Arial', 'BU', 11)
    pdf.cell(60, 10, 'MESSMAN')

    pdf.set_xy(55, 40)
    pdf.set_font('Arial', '', 11)
    pdf.cell(55, 10, '1. PERSONAL INFORMATION')


    pdf.set_font('calibri', '', 10) 
    pdf.set_xy(50, 50)

    # Definir anchos para alineación
    cell_width = 50
    big_cell_width = 100
    height = 7
    pdf.set_font('calibri', '', 10) 
    # Encabezado para Nombres
    pdf.cell(w=cell_width, h=height, txt='NAME', border=1, align='L')
    pdf.cell(w=cell_width, h=height, txt=str(name), border=1, align='C')
    pdf.cell(w=cell_width, h=height, txt=str(second_name), border=1, align='C', ln=1)
    pdf.set_font('calibri', '', 10) 
    # Encabezado para Apellidos
    pdf.set_xy(50, 57)  
    pdf.cell(w=cell_width, h=height, txt='SURNAMES', border=1, align='L')
    pdf.cell(w=cell_width, h=height, txt=str(lastname), border=1, align='C')
    pdf.cell(w=cell_width, h=height, txt=str(second_lastname), border=1, align='C', ln=1)
    pdf.set_font('calibri', '', 10) 
    # Fecha de nacimiento
    pdf.set_xy(50, 64)  
    pdf.multi_cell(w=cell_width, h=6.5, txt='DATE OF BIRTH\n(YYYY-MM-DD)', border=1, align='C')

    # Llenar la fecha de nacimiento
    pdf.set_xy(100, 64) 
    pdf.cell(w=big_cell_width, h=13, txt=str(formatted_timestamp), border=1, align='C', ln=1)

    # Nacionalidad
    pdf.set_xy(50, 77)  
    pdf.cell(w=cell_width, h=height, txt='NATIONALITY', border=1, align='L')
    pdf.cell(w=big_cell_width, h=height, txt=str(nationality), border=1, align='C', ln=1)

    # Sexo y Estado Civil
    pdf.set_xy(50, 84)  
    pdf.cell(w=cell_width, h=7, txt='SEX', border=1, align='L')
    pdf.cell(w=20, h=7, txt=str(sex), border=1, align='C')
    pdf.cell(w=45, h=7, txt='CIVIL STATUS', border=1, align='L')
    pdf.cell(w=35, h=7, txt=str(civil_status), border=1, align='C', ln=1)
    
    # Espaciado y otras celdas
    pdf.set_xy(50, 91)
    pdf.cell(w=30, h=7, txt='HEIGHT (Ft/in)', border=1, align='L')
    pdf.cell(w=20, h=7, txt=str(sex), border=1, align='C')
    pdf.cell(w=30, h=7, txt='WEIGHT (Lb)', border=1, align='L')
    pdf.cell(w=20, h=7, txt=str(civil_status), border=1, align='C')
    pdf.cell(w=20, h=7, txt='BMI', border=1, align='L')
    pdf.cell(w=30, h=7, txt=str(civil_status), border=1, align='C', ln=1)

    pdf.ln(5)
    pdf.set_font('calibri', '', 9.5)
    pdf.multi_cell(w=40, h=7, txt="COMPLETE HOME ADDRESS", border=1, align="L")
    pdf.set_xy(50, 103)
    pdf.cell(w=50, h=13, txt="", border=1, align="C")
    pdf.cell(w=50, h=13, txt="NEARLY AIRPORT", border=1, align="L")
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
    
    pdf.ln(5)
    pdf.set_xy(40,160)
    pdf.cell(0,10,txt="2. EMERGENCY CONTACT / NEXT OF KIN0", border=0, align='L')
    pdf.ln(15)
    pdf.cell(w=0,h=14,txt="EMERGENCY CONTACT / NEXT OF KIN", border=1, align='C',ln=1)
    pdf.cell(w=40,h=14,txt="RELATIONSHIP", border=1, align='C')
    pdf.cell(w=50,h=14,txt="COMPLETE NAME", border=1, align='C')
    pdf.multi_cell(w=60,h=7,txt="TELEPHONE NUMBER / MOBILE", border=1, align='C')
    pdf.set_xy(160,189)
    pdf.cell(w=40,h=14,txt="ADDRESS", border=1, align='C',ln=1)
    for fila in datos:
    # Recorrer cada columna y valor de la fila
        for i, (columna, valor) in enumerate(fila.items()):
            pdf.cell(w=anchuras[i], h=8, txt=valor, border=1, align='C')
        pdf.ln(8)
    pdf.cell(0, 10, txt='3.WORK EXPERIENCE ONBOARD', align="L")
    pdf.ln(10)
   # Obtener posiciones iniciales
    x_inicial = pdf.get_x()
    y_inicial = pdf.get_y()

    anchuras_columnas = [28, 28, 24, 21, 18, 18, 23, 30]  
    altura_fila = [7,7,7,7,14,14,7,7]
    pdf.set_font('arial','', 9)
    titulos_columnas = [
    'DATE ON\n(MM/DD/YYYY)',
    'DATE OFF\n(MM/DD/YYYY)',
    'COMPANY\nNAME',
    'VESSEL\nNAME',
    'IMO #',
    'GT / HP',
    'TYPE OF\nVESSEL',
    'RANK/\nPOSITION'
]
    align_type = ['C', 'C', 'C', 'L', 'C', 'L', 'C', 'C']
    pdf.set_xy(x_inicial, y_inicial)
    for i in range(len(titulos_columnas)):
        pdf.multi_cell(w=anchuras_columnas[i], h=altura_fila[i], txt=titulos_columnas[i], align=align_type[i], border=1)
        x_inicial += anchuras_columnas[i]
        pdf.set_xy(x_inicial, y_inicial)
    pdf.ln(20)
    
    pdf.cell(0, 10, txt='4. Personal Documentation / Seafarer Documentation', align='L')
    pdf.ln(10)  


    pdf.cell(w=0, h=7, txt='PERSONAL DOCUMENTATION / SEAFARER DOCUMENTATION', align='C', border=1, ln=1)
    pdf.set_font('Calibri', '', 10)


    pdf.multi_cell(w=30, h=7, txt='TYPE OF DOCUMENT / ID', align='C', border=1)
    pdf.multi_cell(w=30, h=7, txt='COUNTRY OF ISSUE', align='C', border=1)
    pdf.cell(w=30, h=7, txt='NO.', align='C', border=1)
    pdf.multi_cell(w=30, h=7, txt='ISSUED AT (PLACE)', align='C', border=1)
    pdf.multi_cell(w=30, h=7, txt='DATE OF ISSUE (MM / DD / YYYY)', align='C', border=1)
    pdf.multi_cell(w=30, h=7, txt='VALID UNTIL (MM / DD / YYYY)', align='C', border=1)
    pdf.ln(5)
    pdf.cell(0,10, txt='5. TRAINING AND CERTIFICATION.', align='L')
    pdf.ln(10)
    pdf.cell(w=0, h=7,txt='STCW CERTIFICATES', align='C', border=1)
    pdf.ln(8)
    pdf.multi_cell(w=30,h=7,txt='DESCRIPTION OF CERT / COURSE', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='COUNTRY OF ISSUE', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='NUMBER', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='DATE OF ISSUE (MM/DD/YYYY)', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='DATE OF EXPIRY(MM/DD/YYYY)', align='C', border=1)
    pdf.ln(5)
    pdf.cell(0,10, txt='6. WORK EXPERIENCE ONSHORE', align='L')
    pdf.ln(10)
    pdf.multi_cell(w=30,h=7,txt='DATE ON(MM/DD/YYYY)', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='DATE OFF(MM/DD/YYYY)', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='COMPANY NAME / SHIP-OWNER', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='DUTIES OR RESPONSABILITIES', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='RANK/POSITION', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='REASON FOR LEAVING', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='NAME OF CONTACT PERSON & TELEPHONE NUMBER', align='C', border=1)
    
    pdf.output('hoja.pdf')

    return jsonify({"message": "PDF generated successfully!"})

if __name__ == "__main__":
    app.run(host='localhost', port=4000)
