# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:24:37 2023

@author: Alumno
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")

# En una cadena guardaremos el script de creacion de la tabla pais
tabla_pais = """CREATE TABLE pais(
                    idpais INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT UNIQUE,
                    estado TEXT
                    )
            """
cursor = conexion.cursor()
cursor.execute(tabla_pais)

conexion.close()
