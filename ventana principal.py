import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


#importar nuevas ventanas
import importlib
ventana_registro=importlib.import_module("registro")
ventana_almacen=importlib.import_module("almacen")
ventana_ganancias=importlib.import_module("ganancias")
 
#Crear conexión con tabla
conexion=sqlite3.connect("base_datos.db")
c=conexion.cursor()


class Libro(object):
	
	#Ventana principal
	def __init__(self, ventana):	
		self.ventana=ventana
		self.ventana.geometry("900x600")
		self.ventana.resizable(width=0, height=0)

		self.imagen=PhotoImage(file="libros.gif")
		self.label_imagen=Label(self.ventana,image=self.imagen).place(x=0,y=0)
		
	#Agregar contenedor
		

	#Agregar botones
		self.nombre=Button(ventana,text=" GaBooks ",height=3,width=25)
		self.nombre.place(x="130",y="80")

		self.nombre_a=Button(ventana,text=" ALMACÉN ", command=self.almacen,height=3,width=20)
		self.nombre_a.place(x="150",y="200")

		self.nombre_b=Button(ventana,text=" REGISTRO ", command=self.registro,height=3,width=20)
		self.nombre_b.place(x="150",y="300")

		self.nombre_c=Button(ventana,text=" GANANCIAS ", command=self.ganancias,height=3,width=20)
		self.nombre_c.place(x="150",y="400")

	def registro (self):
		agregar=ventana_registro.Nuevo()

	def almacen(self):
		agregar=ventana_almacen.Almacen()

	def ganancias(self):
		agregar=ventana_ganancias.Vendido()




#Correr ventana principal
def ventana_principal():
	ventana_p = Tk()
	app=Libro(ventana_p)
	ventana_p.title("GaBooks")
	#ventana_p.geometry("800x600")
	ventana_p.mainloop()


if __name__ == '__main__':
	ventana_principal()




