# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 01:11:17 2020

@author: Jonathan A. Yepez M.
"""
import requests
from bs4 import BeautifulSoup
import random
#import pandas as pd
#import time

#print("All the libraries have been imported")

#Job site: es.indeed.com


URL="https://es.indeed.com/jobs?q=Ingeniero" #podemos crear un diccionario para tomar URLs

page = requests.get(URL) #conduct the request from the URL

soup = BeautifulSoup(page.content, "html.parser")

a=list(soup.children)
[type(item) for item in a]
html = list(soup.children)[2] #we get the HTML contents
b = list(html.children)
body = b[3] #we retrieve the body from the HTML 
x = soup.find_all('tbody') #in the page there are only two (2) tbody
info = x[1] #we select the 2nd instance of tbody
table = info.find_all('td')[1]
divs = table.find_all('div', class_="jobsearch-SerpJobCard unifiedRow row result") #select all the div elements with specific class. 

def get_divs(profesion):
    URL="https://es.indeed.com/jobs?q="+profesion
    page = requests.get(URL) #conduct the request from the URL
    soup = BeautifulSoup(page.content, "html.parser")
    #a=list(soup.children)
    #[type(item) for item in a]
    #html = list(soup.children)[2] #we get the HTML contents
    #b = list(html.children)
    #body = b[3] #we retrieve the body from the HTML 
    x = soup.find_all('tbody') #in the page there are only two (2) tbody
    info = x[1] #we select the 2nd instance of tbody
    table = info.find_all('td')[1]
    divs = table.find_all('div', class_="jobsearch-SerpJobCard unifiedRow row result") #select all the div elements with specific class. 
    return divs

def get_title(div):
    trabajo=str(div.find_all('h2'))
    tit_html = trabajo.split("title")[3]
    temp_tit = tit_html.split('"')[1].upper()
    return temp_tit

def get_link(div):
    trabajo = str(div.find_all('h2'))
    referencia = trabajo.split("href")
    post_li = referencia[1].split('"')
    direccion = post_li[1].split("?")
    link = "es.indeed.com/ver-oferta?"+direccion[1]
    return link

def get_company(div):
    comp = str(div.find_all(class_='company'))
    beg = comp.split("\n")
    company = beg[-1].split("<")[0]
    return company

def get_loc(div):
    ubi = str(div.find_all(class_='recJobLoc'))
    opts = ubi.split('"')
    temp_loc = opts[3]
    return temp_loc
    
def get_summary(div):
    resu = str(div.find_all(class_='summary'))
    subst = resu.split('">')[-1]
    cuerdas = subst.split("<")
    summary=[]
    for i in range(len(cuerdas)):
        if "/" not in cuerdas[i]:
            summary.append(cuerdas[i])
    summary = " ".join(summary)
    return summary

def get_salary(div):
    try:
        infor = str(div.find_all(class_='salarySnippet'))
        chunk = infor.split(">")[3]
        chunks = chunk.split()
        flag=0
        salary=0
        for i in chunks:
            if "€" in i and flag==0:
                salary = i.replace(".","") #if there is no "." it does not matter
                salary=float(salary[:-1])
                flag=1
        #return salary
    except:
        salary=float(random.randint(12000,48000)) #get random salaries between 12k and 48k
    return salary 

def get_jobs(div_list):
    titles = []
    links = []
    companies = []
    locations = []
    summaries = []
    salaries = []
    for i in range(len(div_list)):
        titles.append(get_title(div_list[i]))
        links.append(get_link(div_list[i]))
        companies.append(get_company(div_list[i]))
        locations.append(get_loc(div_list[i]))
        summaries.append(get_summary(div_list[i]))
        salaries.append(get_salary(div_list[i]))
    
    return titles, links, companies, locations, summaries, salaries    


#TITLES,COMPANIES,LOCATIONS,SUMMARIES,SALARIES = get_jobs(divs)
