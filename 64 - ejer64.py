#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
"""
conn = pymysql.connect(host='localhost', user='root', passwd='', db='bd_python', charset = 'utf8')

cur = conn.cursor()

cur.execute( 
            SELECT * FROM prueba
            )

for row in cur:
    print(row) # Lista records o tuplas
"""
#Funcion para conectarse a la base de datos

def run_query(query=''):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='bd_python', charset = 'utf8')  # Conectar a la base de datos
    cursor = conn.cursor()  # Crear un cursor
    cursor.execute(query)  # Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()  # Traer los resultados de un select
        archivo = open("archivos/bd.txt","w")
        for i in range(len(data)):
            archivo.write(str(data[i])+"\n")
        archivo.close()
    else:
        conn.commit()  # Hacer efectiva la escritura de datos
        data = 'Insercion realizada correctamente'

    cursor.close()  # Cerrar el cursor
    conn.close()  # Cerrar la conexión

    return data

#query = "insert into prueba (nombre,apellidos,dni) values ('javi','rodriguez','0223145B')"
#query = "select * from prueba"
query = "update prueba set apellidos = 'perez' where id = 1"
result = run_query(query)
print (result)