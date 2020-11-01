# Master-C7
Almacenamiento e Integracion de Datos

Antes de correr los scripts es necesario que generen (al menos) 200 datos aleatorios para Nombres, Ciudades, Apellidos desde esta pagina: http://www.generatedata.com/?lang=es
Se deben descargar en 'batches' de 100 registros (porque asi es la vida gratis). 

Se deben descargar un total de 6 documentos en Excel (pueden cambiar esto dado que sean mas eficientes que yo al momento de usar el codigo de Python x.X jaja ). 

Dentro de la pagina generatedata, los archivos Excel a ser descargados tienen los siguientes nombres y estructuras

* Nombres_1 => Nombre <STRING>, Apellidos <STRING>
* Nombres_2 => Nombre <STRING>, Apellidos <STRING>
* Apellidos_1 => Apellidos <STRING>
* Apellidos_2 => Apellidos <STRING>
* Datos_1 => DNI <INT>, Cidudad <STRING>, Experiencia Previa <Yes/No>
* Datos_2 => DNI <INT>, Cidudad <STRING>, Experiencia Previa <Yes/No>

He incluido ejemplos de estos archivos dentro del repo para su referencia. 

Una vez que tengan esto nada mas deben asegurarse de descargar los scripts de python, y tenerlos en el mismo folder de los Excel. 

Abrir el script "jobLists.py" y ahi pueden cambiar el listado de <b>*PROFESIONES*</b>
Despues nada mas correr (F5) el script. 
jobLists viene a ser el pseudo-main

PD: por favor no critiquen mucho el codigo, fue realizado on the fly y con sueño jaja 
