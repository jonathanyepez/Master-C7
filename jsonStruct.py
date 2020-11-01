# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 09:58:17 2020

@author: Jonathan A. Yepez M. 
"""
#import any relevant libraries
import datetime
import random
#Generate JSON structure

def portal():
    return '"Portal_Web":"Indeed España",'

letra=["A","C","G"]

def usuario(pandas_row):
    string = '"Usuario":{'
    dni = '"DNI":"'+str(pandas_row['DNI'])+random.choice(letra)+'",'
    nombre = '"Nombre":"'+pandas_row['Nombre ']+'",'
    apellidos = '"Apellidos":"'+pandas_row['Apellidos_x']+" "+pandas_row['Apellidos_y']+'",'
    email = '"email":"'+pandas_row['email']+'",'
    ciudad_ori = '"Ciudad_Origen":"'+pandas_row['Ciudad']+'"},'
    string = string + dni + nombre + apellidos + email + ciudad_ori
    return string

#Para fechas:
start_date = datetime.date(2020,1,1)
end_date = datetime.date(2020,12,31)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
 
def oferta(title, summary, salary, city, company):
    string = '"Oferta":{'
    titulo = '"Titulo":"'+title+'",'
    resumen = '"Resumen":"'+summary+'",'
    sueldo = '"Sueldo":'+str(salary)+','
    ciudad_dest = '"Ciudad_Destino":"'+city+'",'
    fecha_temp = start_date + datetime.timedelta(days=random_number_of_days)
    fecha_inicio = '"Fecha_Inicio":{"$date":"'+str(fecha_temp)+'"},'
    empresa = '"Empresa":"'+company+'"},'
    string = string + titulo + resumen + sueldo + ciudad_dest + fecha_inicio + empresa
    return string


tipos_contrato=["indefinido","por servicio", "eventual", "de interinidad", "de relevo", "de formacion", "practicas"] #EDITABLE
skills=["adaptabilidad","análisis","creatividad","comunicación","compromiso","control","tolerancia","flexibilidad",
        "independencia","iniciativa","liderazgo","organización","tenacidad","trabajo en equipo"] #EDITABLE

def caract(exper): #experiencia is a value from pandas_row though
    string = '"Caracteristicas":{'
    temp_reqs = str(random.sample(skills,3))
    reqs = '"Requisitos":'+temp_reqs.replace("'",'"')+','
    temp_exp = "Si"
    if exper == "No":
        temp_exp=exper
    experiencia = '"Experiencia_Previa":"'+temp_exp+'",'
    contrato = '"Tipo_Contrato":"'+random.choice(tipos_contrato)+'"},'
    string = string + reqs + experiencia + contrato
    return string
    
def enlace(link): #from the list LINKS
    return '"Enlace":"'+link+'"'

def jobJSON(user, site, offer, chars, link):
    string = '{'+user+site+offer+chars+link+'}'
    return string
