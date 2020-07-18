from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

conexion=sqlite3.connect("base_datos.db")
c=conexion.cursor()

class Vendido(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		#self.geometry("600x600")
		self.title("Ganancias")
		self.resizable(False,False)


	#cuadro de ganancias

	#crear espacio para mostrar vendidos
		self.vendidos=Frame(self)
		self.vendidos.pack()

		self.label=Label(self.vendidos,text="Libros vendidos").pack()

		self.boton=Button(self.vendidos,text="Mostrar libros vendidos",command=self.mostrar_vendidos).pack()

		self.tabla=ttk.Treeview(self.vendidos, columns=('Nombre','Autor','Precio','Cantidad','Mes'))
		
		self.tabla.heading('#0',text="",anchor='w')
		self.tabla.column('#0',anchor='center',width=5,stretch=NO)
		
		self.tabla.heading('#1',text='Nombre', anchor="w")
		self.tabla.column('#1',anchor='center',width=230)
		
		self.tabla.heading('#2',text='Autor', anchor=CENTER)
		self.tabla.column('#2',anchor='center',width=180)
		
		self.tabla.heading('#3',text='Precio', anchor=CENTER)
		self.tabla.column('#3',anchor='center',width=60)

		self.tabla.heading('#4',text='Cantidad', anchor=CENTER)
		self.tabla.column('#4',anchor='center',width=60)

		self.tabla.heading('#5',text='Mes', anchor=CENTER)
		self.tabla.column('#5',anchor='center',width=100)
		self.tabla.pack()

	#espacio mostrar ganancias
		self.espacio=Frame(self)
		self.espacio.pack()

		self.boton_grafico=Button(self.espacio,text="Mostrar ganancias",command=self.ganancias)
		self.boton_grafico.pack()

		#Tabla ganancias
		self.tabla_ganancias=ttk.Treeview(self.espacio, columns=('Mes','Ganancia'))
		
		self.tabla_ganancias.heading('#0',text="",anchor='w')
		self.tabla_ganancias.column('#0',anchor='center',width=5,stretch=NO)
		
		self.tabla_ganancias.heading('#1',text='Mes', anchor="w")
		self.tabla_ganancias.column('#1',anchor='center',width=100)
		
		self.tabla_ganancias.heading('#2',text='Cantidad', anchor="w")
		self.tabla_ganancias.column('#2',anchor='center',width=70)

		self.tabla_ganancias.pack()


	

	
	def ganancias(self):
		#leer informacion de vendidos
		libros_vendidos=c.execute("SELECT * FROM vendidos").fetchall()
		
		ganancia_enero=0
		ganancia_febrero=0
		ganancia_marzo=0
		ganancia_abril=0
		ganancia_mayo=0
		ganancia_junio=0
		ganancia_julio=0
		ganancia_agosto=0
		ganancia_septiembre=0
		ganancia_octubre=0
		ganancia_noviembre=0
		ganancia_diciembre=0	

		#reunir cantidad total por mes e INSERTAR en la base de datos

		for fila in libros_vendidos:
			mes=fila[4]
			precio=int(fila[2])
			cantidad=int(fila[3])
			ganancia_libro=precio*cantidad

			if mes=="Enero":
				ganancia_enero=ganancia_enero+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_enero,mes,))
				conexion.commit()

			if mes=="Febrero":
				ganancia_febrero=ganancia_febrero+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_febrero,mes,))
				conexion.commit()

			if mes=="Marzo":
				ganancia_marzo=ganancia_marzo+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_marzo,mes,))
				conexion.commit()

			if mes=="Abril":
				ganancia_abril=ganancia_abril+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_abril,mes,))
				conexion.commit()

			if mes=="Mayo":
				ganancia_mayo=ganancia_mayo+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_mayo,mes,))
				conexion.commit()

			if mes=="Junio":
				ganancia_junio=ganancia_junio+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_junio,mes,))
				conexion.commit()

			if mes=="Julio":
				ganancia_julio=ganancia_julio+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_julio,mes,))
				conexion.commit()

			if mes=="Agosto":
				ganancia_agosto=ganancia_agosto+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_agosto,mes,))
				conexion.commit()
			
			if mes=="Septiembre":
				ganancia_septiembre=ganancia_septiembre+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_septiembre,mes,))
				conexion.commit()
			
			if mes=="Octubre":
				ganancia_octubre=ganancia_octubre+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_octubre,mes,))
				conexion.commit()
			
			if mes=="Noviembre":
				ganancia_noviembre=ganancia_noviembre+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_noviembre,mes,))
				conexion.commit()
			
			if mes=="Diciembre":
				ganancia_diciembre=ganancia_diciembre+ganancia_libro
				c.execute('UPDATE ganancias SET Ganancias = ? WHERE Mes=?',(ganancia_diciembre,mes,))
				conexion.commit()
			
		
		meses=[]
		
		ganancias=[]

		#insertar en la tabla de ganancias de base de datos 

		

		
		#insertar en la tabla de mostrar
		ganancias_mes=c.execute("SELECT *FROM ganancias").fetchall()
		for mes in ganancias_mes:
			self.tabla_ganancias.insert('','end',text='',values=mes)

		

	def mostrar_vendidos(self):
		
		#limpiando tabla
		borrar=self.tabla.get_children()
		for fila in borrar:
			self.tabla.delete(fila)
		
		#motrar libros
		libros_vendidos=c.execute("SELECT * FROM vendidos").fetchall()
		for fila in libros_vendidos:
			self.tabla.insert('','end',text='', values=fila)
