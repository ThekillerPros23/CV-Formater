from fpdf import FPDF
from flask import Flask, jsonify,Response, request
from datetime import datetime
from applications import *
import io
import requests
from skills import *
from formatsApplication.hotel_staff import *
from formatsApplication.messman import * 
from formatsApplication.ab_os import *
from formatsApplication.bosun import *
from formatsApplication.cook import *
import json
from formatsApplication.oiler import *
from formatsApplication.fitter import *
from formatsApplication.officer import *

from formatsSeafarers.hotel_staff import *
from formatsSeafarers.messman import * 
from formatsSeafarers.ab import *
from formatsSeafarers.bosun import *
from formatsSeafarers.cook import *
from formatsSeafarers.oiler import *
from formatsSeafarers.fitter import *
from formatsSeafarers.officer import *



from seafares import *
databaseApplication = FirebaseDataApplication()
databaseSeafarers = FirebaseDataSeafarers()

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
    
    pdf.add_font('calibri', '', 'calibri.ttf', uni=True)
    pdf.add_font('calibri', 'I','calibrii.ttf',uni=True)
    pdf.add_font('calibri', 'BU','calibri.ttf',uni=True)
    pdf.add_font('calibri', 'B','calibrib.ttf',uni=True)
    formatId = request.args.get('formatId')
    uid = request.args.get('id')
    version = request.args.get('version')
    footer_data = {}
    if int(formatId) == 1:
        hotel = HotelStaffApplication()
        hotel.format_hotel(pdf, databaseApplication, uid) 
        
    elif int(formatId) == 2:
        ab_os = Ab_OsApplication()
        ab_os.format_ab_os(pdf,databaseApplication,uid)
    elif int(formatId) == 3:
        cook = CookApplication()
        cook.format_cook(pdf, databaseApplication, uid)
    elif int(formatId) == 4:
        bosun = BosunApplication()
        bosun.format_bosun(pdf,databaseApplication, uid)
    elif int(formatId) == 5:
        oiler = OilerApplication()
        oiler.format_oiler(pdf,databaseApplication, uid)
    elif int(formatId) == 6:
        messman = MessmanApplication()
        messman.format_messman(pdf,databaseApplication, uid)
    elif int(formatId) == 7:
        fitter = FitterApplication()
        fitter.format_fitter(pdf,databaseApplication, uid)
    elif int(formatId) == 8:
        officer = OfficerApplication()
        officer.format_officer(pdf,databaseApplication,uid)
    
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
    pdf.add_font('calibri', '', 'calibri.ttf', uni=True)
    pdf.add_font('calibri', 'I','calibrii.ttf',uni=True)
    pdf.add_font('calibri', 'BU','calibri.ttf',uni=True)
    pdf.add_font('calibri', 'B','calibrib.ttf',uni=True)
    uid = request.args.get('id')
    formatId = request.args.get('formatId')
 
    if int(formatId) == 1:

        hotel = HotelStaffSeafarers()
        hotel.format_hotel(pdf, databaseSeafarers, uid) 
        
    elif int(formatId) == 2:
     
        ab_os = Ab_OsSeafarers()
        ab_os.format_ab_os(pdf,databaseSeafarers,uid)
      
    elif int(formatId) == 3:
        cook = CookSeafarers()
        cook.format_cook()
    elif int(formatId) == 4:
        bosun = BosunSeafarers()
        bosun.format_bosun()
    elif int(formatId) == 5:
        oiler = OilerSeafarers()
        oiler.format_oiler(pdf,databaseSeafarers, uid)
    elif int(formatId) == 6:
        messman = MessmanSeafarers()
        messman.format_messman(pdf,databaseSeafarers, uid)
    elif int(formatId) == 7:
        fitter = FitterSeafarers()
        fitter.format_fitter(pdf,databaseSeafarers, uid)
    elif int(formatId) == 8:
        officer = OfficerSeafarers()
        officer.format_officer(pdf,databaseSeafarers,uid)
    
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


