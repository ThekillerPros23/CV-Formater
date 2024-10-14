from fpdf import FPDF
from flask import Flask, jsonify,Response, request
from datetime import datetime
from applications import *
import io
import requests
from skills import *
from formats.hotel_staff import *
from formats.messman import * 
from formats.ab_os import *
from formats.bosun import *
from formats.cook import *
import json
from formats.oiler import *
from formats.fitter import *
from formats.officer import *
database = FirebaseData()


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
        self.cell(0, 3.5, 'F-PMSSA-01', ln=True, align='R')

        # Revisión
        self.set_x(-60)
        self.cell(0, 3.5, 'Revisión: 03', ln=True, align='R')

        # Fecha
        self.set_x(-60)
        self.cell(0, 3, 'Fecha: 17 de mayo de 2022', ln=True, align='R')

        # Número de página
        self.set_x(-30)
        page_text = f'Página {self.page_no()} de {{nb}}'
        self.cell(0, 3, page_text, ln=True, align='R')
def dividir_texto(texto, pdf, ancho_celda):
    # Dividir el texto en palabras
    palabras = texto.split(' ')
    lineas = []
    linea_actual = ''
    
    for palabra in palabras:
        # Probar si la palabra cabe en la línea actual
        if pdf.get_string_width(linea_actual + palabra) < ancho_celda:
            linea_actual += palabra + ' '
        else:
            # Si no cabe, agregar la línea actual a la lista y comenzar una nueva
            lineas.append(linea_actual.strip())
            linea_actual = palabra + ' '
    
    # Agregar la última línea
    if linea_actual:
        lineas.append(linea_actual.strip())
    
    return lineas
app = Flask(__name__)

@app.route('/pdf_render/applications', methods=['GET','POST'])
def pdf_render():
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_font("NotoEmoji", "", "NotoColorEmoji-Regular.ttf", uni=True)
    pdf.add_font('calibri', '', 'calibri.ttf', uni=True)
    pdf.add_font('calibri', 'I','calibrii.ttf',uni=True)
    pdf.add_font('calibri', 'BU','calibri.ttf',uni=True)
    pdf.add_font('calibri', 'B','calibrib.ttf',uni=True)
    formatId = request.args.get('formatId')
    uid = request.args.get('id')
    version = request.args.get('version')
    print(uid)
    print(version)
    #data = requests.get("https://bd-my-sql.vercel.app/positions/")
    #datos = data.json()
 
    print(database.marine_position(uid))
    if int(formatId) == 1:
        hotel = HotelStaff()
        hotel.format_hotel(pdf, database, uid, version) 
        
    elif int(formatId) == 2:
        ab_os = Ab_Os()
        ab_os.format_ab_os(pdf,database,uid, version)
    elif int(formatId) == 3:
        cook = Cook()
        cook.format_cook()
    elif int(formatId) == 4:
        bosun = Bosun()
        bosun.format_bosun()
    elif int(formatId) == 5:
        oiler = Oiler()
        oiler.format_oiler(pdf,database, uid, version)
    elif int(formatId) == 6:
        messman = Messman()
        messman.format_messman(pdf,database, uid, version)
    elif int(formatId) == 7:
        fitter = Fitter()
        fitter.format_fitter(pdf,database, uid, version)
    elif int(formatId) == 8:
        pass
    
    pdf_buffer = io.BytesIO()

    # Generar el contenido del PDF como cadena
    pdf_output = pdf.output(dest='S').encode('latin1')  # 'S' significa 'return as string'
    
    # Escribir el contenido en el buffer
    pdf_buffer.write(pdf_output)
    
    # Colocamos el cursor al inicio del buffer para que se pueda leer
    pdf_buffer.seek(0)

    # Devolver el PDF como respuesta HTTP con el tipo de contenido adecuado
    return Response(pdf_buffer, mimetype='application/pdf', headers={
        'Content-Disposition': 'inline'  
    })
    
@app.route('/pdf_render/seafarers', methods=['GET','POST'])
def pdf_render_seafarers():
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_font("NotoEmoji", "", "NotoColorEmoji-Regular.ttf", uni=True)
    pdf.add_font('calibri', '', 'calibri.ttf', uni=True)
    pdf.add_font('calibri', 'I','calibrii.ttf',uni=True)
    pdf.add_font('calibri', 'BU','calibri.ttf',uni=True)
    pdf.add_font('calibri', 'B','calibrib.ttf',uni=True)
    uid = request.args.get('id')
    version = request.args.get('version')
    print(uid)
    print(version)
  
    print(database.marine_position(uid))
    for data_enchange in datos:
        if int(data_enchange["Id"]) == int(database.marine_position(uid)):
            if int(data_enchange["CVFormatId"]) == 1:
                hotel = HotelStaff()
                hotel.format_hotel(pdf, database, uid, version) 
                
            elif int(data_enchange["CVFormatId"]) == 2:
                ab_os = Ab_Os()
                ab_os.format_ab_os(pdf,database,uid, version)
            elif int(data_enchange["CVFormatId"]) == 3:
                cook = Cook()
                cook.format_cook()
            elif int(data_enchange["CVFormatId"]) == 4:
                bosun = Bosun()
                bosun.format_bosun()
            elif int(data_enchange["CVFormatId"]) == 5:
                oiler = Oiler()
                oiler.format_oiler(pdf,database, uid, version)
            elif int(data_enchange["CVFormatId"]) == 6:
                messman = Messman()
                messman.format_messman(pdf,database, uid, version)
            elif int(data_enchange["CVFormatId"]) == 7:
                fitter = Fitter()
                fitter.format_fitter(pdf,database, uid, version)
            elif int(data_enchange["CVFormatID"]) == 8:
                pass
    pdf_buffer = io.BytesIO()

    # Generar el contenido del PDF como cadena
    pdf_output = pdf.output(dest='S').encode('latin1')  # 'S' significa 'return as string'
    
    # Escribir el contenido en el buffer
    pdf_buffer.write(pdf_output)
    
    # Colocamos el cursor al inicio del buffer para que se pueda leer
    pdf_buffer.seek(0)

    # Devolver el PDF como respuesta HTTP con el tipo de contenido adecuado
    return Response(pdf_buffer, mimetype='application/pdf', headers={
        'Content-Disposition': 'inline'  
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)


