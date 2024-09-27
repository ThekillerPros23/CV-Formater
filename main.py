from fpdf import FPDF
from flask import Flask, jsonify, request
from datetime import datetime
from firebase_data import *

database = FirebaseData()
class PDF(FPDF):
    def header(self):
        # Solo agregar el encabezado en la primera página
        if self.page_no() == 1:  
            self.image("LOGISTIC-SinFondo.png", 160, 8, 33)  # Alineado a la derecha
    def footer(self):
        self.set_y(-20)
        self.set_font('calibri', 'I', 8)

        # Código
        self.set_x(-60)
        self.cell(0, 3.5, 'Código: F-PMSSA-01-E', ln=True, align='R')

        # Revisión
        self.set_x(-60)
        self.cell(0, 3.5, 'Revisión: 00', ln=True, align='R')

        # Fecha
        self.set_x(-60)
        self.cell(0, 3, 'Fecha: 17 de mayo de 2022', ln=True, align='R')

        # Número de página
        self.set_x(-30)
        page_text = f'Página {self.page_no()} de {{nb}}'
        self.cell(0, 3, page_text, ln=True, align='R')
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
    pdf.add_font('calibri', 'BU','calibri.ttf',uni=True)
    pdf.add_font('calibri', 'B','calibrib.ttf',uni=True)
    
    pdf.add_page()
    pdf.alias_nb_pages()
    # Agregar contenido al PDF
    pdf.set_xy(0, 20)  # Ajustar la posición para el título
    pdf.set_font('calibri', '', 22)
    pdf.cell(0, 10, 'SEAFARER APPLICATION FORM', align='C')

    pdf.set_xy(55, 30)  # Ajustar la posición para el siguiente texto
    pdf.set_font('calibri', '', 11)
    pdf.cell(30, 10, 'POSITION APPLYING FOR RANK: ')
    
    pdf.set_xy(116, 30)
    pdf.set_font('calibri', 'BU', 11)
    pdf.cell(60, 10, 'MESSMAN')

    pdf.set_xy(55, 40)
    pdf.set_font('calibri', '', 11)
    pdf.cell(55, 10, '1. PERSONAL INFORMATION')


    pdf.set_font('calibri', '', 10) 
    pdf.set_xy(50, 50)

    # Definir anchos para alineación
    cell_width = 50
    big_cell_width = 100
    height = 7
    pdf.set_font('calibri', '', 8) 
    # Encabezado para Nombres
    
    pdf.cell(w=40, h=height, txt='NAME', border=1, align='L')
    pdf.cell(w=40, h=height, txt=str(name), border=1, align='C')
    pdf.cell(w=40, h=height, txt=str(second_name), border=1, align='C', ln=1)
    pdf.set_font('calibri', '', 8) 
    # Encabezado para Apellidos
    pdf.set_xy(50, 57)  
    pdf.cell(w=40, h=height, txt='SURNAMES', border=1, align='L')
    pdf.cell(w=40, h=height, txt=str(lastname), border=1, align='C')
    pdf.cell(w=40, h=height, txt=str(second_lastname), border=1, align='C', ln=1)
    pdf.set_font('calibri', '', 8) 
    # Fecha de nacimiento
    pdf.set_xy(50, 64)  
    pdf.multi_cell(w=40, h=6.5, txt='DATE OF BIRTH\n(YYYY-MM-DD)', border=1, align='C')

    # Llenar la fecha de nacimiento
    pdf.set_xy(90, 64) 
    pdf.cell(w=80, h=13, txt=str(formatted_timestamp), border=1, align='C', ln=1)

    # Nacionalidad
    pdf.set_xy(50, 77)  
    pdf.cell(w=40, h=height, txt='NATIONALITY', border=1, align='L')
    pdf.cell(w=80, h=height, txt=str(nationality), border=1, align='C', ln=1)

    # Sexo y Estado Civil
    pdf.set_xy(50, 84)  
    pdf.cell(w=40, h=7, txt='SEX', border=1, align='L')
    pdf.cell(w=20, h=7, txt=str(sex), border=1, align='C')
    pdf.cell(w=30, h=7, txt='CIVIL STATUS', border=1, align='L')
    pdf.cell(w=30, h=7, txt=str(civil_status), border=1, align='C', ln=1)
    
    # Espaciado y otras celdas
    pdf.set_xy(50, 91)
    pdf.cell(w=25, h=7, txt='HEIGHT (Ft/in)', border=1, align='L')
    pdf.cell(w=20, h=7, txt=str(sex), border=1, align='C')
    pdf.cell(w=22, h=7, txt='WEIGHT (Lb)', border=1, align='L')
    pdf.cell(w=18, h=7, txt=str(civil_status), border=1, align='C')
    pdf.cell(w=15, h=7, txt='BMI', border=1, align='L')
    pdf.cell(w=20, h=7, txt=str(civil_status), border=1, align='C', ln=1)

   # Configuración inicial
    pdf.ln(5)
    pdf.set_font('calibri', '', 8)

    # Guardar posición inicial
    x_inicial = pdf.get_x()
    y_inicial = pdf.get_y()

    # Primera celda "COMPLETE HOME ADDRESS" con multi_cell
    pdf.set_xy(x_inicial, y_inicial)
    pdf.multi_cell(w=40, h=7, txt="COMPLETE HOME ADDRESS", border=1, align="L")
    height_complete_home = pdf.get_y() - y_inicial  # Altura ocupada por esta celda

    # Segunda celda "BARRIADA EL ALBA..."
    pdf.set_xy(x_inicial + 40, y_inicial)
    pdf.multi_cell(w=50, h=7, txt="BARRIADA EL ALBA ENTRANDO POR EL CHINO NUEVO MUNDO", border=1, align="C")
    height_barrio = pdf.get_y() - y_inicial  # Altura ocupada por esta celda

    # Tercera celda "NEARLY AIRPORT"
    pdf.set_xy(x_inicial + 90, y_inicial)
    pdf.multi_cell(w=50, h=7, txt="NEARLY AIRPORT", border=1, align="L")
    height_airport = pdf.get_y() - y_inicial  # Altura ocupada por esta celda

    # Cuarta celda vacía
    pdf.set_xy(x_inicial + 140, y_inicial)
    pdf.multi_cell(w=50, h=7, txt="", border=1, align="C")
    height_empty = pdf.get_y() - y_inicial  # Altura ocupada por esta celda (debería ser 7)

    # Obtener la altura máxima de la fila
    max_height = max(height_complete_home, height_barrio, height_airport, height_empty)

    # Rellenar celdas para que todas ocupen la misma altura
    # Si alguna celda es más pequeña, agregamos un espacio en blanco para que se ajuste a la altura máxima

    # Si la primera celda "COMPLETE HOME ADDRESS" es más pequeña, la rellenamos
    if height_complete_home < max_height:
        pdf.set_xy(x_inicial, y_inicial + height_complete_home)
        pdf.cell(w=40, h=max_height - height_complete_home, txt="", border=1)

    # Si la segunda celda es más pequeña, la rellenamos
    if height_barrio < max_height:
        pdf.set_xy(x_inicial + 40, y_inicial + height_barrio)
        pdf.cell(w=50, h=max_height - height_barrio, txt="", border=1)

    # Si la tercera celda es más pequeña, la rellenamos
    if height_airport < max_height:
        pdf.set_xy(x_inicial + 90, y_inicial + height_airport)
        pdf.cell(w=50, h=max_height - height_airport, txt="", border=1)

    # Si la cuarta celda es más pequeña, la rellenamos
    if height_empty < max_height:
        pdf.set_xy(x_inicial + 140, y_inicial + height_empty)
        pdf.cell(w=50, h=max_height - height_empty, txt="", border=1)

    # Mover a la siguiente línea después de ajustar todas las celdas
    pdf.set_xy(x_inicial, y_inicial + max_height)

    # Segunda fila con "PHONE/CELL" y demás datos
    pdf.cell(w=30, h=7, txt="PHONE/CELL", border=1, align="C")
    pdf.cell(w=30, h=7, txt="", border=1, align="L")
    pdf.cell(w=30, h=7, txt="WHATSAPP", border=1, align="C")
    pdf.cell(w=30, h=7, txt="", border=1, align="C")
    pdf.cell(w=20, h=7, txt="E-MAIL", border=1, align="L")
    pdf.cell(w=50, h=7, txt="", border=1, align="C", ln=1)

    # Tercera fila con "LANGUAGES"
    pdf.cell(w=30, h=7, txt="LANGUAGES", border=1, align="C")
    pdf.cell(w=30, h=7, txt="SPANISH", border=1, align="L")
    pdf.cell(w=30, h=7, txt="100%", border=1, align="R")
    pdf.cell(w=30, h=7, txt="ENGLISH", border=1, align="L")
    pdf.cell(w=20, h=7, txt="80%", border=1, align="R")
    pdf.cell(w=20, h=7, txt="OTHERS", border=1, align="L")
    pdf.cell(w=30, h=7, txt="50%", border=1, align="R", ln=1)

    pdf.ln(5)
    pdf.set_font('calibri','',8)
    pdf.cell(w=0, h=7, txt="MARLINS / LANGUAGE -TEST", border=1, align="C",ln=1)
    pdf.cell(w=60, h=7, txt="TOTAL %", border=1, align="C")
    pdf.cell(w=60, h=7, txt="ISSUE DATE", border=1, align="C")
    pdf.cell(w=70, h=7, txt="PLACE OF ISSUE", border=1, align="C",ln=1)
    pdf.cell(w=60, h=7, txt="", border=1, align="C")
    pdf.cell(w=60, h=7, txt="", border=1, align="C")
    pdf.cell(w=70, h=7, txt="", border=1, align="C",ln=1)
    
    pdf.ln(5)
    pdf.set_font('calibri','',8)
    pdf.cell(0,10,txt="2. EMERGENCY CONTACT / NEXT OF KIN0", border=0, align='L')
    pdf.ln(15)
    pdf.cell(w=0,h=7,txt="EMERGENCY CONTACT / NEXT OF KIN", border=1, align='C',ln=1)
    pdf.cell(w=40,h=7,txt="RELATIONSHIP", border=1, align='C')
    pdf.cell(w=50,h=7,txt="COMPLETE NAME", border=1, align='C')
    pdf.multi_cell(w=60,h=7,txt="TELEPHONE NUMBER / MOBILE", border=1, align='C')
   # Posicionamos el inicio del contenido
# Después de tus celdas anteriores, ajustamos la posición y alineamos la celda ADDRESS correctamente.

# Mover a la siguiente línea después de ajustar todas las celdas anteriores
# Supongamos que la suma de las anchuras de las columnas anteriores es 160 (ajústalo según sea necesario)
anchura_total_filas_anterior = 160  # Ajusta este valor según las columnas anteriores

# Mover a la siguiente línea después de ajustar todas las celdas anteriores
pdf.ln(max_height)

# Posicionar el cursor en la posición adecuada en el eje X (alineado con la última columna)
pdf.set_x(anchura_total_filas_anterior)

# Dibujar la celda "ADDRESS" alineada con la última columna
pdf.cell(w=40, h=7, txt="ADDRESS", border=1, align='C', ln=1)

# Dibujar la siguiente tabla de datos, asegurando que las celdas se alineen correctamente
for fila in datos:
    for i, (columna, valor) in enumerate(fila.items()):
        pdf.cell(w=anchuras[i], h=8, txt=valor, border=1, align='C')
    pdf.ln(8)  # Saltar a la siguiente línea después de cada fila


# Agregar el título "3.WORK EXPERIENCE ONBOARD"
   
    pdf.ln(5)
    pdf.cell(0, 10, txt='3.WORK EXPERIENCE ONBOARD', align="L")
    pdf.ln(10)
    
    
    anchuras_columnas = [28, 28, 24, 21, 18, 18, 23, 30]  
    altura_fila = [7,7,7,7,14,14,7,7]
    
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
    x_inicial = pdf.get_x()
    y_inicial = pdf.get_y()
    align_type = ['C', 'C', 'C', 'L', 'C', 'L', 'C', 'C']
    pdf.set_xy(x_inicial, y_inicial)
    pdf.set_font('calibri','', 8)
    for i in range(len(titulos_columnas)):
        pdf.multi_cell(w=anchuras_columnas[i], h=altura_fila[i], txt=titulos_columnas[i], align=align_type[i], border=1)
        x_inicial += anchuras_columnas[i]
        pdf.set_xy(x_inicial, y_inicial)
    pdf.ln(14)

    datosNuevos = [
    ['01/01/2023', '01/02/2023', 'Company A', 'Vessel A', '1234567', '5000 / 3000', 'Type A', 'Captain'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
      ['01/01/2023', '01/02/2023', 'Company A', 'Vessel A', '1234567', '5000 / 3000', 'Type A', 'Captain'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
      ['01/01/2023', '01/02/2023', 'Company A', 'Vessel A', '1234567', '5000 / 3000', 'Type A', 'Captain'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
      ['01/01/2023', '01/02/2023', 'Company A', 'Vessel A', '1234567', '5000 / 3000', 'Type A', 'Captain'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
      ['01/01/2023', '01/02/2023', 'Company A', 'Vessel A', '1234567', '5000 / 3000', 'Type A', 'Captain'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
      ['01/01/2023', '01/02/2023', 'Company A', 'Vessel A', '1234567', '5000 / 3000', 'Type A', 'Captain'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
      ['01/01/2023', '01/02/2023', 'Company A', 'Vessel A', '1234567', '5000 / 3000', 'Type A', 'Captain'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
      ['01/01/2023', '01/02/2023', 'Company A', 'Vessel A', '1234567', '5000 / 3000', 'Type A', 'Captain'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
      ['01/01/2023', '01/02/2023', 'Company A', 'Vessel A', '1234567', '5000 / 3000', 'Type A', 'Captain'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
      ['01/01/2023', '01/02/2023', 'Company A', 'Vessel A', '1234567', '5000 / 3000', 'Type A', 'Captain'],
    ['02/01/2023', '02/02/2023', 'Company B', 'Vessel B', '2345678', '6000 / 3500', 'Type B', 'First Officer'],
    
    # Agrega más filas según sea necesario
]

# Dibujar los datos
    nuevaaltura_fila = [7,7,7,7,7,7,7,7]
    for fila in datosNuevos:
        x_inicial = pdf.get_x()
        y_inicial = pdf.get_y()
        for i in range(len(fila)):
            pdf.multi_cell(w=anchuras_columnas[i], h=nuevaaltura_fila[i], txt=fila[i], align=align_type[i], border=1)
            x_inicial += anchuras_columnas[i]
            pdf.set_xy(x_inicial, y_inicial)
        pdf.ln(nuevaaltura_fila[0]) 
    pdf.ln(5)
    pdf.cell(0, 10, txt='4. Personal Documentation / Seafarer Documentation', align='L')
    pdf.ln(10)  


    pdf.cell(w=0, h=7, txt='PERSONAL DOCUMENTATION / SEAFARER DOCUMENTATION', align='C', border=1, ln=1)
    pdf.set_font('Calibri', '', 8)


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
    pdf.set_font('calibri', '', 8)
    pdf.cell(0,10, txt='6. WORK EXPERIENCE ONSHORE', align='L')
    pdf.ln(10)
    pdf.multi_cell(w=30,h=7,txt='DATE ON(MM/DD/YYYY)', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='DATE OFF(MM/DD/YYYY)', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='COMPANY NAME / SHIP-OWNER', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='DUTIES OR RESPONSABILITIES', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='RANK/POSITION', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='REASON FOR LEAVING', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='NAME OF CONTACT PERSON & TELEPHONE NUMBER', align='C', border=1)
    pdf.ln(10)
    pdf.cell(0,10, txt='7. HIGHEST LEVEL OF EDUCATION / OTHER TRAINING OR CERTIFICATE', align='L')
    pdf.ln(10)
    pdf.cell(w=0, h=7,txt='HIGHEST LEVEL OF EDUCATION / OTHER TRAINING OR CERTIFICATE', align='C', border=1)
    pdf.ln(10)
    pdf.multi_cell(w=30,h=7,txt='NAME OF EDUCATION INSTITUTION / TECHNICAL INSTITUTE / UNIVERSITY', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='OBTAINED TITLE OR GRADE', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='DATE ON(MM/DD/YYYY)', align='C', border=1)
    pdf.multi_cell(w=30,h=7,txt='DATE OFF(MM/DD/YYYY)', align='C', border=1)
    pdf.ln(10)
    pdf.cell(0,10, txt='8. VACCINATION BOOK', align='L')
    pdf.ln(10)
    pdf.cell(w=0, h=6,txt='VACCINATION BOOK', align='C', border=1)
    pdf.ln(10)
    pdf.set_font('calibri','',8)
    pdf.cell(w=40,h=6,txt="TYPE OF VACCINE", border=1, align='C')
    pdf.cell(w=40,h=6,txt="COUNTRY", border=1, align='C')
    pdf.cell(w=40,h=6,txt="DOZE", border=1, align='C')
    pdf.multi_cell(w=40,h=3,txt='DATE OF ISSUE\n(MM / DD / YYYY)', align='C', border=1)
    pdf.multi_cell(w=30,h=6,txt='VACCINATION MARK', align='C', border=1)
    pdf.ln(10)
    pdf.cell(0,10, txt='9. SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS', align='L')
    pdf.ln(10)
    pdf.cell(w=110,h=6,txt="SKILLS / RESPONSIBILITIES / LEARNING EXPERIENCE / ACHIEVEMENTS", border=1, align='L')
    pdf.cell(w=40,h=6,txt="YES", border=1, align='C')
    pdf.cell(w=40,h=6,txt="NO", border=1, align='C')
   
    pdf.output('hoja.pdf')

    return jsonify({"message": "PDF generated successfully!"})

if __name__ == "__main__":
    app.run(host='localhost', port=4000)
