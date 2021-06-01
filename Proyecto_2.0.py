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
    
#Solicitar clave de acceso

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

    #Si la clave esta entrar al menu
def verificar_clave(clave,pantalla,frame):
    verificar = leer_archivo_claves()
    if (clave in verificar):
        transicion(frame,menu_administrativo,pantalla)
    else:
        messagebox.askyesno("Error","La contraseña es incorrecta o no esta registrada. ¿Desea continuar o intentar otra vez?")
    #Buscar clave en el archivo    
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
#Gestion de Empresas menu

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

#Interfaz de agregar empresas
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
    
#Agrega la empresa
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

#Interfaz de eliminar empresas
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
#Muestra una listbox con las empresas añadidas
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
#Interfaz de modificar la empresa

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
        
#Pidiendo los nuevos datos
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
        almacenar_transporte.write("Cedula Empresa:"+empresa +"\n")
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
        
#Pidiendo los nuevos datos
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
def numeroAutomatico(archivo,contador):
    if archivo == []:
        return contador//9+1
    else:
        return numeroAutomatico(archivo[1:],contador+1)


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


    etiqueta12 =tk.Label(window,text="Cedula de la Empresa: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=480)
    Empresa = tk.Entry(window,textvariable = empresa,font=("Times new roman","12"),fg="Black").place(x=159,y=480)

    etiqueta13 =tk.Label(window,text="Placa del Transporte: ",font=("Times new roman","12"),bg="gray",fg="black").place(x=5,y=480)
    Transporte = tk.Entry(window,textvariable = transporte,font=("Times new roman","12"),fg="Black").place(x=159,y=480)
    
    tk.Button(window,text="Agregar",font = ("Times new roman","12"),bg="#e7c4e5",fg="Black",
              command = lambda: registrar_transporte(placa.get(),transporte.get(),marca.get(), modelo.get(), año.get(), empresa.get(),
                                                     asientos_normal.get(),asientos_economicos.get(),asientos_vip.get(),empresa.get(),
                                                     transporte.get())).place(x=179,y=520)

    
    window.mainloop()

def registrar_viaje(provincia_salida,ciudad_salida,fecha_salida,hora_salida,provincia_llegada,ciudad_llegada,fecha_llegada,hora_llegada,precio_normal,
                         precio_economico,precio_vip):
    almacenar_viaje = open("Viajes.txt","a")
    Archivo = "Información por viaje.txt"
    Archivo2 = open(Archivo,"a")
    Archivo3 = open(Archivo)
    Archivo3 = Archivo3.readlines()
    NumeroViaje = numeroAutomatico(Archivo3,1)
    
    abrir = open(file)
        
    almacenar_viaje.write((generarNum())+"\n")
     
    almacenar_viaje.write("Provincia de Salida"+provincia_salida +"\n")
    almacenar_viaje.write("Ciudad de Salida"+ciudad_salida+"\n")
    almacenar_viaje.write("Fecha de Salida"+fecha_salida +"\n")
    almacenar_viaje.write("Hora de Salida"+hora_salida +"\n")
    almacenar_viaje.write("Provincia de llegada"+provincia_llegada +"\n")
    almacenar_viaje.write("Ciudad de Llegada"+ciudad_llegada +"\n")
    almacenar_viaje.write("Fecha de Llegada"+fecha_llegada +"\n")
    almacenar_viaje.write("Hora de Llegada"+hora_llegada+"\n")
    almacenar_viaje.write("Precio Normal"+precio_normal +"\n")
    almacenar_viaje.write("Precio Económico"+precio_economico +"\n")
    almacenar_viaje.write("Preciio VIP"+precio_vip +"\n")
    almacenar_viaje.write("Cedula Empresa:"+empresa+"\n")
    almacenar_viaje.write("Placa Transporte:"+transporte+"\n")
     
    almacenar_viaje.write("************************************************"+"\n")
     
    almacenar_viaje.close()
    messagebox.showinfo(title = "Viaje añadido",message = "¡El viaje se ha registrado exitosamente!")

def generarNum():
    archivo="Viajes.txt"
    anexar_archivo=open (archivo,'a')
    lista_viajes= open (archivo,'r')
    cont=0
    for linea in agenda:
        cont += 1
    lista_viajes.close()
    return str(cont//12+1)


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
    if contador == 14:
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

def modificar_viajes():
    ventana=tk.Tk()
    ventana.title("Modificar Transporte")
    ventana.geometry("600x600")
    
    Numero=tk.Label(ventana,text="Numero:",font=("Times New Roman",12), fg="Black")
    Numero.pack()
    
    numero=tk.Entry(ventana,text="", font=("Times New Roman", 12), fg="Black")
    numero.pack()
    
    boton=tk.Button(ventana,text="Modificar Viaje",font=("Times New Roman",12),fg="Black",
                          command = lambda: modificar_viaje_aux(placa.get()))
    boton.pack()
    
    boton2 = tk.Button(ventana,text="Salir",font=("Times New Roman",12),fg="Black",
               command = lambda: gestion_viaje())
    boton2.pack()
    
    ventana.mainloop()

def modificar_viaje_aux(placa):
     abrir_file_viajes = open("Viajes.txt")
     viajes = abrir_file_transportes.readlines()
     if("Numero:"+numero+"\n")in viajes:
          numero=str(numero)
          indice = viajes.index("Numero:"+numero+"\n")
          numero = modificar_viaj(viajes, indice+1, 1)
          abrir_file_viajes.close()

     else:
          messagebox.showerror(title = "Error", message = "El numero del viaje no se encuentra registrado")
        
#Pidiendo los nuevos datos
def modificar_viaj(datos,indice,cont):
    ventana=Tk()
    ventana.geometry("600x300")
    
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
        

        
        return modificar_viaj2_aux(provincia_salida,ciudad_salida,fecha_salida,hora_salida,provincia_llegada,hora_llegada,precio_normal,
                                    precio_economico,precio_vip,empresa,transporte,datos,indice,cont)
    
    boton=tk.Button(ventana,text="Aceptar",command = modificar_aux3)
    boton.pack()



def modificar_viaj2_aux(provincia_salida,ciudad_salida,fecha_salida,hora_salida,provincia_llegada,hora_llegada,precio_normal,
                                    precio_economico,precio_vip,empresa,transporte,datos,indice,cont):
    archivo = open("Viajes.txt","w")
    datos[indice]=("Provincia de Salida:"+provincia_salida+"\n")
    datos[indice+1]=("Ciudad de Salida:"+ciudad_salida+"\n")
    datos[indice+2]=("Fecha de Salida:"+fecha_salida+"\n")
    datos[indice+3]=("Hora de Salida:"+hora_salida+"\n")
    datos[indice+4]=("Provincia de Llegada:"+provincia_llegada+"\n")
    datos[indice+5]=("Hora de Llegada:"+hora_llegada+"\n")
    datos[indice+6]=("Precio Normal:"+precio_normal+"\n")
    datos[indice+7]=("Precio Económico:"+precio_economico+"\n")
    datos[indice+8]=("Precio VIP:"+precio_vip+"\n")
    datos[indice+9]=("Cedula Empresa:"+empresa+"\n")
    datos[indice+10]=("Placa Transporte:"+transporte+"\n")
    datos[indice+11]=("****************************************************"+"\n")
    
    archivo.write( TransformarSTR(datos))



   

















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
