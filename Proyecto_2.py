from tkinter import *
import tkinter
from tkinter import messagebox

"""
Funcionalidad: crea la ventana principal, se define el tamaño, el título
               el ícono y la imagen de fondo
"""

ventana = Tk()#ventana principal
ventana.geometry("600x300")#tamaño de la ventana
ventana.title("Sistema de reservación de boletos")#titulo de la ventana
ventana.config(bg = "lightgray")
ventana.iconbitmap("python.ico")#ícono de la ventana

#---------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: ventanaPrincipal
Funcionalidad: crea la barra del menú principal en la ventana principal
"""
def ventanaPrincipal():
    menu = Menu(ventana)
    ventana.config(menu=menu)
    menuPrincipal = Menu(menu,tearoff = 0)#quita la linea de puntos
    #opciones del menú principal, fuente, tamaño, inclinación y espesor
    menuPrincipal.add_command(label = "1 - Opciones administrativas",font =("Times new roman","12","italic","bold"),command = menuAdministrativo)
    menuPrincipal.add_command(label = "2 - Opciones de usuario normal",font =("Times new roman","12","italic","bold"),command = menuGeneral)
    menuPrincipal.add_command(label = "3 - Salir",font =("Times new roman","12","italic","bold"),command = ventana.destroy)

    menu.add_cascade(label="Menú principal", menu = menuPrincipal)#diseño del menú principal
    
    

def menuAdministrativo():
    abrirVentana = Tk()
    abrirVentana.geometry("600x300")
    abrirVentana.title("Menú administrativo")
    abrirVentana.config(bg = "lightgreen")
    abrirVentana.iconbitmap("python.ico")
    etiqueta=tkinter.Label(abrirVentana,text="Escriba la clave de acceso",bg = "white",font =("Times new roman","14","italic","bold"))
    etiqueta.place(x=180,y=60)
    entrada = tkinter.Entry(abrirVentana)
    entrada.place(x=225,y=90)
    
    
    def clave():
        acceso=entrada.get()
        if(acceso == "acceso"):
            
            menu = Menu(abrirVentana)
            abrirVentana.config(menu=menu)

            opAdmi = Menu(menu,tearoff = 0)
            opAdmi.add_command(label = "1 - Gestión de empresas",font=("Times new roman","12"),command = gestionEmpresa)
            opAdmi.add_command(label = "2 - Gestión de transporte por empresa",font=("Times new roman","12"),command = gestionTransporte)
            opAdmi.add_command(label = "3 - Gestión de viaje",font=("Times new roman","12"), command = gestionViaje)
            opAdmi.add_command(label = "4 - Consultar historial de reservaciones",font=("Times new roman","12"), command = consultaHistorial)
            opAdmi.add_command(label = "5 - Estadísticas de viaje",font=("Times new roman","12"), command = estadisticas)
            opAdmi.add_command(label = "6 - Salir de menu administrativo", font=("Times new roman","12"),command = ventanaPrincipal)
            menu.add_cascade(label="1 - Opciones administrativas", font=("Times new roman","12"), menu = opAdmi)
            
        else:
            advertencia=messagebox.askyesno("Error","La contraseña es incorrecta. ¿Desea continuar o intentar otra vez?")
            if advertencia:
                abrirVentana.destroy()
                return menuAdministrativo()
            else:
                abrirVentana.destroy()
                return ventanaPrincipal()

    boton = tkinter.Button(abrirVentana,text = "Ingresar",font=("Times new roman","12"),command = clave)
    boton.place(x=260,y=120)
    
    



    def gestionEmpresa():
        ventana2 = Tk()
        ventana2.geometry("250x200")
        ventana2.title("Menú administrativo")
        ventana2.config(bg = "Turquoise")
        ventana2.iconbitmap("python.ico")
        menu1 = Menu(ventana2)
        
        op1 = Menu(menu1,tearoff = 0)
        op1.add_command(label = "1 - Incluir empresa",font=("Times new roman","12"))
        op1.add_command(label = "2 - Eliminar empresa",font=("Times new roman","12"))
        op1.add_command(label = "3 - Modificar empresa",font=("Times new roman","12"))
        op1.add_command(label = "4 - Mostrar empresa",font=("Times new roman","12"))
        op1.add_command(label = "5 - Retornar",font=("Times new roman","12"),command = menuAdministrativo)
        menu1.add_cascade(label=" Gestión de empresa",font=("Times new roman","12"), menu = op1)
        ventana2.config(menu=menu1)
        ventana2.mainloop()

    def gestionTransporte():
        ventana3 = Tk()
        ventana3.geometry("250x200")
        ventana3.title("Menú administrativo")
        ventana3.config(bg = "Turquoise")
        ventana3.iconbitmap("python.ico")
        menu2 = Menu(ventana3)
        op2 = Menu(menu2,tearoff = 0)
        op2.add_command(label = "1 - Incluir transporte",font=("Times new roman","12"))
        op2.add_command(label = "2 - Eliminar transporte",font=("Times new roman","12"))
        op2.add_command(label = "3 - Modificar transporte",font=("Times new roman","12"))
        op2.add_command(label = "4 - Mostrar transportes",font=("Times new roman","12"))
        op2.add_command(label = "5 - Retornar",font=("Times new roman","12"),command = menuAdministrativo)
        menu2.add_cascade(label=" Gestión de transporte por empresa",font=("Times new roman","12"), menu = op2)
        ventana3.config(menu=menu2)
        ventana3.mainloop()

    def gestionViaje():
        ventana4 = Tk()
        ventana4.geometry("250x200")
        ventana4.title("Menú administrativo")
        ventana4.config(bg = "Turquoise")
        ventana4.iconbitmap("python.ico")
        menu3 = Menu(ventana4)
        op3 = Menu(menu3,tearoff = 0)
        op3.add_command(label = "1 - Incluir viaje",font=("Times new roman","12"))
        op3.add_command(label = "2 - Eliminar viaje",font=("Times new roman","12"))
        op3.add_command(label = "3 - Modificar viaje",font=("Times new roman","12"))
        op3.add_command(label = "4 - Mostrar viajes",font=("Times new roman","12"))
        op3.add_command(label = "5 - Retornar",font=("Times new roman","12"),command = menuAdministrativo)
        menu3.add_cascade(label=" Gestión de viaje",font=("Times new roman","12"), menu = op3)
        ventana4.config(menu=menu3)
        ventana4.mainloop()

    def consultaHistorial():
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
        return menuAdministrativo()

def menuGeneral():
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

def consultaViajes():
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
    



ventanaPrincipal()
