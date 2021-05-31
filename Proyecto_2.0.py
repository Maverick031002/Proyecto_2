from tkinter import *
import tkinter as tk
from tkinter import messagebox



#############################################################################################################################################
def iniciar():
    pantalla = tk.Tk()
    pantalla.geometry("600x300")
    pantalla.title("Sistema de reservación de boletos")
    pantalla.config(bg = "skyblue")
    ventana_principal(pantalla)
    pantalla.mainloop()
    
def transicion(frame_viejo,siguiente_frame,pantalla):
    frame_viejo.pack_forget()
    siguiente_frame(pantalla)


#Nombre: TransformarSTR
#Entradas: un parámetro llamado delete
#Salidas: transformar el parámetro a una lista
#Restricciones: el parámetro debe ser una lista
    
def TransformarSTR(delete):
    if isinstance(delete,list):
        STR = ""
        for indice in delete:
            STR += indice
        return STR
    else:
        print("")

#Nombre: TransformarSTR_aux
#Entradas: Un parámetro llamado delete
#Salidas: retornar STR
#Restricciones: delete debe ser una lista

def TransformarSTR_aux(delete):
    if isinstance(delete,list):
        STR = ""
        for indice in delete:
            STR += indice
        return STR
    else:
        print("")
#############################################################################################################################################


    












#############################################################################################################################################

#Creación de la ventana
  
def ventana_principal(pantalla):
    frame = tk.Frame(pantalla)
    frame.pack()
    menu = Menu(pantalla)
    pantalla.config(menu=menu)
    menuPrincipal = Menu(menu,tearoff = 0)#quita la linea de puntos
    menuPrincipal.add_command(label = "1 - Opciones administrativas",font =("Times new roman","12","italic","bold"),
                              command = lambda: transicion(frame,solicitar_clave,pantalla))
    menuPrincipal.add_command(label = "2 - Opciones de usuario normal",font =("Times new roman","12","italic","bold"),
                              command = lambda: transicion(frame,menu_general,pantalla))
    menuPrincipal.add_command(label = "3 - Salir",font =("Times new roman","12","italic","bold"),
                              command = pantalla.destroy)
    menu.add_cascade(label="Menú principal", menu = menuPrincipal)

#Menu administrativo

def menu_administrativo(pantalla):
    frame = tk.Frame(pantalla)
    pantalla.title("Menú administrativo")
    pantalla.config(bg = "lightgreen")

    menu = Menu(pantalla)
    pantalla.config(menu=menu)

    opAdmi = Menu(menu,tearoff = 0)
    opAdmi.add_command(label = "1 - Gestión de empresas",font=("Times new roman","12"),
                       command = lambda: transicion(frame,gestion_empresa,pantalla))
    opAdmi.add_command(label = "2 - Gestión de transporte por empresa",font=("Times new roman","12"),
                       command = lambda: transicion(frame,gestion_transporte,pantalla))
    opAdmi.add_command(label = "3 - Gestión de viaje",font=("Times new roman","12"),
                       command = lambda: transicion(frame,gestion_viaje,pantalla))
    opAdmi.add_command(label = "4 - Consultar historial de reservaciones",font=("Times new roman","12"),
                       command = lambda: transicion(frame,consultar_historial,pantalla))
    opAdmi.add_command(label = "5 - Estadísticas de viaje",font=("Times new roman","12"),
                       command = lambda: transicion(estadisticas,pantalla))
    opAdmi.add_command(label = "6 - Salir de menu administrativo", font=("Times new roman","12"),
                       command = lambda: transicion(frame,ventana_principal,pantalla))
    menu.add_cascade(label="1 - Opciones administrativas", font=("Times new roman","12"), menu = opAdmi)
    frame.pack()
    
#Verificación de acceso

def solicitar_clave(pantalla):
    frame = tk.Frame(pantalla,height=300, width=600)
    frame.pack()
    etiqueta=tk.Label(frame, text="Escriba la clave de acceso",bg = "white",font =("Times new roman","14","italic","bold"))
    etiqueta.place(x=180,y=60)
    entrada_var = tk.StringVar()
    entrada = tk.Entry(frame, textvariable = entrada_var)
    entrada.place(x=225,y=90)
    boton = tk.Button(frame,text = "Ingresar",font=("Times new roman","12"),
                      command = lambda: verificar_clave(entrada_var.get(),pantalla,frame))
    boton.place(x=260,y=120)
    
def verificar_clave(clave,pantalla,frame):
    verificar = leer_archivo_claves()
    if (clave in verificar):
        transicion(frame,menu_administrativo,pantalla)
    else:
        messagebox.askyesno("Error","La contraseña es incorrecta o no esta registrada. ¿Desea continuar o intentar otra vez?")
        
def leer_archivo_claves():
    archivo_claves = open("claves.txt")
    lineas = archivo_claves.readlines()
    archivo_claves.close()
    lineas_modificadas = []
    for linea in lineas:
        linea = linea.replace("\n","")
        lineas_modificadas += [linea]
    return lineas_modificadas

#############################################################################################################################################
#Gestion de Empresas

def gestion_empresa(pantalla):
    frame = tk.Frame(pantalla)
    frame.pack()
    
    pantalla.title("Gestión de Empresas")
    pantalla.config(bg = "lightgreen")
    menu1 = Menu(pantalla)
    pantalla.config(menu=menu1)
    
    op1 = Menu(menu1,tearoff = 0)
    op1.add_command(label = "1 - Incluir empresa",font=("Times new roman","12"),
                    command = incluir_empresa)
    
    op1.add_command(label = "2 - Eliminar empresa",font=("Times new roman","12"),
                    command = eliminar_empresa)
    
    op1.add_command(label = "3 - Modificar empresa",font=("Times new roman","12"),
                    command = modificar_empresa)
    
    op1.add_command(label = "4 - Mostrar empresa",font = ("Times new roman","12"),
                    command = mostrar_empresas)
    
    op1.add_command(label = "5 - Retornar",font=("Times new roman","12"),
                    command = lambda: transicion(frame,menu_administrativo,pantalla))
    
    menu1.add_cascade(label = "Gestión de empresa",font = ("Times new roman","12"), menu = op1)
    
    frame.pack()


def incluir_empresa():
    window = tk.Tk()
    window.geometry("600x300")
    window.title("Registrando Empresa")
    cedula = tk.StringVar()
    nombre = tk.StringVar()
    provincia = tk.StringVar()
    direccion = tk.StringVar()
    señas = tk.StringVar()
    
    etiqueta1 = tk.Label(window,text="Cédula Juridica: ",font=("Times new roman","12"), fg="black").place(x=5,y=40)
    Cedula = tk.Entry(window,textvariable = cedula, font=("Times new roman","12"), fg="Black")
    Cedula.place(x=159,y=40)
    
    etiqueta2 =tk.Label(window,text="Nombre: ",font=("Times new roman","12"),fg="black").place(x=5,y=80)
    Nombre=tk.Entry(window,textvariable = nombre,font=("Times new roman","12"),fg="Black")
    Nombre.place(x=159,y=85)
    
    etiqueta3 = tk.Label(window,text="Provincia: ",font=("Times new roman","12"),fg="black").place(x=5,y=120)
    Provincia = tk.Entry(window,textvariable = provincia,font=("Times new roman","12"),fg="Black")
    Provincia.place(x=159,y=120)

    etiqueta4 = tk.Label(window,text="Dirección del negocio: ",font=("Times new roman","12"),fg="black").place(x=5,y=160)
    Direccion = tk.Entry(window,textvariable = direccion,font=("Times new roman","12"),fg="Black")
    Direccion.place(x=159,y=160)

    etiqueta5 = tk.Label(window,text="Señas exactas: ",font=("Times new roman","12"),fg="black").place(x=5,y=200)
    Señas = tk.Entry(window,textvariable = señas,font=("Times new roman","12"),fg="Black")
    Señas.place(x=159,y=200)

    tk.Button(window,text="Agregar",font = ("Times new roman","12"),fg="Black",
              command = lambda: registrar_empresa(Cedula.get(), Nombre.get(), Provincia.get(), Direccion.get(),Señas.get())).place(x=169,y=250)
    
    
    window.mainloop()
    

def registrar_empresa(cedula,nombre,provincia,direccion,señas):
    almacenar_empresas = open("Empresas.txt","a")
    if len (cedula)==10:
        archivo= open("Empresas.txt")
        archivo2 = archivo.readlines()
        abrirTrans= open("Transportes.txt")
        abrir=abrirTrans.readlines()
        if (("Cedula Jurídica:"+cedula + "\n") in archivo2):
            messagebox.showerror(title = "Error", message = "La empresa ya existe")
                
        else:
            almacenar_empresas.write("Cedula Jurídica:"+ cedula +"\n")
            almacenar_empresas.write("Nombre:"+ nombre +"\n")
            almacenar_empresas.write("Provincia:"+ provincia +"\n")
            almacenar_empresas.write("Dirección:"+ direccion +"\n")
            almacenar_empresas.write("Señas exactas:"+ señas +"\n")
            almacenar_empresas.write("************************************************"+"\n")
            almacenar_empresas.close()
            messagebox.showinfo(title = "Empresa añadida",message = "¡La empresa se ha registrado exitosamente!")
    else:
        messagebox.showerror(title = "Error", message = "La cedula debe tener 10 digitos")

def eliminar_empresa():
    window = tk.Tk()
    window.geometry("600x300")
    window.title("Eliminando Empresa")
    
    etiqueta1 = tk.Label(window, text = "Cedula a eliminar").pack()
    Cedula = tk.Entry(window,text = "", font=("Times new roman","12"), bg="white", fg="Black")
    Cedula.pack()


    def eliminar_emp2():
        variable = Cedula.get()
        return eliminar_emp(variable)
    
    tk.Button(window,text="Eliminar",font = ("Times new roman","12"),bg="#e7c4e5",fg="Black",
              command =  eliminar_emp2).pack()
    
    window.mainloop()


def eliminar_emp(cedula_juridica):
    open_file = open("Empresas.txt")
    empresas = open_file.readlines()
    open_file2 = open("Transportes.txt")
    transportes = open_file2.readlines()
    if (("Cedula Jurídica:"+cedula_juridica+"\n")in empresas):
        if (("Cedula Jurídica:"+cedula_juridica+ "\n") in transportes):
            messagebox.showerror(title = "Error", message = "La empresa esta asociada un transporte")
        else:
            cedula_juridica=str(cedula_juridica)
            potencia = empresas.index("Cedula Jurídica:"+cedula_juridica+"\n")
            cedula_juridica = deleteEmpresa(empresas, potencia, 0)
            open_file.close()
            open_file = open("Empresas.txt", "w")
            open_file.write(cedula_juridica)
            open_file.close()
            messagebox.showinfo(title = "Delete", message = "La empresa ha sido eliminada exitosamente")
            
    else:
        messagebox.showerror(title = "Error", message = "No existe una empresa con la cedula juridica escrita")
        
    
def deleteEmpresa(delete,ContarLineas,contador):
    if contador == 6:
        return TransformarSTR(delete)
    else:
        delete.pop(ContarLineas)
        return deleteEmpresa(delete,ContarLineas,contador+1)

############################################################################################################################################
def mostrar_empresas():
    ventana = tk.Tk()
    ventana.geometry("600x300")
    ventana.title("Mostrar Empresas")
    ventana.config(bg = "white")
    abrir = open("Empresas.txt")
    abrir2 = abrir.readlines()
    mostrar_datos = tk.Listbox(ventana)
    mostrar_datos.pack()
    contador = 0
    for datos in abrir2:
        mostrar_datos.insert(contador,datos)
        contador += 1
    

    
#############################################################################################################################################
def modificar_empresa():
     ventana=tk.Tk()
     ventana.title("Modificar Empresa")
     ventana.geometry("600x300")
    
     Cedula=tk.Label(ventana,text="Cédula Juridica:",font=("Times New Roman",12), fg="Black")
     Cedula.pack()
    
     cedula=tk.Entry(ventana,text="", font=("Times New Roman", 12), fg="Black")
     cedula.pack()
    
     boton=tk.Button(ventana,text="Modificar Empresa",font=("Times New Roman",12),fg="Black",
                          command = lambda:modificar_empresa_aux(cedula.get()))
     boton.pack()
    
     boton2 = tk.Button(ventana,text="Salir",font=("Times New Roman",12),fg="Black",
               command=lambda:gestion_empresa())
     boton2.pack()
    
     ventana.mainloop()

def modificar_empresa_aux(cedula):
     abrir_file_empresas = open("Empresas.txt")
     empresas = abrir_file_empresas.readlines()
     print(("Cedula Jurídica:"+cedula+"\n"), empresas)
     if("Cedula Jurídica:"+cedula+"\n")in empresas:
          cedula=str(cedula)
          indice = empresas.index("Cedula Jurídica:"+cedula+"\n")
          cedula = deleteEmpresa(empresas, indice, 0)
          abrir_file_empresas.close()
          abrir_file_empresas = open("Empresas.txt", "w")
          abrir_file_empresas.write(cedula)
          abrir_file_empresas.close()
          return modificar_empresa_aux2()
     else:
          messagebox.showerror(title = "Error", message = "La cedula no se encuentra registrada")
        
#Pidiendo los nuevos datos
def modificar_empresa_aux2():
     ventana = tk.Tk()
     ventana.title("Modificar Empresa")
     ventana.geometry("600x300")
         
     tk.Label(ventana, text="Nueva Empresa", font=("Times New Roman", 12), fg="Black").pack()
     Cedula=tk.Label(ventana,text="Nueva Cedula Jurídica",font=("Times New Roman", 12), fg="Black")
     Cedula.place(x=5,y=40)
     cedula=tk.Entry(ventana,text="", font=("Times New Roman", 12), fg="Black")
     cedula.place(x=200,y=40)
         
     Nombre=tk.Label(ventana,text="Nueva empresa:",font=("Times New Roman", 12),fg="Black")
     Nombre.place(x=5,y=80) 
     nombre=tk.Entry(ventana,text="",font=("Times New Roman", 12), bg="SkyBlue1",fg="Black")
     nombre.place(x=200,y=80)
         
     Provincia=tk.Label(ventana,text="Nueva Provincia:",font=("Times New Roman", 12), fg="Black")
     Provincia.place(x=5,y=120)
     provincia=tk.Entry(ventana,text="",font=("Times New Roman", 12), bg="SkyBlue1",fg="Black")
     provincia.place(x=200,y=120)

     Direccion=tk.Label(ventana,text="Nueva dirección:",font=("Times New Roman", 12), fg="Black")
     Direccion.place(x=5,y=120)
     direccion=tk.Entry(ventana,text="",font=("Times New Roman", 12),fg="Black")
     direccion.place(x=200,y=120)

     Señas=tk.Label(ventana,text="Nuevas Señas exactas:",font=("Times New Roman", 12), fg="Black")
     Señas.place(x=5,y=120)
     señas=tk.Entry(ventana,text="",font=("Times New Roman", 12),fg="Black")
     señas.place(x=200,y=120)

     tk.Button(ventana,text="Aceptar",font=("Times New Roman", 12),fg="Black",
               command= lambda: registrar_empresa(cedula.get(),nombre.get(),provincia.get(),direccion.get(),señas.get())).place(x=205,y=180)
    
     ventana.mainloop()






#############################################################################################################################################
#############################################################################################################################################
def gestion_transporte(pantalla):
    frame = tk.Frame(pantalla)
    frame.pack()
    pantalla.title("Gestión de Transportes")
    pantalla.config(bg = "pink")
    menu1 = Menu(pantalla)

    op1 = Menu(menu1,tearoff = 0)
    op1.add_command(label = "1 - Incluir Transporte",font = ("Times new roman","12"),
                    command = incluir_transporte)
    
    op1.add_command(label = "2 - Eliminar Transporte",font = ("Times new roman","12"),
                    command = eliminar_transporte)
    
    op1.add_command(label = "3 - Modificar Transporte",font = ("Times new roman","12"),
                    command = lambda: transicion(frame,modificar_transporte,pantalla))
    
    op1.add_command(label = "4 - Mostrar Transporte",font = ("Times new roman","12"),
                    command = mostrar_transportes)
    
    op1.add_command(label = "5 - Retornar",font = ("Times new roman","12"),
                    command = lambda: transicion(frame,menu_administrativo,pantalla))
    
    menu1.add_cascade(label =" Gestión de Transporte",font = ("Times new roman","12"), menu = op1)
    pantalla.config(menu=menu1)
    pantalla.mainloop()


def incluir_transporte():
    window = tk.Tk()
    window.geometry("600x600")
    window.config(bg="gray")
    window.title("Registrando Transporte")
    placa = tk.StringVar()
    transporte = tk.StringVar()
    marca = tk.StringVar()
    modelo = tk.StringVar()
    año = tk.StringVar()
    empresa = tk.StringVar()
    asientos_normal = tk.StringVar()
    asientos_economicos = tk.StringVar()
    asientos_vip = tk.StringVar()

    etiqueta1 = tk.Label(window,text="Placa: ",font=("Times new roman","12"),bg="gray" ,fg="black").place(x=5,y=40)
    Placa = tk.Entry(window,textvariable = placa, font=("Times new roman","12"), fg="Black")
    Placa.place(x=159,y=40)
    
    etiqueta2 =tk.Label(window,text="Tipo de transporte: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=80)
    etiqueta22= tk.Label(window, text= "Buseta/Limosina: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=120)
    Transporte = tk.Entry(window,textvariable = transporte,font=("Times new roman","12"),fg="Black")
    Transporte.place(x=159,y=120)
    
    etiqueta3 = tk.Label(window,text="Marca: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=160)
    Marca = tk.Entry(window,textvariable = marca,font=("Times new roman","12"),fg="Black")
    Marca.place(x=159,y=160)

    etiqueta4 = tk.Label(window,text="Modelo: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=200)
    Modelo = tk.Entry(window,textvariable = modelo,font=("Times new roman","12"),fg="Black")
    Modelo.place(x=159,y=200)

    etiqueta5 = tk.Label(window,text="Año: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=240)
    Año = tk.Entry(window,textvariable = año,font=("Times new roman","12"),fg="Black")
    Año.place(x=159,y=240)

    etiqueta6 = tk.Label(window,text="Cedula de la Empresa: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=280)
    Empresa = tk.Entry(window,textvariable = empresa,font=("Times new roman","12"),fg="Black")
    Empresa.place(x=159,y=280)

    etiqueta7 =tk.Label(window,text="Asientos Normales: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=320)
    Asiento_normal = tk.Entry(window,textvariable = asientos_normal,font=("Times new roman","12"),fg="Black")
    Asiento_normal.place(x=159,y=320)

    etiqueta8 =tk.Label(window,text="Asientos Económicos: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=360)
    Asiento_economico = tk.Entry(window,textvariable = asientos_economicos,font=("Times new roman","12"),fg="Black")
    Asiento_economico.place(x=159,y=360)

    etiqueta9 =tk.Label(window,text="Asientos VIP: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=400)
    Asiento_vip = tk.Entry(window,textvariable = asientos_vip,font=("Times new roman","12"),fg="Black")
    Asiento_vip.place(x=159,y=400)
    
    tk.Button(window,text="Agregar",font = ("Times new roman","12"),bg="#e7c4e5",fg="Black",
              command = lambda: registrar_transporte(Placa.get(),Transporte.get(),Marca.get(), Modelo.get(), Año.get(), Empresa.get(),
                                                     Asiento_normal.get(),Asiento_economico.get(),Asiento_vip.get())).place(x=179,y=440)
    
    window.mainloop()



def registrar_transporte(placa,tipo,marca, modelo, año, empresa, asientos_normal,asientos_economicos,asientos_vip):
    almacenar_transporte = open("Transportes.txt","a")
    archivo= open("Transportes.txt")
    archivo2 = archivo.readlines()
    if (("Placa:"+placa + "\n") in archivo2):
            messagebox.showerror(title = "Error", message = "Esa matricula ya existe")
    else:
        almacenar_transporte = open("Transportes.txt","a")
        almacenar_transporte.write("Placa:"+placa +"\n")
        almacenar_transporte.write("Tipo:"+tipo+"\n")
        almacenar_transporte.write("Marca:"+marca +"\n")
        almacenar_transporte.write("Modelo:"+modelo +"\n")
        almacenar_transporte.write("Año:"+año +"\n")
        almacenar_transporte.write("Empresa:"+empresa +"\n")
        almacenar_transporte.write("Asientos Normales:"+asientos_normal +"\n")
        almacenar_transporte.write("Asientos Economicos:"+asientos_economicos+"\n")
        almacenar_transporte.write("Asientos VIP:"+asientos_vip +"\n")
        almacenar_transporte.write("************************************************"+"\n")
        almacenar_transporte.close()
        messagebox.showinfo(title = "Transporte añadido",message = "¡El transporte se ha registrado exitosamente!")



def eliminar_transporte():
    window = tk.Tk()
    window.geometry("600x300")
    window.title("Eliminando Transporte")
    
    etiqueta1 = tk.Label(window, text = "Plca del transporte a eliminar").pack()
    Placa = tk.Entry(window,text = "", font=("Times new roman","12"), bg="white", fg="Black")
    Placa.pack()


    def eliminar_trans2():
        variable = Placa.get()
        return eliminar_trans(variable)
    
    tk.Button(window,text="Eliminar",font = ("Times new roman","12"),bg="#e7c4e5",fg="Black",
              command =  eliminar_trans2).pack()


def eliminar_trans(placa):
    open_file = open("Transportes.txt")
    transportes = open_file.readlines()
    if (("Placa:"+placa+"\n")in transportes):
        placa=str(placa)
        potencia = transportes.index("Placa:"+placa+"\n")
        placa = deleteTransportes(transportes, potencia, 0)
        open_file.close()
        open_file = open("Transportes.txt", "w")
        open_file.write(placa)
        open_file.close()
        messagebox.showinfo(title = "Delete", message = "El transporte ha sido eliminado exitosamente")
            
    else:
        messagebox.showerror(title = "Error", message = "No existe un transporte con esa matricula")
        
    
def deleteTransportes(delete,ContarLineas,contador):
    if contador == 10:
        return TransformarSTR(delete)
    else:
        delete.pop(ContarLineas)
        return deleteTransportes(delete,ContarLineas,contador+1)


def mostrar_transportes():
    ventana = tk.Tk()
    ventana.geometry("600x300")
    ventana.title("Mostrar Transportes")
    ventana.config(bg = "white")
    abrir = open("Transportes.txt")
    abrir2 = abrir.readlines()
    mostrar_datos = tk.Listbox(ventana)
    mostrar_datos.pack(fill=X, expand = YES)
    contador = 0
    for datos in abrir2:
        mostrar_datos.insert(contador,datos)
        contador += 1


    
#################################################################################################################################
def gestion_viaje(pantalla):
    frame = tk.Frame(pantalla)
    frame.pack()
    pantalla.title("Gestión de Viajes")
    pantalla.config(bg = "white")
    menu1 = Menu(pantalla)

    op1 = Menu(menu1,tearoff = 0)
    op1.add_command(label = "1 - Incluir Viaje",font = ("Times new roman","12"),
                    command = incluir_viaje)
    
    op1.add_command(label = "2 - Eliminar Transporte",font = ("Times new roman","12"),
                    command = eliminar_viaje)
    
    op1.add_command(label = "3 - Modificar Transporte",font = ("Times new roman","12"),
                    command = lambda: transicion(frame,modificar_transporte,pantalla))
    
    op1.add_command(label = "4 - Mostrar Transporte",font = ("Times new roman","12"),
                    command =  mostrar_viajes)
    
    op1.add_command(label = "5 - Retornar",font = ("Times new roman","12"),
                    command = lambda: transicion(frame,menu_administrativo,pantalla))
    
    menu1.add_cascade(label =" Gestión de Transporte",font = ("Times new roman","12"), menu = op1)
    pantalla.config(menu=menu1)
    pantalla.mainloop()

def incluir_viaje():
    window = tk.Tk()
    window.geometry("600x600")
    window.config(bg="gray")
    window.title("Registrando Viaje")
    provincia_salida = tk.StringVar()
    ciudad_salida = tk.StringVar()
    fecha_salida = tk.StringVar()
    hora_salida = tk.StringVar()
    provincia_llegada = tk.StringVar()
    ciudad_llegada = tk.StringVar()
    fecha_llegada = tk.StringVar()
    hora_llegada = tk.StringVar()
    precio_normal = tk.StringVar()
    precio_economico = tk.StringVar()
    precio_vip = tk.StringVar()

    etiqueta2 =tk.Label(window,text="Provincia de salida: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=80)
    ProvinciaS = tk.Entry(window,textvariable = provincia_salida, font=("Times new roman","12"), fg="Black").place(x=159,y=80)
        
    etiqueta22= tk.Label(window, text= "Ciudad de salida: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=120)
    CiudadS = tk.Entry(window,textvariable = ciudad_salida,font=("Times new roman","12"),fg="Black").place(x=159,y=120)
    
    etiqueta3 = tk.Label(window,text="Fecha de salida: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=160)
    FechaS = tk.Entry(window,textvariable = fecha_salida,font=("Times new roman","12"),fg="Black").place(x=159,y=160)

    etiqueta4 = tk.Label(window,text="Hora de salida: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=200)
    HoraS = tk.Entry(window,textvariable = hora_salida,font=("Times new roman","12"),fg="Black").place(x=159,y=200)

    etiqueta5 = tk.Label(window,text="Provincia de llegada: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=240)
    ProvinciaL = tk.Entry(window,textvariable = provincia_llegada,font=("Times new roman","12"),fg="Black").place(x=159,y=240)

    etiqueta6 = tk.Label(window,text="Ciudad de llegada: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=280)
    CiudadL = tk.Entry(window,textvariable = ciudad_llegada,font=("Times new roman","12"),fg="Black").place(x=159,y=280)

    etiqueta7 =tk.Label(window,text="Fecha de llegada: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=320)
    FechaL = tk.Entry(window,textvariable = fecha_llegada,font=("Times new roman","12"),fg="Black").place(x=159,y=320)

    etiqueta8 =tk.Label(window,text="Hora de llegada: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=360)
    HoraL = tk.Entry(window,textvariable = hora_llegada,font=("Times new roman","12"),fg="Black").place(x=159,y=360)

    etiqueta9 =tk.Label(window,text="Precio de normal: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=400)
    PrecioN = tk.Entry(window,textvariable = precio_normal,font=("Times new roman","12"),fg="Black").place(x=159,y=400)

    etiqueta10 =tk.Label(window,text="Precio de económico: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=440)
    PrecioE = tk.Entry(window,textvariable = precio_economico,font=("Times new roman","12"),fg="Black").place(x=159,y=440)
    
    etiqueta11 =tk.Label(window,text="Precio de VIP: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=480)
    PrecioV = tk.Entry(window,textvariable = precio_vip,font=("Times new roman","12"),fg="Black").place(x=159,y=480)
    
    tk.Button(window,text="Agregar",font = ("Times new roman","12"),bg="#e7c4e5",fg="Black",
              command = lambda: registrar_transporte(placa.get(),transporte.get(),marca.get(), modelo.get(), año.get(), empresa.get(),
                                                     asientos_normal.get(),asientos_economicos.get(),asientos_vip.get())).place(x=179,y=520)

    
    window.mainloop()

def registrar_viaje(provincia_salida,ciudad_salida,fecha_salida,hora_salida,provincia_llegada,ciudad_llegada,fecha_llegada,hora_llegada,precio_normal,
                         precio_economico,precio_vip):
     almacenar_viaje = open("Viajes.txt","a")
     almacenar_viaje.write(provincia_salida +"\n")
     almacenar_viaje.write(ciudad_salida+"\n")
     almacenar_viaje.write(fecha_salida +"\n")
     almacenar_viaje.write(hora_salida +"\n")
     almacenar_viaje.write(provincia_llegada +"\n")
     almacenar_viaje.write(ciudad_llegada +"\n")
     almacenar_viaje.write(fecha_llegada +"\n")
     almacenar_viaje.write(hora_llegada+"\n")
     almacenar_viaje.write(precio_normal +"\n")
     almacenar_viaje.write(precio_economico +"\n")
     almacenar_viaje.write(precio_vip +"\n")
     almacenar_viaje.write("************************************************"+"\n")
     almacenar_viaje.close()
     messagebox.showinfo(title = "Viaje añadido",message = "¡El viaje se ha registrado exitosamente!")



def eliminar_viaje():
    window = tk.Tk()
    window.geometry("600x300")
    window.title("Eliminando viaje")
    
    placa = tk.StringVar()
    
    etiqueta1 = tk.Label(window, text = "Placa del transporte a eliminar").pack()
    Placa = tk.Entry(window,textvariable = placa, font=("Times new roman","12"), bg="white", fg="Black")
    Placa.pack()

    tk.Button(window,text="Eliminar",font = ("Times new roman","12"),bg="#e7c4e5",fg="Black",
              command = lambda: eliminar_trans(Placa.get())).pack()
    
    window.mainloop()


def eliminar_viaj(placa):
    open_file = open("Transportes.txt")
    transportes = open_file.readlines()
    if (("Placa"+placa+"\n")in transportes):
        placa=str(placa)
        potencia = transportes.index(cedula+"\n")
        placa = deleteTransporte(transportes, potencia, 0)
        open_file.close()
        open_file = open("Transportes.txt", "w")
        open_file.write(placa)
        open_file.close()
        messagebox.showinfo(title = "Delete", message = "El transporte ha sido eliminado exitosamente")
    else:
        messagebox.showerror(title = "Error", message = "No existe un transporte con la placa ingresada")
        
    
def deleteTransporte(delete,ContarLineas,contador):
    if contador == 10:
        return TransformarSTR(delete)
    else:
        delete.pop(ContarLineas)
        return deleteEmpresa(delete,ContarLineas,contador+1)




def mostrar_viajes():
    ventana = tk.Tk()
    ventana.geometry("600x300")
    ventana.title("Mostrar Viajes")
    ventana.config(bg = "white")
    abrir = open("Viajes.txt")
    abrir2 = abrir.readlines()
    mostrar_datos = tk.Listbox(ventana)
    mostrar_datos.pack(fill=X, expand = YES)
    contador = 0
    for datos in abrir2:
        mostrar_datos.insert(contador,datos)
        contador += 1























"""
    etiqueta9 =tk.Label(window,text=" VIP: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=400)
    Asiento_vip = tk.Entry(window,textvariable = asientos_vip,font=("Times new roman","12"),fg="Black").place(x=159,y=400)
"""    
   

















"""

    def consulta_historial():
        ventana5 = Tk()
        ventana5.geometry("250x200")
        ventana5.title("Menú administrativo")
        ventana5.config(bg = "Turquoise")
        ventana5.iconbitmap("python.ico")
        menu4 = Menu(ventana5)
        op4 = Menu(menu4,tearoff = 0)
        op4.add_command(label = "1 - Rango de fecha de salida",font=("Times new roman","12"))
        op4.add_command(label = "2 - Rango de fecha de llegada",font=("Times new roman","12"))
        op4.add_command(label = "3 - Rango de fecha de la reservacion",font=("Times new roman","12"))
        op4.add_command(label = "4 - Lugar de salida",font=("Times new roman","12"))
        op4.add_command(label = "5 - Lugar de llegada",font=("Times new roman","12"))
        op4.add_command(label = "6 - Salir",font=("Times new roman","12"),command = menuAdministrativo)
        menu4.add_cascade(label=" Consultar historial de reservaciones",font=("Times new roman","12"), menu = op4)
        ventana5.config(menu=menu4)
        ventana5.mainloop()

    def estadisticas():
        ventana6 = Tk()
        ventana6.geometry("250x200")
        ventana6.title("Menú administrativo")
        ventana6.config(bg = "Turquoise")
        ventana6.iconbitmap("python.ico")
        menu5 = Menu(ventana6)  
        
        op5 = Menu(menu5,tearoff = 0)
        menu5.add_cascade(label=" Estadísticas de viaje",font=("Times new roman","12"), menu = op5)
        ventana6.config(menu=menu5)
        ventana6.mainloop()
        return menu_administrativo()

def menu_general():
    ventana7 = Tk()
    ventana7.geometry("250x200")
    ventana7.config(bg = "Turquoise")
    ventana7.title("Menu General")
    ventana7.iconbitmap("python.ico")
    
    menu6 = Menu(ventana7)
    ventana7.config(menu=menu6)
    
    op6 = Menu(menu6,tearoff = 0)
    op6.add_command(label = "1 - Consulta de viajes",font=("Times new roman","12"),command = consultaViajes)
    op6.add_command(label = "2 - Reservacion de viaje",font=("Times new roman","12"),comman = reservacion)
    op6.add_command(label = "3 - Cancelacion de viaje",font=("Times new roman","12"), command = cancelacion)
    op6.add_command(label = "4 - Salir de menu general",font=("Times new roman","12"),command = ventanaPrincipal)
    menu6.add_cascade(label="2 - Opciones de usuario general", font=("Times new roman","12"), menu = op6)

def consulta_viajes():
    ventana8 = Tk()
    ventana8.geometry("250x200")
    ventana8.title("Menú general")
    ventana8.config(bg = "Turquoise")
    ventana8.iconbitmap("python.ico")
    menu7 = Menu(ventana8)
    ventana8.config(menu=menu7)   
    op7 = Menu(menu7,tearoff = 0)
    op7.add_command(label = "1 - Empresa",font=("Times new roman","12"))
    op7.add_command(label = "2 - Lugar de salida",font=("Times new roman","12"))
    op7.add_command(label = "3 - Lugar de llegada",font=("Times new roman","12"))
    op7.add_command(label = "4 - Rango de fecha de salida",font=("Times new roman","12"))
    op7.add_command(label = "5 - Rango de fecha de llegada",font=("Times new roman","12"))
    op7.add_command(label = "6 - Salir",font=("Times new roman","12"),command = menuGeneral)
    menu7.add_cascade(label=" Consulta de viajes",font=("Times new roman","12"), menu = op7)
    ventana8.config(menu=menu7)
    ventana8.mainloop()

def reservacion():
    ventana9 = Tk()
    ventana9.geometry("250x200")
    ventana9.title("Menú general")
    ventana9.config(bg = "Turquoise")
    ventana9.iconbitmap("python.ico")
    menu8 = Menu(ventana9)  
        
    op8 = Menu(menu8,tearoff = 0)
        
    ventana9.config(menu=menu8)
    ventana9.mainloop()
        

def cancelacion():
    ventana10 = Tk()
    ventana10.geometry("250x200")
    ventana10.title("Menú general")
    ventana10.config(bg = "Turquoise")
    ventana10.iconbitmap("python.ico")
    menu9 = Menu(ventana10)  
    op9 = Menu(menu9,tearoff = 0)
    ventana10.config(menu=menu9)
    ventana10.mainloop()
    


"""    
iniciar()  
