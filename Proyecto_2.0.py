#Importacion de las librerias

from tkinter import *
import tkinter as tk
from tkinter import messagebox



#############################################################################################################################################
#Nomnbre: iniciar
#Entradas: No recibe
#Salidas: Generar una ventana
#Restricciones: No recibe

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

#Nomnbre: ventana_principal
#Entradas: panatalla
#Salidas: Una interfaz con un menu principal
#Restricciones: No recibe
  
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

#Nomnbre: menu_administrativo
#Entradas: pantalla
#Salidas: Generar un menu administrativo
#Restricciones: No recibe

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

#Nomnbre: menu_general
#Entradas: pantalla
#Salidas: Generar un menu general
#Restricciones: No recibe

def menu_general(pantalla):
    frame = tk.Frame(pantalla)
    pantalla.title("Menú general")
    pantalla.config(bg = "lightgreen")

    menu = Menu(pantalla)
    pantalla.config(menu=menu)

    opAdmi = Menu(menu,tearoff = 0)
    opAdmi.add_command(label = "1 - Consulta de viajes",font=("Times new roman","12"),
                       command = lambda: transicion(frame,consultar_viaje,pantalla))
    opAdmi.add_command(label = "2 - Apartado de reservaccion",font=("Times new roman","12"),
                       command = lambda: transicion(frame,reservacion_interfaz,pantalla))
    opAdmi.add_command(label = "3 - Cancelacion de viajes",font=("Times new roman","12"),
                       command = cancelar_reservacion)
    menu.add_cascade(label="1 - Opciones Generales", font=("Times new roman","12"), menu = opAdmi)
    frame.pack()
    
#Nomnbre: solicitar_clave
#Entradas: pantalla
#Salidas: Solicitar una clave al usuario
#Restricciones: No recibe

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

#Nomnbre: verificar_clave
#Entradas: clave y pantalla
#Salidas: Generar una ventana
#Restricciones: No recibe
    
def verificar_clave(clave,pantalla,frame):
    verificar = leer_archivo_claves()
    if (clave in verificar):
        transicion(frame,menu_administrativo,pantalla)
    else:
        messagebox.askyesno("Error","La contraseña es incorrecta o no esta registrada. ¿Desea continuar o intentar otra vez?")

#Nomnbre: leer_archivo_claves
#Entradas: No recibe
#Salidas: verificar si se encuentra la clave en un archivo.txt
#Restricciones: No recibe

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

#Nomnbre: gestion_empresa
#Entradas: pantalla
#Salidas: Un menu de gestion de empresas
#Restricciones: No recibe

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

#Nomnbre: incluir_empresa
#Entradas: No recibe
#Salidas: Una interfaz donde pedira algunos datos
#Restricciones: No recibe
    
def incluir_empresa():
    window = tk.Tk()
    window.geometry("600x300")
    window.title("Registrando Empresa")
    cedula = tk.StringVar()
    nombre = tk.StringVar()
    provincia = tk.StringVar()
    direccion = tk.StringVar()
    señas = tk.StringVar()
    
    etiqueta1 = tk.Label(window,text="Cédula Empresa: ",font=("Times new roman","12"), fg="black").place(x=5,y=40)
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
    
#Nomnbre: registrar_empresa
#Entradas: 5 parametros
#Salidas: registrar la empresa en un archivo.txt
#Restricciones: cedula debe contener 10 digitos
    
def registrar_empresa(cedula,nombre,provincia,direccion,señas):
    almacenar_empresas = open("Empresas.txt","a")
    if len (cedula)==10:
        archivo= open("Empresas.txt")
        archivo2 = archivo.readlines()
        abrirTrans= open("Transportes.txt")
        abrir=abrirTrans.readlines()
        if (("Cedula Empresa:"+cedula + "\n") in archivo2):
            messagebox.showerror(title = "Error", message = "La empresa ya existe")
                
        else:
            almacenar_empresas.write("Cedula Empresa:"+ cedula +"\n")
            almacenar_empresas.write("Nombre:"+ nombre +"\n")
            almacenar_empresas.write("Provincia:"+ provincia +"\n")
            almacenar_empresas.write("Dirección:"+ direccion +"\n")
            almacenar_empresas.write("Señas exactas:"+ señas +"\n")
            almacenar_empresas.write("************************************************"+"\n")
            almacenar_empresas.close()
            messagebox.showinfo(title = "Empresa añadida",message = "¡La empresa se ha registrado exitosamente!")
    else:
        messagebox.showerror(title = "Error", message = "La cedula debe tener 10 digitos")

#Nomnbre: eliminar_empresa
#Entradas: No recibe
#Salidas: Generar un menu de eliminar empresa
#Restricciones: No recibe
        
def eliminar_empresa():
    window = tk.Tk()
    window.geometry("600x300")
    window.title("Eliminando Empresa")
    
    etiqueta1 = tk.Label(window, text = "Cedula a eliminar").pack()
    Cedula = tk.Entry(window,text = "", font=("Times new roman","12"), bg="white", fg="Black")
    Cedula.pack()

#Pasa los datos a la siguiente funcion
    def eliminar_emp2():
        variable = Cedula.get()
        return eliminar_emp(variable)
    
    tk.Button(window,text="Eliminar",font = ("Times new roman","12"),bg="#e7c4e5",fg="Black",
              command =  eliminar_emp2).pack()
    
    window.mainloop()

#Verifica si la cedula de la empresa que va a eliminar esta en el archivo
def eliminar_emp(cedula_juridica):
    open_file = open("Empresas.txt")
    empresas = open_file.readlines()
    open_file2 = open("Transportes.txt")
    transportes = open_file2.readlines()
    if (("Cedula Empresa:"+cedula_juridica+"\n")in empresas):
        if (("Cedula Empresa:"+cedula_juridica+ "\n") in transportes):
            messagebox.showerror(title = "Error", message = "La empresa esta asociada un transporte")
        else:
            cedula_juridica=str(cedula_juridica)
            potencia = empresas.index("Cedula Empresa:"+cedula_juridica+"\n")
            cedula_juridica = deleteEmpresa(empresas, potencia, 0)
            open_file.close()
            open_file = open("Empresas.txt", "w")
            open_file.write(cedula_juridica)
            open_file.close()
            messagebox.showinfo(title = "Delete", message = "La empresa ha sido eliminada exitosamente")
            
    else:
        messagebox.showerror(title = "Error", message = "No existe una empresa con la cedula juridica escrita")
        
    #elimina las lineas 
def deleteEmpresa(delete,ContarLineas,contador):
    if contador == 6:
        return TransformarSTR(delete)
    else:
        delete.pop(ContarLineas)
        return deleteEmpresa(delete,ContarLineas,contador+1)

############################################################################################################################################
#Nomnbre: mostrar_empresas
#Entradas: No recibe
#Salidas: Generar una lista con empresas registradas
#Restricciones: No recibe
    
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
#Nomnbre: modificar_empresa
#Entradas: No recibe
#Salidas: Generar un menu de modificar empresas
#Restricciones: No recibe
        
def modificar_empresa():
     ventana=tk.Tk()
     ventana.title("Modificar Empresa")
     ventana.geometry("600x300")
    
     Cedula=tk.Label(ventana,text="Cédula Empresa:",font=("Times New Roman",12), fg="Black")
     Cedula.pack()
    
     cedula=tk.Entry(ventana,text="", font=("Times New Roman", 12), fg="Black")
     cedula.pack()
    
     boton=tk.Button(ventana,text="Modificar Empresa",font=("Times New Roman",12),fg="Black",
                          command = lambda: modificar_empresa_aux(cedula.get()))
     boton.pack()
    
     boton2 = tk.Button(ventana,text="Salir",font=("Times New Roman",12),fg="Black",
               command = lambda: gestion_empresa())
     boton2.pack()
    
     ventana.mainloop()

#Nombre: modificar_empresa_aux
#Entradas: cedula
#Salidas: Buscar la cedula de la empresa a modificar
#Restricciones: No recibe
     
def modificar_empresa_aux(cedula):
     abrir_file_empresas = open("Empresas.txt")
     empresas = abrir_file_empresas.readlines()
     if("Cedula Empresa:"+cedula+"\n")in empresas:
          cedula=str(cedula)
          indice = empresas.index("Cedula Empresa:"+cedula+"\n")
          cedula = modificar(empresas, indice+1, 1)
          abrir_file_empresas.close()

     else:
          messagebox.showerror(title = "Error", message = "La cedula no se encuentra registrada")
        
#Pide los nuevos datos
def modificar(datos,indice,cont):
    ventana=Tk()
    ventana.geometry("600x300")
    
    etiqueta=tk.Label(ventana,text="Empresa:")
    etiqueta.pack()
    entry=tk.Entry(ventana)
    entry.pack()
    
    etiqueta2=tk.Label(ventana,text="Provicia:")
    etiqueta2.pack()
    entry2=tk.Entry(ventana)
    entry2.pack()
    
    etiqueta3=tk.Label(ventana,text="Ciudad:")
    etiqueta3.pack()
    entry3=tk.Entry(ventana)
    entry3.pack()

    etiqueta4=tk.Label(ventana,text="Direccion:")
    etiqueta4.pack()
    entry4=tk.Entry(ventana)
    entry4.pack()

    etiqueta5=tk.Label(ventana,text="Señas Exactas:")
    etiqueta5.pack()
    entry5=tk.Entry(ventana)
    entry5.pack()
    
    def modificar_aux():
        empresa = entry.get()
        provincia = entry2.get()
        ciudad = entry3.get()
        direccion = entry4.get()
        señas = entry5.get()
        return modificar2_aux(empresa,provincia,ciudad,direccion,señas,datos,indice,cont)
    boton=tk.Button(ventana,text="Modificar",command=modificar_aux)
    boton.pack()

#Registra la empresa con los datos modificados 


def modificar2_aux(empresa,provincia,ciudad,direccion,señas,datos,indice,cont):
    archivo = open("Empresas.txt","w")
    datos[indice]=("Nombre:"+empresa+"\n")
    datos[indice+1]=("Provincia:"+provincia+"\n")
    datos[indice+2]=("Ciudad:"+ciudad+"\n")
    datos[indice+3]=("Direccion:"+direccion+"\n")
    datos[indice+4]=("Señas Exactas:"+señas+"\n")
    datos[indice+5]=("************************************************"+"\n")

    
    archivo.write( TransformarSTR(datos))
    


#############################################################################################################################################
#############################################################################################################################################

#Nomnbre: gestion_transporte
#Entradas: pantalla
#Salidas: Generar un menu de transporte
#Restricciones: No recibe

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
                    command = modificar_transporte)
    
    op1.add_command(label = "4 - Mostrar Transporte",font = ("Times new roman","12"),
                    command = mostrar_transportes)
    
    op1.add_command(label = "5 - Retornar",font = ("Times new roman","12"),
                    command = lambda: transicion(frame,menu_administrativo,pantalla))
    
    menu1.add_cascade(label =" Gestión de Transporte",font = ("Times new roman","12"), menu = op1)
    pantalla.config(menu=menu1)
    pantalla.mainloop()
    
#Nomnbre: incluir_transporte
#Entradas: No recibe
#Salidas: Generar una ventana pidiendo algunos datos
#Restricciones: No recibe

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

#Nomnbre: registrar_transporte
#Entradas: 9 parametros
#Salidas: registrar un transporte
#Restricciones: No recibe

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
        almacenar_transporte.write("Cedula Empresa:"+empresa +"\n")
        almacenar_transporte.write("Asientos Normales:"+asientos_normal +"\n")
        almacenar_transporte.write("Asientos Economicos:"+asientos_economicos+"\n")
        almacenar_transporte.write("Asientos VIP:"+asientos_vip +"\n")
        almacenar_transporte.write("************************************************"+"\n")
        almacenar_transporte.close()
        messagebox.showinfo(title = "Transporte añadido",message = "¡El transporte se ha registrado exitosamente!")

#Nomnbre: eliminar_transporte
#Entradas: No recibe
#Salidas: Generar una ventana pidiendo algunos datos
#Restricciones: No recibe

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

#Nomnbre: eliminar_trans
#Entradas: placa
#Salidas: verificar si la placase encuentra en un archivo.txt
#Restricciones: No recibe

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
        
#Eliminar las lineas en el archivo.txt

def deleteTransportes(delete,ContarLineas,contador):
    if contador == 10:
        return TransformarSTR(delete)
    else:
        delete.pop(ContarLineas)
        return deleteTransportes(delete,ContarLineas,contador+1)

#Nomnbre: mostrar_transportes
#Entradas: No recibe
#Salidas: Generar una ventana con una lista de los transportes 
#Restricciones: No recibe
    
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

#Nomnbre: modificar_transporte
#Entradas: No recibe
#Salidas: Generar una ventana pidiendo algunos datos
#Restricciones: No recibe

def modificar_transporte():
    ventana=tk.Tk()
    ventana.title("Modificar Transporte")
    ventana.geometry("600x600")
    
    Placa=tk.Label(ventana,text="Placa:",font=("Times New Roman",12), fg="Black")
    Placa.pack()
    
    placa=tk.Entry(ventana,text="", font=("Times New Roman", 12), fg="Black")
    placa.pack()
    
    boton=tk.Button(ventana,text="Modificar Transporte",font=("Times New Roman",12),fg="Black",
                          command = lambda: modificar_transporte_aux(placa.get()))
    boton.pack()
    
    boton2 = tk.Button(ventana,text="Salir",font=("Times New Roman",12),fg="Black",
               command = lambda: gestion_transporte())
    boton2.pack()
    
    ventana.mainloop()

#Nomnbre: modificar_transporte_aux
#Entradas: No recibe
#Salidas: verificar si la placa se encuentra en un archivo.txt
#Restricciones: No recibe

def modificar_transporte_aux(placa):
     abrir_file_transportes = open("Transportes.txt")
     transportes = abrir_file_transportes.readlines()
     if("Placa:"+placa+"\n")in transportes:
          placa=str(placa)
          indice = transportes.index("Placa:"+placa+"\n")
          placa = modificar_trans(transportes, indice+1, 1)
          abrir_file_transportes.close()

     else:
          messagebox.showerror(title = "Error", message = "La placa no se encuentra registrada")
        
#Pide los nuevos datos
def modificar_trans(datos,indice,cont):
    ventana=Tk()
    ventana.geometry("600x300")
    
    etiqueta=tk.Label(ventana,text="Tipo:")
    etiqueta.pack()
    entry=tk.Entry(ventana)
    entry.pack()
    
    etiqueta2=tk.Label(ventana,text="Marca:")
    etiqueta2.pack()
    entry2=tk.Entry(ventana)
    entry2.pack()
    
    etiqueta3=tk.Label(ventana,text="Modelo:")
    etiqueta3.pack()
    entry3=tk.Entry(ventana)
    entry3.pack()

    etiqueta4=tk.Label(ventana,text="Año:")
    etiqueta4.pack()
    entry4=tk.Entry(ventana)
    entry4.pack()

    etiqueta5=tk.Label(ventana,text="Cedula Empresa:")
    etiqueta5.pack()
    entry5=tk.Entry(ventana)
    entry5.pack()

    etiqueta6=tk.Label(ventana,text="Asientos Normales:")
    etiqueta6.pack()
    entry6=tk.Entry(ventana)
    entry6.pack()

    etiqueta7=tk.Label(ventana,text="Asientos Economicos:")
    etiqueta7.pack()
    entry7=tk.Entry(ventana)
    entry7.pack()

    etiqueta8=tk.Label(ventana,text="Asientos VIP:")
    etiqueta8.pack()
    entry8=tk.Entry(ventana)
    entry8.pack()
    
    def modificar_aux2():
        tipo = entry.get()
        marca = entry2.get()
        modelo = entry3.get()
        año = entry4.get()
        empresa = entry5.get()
        asientos_normales = entry6.get()
        asientos_economicos = entry7.get()
        asientos_vip = entry8.get()
        return modificar_trans2_aux(tipo,marca,modelo,año,empresa,asientos_normales,asientos_economicos,asientos_vip,datos,indice,cont)
    
    boton=tk.Button(ventana,text="Aceptar",command = modificar_aux2)
    boton.pack()

#Registra los nuevos datos del transporte

def modificar_trans2_aux(tipo,marca,modelo,año,empresa,asientos_normales,asientos_economicos,asientos_vip,datos,indice,cont):
    archivo = open("Transportes.txt","w")
    datos[indice]=("Tipo de transporte:"+tipo+"\n")
    datos[indice+1]=("Provincia:"+marca+"\n")
    datos[indice+2]=("Ciudad:"+modelo+"\n")
    datos[indice+3]=("Direccion:"+año+"\n")
    datos[indice+4]=("Cedula Empresa:"+empresa+"\n")
    datos[indice+5]=("Asientos Normales:"+asientos_normales+"\n")
    datos[indice+6]=("Asientos Economicos:"+asientos_economicos+"\n")
    datos[indice+7]=("Asientos VIP:"+asientos_vip+"\n")
    
    archivo.write( TransformarSTR(datos))
    
   
#################################################################################################################################
#Nomnbre: gestion_viaje
#Entradas: pantalla
#Salidas: Generar un menu de gestion de viajes 
#Restricciones: No recibe

def gestion_viaje(pantalla):
    frame = tk.Frame(pantalla)
    frame.pack()
    pantalla.title("Gestión de Viajes")
    pantalla.config(bg = "white")
    menu1 = Menu(pantalla)

    op1 = Menu(menu1,tearoff = 0)
    op1.add_command(label = "1 - Incluir Viaje",font = ("Times new roman","12"),
                    command = incluir_viaje)
    
    op1.add_command(label = "2 - Eliminar Viaje",font = ("Times new roman","12"),
                    command = eliminar_viaje)
    
    op1.add_command(label = "3 - Modificar Viaje",font = ("Times new roman","12"),
                    command = modificar_viajes)
    
    op1.add_command(label = "4 - Mostrar Viaje",font = ("Times new roman","12"),
                    command =  mostrar_viajes)
    
    op1.add_command(label = "5 - Retornar",font = ("Times new roman","12"),
                    command = lambda: transicion(frame,menu_administrativo,pantalla))
    
    menu1.add_cascade(label =" Gestión de Viajes",font = ("Times new roman","12"), menu = op1)
    pantalla.config(menu=menu1)
    pantalla.mainloop()

#Nomnbre: incluir_viaje
#Entradas: No recibe
#Salidas: Generar una ventana pidiendo datos
#Restricciones: No recibe

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
    empresa = tk.StringVar()
    transporte = StringVar()

    etiqueta2 =tk.Label(window,text="Provincia de salida: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=40)
    ProvinciaS = tk.Entry(window,textvariable = provincia_salida, font=("Times new roman","12"), fg="Black")
    ProvinciaS.place(x=159,y=40)
        
    etiqueta22= tk.Label(window, text= "Ciudad de salida: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=80)
    CiudadS = tk.Entry(window,textvariable = ciudad_salida,font=("Times new roman","12"),fg="Black")
    CiudadS.place(x=159,y=80)
    
    etiqueta3 = tk.Label(window,text="Fecha de salida: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=120)
    FechaS = tk.Entry(window,textvariable = fecha_salida,font=("Times new roman","12"),fg="Black")
    FechaS.place(x=159,y=120)

    etiqueta4 = tk.Label(window,text="Hora de salida: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=160)
    HoraS = tk.Entry(window,textvariable = hora_salida,font=("Times new roman","12"),fg="Black")
    HoraS.place(x=159,y=160)

    etiqueta5 = tk.Label(window,text="Provincia de llegada: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=200)
    ProvinciaL = tk.Entry(window,textvariable = provincia_llegada,font=("Times new roman","12"),fg="Black")
    ProvinciaL.place(x=159,y=200)

    etiqueta6 = tk.Label(window,text="Ciudad de llegada: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=240)
    CiudadL = tk.Entry(window,textvariable = ciudad_llegada,font=("Times new roman","12"),fg="Black")
    CiudadL.place(x=159,y=240)

    etiqueta7 =tk.Label(window,text="Fecha de llegada: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=280)
    FechaL = tk.Entry(window,textvariable = fecha_llegada,font=("Times new roman","12"),fg="Black")
    FechaL.place(x=159,y=280)

    etiqueta8 =tk.Label(window,text="Hora de llegada: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=320)
    HoraL = tk.Entry(window,textvariable = hora_llegada,font=("Times new roman","12"),fg="Black")
    HoraL.place(x=159,y=320)

    etiqueta9 =tk.Label(window,text="Precio de normal: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=360)
    PrecioN = tk.Entry(window,textvariable = precio_normal,font=("Times new roman","12"),fg="Black")
    PrecioN.place(x=159,y=360)

    etiqueta10 =tk.Label(window,text="Precio de económico: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=400)
    PrecioE = tk.Entry(window,textvariable = precio_economico,font=("Times new roman","12"),fg="Black")
    PrecioE.place(x=159,y=400)
    
    etiqueta11 =tk.Label(window,text="Precio de VIP: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=440)
    PrecioV = tk.Entry(window,textvariable = precio_vip,font=("Times new roman","12"),fg="Black")
    PrecioV.place(x=159,y=440)


    etiqueta12 =tk.Label(window,text="Cedula de la Empresa: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=480)
    Empresa = tk.Entry(window,textvariable = empresa,font=("Times new roman","12"),fg="Black")
    Empresa.place(x=159,y=480)

    etiqueta13 =tk.Label(window,text="Placa del Transporte: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=520)
    Transporte = tk.Entry(window,textvariable = transporte,font=("Times new roman","12"),fg="Black")
    Transporte.place(x=159,y=520)
    
    tk.Button(window,text="Agregar",font = ("Times new roman","12"),bg="#e7c4e5",fg="Black",
              command = lambda: registrar_viaje(ProvinciaS.get(),CiudadS.get(),FechaS.get(),HoraS.get()
                                                ,ProvinciaL.get(),CiudadL.get(),FechaL.get(),HoraL.get()
                                                ,PrecioN.get(),PrecioE.get(),PrecioV.get(),Empresa.get(),Transporte.get())).place(x=200,y=560)

    
    window.mainloop()

#Nomnbre: registrar_viaje
#Entradas: 14 parametros
#Salidas: registrar un viaje en un archivo.txt
#Restricciones: No recibe

def registrar_viaje(provincia_salida,ciudad_salida,fecha_salida,hora_salida,provincia_llegada,ciudad_llegada,fecha_llegada,hora_llegada,precio_normal,
                         precio_economico,precio_vip,empresa,transporte):
    
    Archivo = "Viajes.txt"
    almacenar_viaje = open(Archivo,"a")
    NumeroViaje = generarNum()
    almacenar_viaje.write("Numero:"+NumeroViaje+"\n")
    almacenar_viaje.write("Provincia de Salida:"+provincia_salida +"\n")
    almacenar_viaje.write("Ciudad de Salida:"+ciudad_salida+"\n")
    almacenar_viaje.write("Fecha de Salida:"+fecha_salida +"\n")
    almacenar_viaje.write("Hora de Salida:"+hora_salida +"\n")
    almacenar_viaje.write("Provincia de llegada:"+provincia_llegada +"\n")
    almacenar_viaje.write("Ciudad de Llegada:"+ciudad_llegada +"\n")
    almacenar_viaje.write("Fecha de Llegada:"+fecha_llegada +"\n")
    almacenar_viaje.write("Hora de Llegada:"+hora_llegada+"\n")
    almacenar_viaje.write("Precio Normal:"+precio_normal +"\n")
    almacenar_viaje.write("Precio Económico:"+precio_economico +"\n")
    almacenar_viaje.write("Precio VIP:"+precio_vip +"\n")
    almacenar_viaje.write("Cedula Empresa:"+empresa+"\n")
    almacenar_viaje.write("Placa Transporte:"+transporte+"\n")
    almacenar_viaje.write("************************************************"+"\n")
    almacenar_viaje.close()
    messagebox.showinfo(title = "Viaje añadido",message = "¡El viaje se ha registrado exitosamente!")

#Genera un numero automaticamente

def generarNum():
    archivo="Viajes.txt"
    anexar_archivo=open (archivo,'a')
    lista_viajes= open (archivo,'r')
    cont=0
    for linea in lista_viajes:
        cont += 1
    lista_viajes.close()
    return str(cont//12+1)


def eliminar_viaje():
    window = tk.Tk()
    window.geometry("600x300")
    window.title("Eliminando viaje")
    numero = tk.StringVar()
    
    etiqueta1 = tk.Label(window, text = "Numero del viaje a eliminar").pack()
    Numero = tk.Entry(window,textvariable = numero, font=("Times new roman","12"), bg="white", fg="Black")
    Numero.pack()

    tk.Button(window,text="Aceptar",font = ("Times new roman","12"),bg="#e7c4e5",fg="Black",
              command = lambda: eliminar_viaj(Numero.get())).pack()
    
    window.mainloop()


def eliminar_viaj(numero):
    open_file = open("Viajes.txt")
    viajes = open_file.readlines()
    if (("Numero:"+numero+"\n")in viajes):
        numero=str(numero)
        potencia = viajes.index("Numero:"+numero+"\n")
        numero = deleteViaje(viajes, potencia, 0)
        open_file.close()
        open_file = open("Viajes.txt", "w")
        open_file.write(numero)
        open_file.close()
        messagebox.showinfo(title = "Delete", message = "El viaje ha sido eliminado exitosamente")
    else:
        messagebox.showerror(title = "Error", message = "No existe un viaje con el numero ingresado")
        
    
def deleteViaje(delete,ContarLineas,contador):
    if contador == 15:
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




##############################################################################################################################################

#Nomnbre: modificar_viajes
#Entradas: No recibe
#Salidas: Generar una ventana pidiendo algunos datos
#Restricciones: No recibe

def modificar_viajes():
    ventana=tk.Tk()
    ventana.title("Modificar Transporte")
    ventana.geometry("600x600")
    
    Numero=tk.Label(ventana,text="Numero:",font=("Times New Roman",12), fg="Black")
    Numero.pack()
    
    numero=tk.Entry(ventana,text="", font=("Times New Roman", 12), fg="Black")
    numero.pack()
    
    boton=tk.Button(ventana,text="Modificar Viaje",font=("Times New Roman",12),fg="Black",
                          command = lambda: modificar_viaje_aux(numero.get()))
    boton.pack()
    
    boton2 = tk.Button(ventana,text="Salir",font=("Times New Roman",12),fg="Black",
               command = lambda: ventana.destroy)
    boton2.pack()
    
    ventana.mainloop()

#Nomnbre: modificar_viaje_aux
#Entradas: numero
#Salidas: verificar si el numero se encuentra en el archivo.txt
#Restricciones: No recibe

def modificar_viaje_aux(numero):
     abrir_file_viajes = open("Viajes.txt")
     viajes = abrir_file_viajes.readlines()
     if("Numero:"+numero+"\n")in viajes:
          numero=str(numero)
          indice = viajes.index("Numero:"+numero+"\n")
          numero = modificar_viaj(viajes, indice+1, 1)
          abrir_file_viajes.close()

     else:
          messagebox.showerror(title = "Error", message = "El numero del viaje no se encuentra registrado")
        
#Pide los nuevos datos
def modificar_viaj(datos,indice,cont):
    ventana=Tk()
    ventana.geometry("600x700")
    
    etiqueta=tk.Label(ventana,text="Provincia de Salida:")
    etiqueta.pack()
    entry=tk.Entry(ventana)
    entry.pack()
    
    etiqueta2=tk.Label(ventana,text="Ciudad de Salida:")
    etiqueta2.pack()
    entry2=tk.Entry(ventana)
    entry2.pack()
    
    etiqueta3=tk.Label(ventana,text="Fecha de Salida:")
    etiqueta3.pack()
    entry3=tk.Entry(ventana)
    entry3.pack()

    etiqueta4=tk.Label(ventana,text="Hora de Salida:")
    etiqueta4.pack()
    entry4=tk.Entry(ventana)
    entry4.pack()

    etiqueta5=tk.Label(ventana,text="Provincia de Llegada:")
    etiqueta5.pack()
    entry5=tk.Entry(ventana)
    entry5.pack()

    etiqueta6=tk.Label(ventana,text="Ciudad de Llegada:")
    etiqueta6.pack()
    entry6=tk.Entry(ventana)
    entry6.pack()

    etiqueta7=tk.Label(ventana,text="Fecha de Llegada:")
    etiqueta7.pack()
    entry7=tk.Entry(ventana)
    entry7.pack()

    etiqueta8=tk.Label(ventana,text="Hora de Llegada:")
    etiqueta8.pack()
    entry8=tk.Entry(ventana)
    entry8.pack()

    etiqueta9=tk.Label(ventana,text="Precio Normal:")
    etiqueta9.pack()
    entry9=tk.Entry(ventana)
    entry9.pack()

    etiqueta10=tk.Label(ventana,text="Precio Economico:")
    etiqueta10.pack()
    entry10=tk.Entry(ventana)
    entry10.pack()

    etiqueta11=tk.Label(ventana,text="Precio VIP:")
    etiqueta11.pack()
    entry11=tk.Entry(ventana)
    entry11.pack()

    etiqueta12=tk.Label(ventana,text="Cedula Empresa:")
    etiqueta12.pack()
    entry12=tk.Entry(ventana)
    entry12.pack()

    etiqueta13=tk.Label(ventana,text="Placa del Transporte:")
    etiqueta13.pack()
    entry13=tk.Entry(ventana)
    entry13.pack()


    
    def modificar_aux3():
        provincia_salida = entry.get()
        ciudad_salida = entry2.get()
        fecha_salida = entry3.get()
        hora_salida = entry4.get()
        provincia_llegada = entry5.get()
        ciudad_llegada = entry6.get()
        fecha_llegada = entry7.get()
        hora_llegada = entry8.get()
        precio_normal = entry9.get()
        precio_economico = entry10.get()
        precio_vip = entry11.get()
        empresa=entry12.get()
        transporte=entry13.get()
        

        
        return modificar_viaj2_aux(provincia_salida,ciudad_salida,fecha_salida,hora_salida,
                                   provincia_llegada,ciudad_llegada,fecha_llegada,hora_llegada,
                                   precio_normal,precio_economico,precio_vip,
                                   empresa,transporte,datos,indice,cont)
    
    boton=tk.Button(ventana,text="Aceptar",command = modificar_aux3)
    boton.pack()

#registra el viaje con los nuevos datos

def modificar_viaj2_aux(provincia_salida,ciudad_salida,fecha_salida,hora_salida,
                        provincia_llegada,ciudad_llegada,fecha_llegada,hora_llegada,
                        precio_normal,precio_economico,precio_vip,
                        empresa,transporte,datos,indice,cont):
    
    archivo = open("Viajes.txt","w")
    datos[indice]=("Provincia de Salida:"+provincia_salida+"\n")
    datos[indice+1]=("Ciudad de Salida:"+ciudad_salida+"\n")
    datos[indice+2]=("Fecha de Salida:"+fecha_salida+"\n")
    datos[indice+3]=("Hora de Salida:"+hora_salida+"\n")
    datos[indice+4]=("Provincia de Llegada:"+provincia_llegada+"\n")
    datos[indice+5]=("Ciudad de Llegada:"+ciudad_llegada+"\n")
    datos[indice+6]=("Fecha de Llegada:"+fecha_llegada+"\n")
    datos[indice+7]=("Hora de Llegada:"+hora_llegada+"\n")
    datos[indice+8]=("Precio Normal:"+precio_normal+"\n")
    datos[indice+9]=("Precio Económico:"+precio_economico+"\n")
    datos[indice+10]=("Precio VIP:"+precio_vip+"\n")
    datos[indice+11]=("Cedula Empresa:"+empresa+"\n")
    datos[indice+12]=("Placa Transporte:"+transporte+"\n")
    datos[indice+13]=("****************************************************"+"\n")
    
    archivo.write( TransformarSTR(datos))
###############################################################################################################################################3

#Nomnbre: reservacion_interfaz
#Entradas: pantalla
#Salidas: Generar una ventana pidiendo datos
#Restricciones: No recibe

def reservacion_interfaz(pantalla):
    ventana = tk.Frame(pantalla,height=300, width=600)
    ventana.pack()
    
    numero = tk.StringVar()
    nombre = tk.StringVar()
    asientos_normales = tk.StringVar()
    asientos_economicos = tk.StringVar()
    asientos_vip = tk.StringVar()
    
    etiqueta1 = tk.Label(ventana,text="Numero de Viaje: ",font=("Times new roman","12"), fg="black").place(x=5,y=40)
    Numero = tk.Entry(ventana,textvariable = numero, font=("Times new roman","12"), fg="Black")
    Numero.place(x=159,y=40)
    
    etiqueta2 =tk.Label(ventana,text="Nombre: ",font=("Times new roman","12"),fg="black").place(x=5,y=80)
    Nombre=tk.Entry(ventana,textvariable = nombre,font=("Times new roman","12"),fg="Black")
    Nombre.place(x=159,y=85)
    
    etiqueta3 = tk.Label(ventana,text="Asientos Normales: ",font=("Times new roman","12"),fg="black").place(x=5,y=120)
    Asientos_normales = tk.Entry(ventana,textvariable = asientos_normales,font=("Times new roman","12"),fg="Black")
    Asientos_normales.place(x=159,y=120)

    etiqueta4 = tk.Label(ventana,text="Asientos Economicos: ",font=("Times new roman","12"),fg="black").place(x=5,y=160)
    Asientos_economicos= tk.Entry(ventana,textvariable = asientos_economicos,font=("Times new roman","12"),fg="Black")
    Asientos_economicos.place(x=159,y=160)

    etiqueta5 = tk.Label(ventana,text="Asientos VIP: ",font=("Times new roman","12"),fg="black").place(x=5,y=200)
    Asientos_vip = tk.Entry(ventana,textvariable = asientos_vip,font=("Times new roman","12"),fg="Black")
    Asientos_vip.place(x=159,y=200)

    tk.Button(ventana,text="Agregar",font = ("Times new roman","12"),fg="Black",
              command = lambda: registrar_reservacion(Numero.get(), Nombre.get(), Asientos_normales.get(), Asientos_economicos.get()
                                                      ,Asientos_vip.get())).place(x=169,y=250)
    
    
    ventana.mainloop()
    

#Nomnbre: registrar_reservacion
#Entradas: 5 parametros
#Salidas: registra la reservacion de viajes en un archivo.txt
#Restricciones: No recibe

def registrar_reservacion(numero,nombre, asientos_normal,asientos_economicos,asientos_vip):
    from datetime import datetime
    
    almacenar_reservacion = open("Reservaciones.txt","a")
    almacenar_reservacion.close()
    
    abrir_viajes = open("Viajes.txt")
    abrir_viajes2 = abrir_viajes.read()
    abrir_viajes3 = open("Viajes.txt")
    abrir_viajes = abrir_viajes3.readlines()
    
    ubicar = localizar_indice(abrir_viajes,"Numero:"+numero+"\n",0)

    empresa = abrir_viajes[ubicar+12][15:-1]
    
    transporte = abrir_viajes[ubicar+13][17:-1]
    
    lugar_salida = abrir_viajes[ubicar+1][20:-1]
    
    fecha_salida = abrir_viajes[ubicar+3][16:-1]
    
    hora_salida = abrir_viajes[ubicar+4][15:-1]
    
    lugar_llegada = abrir_viajes[ubicar+5][21:-1]
    
    fecha_llegada = abrir_viajes[ubicar+7][17:-1]
    
    hora_llegada = abrir_viajes[ubicar+8][16:-1]
    
    precio_vip = abrir_viajes[ubicar+11][11:-1]
    
    precio_normal = abrir_viajes[ubicar+9][14:-1]
    
    precio_economicos = abrir_viajes[ubicar+10][17:-1]

    matricula = abrir_viajes [ubicar+13][17:-1]

    
    abrir_transportes = open("Transportes.txt")
    
    abrir_transportes = abrir_transportes.readlines()
    
    ubicar_indice_matricula = abrir_transportes.index("Placa:"+matricula+"\n")
    guardar_vip_disponibles = abrir_transportes[ubicar_indice_matricula+8][13:-1]
    
    if int(guardar_vip_disponibles)-int(asientos_vip) >=0:
            guardar_normal_disponibles = abrir_transportes[ubicar_indice_matricula+6][18:-1]
            
            if int(guardar_normal_disponibles)-int(asientos_normal) >=0:
                    guardar_economicos_disponibles = abrir_transportes[ubicar_indice_matricula+7][20:-1]
                    
                    if int(guardar_economicos_disponibles)-int(asientos_economicos) >=0:
                        
                        monto_vip = int (asientos_vip)  * (int(precio_vip))
                        monto_economico = int (asientos_economicos)  * (int(precio_economicos))
                        monto_normal = int (asientos_normal)  * (int(precio_normal))
                        
                        archivo= "Reservaciones.txt"
                        archivo2 = open(archivo)
                        archivo3 = archivo2.readlines()
                        ID = identificar(archivo3,0)
                        archivo2 = open(archivo,"a")
                        tiempo = datetime.now()
                        archivo2.write("Identificador:"+str(ID)+"\n")
                        archivo2.write("Numero:"+str(numero) +"\n")
                        archivo2.write("Nombre:"+nombre+"\n")
                        archivo2.write("Cedula Empresa:"+empresa+"\n")
                        archivo2.write("Placa del Transporte:"+transporte+"\n")
                        archivo2.write("Lugar de Salida:"+lugar_salida+"\n")
                        archivo2.write("Fecha de Salida:"+fecha_salida+"\n")
                        archivo2.write("Hora de Salida:"+hora_salida+"\n")
                        archivo2.write("Lugar de Llegada:"+lugar_llegada+"\n")
                        archivo2.write("Fecha de Llegada:"+fecha_llegada+"\n")
                        archivo2.write("Hora de Llegada:"+hora_llegada+"\n")
                        archivo2.write("Asientos Normales:"+asientos_normal +"\n")
                        archivo2.write("Asientos Economicos:"+asientos_economicos+"\n")
                        archivo2.write("Asientos VIP:"+asientos_vip +"\n")
                        archivo2.write("Precio Total:"+str(monto_vip+monto_economico+monto_normal)+"\n")
                        archivo2.write("Fecha y Hora de la reservacion:"+str(tiempo)+"\n")
                        archivo2.write("************************************************"+"\n")
                        archivo2.close()
                        messagebox.showinfo("Reservacion Registrada","¡La reservacion se ha registrado exitosamente!")
                    else:
                        messagebox.showerror("Agotado","No hay asientos disponibles")
            else:
                messagebox.showerror("Agotado","No hay asientos disponibles")
    else:
        messagebox.showerror("Agotado","No hay asientos disponibles")


#localiza la ubicacion de el indice

def localizar_indice(indice,ubicacion,cont):
    if indice == []:
        return False
    elif ubicacion in indice[0]:
        return cont
    else:
        return localizar_indice(indice[1:],ubicacion,cont+1)

#Identifica el numero automatico

def identificar(archivo3,cont):
    if archivo3 == []:
        return cont //16+1
    else:
        return identificar(archivo3[1:],cont+1)
    
##########################################################################################################################

#Nomnbre: cancelar_reservacion
#Entradas: No recibe
#Salidas: Generar una ventana pidiendo datos
#Restricciones: No recibe

def cancelar_reservacion():
    window = tk.Tk()
    window.geometry("600x300")
    window.title("Eliminando reserva")
    identificador = tk.StringVar()
    
    etiqueta1 = tk.Label(window, text = "Identificador de la reserva a eliminar").pack()
    Identificador = tk.Entry(window,textvariable = identificador, font=("Times new roman","12"), bg="white", fg="Black")
    Identificador.pack()

    tk.Button(window,text="Aceptar",font = ("Times new roman","12"),bg="#e7c4e5",fg="Black",
              command = lambda: eliminar_res(Identificador.get())).pack()
    
    window.mainloop()


def eliminar_res(identificador):
    open_file = open("Reservaciones.txt")
    reservas = open_file.readlines()
    if (("Identificador:"+identificador+"\n")in reservas):
        identificador=str(identificador)
        potencia = reservas.index("Identificador:"+identificador+"\n")
        identificador = deleteReservas(reservas, potencia, 0)
        open_file.close()
        open_file = open("Reservas.txt", "w")
        open_file.write(identificador)
        open_file.close()
        messagebox.showinfo(title = "Delete", message = "La reserva ha sido eliminado exitosamente")
    else:
        messagebox.showerror(title = "Error", message = "No existe una reserva con el identificador ingresado")
        
    
def deleteReservas(delete,ContarLineas,contador):
    if contador == 17:
        return TransformarSTR(delete)
    else:
        delete.pop(ContarLineas)
        return deleteReservas(delete,ContarLineas,contador+1)


##########################################################################################################################

#Nomnbre: consulta_historial
#Entradas: No recibe
#Salidas: Generar una ventana pidiendo datos
#Restricciones: No recibe
    
def consultar_historial(pantalla):
    frame = tk.Frame(pantalla)
    frame.pack()
    pantalla.geometry("600x300")
    pantalla.title("Menú administrativo")
    pantalla.config(bg = "Turquoise")
    
    menu4 = Menu(pantalla)
    op4 = Menu(menu4,tearoff = 0)
    op4.add_command(label = "1 - Rango de fecha de salida",font=("Times new roman","12"),
                    command = rango_fecha_salida)
    op4.add_command(label = "2 - Rango de fecha de llegada",font=("Times new roman","12"),
                    command = rango_fecha_llegada)
    op4.add_command(label = "3 - Rango de fecha de la reservacion",font=("Times new roman","12"),
                    command = rango_fecha_reservacion)
    op4.add_command(label = "4 - Lugar de salida",font=("Times new roman","12"),
                    command = rango_lugar_salida)
    op4.add_command(label = "5 - Lugar de llegada",font=("Times new roman","12"),
                    command = rango_lugar_llegada)
    op4.add_command(label = "6 - Salir",font=("Times new roman","12"),
                    command = menu_administrativo)
    menu4.add_cascade(label=" Consultar historial de reservaciones",font=("Times new roman","12"), menu = op4)

    pantalla.config(menu=menu4)
    pantalla.mainloop()

#ubica el rango de salida

def rango_fecha_salida():
    pestaña = tk.Tk()
    pestaña.geometry("600x300")
    pestaña.title("Menú administrativo")
    pestaña.config(bg = "Turquoise")

    etiqueta = tk.Label(pestaña, text = "Rango de la fecha de salida")
    etiqueta.pack()
    entrada = tk.Entry(pestaña)
    entrada.pack()


    #Buscar la informacion en un archivo.txt
    def buscar_info():
        abrir_reservas = open("Reservas.txt")
        almacenar = abrir_reservas.readlines()
        variable_entry = entrada.get()
        if variable_entry in almacenar:
            return buscar_info_aux(almacenar,variable_entry,6,6)
        else:
            messagebox.showerror("Error","Error")
    
    boton = tk.Button(pestaña, text = "Aceptar",command = buscar_info)
    boton.pack()

def rango_fecha_llegada():
    pestaña = tk.Tk()
    pestaña.geometry("600x300")
    pestaña.title("Menú administrativo")
    pestaña.config(bg = "Turquoise")

    etiqueta = tk.Label(pestaña, text = "Rango de la fecha de llegada")
    etiqueta.pack()
    entrada = tk.Entry(pestaña)
    entrada.pack()


    #Buscar la informacion en un archivo.txt
    def buscar_info2():
        abrir_reservas = open("Reservas.txt")
        almacenar = abrir_reservas.readlines()
        variable_entry = entrada.get()
        if variable_entry in almacenar:
            return buscar_info_aux(almacenar,variable_entry,9,9)
    
    boton = tk.Button(pestaña, text = "Aceptar",command = buscar_info2)
    boton.pack()

def rango_fecha_reservacion():
    pestaña = tk.Tk()
    pestaña.geometry("600x300")
    pestaña.title("Menú administrativo")
    pestaña.config(bg = "Turquoise")

    etiqueta = tk.Label(pestaña, text = "Rango de la fecha de reservacion")
    etiqueta.pack()
    entrada = tk.Entry(pestaña)
    entrada.pack()


    #Buscar la informacion en un archivo.txt
    def buscar_info3():
        abrir_reservas = open("Reservas.txt")
        almacenar = abrir_reservas.readlines()
        variable_entry = entrada.get()
        if variable_entry in almacenar:
            return buscar_info_aux(almacenar,variable_entry,15,15)
    
    boton = tk.Button(pestaña, text = "Aceptar",command = buscar_info3)
    boton.pack()


def rango_lugar_salida():
    pestaña = tk.Tk()
    pestaña.geometry("600x300")
    pestaña.title("Menú administrativo")
    pestaña.config(bg = "Turquoise")

    etiqueta = tk.Label(pestaña, text = "Rango del lugar de salida")
    etiqueta.pack()
    entrada = tk.Entry(pestaña)
    entrada.pack()


    #Buscar la informacion en un archivo.txt
    def buscar_info4():
        abrir_reservas = open("Reservas.txt")
        almacenar = abrir_reservas.readlines()
        variable_entry = entrada.get()
        if variable_entry in almacenar:
            return buscar_info_aux(almacenar,variable_entry,5,5)
    
    boton = tk.Button(pestaña, text = "Aceptar",command = buscar_info4)
    boton.pack()

def rango_lugar_llegada():
    pestaña = tk.Tk()
    pestaña.geometry("600x300")
    pestaña.title("Menú administrativo")
    pestaña.config(bg = "Turquoise")

    etiqueta = tk.Label(pestaña, text = "Rango del lugar de llegada")
    etiqueta.pack()
    entrada = tk.Entry(pestaña)
    entrada.pack()


    #Buscar la informacion en un archivo.txt
    def buscar_info5():
        abrir_reservas = open("Reservas.txt")
        almacenar = abrir_reservas.readlines()
        variable_entry = entrada.get()
        if variable_entry in almacenar:
            return buscar_info_aux(almacenar,variable_entry,8,8)
    
    boton = tk.Button(pestaña, text = "Aceptar",command = buscar_info5)
    boton.pack()

def buscar_info_aux(lista_info,buscar,indice,indice2):
    pestaña=Tk()
    pestaña.geometry("600x300")
    pestaña.config(bg="white")
    mostrar=[]
    
    while indice < len(lista_info):
        if buscar in lista_info[indice]:
            contador = 0
            indice3=indice-indice2
            while contador != 20:
                mostrar += [lista_info[indice3]]
                indice3 += 1
                contador += 1

            lista_info
            buscar
            indice+=20
            indice2
        else:
            lista_info
            buscar
            indice += 20
            indice2
    lista_info = Listbox(pestaña, font=("Times New Roman",12), bg="white", fg="Black")
    lista_info.pack()
    contador = 0
    
    for datos in mostrar:
        lista_info.insert(contador,f"linea_info {contador} : {datos}")
        contador += 1
    etiqueta = tk.Label(pestaña,text=f"Estos son las reservaciones encontrados según el dato que ingreso. ",
                        font=("Times New Roman",14), bg="white", fg="Black")
    etiqueta.pack()
    
    def exittt():
        Salir = messagebox.askyesno("Salir", "¿Desea salir de la pestaña?")
        if(Salir):
            pestaña.destroy()
            return menu()

    boton = tk.Button(pestaña,text="Aceptar",font=("Times New Roman",12), bg="white", fg="Black",
                         command=exittt)
    boton.pack()

    
##############################################################################################################################







#Y aqui parte de las funciones que no logre terminar. Lo inrente que es lo importante :)

"""
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

"""    
iniciar()  
