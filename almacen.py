from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import datetime

conexion=sqlite3.connect("base_datos.db")
c=conexion.cursor()

class Almacen(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		#self.geometry("800x600")
		self.title("ALMACÉN")
		self.resizable(False,False)


	######## contenedor ARRIBA
		self.frame=Frame(self)
		self.frame.grid()
	

	##### CONTENEDOR IZQUIERDA / busqueda
		self.frame1=Frame(self.frame)
		self.frame1.grid(row=1,column=1)
		
		#self.label_title1=Label(self.frame1,text="ALMACEN ")
		#self.label_title1.grid(row=0,sticky=W+E)

		#area de búsqueda
		self.barra_busqueda=LabelFrame(self.frame1,text='Búsqueda',width=290,height=150)
		self.barra_busqueda.grid_propagate(False)
		self.barra_busqueda.grid(row=1,column=1,padx=40,pady=10)

		self.label_busqueda=Label(self.barra_busqueda,text='Buscar libro')
		self.label_busqueda.grid(row=1,column=1,padx=5,pady=5)

	#opciones
		OPCIONESB = [
		"General",
		"Autor",
		"Nombre",
		"Editorial"
		] 
	#
		self.variable = StringVar(self.barra_busqueda)
		self.variable.set("Buscar por")

		self.opciones =OptionMenu(self.barra_busqueda, self.variable, *OPCIONESB) 
		self.opciones.grid(row=1,column=2)
		

		self.texto_busqueda=Entry(self.barra_busqueda)
		self.texto_busqueda.grid(row=2,column=1,columnspan=2,sticky=W+E,padx=5,pady=5)

		self.boton_buscar=Button(self.barra_busqueda,text='Buscar',command=self.buscar)
		self.boton_buscar.grid(row=3,column=1,columnspan=2,sticky=W+E,padx=5,pady=5)
		
	###### CONTENEDOR DERECHA / botones
		self.frame3=Frame(self.frame)
		self.frame3.grid(row=1,column=2)

		self.opciones=LabelFrame(self.frame3,text='Opciones mostrar todo',width=290,height=150)
		self.opciones.grid_propagate(False)
		self.opciones.pack()

	#mostrar todo
		self.boton_mostrar=Button(self.opciones,text='Mostrar todo',command=self.mostrar_libros)
		self.boton_mostrar.grid(row=0,column=1,columnspan=3,sticky=W+E,padx=5,pady=5)

	#ordenar
		self.label_ordenar=Label(self.opciones,text='Ordenar por')
		self.label_ordenar.grid(row=1,column=1,sticky=E,padx=5,pady=5)

		self.seleccion=IntVar()
		
		self.opcion_autor=Radiobutton(self.opciones,text='autor', var=self.seleccion,value=1)
		self.opcion_autor.grid(row=1,column=2)
		
		self.opcion_nombre=Radiobutton(self.opciones,text='nombre',var=self.seleccion,value=2)
		self.opcion_nombre.grid(row=1,column=3)
		
		self.opcion_editorial=Radiobutton(self.opciones,text='editorial',var=self.seleccion,value=3)
		self.opcion_editorial.grid(row=2,column=2)
		
		self.opcion_precio=Radiobutton(self.opciones,text='precio',var=self.seleccion,value=4)
		self.opcion_precio.grid(row=2,column=3)

		self.boton_ordenar=Button(self.opciones,text='Ordenar',command=self.ordenar)
		self.boton_ordenar.grid(row=3,column=1,columnspan=3,sticky=W+E,padx=5,pady=5)


	##### CONTENEDOR ABAJO / libros
		self.frame2=Frame(self)
		self.frame2.grid()

		self.libros=LabelFrame(self.frame2,text='Libros')
		self.libros.grid()

	#botones
		self.boton_vender=Button(self.libros,text='Vender',command=self.vender)
		self.boton_vender.grid(row=1,column=1)

		self.boton_borrar=Button(self.libros,text='Borrar',command=self.borrar)
		self.boton_borrar.grid(row=1,column=2)

		#self.boton_editar=Button(self.libros,text='Editar',command=self.editar)
		#self.boton_editar.grid(row=1,column=3)

	#espacio para mostrar libros
		self.tabla=ttk.Treeview(self.libros, columns=('Código','Nombre del libro','Autor','Año','Editorial', 'Precio','Cantidad'))
		
		self.tabla.heading('#0',text="",anchor='w')
		self.tabla.column('#0',anchor='center',width=5,stretch=NO)
		
		self.tabla.heading('#1',text='Código', anchor="w")
		self.tabla.column('#1',anchor='center',width=80)
		
		self.tabla.heading('#2',text='Nombre del libro', anchor=CENTER)
		self.tabla.column('#2',anchor='center',width=230)
		
		self.tabla.heading('#3',text='Autor', anchor=CENTER)
		self.tabla.column('#3',anchor='center',width=180)
		
		self.tabla.heading('#4',text='Año', anchor=CENTER)
		self.tabla.column('#4',anchor='center',width=50)
		
		self.tabla.heading('#5',text='Editorial', anchor=CENTER)
		self.tabla.column('#5',anchor='center',width=90)
		
		self.tabla.heading('#6',text='Precio', anchor=CENTER)
		self.tabla.column('#6',anchor='center',width=60)

		self.tabla.heading('#7',text='Cantidad', anchor=CENTER)
		self.tabla.column('#7',anchor='center',width=60)

		self.tabla.grid(row=2,column=1,columnspan=3)

		#mostrar_libros(self)

		#self.boton_volver=Button(self.libros,text='Volver')
		#self.boton_volver.grid(row=3,column=3)

	##### funciones

	# COLOCAR LIBROS
	def mostrar_libros(self):
		
		#limpiando tabla
		borrar=self.tabla.get_children()
		for fila in borrar:
			self.tabla.delete(fila)
		
		#motrar libros
		libros=c.execute("SELECT * FROM libros").fetchall()
		for fila in libros:
			self.tabla.insert('','end',text='', values=fila)

	# BUSCAR LIBROS
	
	def buscar (self):
		
		filtro=self.variable.get()

		#limpiando tabla
		borrar=self.tabla.get_children()
		for fila in borrar:
			self.tabla.delete(fila)
		
		#buscar en general
		if filtro == "General":
			valor=(self.texto_busqueda.get()).title()
			busqueda=c.execute("SELECT * FROM libros WHERE nombre LIKE ?",('%'+valor+'%',)).fetchall()
			busqueda2=c.execute("SELECT * FROM libros WHERE autor LIKE ?",('%'+valor+'%',)).fetchall()
			busqueda3=c.execute("SELECT * FROM libros WHERE editorial LIKE ?",('%'+valor+'%',)).fetchall()
			for fila in busqueda:
				self.tabla.insert('','end',text='', values=fila)
			for fila in busqueda2:
				self.tabla.insert('','end',text='', values=fila)
			for fila in busqueda3:
				self.tabla.insert('','end',text='', values=fila)
		
		#buscar por autor
		elif filtro == "Autor":
			valor=(self.texto_busqueda.get()).title()
			busqueda=c.execute("SELECT * FROM libros WHERE autor LIKE ?",('%'+valor+'%',)).fetchall()
			for fila in busqueda:
				self.tabla.insert('','end',text='', values=fila)

		#buscar por nombre
		elif filtro == "Nombre":
			valor=(self.texto_busqueda.get()).title()
			busqueda=c.execute("SELECT * FROM libros WHERE nombre LIKE ?",('%'+valor+'%',)).fetchall()
			for fila in busqueda:
				self.tabla.insert('','end',text='', values=fila)

		#buscar por editorial
		elif filtro == "Editorial":
			valor=(self.texto_busqueda.get()).title()
			busqueda=c.execute("SELECT * FROM libros WHERE editorial LIKE ?",('%'+valor+'%',)).fetchall()
			for fila in busqueda:
				self.tabla.insert('','end',text='', values=fila)

		#si no escogio, buscar general
		else:
			valor=(self.texto_busqueda.get()).title()
			busqueda=c.execute("SELECT * FROM libros WHERE nombre LIKE ?",('%'+valor+'%',)).fetchall()
			busqueda2=c.execute("SELECT * FROM libros WHERE autor LIKE ?",('%'+valor+'%',)).fetchall()
			busqueda3=c.execute("SELECT * FROM libros WHERE editorial LIKE ?",('%'+valor+'%',)).fetchall()
			for fila in busqueda:
				self.tabla.insert('','end',text='', values=fila)
			for fila in busqueda2:
				self.tabla.insert('','end',text='', values=fila)
			for fila in busqueda3:
				self.tabla.insert('','end',text='', values=fila)

	# ORDENAR LIBROS

	def ordenar(self):
	
		#limpiar tabla
		borrar=self.tabla.get_children()
		for fila in borrar:
			self.tabla.delete(fila)
			consulta=" "
		
		#conseguir elección
		valor=self.seleccion.get()
		if valor==1:
			consulta1="SELECT * FROM libros ORDER BY Autor"
		if valor==2:
			consulta1="SELECT * FROM libros ORDER BY Nombre"
		if valor==3:
			consulta1="SELECT * FROM libros ORDER BY Editorial"
		if valor==4:
			consulta1="SELECT * FROM libros ORDER BY Precio"
		consulta_orden=c.execute(consulta1).fetchall()

		#colocar libros
		for fila in consulta_orden:
			self.tabla.insert('','end',text='', values=fila)
	
	# BORRAR LIBROS

	def borrar(self):
		#conseguir libro
		valor=self.tabla.item(self.tabla.selection())['values']
		cantidad=""
		
		#conseguir cantidad de libros y restarle uno
		try:
			cantidad=int(valor[6])
			cantidad-=1
		except:
			messagebox.showerror("Error", "Debe escoger un libro", icon='warning')

		#conseguir nombre del libro
		nombree=valor[1]
				
		#si cantidad es igual a 0, borrarlo
		if cantidad == 0:
			c.execute('DELETE FROM libros WHERE Nombre = ?',(nombree,))
		#sino restarle 1 a cantidad
		else:
			c.execute('UPDATE libros SET Cantidad = ? WHERE Nombre=?',(cantidad,nombree,))
			conexion.commit()
		conexion.commit()
		
		self.mostrar_libros()
	
	# EDITAR LIBROS

	def editar(self):
		#conseguir libro
		valor=self.tabla.item(self.tabla.selection())['values']
		cantidad=""
		

	# VENDER LIBROS
	def vender(self):
		#conseguir libro
		valor2=self.tabla.item(self.tabla.selection())['values']
		cantidadsobrante=""
		#conseguir cantidad de libros y restarle uno
		cantidadsobrante=valor2[6]
		cantidadsobrante-=1

		#conseguir datos del libro
		nombreee=valor2[1]
		autor=valor2[2]
		precio=valor2[5]

		#conseguir fecha del venta
		fecha_hora=datetime.datetime.now()
		fecha=fecha_hora.date()
		mes_num=fecha.month

		#mes
		if mes_num==1:
			mes="Enero"
		elif mes_num==2:
			mes="Febrero"
		elif mes_num==3:
			mes="Marzo"
		elif mes_num==4:
			mes="Abril"
		elif mes_num==5:
			mes="Mayo"
		elif mes_num==6:
			mes="Junio"
		elif mes_num==7:
			mes="Julio"
		elif mes_num==8:
			mes="Agosto"
		elif mes_num==9:
			mes="Septiembre"
		elif mes_num==10:
			mes="Octubre"
		elif mes_num==11:
			mes="Noviembre"
		elif mes_num==12:
			mes="Diciembre"

		#quitarlo de libros
		if cantidadsobrante == 0:
			c.execute('DELETE FROM libros WHERE Nombre = ?',(nombreee,))
			conexion.commit()
		else:
			c.execute('UPDATE libros SET Cantidad = ? WHERE Nombre=?',(cantidadsobrante,nombreee,))
			conexion.commit()
		
		self.mostrar_libros()
		
		#Agregrar en vendidos
		
		#buscarlo en tabla de vendidos
		consulta=c.execute("SELECT * FROM vendidos").fetchall()
		
		
		contador=0
		consulta_total='SELECT COUNT (*) FROM vendidos'
		c.execute(consulta_total)
		total=c.fetchone()[0]
		print(total)
				
		#si el libro ya esta en vendidos
		for libro in consulta:
			nombrevendidos=libro[0]
			mesvendidos=libro[4]

			#esta en vendidos en el mismo mes
			if nombreee==nombrevendidos and mes==mesvendidos:
				cantidad_actual=int(libro[3])
				cantidad_actual+=1
				c.execute('UPDATE vendidos SET Cantidad = ? WHERE Nombre=?',(cantidad_actual,nombreee,))
				conexion.commit()
				
			#esta en vendidos en otro mes
			if nombreee==nombrevendidos and mes!=mesvendidos:
				contador+=1
				if contador==total:
					consulta3= "INSERT INTO 'vendidos'(Nombre,Autor,Precio,Cantidad,Mes) VALUES (?,?,?,?,?)"
					cantidad_inicial=int("1")
					c.execute(consulta3,(nombreee,autor,precio,cantidad_inicial,mes))
					conexion.commit()

			#si el libro no está en vendidos
			if nombreee!=nombrevendidos:
				contador+=1
				if contador==total:
					consulta3= "INSERT INTO 'vendidos'(Nombre,Autor,Precio,Cantidad,Mes) VALUES (?,?,?,?,?)"
					cantidad_inicial=int("1")
					c.execute(consulta3,(nombreee,autor,precio,cantidad_inicial,mes))
					conexion.commit()
		
		self.mostrar_libros()

		


		



	''''def mostrar_librasos(self):
			self.caja.delete(0,END)
			libros=c.execute("SELECT * FROM libros").fetchall()
			contador=0
			for libro in libros:
				self.caja.insert(contador,libro[1]+'\t'+libro[2]+'\t'+str(libro[3])+'\t'+libro[4]+'\t'+'S/.'+str(libro[5])+'.00')
				contador += 1


	#espacio para mostrar libros2 
	
		self.espacio_grande=ttk.Notebook(self.mostrar,width=600,height=600)
		self.espacio_grande.pack()

		self.espacio=ttk.Frame(self.espacio_grande)
		self.espacio.pack()

		self.caja=Listbox(self.espacio,width=80, height=30, font='times 12 bold')
		self.barra=Scrollbar(self.espacio, orient=VERTICAL)
		self.caja.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
		self.barra.config(command=self.caja.yview)
		self.caja.config(yscrollcommand=self.barra.set)
		self.barra.grid(row=0,column=0,sticky=N+S+E)
		
		mostrar_libros(self)'''