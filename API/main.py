
from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel
from fastapi import HTTPException,status


class Mensaje(BaseModel):
	mensaje:str

class Contactos(BaseModel):
	id_contacto:int
	nombre:str
	email:str
	telefono:str

class Contacto_post(BaseModel):
	nombre:str
	email:str
	telefono:str

description= """
	#Contactos Api REST
	API para crear un CRUD
	de la tabla contactos
	"""
app= FastAPI(
	title="contactos API REST",
	description=description,
	version= "0.1",
	contact= {"name":"Jesus Yael",
		"email":"1721110698@utectulancingo.edu.mx"
	}
			
)

@app.get(
	"/",
	response_model= Mensaje,
	status_code= status.HTTP_202_ACCEPTED,
	summary="endpoint principal",
	description="regresar mensaje de bienvenida",
)
async def read_root():
	response={"mensaje":"version 0.1"}
	return response

@app.get(
	"/contactos/",
	response_model= List[Contactos],
	status_code= status.HTTP_202_ACCEPTED,
	summary="lista de contactos",
	description="endpoint que regresara un array con todos los contactos",
)
async def get_contactos():
	try:
		with sqlite3.connect("API/sql/contactos.db") as connection:
			connection.row_factory=sqlite3.Row
			cursor=connection.cursor()
			cursor.execute("SELECT id_contacto,nombre,email,telefono FROM contactos;")
			response=cursor.fetchall()
			return response
	except Exception as error:
		print(f"Error interno: {error.args}")
		raise HTTPException(
		status_code=status.HTTP_400_BAD_REQUEST,
		detail="Error al consultar los datos"
		)

@app.get(
	"/contactos/{id_contacto}",
	response_model= Contactos,
	status_code= status.HTTP_202_ACCEPTED,
	summary="lista de contactos",
	description="endpoint que regresara un array con el contacto ingresado",
)		

async def get_contacto_id(id_contacto: int):
	try:
		with sqlite3.connect("API/sql/contactos.db") as connection:
			connection.row_factory=sqlite3.Row
			cursor=connection.cursor()
			sql=("SELECT id_contacto,nombre,email,telefono FROM contactos WHERE id_contacto= ?;")
			values=(id_contacto,)
			cursor.execute(sql,values)
			response=cursor.fetchone()
			return response
	except Exception as error:
		print(f"Error interno: {error.args}")
		raise HTTPException(
		status_code=status.HTTP_400_BAD_REQUEST,
		detail="Error al consultar los datos"
		)

@app.post(
	"/contactos/",
	response_model=Mensaje,
	status_code= status.HTTP_202_ACCEPTED,
	summary="lista de contactos",
	description="endpoint que ingresara un nuevo contacto",
)		

async def get_contacto_post(Contactos: Contacto_post):
	try:
		with sqlite3.connect("API/sql/contactos.db") as connection:
			connection.row_factory=sqlite3.Row
			cursor=connection.cursor()
			sql=("INSERT INTO contactos VALUES (NULL, ?, ?, ?);")
			values= (Contactos.nombre, Contactos.email, Contactos.telefono, )
			cursor.execute(sql,values)
			response={"mensaje":"Contacto registrado"}
			return response
	except Exception as error:
		print(f"Error interno: {error.args}")
		raise HTTPException(
		status_code=status.HTTP_400_BAD_REQUEST,
		detail="Error al insertar contacto"
		)


