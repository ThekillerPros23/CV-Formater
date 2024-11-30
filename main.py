from fpdf import FPDF
from flask import Flask, jsonify,Response, request,make_response
from datetime import datetime
from applications import *
import io
import requests

from formatsApplication.hotel_staff import *
from formatsApplication.messman import * 
from formatsApplication.ab import *
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

class HotelStaffPDF(FPDF):
    def header(self):
        self.set_font('calibri', 'B', 24)
        self.multi_cell(0, 10, "LOGISTIC INTERNATIONAL SERVICES \n CORPORATION ", align='C')
        if self.page_no() == 1:
            self.image("LOGISTIC-SinFondo.png", 173, 8, 32)
        else:
            self.image("LOGISTIC-SinFondo.png", 0, 11, 35)

    def footer(self):
        self.set_text_color(0, 0, 0)
        self.set_y(-20)
        self.set_font('calibri', 'I', 9)
        self.set_x(-60)
        self.cell(0, 3.5, 'Code: F-PMSSA-01', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3.5, 'Revision: 05', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3, 'Date: November 07 2024', ln=True, align='R')
        self.set_x(-30)
        self.cell(0, 3, f'Page {self.page_no()} of {{nb}}', ln=True, align='R')

class AbPDF(FPDF):
    def header(self):
        self.set_font('calibri', 'B', 26)
        self.multi_cell(0, 10, "LOGISTIC INTERNATIONAL SERVICES \n CORPORATION ", align='C')
        if self.page_no() == 1:
            self.image("LOGISTIC-SinFondo.png", 173, 8, 32)
        else:
            self.image("LOGISTIC-SinFondo.png", 0, 11, 35)

    def footer(self):
        self.set_text_color(0, 0, 0)
        self.set_y(-20)
        self.set_font('calibri', 'I', 9)
        self.set_x(-60)
        self.cell(0, 3.5, 'Code: F-PMSSA-01-C', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3.5, 'Revision: 02', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3, 'Date: November 07 2024', ln=True, align='R')
        self.set_x(-30)
        self.cell(0, 3, f'Page {self.page_no()} of {{nb}}', ln=True, align='R')

class CookPDF(FPDF):
    def header(self):
        self.set_font('calibri', 'B', 26)
        self.multi_cell(0, 10, "LOGISTIC INTERNATIONAL SERVICES \n CORPORATION ", align='C')
        if self.page_no() == 1:
            self.image("LOGISTIC-SinFondo.png", 173, 8, 32)
        else:
            self.image("LOGISTIC-SinFondo.png", 0, 11, 35)

    def footer(self):
        self.set_text_color(0, 0, 0)
        self.set_y(-20)
        self.set_font('calibri', 'I', 9)
        self.set_x(-60)
        self.cell(0, 3.5, 'Code: F-PMSSA-01-B', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3.5, 'Revision: 02', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3, 'Date: November 07 2024', ln=True, align='R')
        self.set_x(-30)
        self.cell(0, 3, f'Page {self.page_no()} of {{nb}}', ln=True, align='R')

class BosunPDF(FPDF):
    def header(self):
        self.set_font('calibri', 'B', 26)
        self.multi_cell(0, 10, "LOGISTIC INTERNATIONAL SERVICES \n CORPORATION ", align='C')
        if self.page_no() == 1:
            self.image("LOGISTIC-SinFondo.png", 173, 8, 32)
        else:
            self.image("LOGISTIC-SinFondo.png", 0, 11, 35)

    def footer(self):
        self.set_text_color(0, 0, 0)
        self.set_y(-20)
        self.set_font('calibri', 'I', 9)
        self.set_x(-60)
        self.cell(0, 3.5, 'Code: F-PMSSA-01-D', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3.5, 'Revision: 02', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3, 'Date: November 07 2024', ln=True, align='R')
        self.set_x(-30)
        self.cell(0, 3, f'Page {self.page_no()} of {{nb}}', ln=True, align='R')
class OilerPDF(FPDF):
    def header(self):
        self.set_font('calibri', 'B', 26)
        self.multi_cell(0, 10, "LOGISTIC INTERNATIONAL SERVICES \n CORPORATION ", align='C')
        if self.page_no() == 1:
            self.image("LOGISTIC-SinFondo.png", 173, 8, 32)
        else:
            self.image("LOGISTIC-SinFondo.png", 0, 11, 35)

    def footer(self):
        self.set_text_color(0, 0, 0)
        self.set_y(-20)
        self.set_font('calibri', 'I', 9)
        self.set_x(-60)
        self.cell(0, 3.5, 'Code: F-PMSSA-01-G', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3.5, 'Revision: 02', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3, 'Date: November 07 2024', ln=True, align='R')
        self.set_x(-30)
        self.cell(0, 3, f'Page {self.page_no()} of {{nb}}', ln=True, align='R')

class MessmanPDF(FPDF):
    def header(self):
        self.set_font('calibri', 'B', 26)
        self.multi_cell(0, 10, "LOGISTIC INTERNATIONAL SERVICES \n CORPORATION ", align='C')
        if self.page_no() == 1:
            self.image("LOGISTIC-SinFondo.png", 173, 8, 32)
        else:
            self.image("LOGISTIC-SinFondo.png", 0, 11, 35)

    def footer(self):
        self.set_text_color(0, 0, 0)
        self.set_y(-20)
        self.set_font('calibri', 'I', 9)
        self.set_x(-60)
        self.cell(0, 3.5, 'Code: F-PMSSA-01-E', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3.5, 'Revision: 02', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3, 'Date: November 07 2024', ln=True, align='R')
        self.set_x(-30)
        self.cell(0, 3, f'Page {self.page_no()} of {{nb}}', ln=True, align='R')

class FitterPDF(FPDF):
    def header(self):
        self.set_font('calibri', 'B', 26)
        self.multi_cell(0, 10, "LOGISTIC INTERNATIONAL SERVICES \n CORPORATION ", align='C')
        if self.page_no() == 1:
            self.image("LOGISTIC-SinFondo.png", 173, 8, 32)
        else:
            self.image("LOGISTIC-SinFondo.png", 0, 11, 35)

    def footer(self):
        self.set_text_color(0, 0, 0)
        self.set_y(-20)
        self.set_font('calibri', 'I', 9)
        self.set_x(-60)
        self.cell(0, 3.5, 'Code: F-PMSSA-01-F', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3.5, 'Revision: 02', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3, 'Date: November 07 2024', ln=True, align='R')
        self.set_x(-30)
        self.cell(0, 3, f'Page {self.page_no()} of {{nb}}', ln=True, align='R')

class OfficerPDF(FPDF):
    def header(self):
        self.set_font('calibri', 'B', 26)
        self.multi_cell(0, 10, "LOGISTIC INTERNATIONAL SERVICES \n CORPORATION ", align='C')
        if self.page_no() == 1:
            self.image("LOGISTIC-SinFondo.png", 173, 8, 32)
        else:
            self.image("LOGISTIC-SinFondo.png", 0, 11, 35)

    def footer(self):
        self.set_text_color(0, 0, 0)
        self.set_y(-20)
        self.set_font('calibri', 'I', 9)
        self.set_x(-60)
        self.cell(0, 3.5, 'Code: F-PMSSA-01-A', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3.5, 'Revision: 02', ln=True, align='R')
        self.set_x(-60)
        self.cell(0, 3, 'Date: November 07 2024', ln=True, align='R')
        self.set_x(-30)
        self.cell(0, 3, f'Page {self.page_no()} of {{nb}}', ln=True, align='R')


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
    uid = request.args.get('id')
    formatId = request.args.get('formatId')
    version = request.args.get("version")
    if int(formatId) == 1:
        pdf = HotelStaffPDF(orientation='P', unit='mm', format='A4')

    elif int(formatId) == 2:
        pdf = AbPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 3:
        pdf = CookPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 4:
        pdf = BosunPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 5:
            pdf = OilerPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 6:
            pdf = MessmanPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 7:
            pdf = FitterPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 8:
            pdf = OfficerPDF(orientation='P', unit='mm', format='A4')

    pdf.add_font('calibri', '', 'calibri.ttf', uni=True)
    pdf.add_font('calibri', 'I','calibrii.ttf',uni=True)
    pdf.add_font('calibri', 'BU','calibri.ttf',uni=True)
    pdf.add_font('calibri', 'B','calibrib.ttf',uni=True)

    if int(formatId) == 1:
        #from 
        hotel = HotelStaffApplication()
        hotel.format_hotel(pdf, databaseApplication, uid,version) 
        
    elif int(formatId) == 2:
     
        ab_os = Ab_OsSeafarers()
        ab_os.format_ab_os(pdf,databaseApplication,uid,version)
      
    elif int(formatId) == 3:
        cook = CookSeafarers()
        cook.format_cook(pdf,databaseApplication,uid,version)
    elif int(formatId) == 4:
        bosun = BosunSeafarers()
        bosun.format_bosun(pdf,databaseApplication,uid,version)
    elif int(formatId) == 5:
        oiler = OilerSeafarers()
        oiler.format_oiler(pdf,databaseApplication, uid,version)
    elif int(formatId) == 6:
        messman = MessmanSeafarers()
        messman.format_messman(pdf,databaseApplication, uid,version)
    elif int(formatId) == 7:
        fitter = FitterSeafarers()
        fitter.format_fitter(pdf,databaseApplication, uid,version)
    elif int(formatId) == 8:
        officer = OfficerSeafarers()
        officer.format_officer(pdf,databaseApplication,uid,version)
    
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
    uid = request.args.get('id')
    formatId = request.args.get('formatId')
 
    if int(formatId) == 1:
        pdf = HotelStaffPDF(orientation='P', unit='mm', format='A4')

    elif int(formatId) == 2:
        pdf = AbPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 3:
        pdf = CookPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 4:
        pdf = BosunPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 5:
            pdf = OilerPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 6:
            pdf = MessmanPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 7:
            pdf = FitterPDF(orientation='P', unit='mm', format='A4')
    elif int(formatId) == 8:
            pdf = OfficerPDF(orientation='P', unit='mm', format='A4')

    pdf.add_font('calibri', '', 'calibri.ttf', uni=True)
    pdf.add_font('calibri', 'I','calibrii.ttf',uni=True)
    pdf.add_font('calibri', 'BU','calibri.ttf',uni=True)
    pdf.add_font('calibri', 'B','calibrib.ttf',uni=True)

    if int(formatId) == 1:
        #from 
        hotel = HotelStaffSeafarers()
        hotel.format_hotel(pdf, databaseSeafarers, uid) 
        
    elif int(formatId) == 2:
     
        ab_os = Ab_OsSeafarers()
        ab_os.format_ab_os(pdf,databaseSeafarers,uid)
      
    elif int(formatId) == 3:
        cook = CookSeafarers()
        cook.format_cook(pdf,databaseSeafarers,uid)
    elif int(formatId) == 4:
        bosun = BosunSeafarers()
        bosun.format_bosun(pdf,databaseSeafarers,uid)
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
    app.run(host='0.0.0.0',port=4000)


