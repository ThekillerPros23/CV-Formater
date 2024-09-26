from fpdf import FPDF
from flask import Flask, jsonify, request
from firebase_data import *
from datetime import datetime

app = Flask(__name__)

@app.route('/pdf_render', methods=['GET'])
def pdf_render():
    name = request.args.get('name')
    second_name = request.args.get('second_name')
    lastname = request.args.get('lastname')
    second_lastname = request.args.get('second_lastname')
    date = request.args.get('date')
    nationality = request.args.get('nationality')
    sex = request.args.get('sex')
    civil_status = request.args.get('civil_status')
    timestamp_obj = datetime.fromtimestamp(int(date))
    formatted_timestamp = timestamp_obj.strftime("%Y-%b-%d")
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    
    pdf.set_font('helvetica', '', 16)
    pdf.text(x=60, y=10, txt='SEAFARER APPLICATION FORM')

    
    pdf.set_xy(70, 10)
    pdf.set_font('Arial', '', 12)  
    pdf.cell(30, 10, 'POSITION APPLYING FOR RANK: ')
    
    
    pdf.set_xy(140, 10)
    pdf.set_font('Arial', 'BU', 12)
    pdf.cell(60, 10, 'MESSMAN')

    pdf.set_xy(70, 20)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(60, 10, '1. PERSONAL INFORMATION')

   
    pdf.ln(20)  
    pdf.set_font('Arial', '', 12) 
    pdf.set_xy(50, 40)

    # Define widths for consistent alignment
    cell_width = 50
    big_cell_width = 100
    height = 7

    # Header for Names
    pdf.cell(w=cell_width, h=height, txt='NAME', border=1, align='L')
    pdf.cell(w=cell_width, h=height, txt=str(name), border=1, align='C')
    pdf.cell(w=cell_width, h=height, txt=str(second_name), border=1, align='C', ln=1)

    # Header for Surnames
    pdf.set_xy(50, 47)  
    pdf.cell(w=cell_width, h=height, txt='SURNAMES', border=1, align='L')
    pdf.cell(w=cell_width, h=height, txt=str(lastname), border=1, align='C')
    pdf.cell(w=cell_width, h=height, txt=str(second_lastname), border=1, align='C', ln=1)

    # Date of Birth
    pdf.set_xy(50, 54)  
    pdf.multi_cell(w=cell_width, h=7.5, txt='DATE OF BIRTH\n(YYYY-MM-DD)', border=1, align='C')

    # Fill Date of Birth
    pdf.set_xy(100, 54) 
    pdf.cell(w=big_cell_width, h=15, txt=str(formatted_timestamp), border=1, align='C', ln=1)

    # Nationality
    pdf.set_xy(50, 69)  
    pdf.cell(w=cell_width, h=height, txt='NATIONALITY', border=1, align='L')
    pdf.cell(w=big_cell_width, h=height, txt=str(nationality), border=1, align='C', ln=1)

    # Sex and Civil Status
    pdf.set_xy(50, 76)  
    pdf.cell(w=cell_width, h=7, txt='SEX', border=1, align='L')
    pdf.cell(w=20, h=7, txt=str(sex), border=1, align='C')
    pdf.cell(w=45, h=7, txt='CIVIL STATUS', border=1, align='L')
    pdf.cell(w=35, h=7, txt=str(civil_status), border=1, align='C', ln=1)
    pdf.set_xy(50,100)
    pdf.cell(w=40, h=7, txt='HEIGHY(Ft/in)', border=1, align='L')
    pdf.cell(w=20, h=7, txt=str(sex), border=1, align='C')
    pdf.cell(w=45, h=7, txt='WEIGHT (Lb)', border=1, align='L')
    pdf.cell(w=35, h=7, txt=str(civil_status), border=1, align='C')
    pdf.cell(w=45, h=7, txt='BMI', border=1, align='L')
    pdf.cell(w=35, h=7, txt=str(civil_status), border=1, align='C', ln=1)
    # Guardar el PDF generado
    pdf.output('hoja.pdf')

    return jsonify({"message": "PDF generated successfully!"})

if __name__ == "__main__":
    app.run(host='localhost', port=4000)
 