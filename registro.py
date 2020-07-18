from tkinter import *
from tkinter import messagebox
import sqlite3
conexion=sqlite3.connect("base_datos.db")
c=conexion.cursor()

class Nuevo(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		#self.geometry("600x600")
		self.title("Registro")
		self.resizable(False,False)

	#crear contenedor
		self.frame_grande=Frame(self)
		self.frame_grande.grid()

###### Añadir nuevo

		self.frame=LabelFrame(self.frame_grande,text="Añadir nuevo")
		self.frame.grid(padx=40,pady=10)
		
		self.label_registro=Label(self.frame,text="REGISTRO ")
		self.label_registro.grid(row=0,column=1,columnspan=2)

	#Nombre del libro input
		self.label1=Label(self.frame,text="NOMBRE DEL LIBRO:")
		self.label1.grid(row=1,column=1,padx=5,pady=5,sticky=E)

		self.texto_1=Entry(self.frame,width=30)
		self.texto_1.grid(row=1,column=2)	
		
	#Autor input
		self.label2=Label(self.frame,text="AUTOR:")
		self.label2.grid(row=2,column=1,padx=5,pady=5)	
	
		self.texto_2=Entry(self.frame,width=30)
		self.texto_2.grid(row=2,column=2,padx=10)	

	#Fecha de publicación input
		self.label3=Label(self.frame,text="FECHA DE PUBLICACIÓN:")
		self.label3.grid(row=3,column=1,padx=5,pady=5,sticky=E)	
	
		self.texto_3=Entry(self.frame,width=30)
		self.texto_3.grid(row=3,column=2)	
		
	#Editorial input
		self.label4=Label(self.frame,text="EDITORIAL")
		self.label4.grid(row=4,column=1,padx=5,pady=5)	
	
		self.texto_4=Entry(self.frame,width=30)
		self.texto_4.grid(row=4,column=2)	
	
	#Precio input
		self.label5=Label(self.frame,text="PRECIO:")
		self.label5.grid(row=5,column=1,padx=5,pady=5)	

		self.texto_5=Entry(self.frame,width=30)
		self.texto_5.grid(row=5,column=2)	

	#Cantidad input 
		self.label6=Label(self.frame,text="CANTIDAD:")
		self.label6.grid(row=6,column=1)	

		self.texto_6=Entry(self.frame,width=30)
		self.texto_6.grid(row=6,column=2)	
	
	#Clasificación input
		self.label7=Label(self.frame,text="CLASIFICACIÓN:")
		self.label7.grid(row=7,column=1,padx=5,pady=5)

		OPCIONESCL = [
		"000 Obras generales",
		"100 Filosofía",
		"200 Religión",
		"300 Ciencias Sociales",
		"400 Filología",
		"500 Ciencias Puras",
		"600 Ciencias Aplicadas",
		"700 Bellas Artes",
		"800 Literatura",
		"900 Historia",
		] 

		self.variable = StringVar(self.frame)
		self.variable.set("Elija clasificación")

		self.opciones =OptionMenu(self.frame, self.variable, *OPCIONESCL) 
		self.opciones.grid(row=7,column=2,padx=5,pady=5)

	
	#Botones
		
		self.boton_guardar=Button(self.frame,text="GUARDAR",command=self.guardar)
		self.boton_guardar.grid(row=10, column=1, columnspan=2,padx=5,pady=5)

######Añadir ya existente

		self.frame2=LabelFrame(self.frame_grande,text="Añadir existente")
		self.frame2.grid(padx=10,pady=10)

		self.label8=Label(self.frame2,text="Añadir por:")
		self.label8.grid(row=8,column=1,padx=5,pady=5)

		OPCIONESA = [
		"Título del libro",
		"Código"
		] 

		self.variable2 = StringVar(self.frame2)
		self.variable2.set("Elija opción")

		self.opciones2 =OptionMenu(self.frame2, self.variable2, *OPCIONESA) 
		self.opciones2.grid(row=8,column=2,padx=5,pady=5)

		self.texto_añadir=Entry(self.frame2,width=30)
		self.texto_añadir.grid(row=9,column=1, columnspan=2,padx=5,pady=5)

		self.boton_añadir=Button(self.frame2,text="añadir libro ya existente",command=self.añadir)
		self.boton_añadir.grid(row=10, column=1, columnspan=2,padx=5,pady=5)

		#Botón

		#self.boton_volver=Button(self.frame,text="VOLVER")
		#self.boton_volver.grid(row=12, column=1, columnspan=2,padx=5,pady=5)
	

	def volver (self):
		pass

	def guardar (self):
		nombre=(self.texto_1.get()).title()
		autor=(self.texto_2.get()).title()
		año=self.texto_3.get()
		editorial=(self.texto_4.get()).title()
		precio=self.texto_5.get()
		cantidad=self.texto_6.get()
		clasificacion=self.variable.get()

		#generar código
		nombre_limpio=nombre.replace(" ","")
		autor_limpio=autor.replace(" ","")
		
		clasificacion3=clasificacion[0:3]
		nombre3=(nombre_limpio[0:3]).upper()
		autor3=(autor_limpio[0:3]).upper()
		
		codigo="{}{}{}".format(clasificacion3,nombre3,autor3)

		#insertar a la tabla
		if clasificacion=="Elija clasificación":
			messagebox.showerror("Error", "Todos los campos son obligatorios", icon='warning')
		elif(nombre and autor and año and editorial and precio != ""):
			consulta= "INSERT INTO 'libros'(Código,Nombre,Autor,Año,Editorial,Precio,Cantidad) VALUES (?,?,?,?,?,?,?)"
			c.execute(consulta,(codigo,nombre,autor,año,editorial,precio,cantidad))
			conexion.commit()
			messagebox.showinfo("Éxito","El libro fue guardado exitosamente", icon='info')
			
		else: 
			messagebox.showerror("Error", "Todos los campos son obligatorios", icon='warning')

		#generar código

	def añadir (self):
		
		filtro=self.variable2.get()
		
		consulta4=c.execute("SELECT * FROM libros").fetchall()
		
		contador=0
		consulta_total='SELECT COUNT (*) FROM libros'
		c.execute(consulta_total)
		total=c.fetchone()[0]
		
		
		#buscarlo en tabla de libros por libro

		if filtro=="Título del libro":
			
			nombre_agregado=(self.texto_añadir.get()).title()

			for libro in consulta4:
				nombre_existente=libro[1]
				
				if nombre_agregado==nombre_existente:
					cantidad_actual=int(libro[6])
					cantidad_actual+=1
					c.execute('UPDATE libros SET Cantidad = ? WHERE Nombre=?',(cantidad_actual,nombre_agregado,))
					conexion.commit()
					messagebox.showinfo("Éxito","El libro fue guardado exitosamente\nNueva cantidad del libro: {}".format(cantidad_actual), icon='info')
				
				if nombre_agregado!=nombre_existente:
					contador+=1
					if contador==total:
						messagebox.showerror("Error", "El libro no existe", icon='warning')

		#buscarlo en tabla de libros por libro

		if filtro=="Código":
			
			codigo_agregado=(self.texto_añadir.get()).upper()
			
			for libro in consulta4:
				codigo_existente=libro[0]
				if codigo_agregado==codigo_existente:
					cantidad_actual=int(libro[6])
					cantidad_actual+=1
					c.execute('UPDATE libros SET Cantidad = ? WHERE Código=?',(cantidad_actual,codigo_agregado,))
					conexion.commit()
					messagebox.showinfo("Éxito","El libro fue guardado exitosamente\nNueva cantidad del libro: {}".format(cantidad_actual), icon='info')
				
				if codigo_agregado!=codigo_existente:
					contador+=1
					if contador==total:
						messagebox.showerror("Error", "El libro no existe", icon='warning')

		
		if filtro!="Código" and filtro!="Título del libro":
			messagebox.showerror("Error", "Debe escoger una opción", icon='warning')

		