# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 22:03:50 2020

@author: Jonathan A. Yepez M. 
"""

#Import relevant libraries and scripts
import mainScrapper
import jsonStruct
import pandas as pd
import random
#Initialize all important variables

profesiones=["Profesor","Medico","Abogado","Constructor"] #EDITABLE

TITLES=[]
LINKS=[]
COMPANIES=[]
LOCATIONS=[]
SUMMARIES=[]
SALARIES=[]

for profesion in profesiones:
    divs = mainScrapper.get_divs(profesion) #get the divs for the profession we have selected. 
    titles,links,companies,locations,summaries,salaries = mainScrapper.get_jobs(divs)
    TITLES.extend(titles)
    LINKS.extend(links)
    COMPANIES.extend(companies)
    LOCATIONS.extend(locations)
    SUMMARIES.extend(summaries)
    SALARIES.extend(salaries)
    
for i in range(len(COMPANIES)):
    if COMPANIES[i]=="[]":
        COMPANIES[i]="N.A." #EDITABLE
        
#========================================================================================
#Extract the data randomly generated from the internet (Names, Cities, DNI's, etc)

df_d1 = pd.read_excel("Datos_1.xlsx", encoding='iso-8859-1') #read excel file
df_d2 = pd.read_excel("Datos_2.xlsx", encoding='iso-8859-1') #read excel file
df_datos = df_d1.append(df_d2[0:50], ignore_index=True) #combine and get 150 rows
del df_d1, df_d2 #delete the first dataframes

df_n1 = pd.read_excel("Nombres_1.xlsx", encoding='iso-8859-1')
df_n2 = pd.read_excel("Nombres_2.xlsx", encoding='iso-8859-1')
df_nombres = df_n1.append(df_n2[0:50], ignore_index=True)
del df_n1, df_n2

df_a1 = pd.read_excel("Apellidos_1.xlsx", encoding='iso-8859-1')
df_a2 = pd.read_excel("Apellidos_2.xlsx", encoding='iso-8859-1')
df_apellido = df_a1.append(df_a2[0:50], ignore_index=True)
del df_a1, df_a2

def get_email(nombre, apellido):
    dominios=["@gmail.com","@hotmail.com","@outlook.com","@yahoo.com"] #EDITABLE
    email = nombre[0:2].lower()+apellido.lower()+random.choice(dominios)
    return email

emails=[]
for i in range(150): #number of rows in the current dataframe (numero de registros)
    name= df_nombres.iloc[i,0]
    surname= df_nombres.iloc[i,1]
    emails.append(get_email(name, surname))

df_index = pd.merge(df_datos['DNI'], df_nombres, right_index=True, left_index=True)
df_index = pd.merge(df_index, df_apellido, right_index=True, left_index=True) #aca se crea Apellidos_x y Apellidos_y en el df
df_index = pd.merge(df_index, pd.DataFrame(emails, columns=["email"]), right_index=True, left_index=True)
df_index = pd.merge(df_index, df_datos[['Ciudad','Experiencia Previa']], right_index=True, left_index=True)

change_names = df_index.sample(random.randint(5,15)).index
df_index.loc[change_names,'Nombre ']="Isabel"
df_index.loc[change_names,'Apellidos_x']="Cabrerizo"
df_index.loc[change_names,'Apellidos_y']="Alonso"

print("number of entries by Isabel:", len(change_names))

change_cities = df_index.sample(random.randint(20,50)).index
df_index.loc[change_cities,'Ciudad']="Barcelona"

print("numnber of entries with city of origin=Barcelona:", len(change_cities))

change_dni = df_index.sample(random.randint(10,30)).index
df_index.loc[change_dni,'DNI']=23454543

del df_datos, df_nombres, df_apellido, emails


#=========================================================================================
JOBS=[] #save relevant info in a list

if (len(TITLES)<=len(df_index)):
    entries = len(TITLES)
else:
    entires = len(df_index)

for i in range(entries):
    user = jsonStruct.usuario(df_index.loc[i])
    site = jsonStruct.portal()
    summy = SUMMARIES[i].replace("\n","").replace(">li","").replace(">b","")
    summy = summy.replace(">","").replace("\\","")
    offer = jsonStruct.oferta(TITLES[i],summy,SALARIES[i],LOCATIONS[i],COMPANIES[i])
    chars = jsonStruct.caract(df_index.loc[i]['Experiencia Previa'])
    link = jsonStruct.enlace(LINKS[i])
    job = jsonStruct.jobJSON(user, site, offer, chars, link)
    JOBS.append(job)

#Create JSON File to be used in MongoDB

f = open("data.json","a", encoding='utf-8') #we create a JSON file called 'data' #EDITABLE
f.write("[\n") #specify the beginning of the list of documents
    
for j in range(len(JOBS)-1): #use all the elements from JOBS but the last one
    try:
        f.write(JOBS[j])
        f.write(",\n") #use the coma to separate each document
    except:
        print("error in job #"+str(i))
f.write(JOBS[-1]) #obtain the last element from the JOBS list
f.write("\n")
f.write("]")#finish the list of documents in the JSON file
f.close() #close the file
#=========================================================================================

