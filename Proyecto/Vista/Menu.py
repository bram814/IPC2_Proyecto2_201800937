from tkinter import filedialog,Tk,Frame,Entry,Button,Label,Text, ttk, StringVar
from Controlador.Archivo import Archivo
class Menu():

    def __init__(self):
        self.cargar_archivo = Archivo()
        self.valor_ = ""

        self.root = Tk()
        self.root.title("Proyecto2_201800937")
        self.root.geometry("1000x1000+0+0")

        self.ventana = Frame(self.root)
        self.ventana.pack()

        

        # ------------------------- BARRA DEL MENU -------------------------
        self.barra = Entry(self.ventana)
        self.barra.grid(row=1, column=1, padx=30, pady=30)
        self.barra.config(background="black", fg="#FFE400")


        self.boton_cargar_archivo = Button(self.barra, text="Cargar Archivo", width=20, height=1, command=lambda:self.cargar_archivo.open_File())
        self.boton_cargar_archivo.grid(row=0 , column=0)
        self.boton_cargar_archivo.config(background="#685E5E", fg="#FFFFFF")

        self.boton_operacion = Button(self.barra, text="Operaciones", width=20, height=1)
        self.boton_operacion.grid(row=0 , column=1)
        self.boton_operacion.config(background="#685E5E", fg="#FFFFFF")

        self.boton_reporte = Button(self.barra, text="Reportes", width=20, height=1)
        self.boton_reporte.grid(row=0 , column=2)
        self.boton_reporte.config(background="#685E5E", fg="#FFFFFF")

        self.boton_ayuda = Button(self.barra, text="Ayuda", width=20, height=1)
        self.boton_ayuda.grid(row=0 , column=3)
        self.boton_ayuda.config(background="#685E5E", fg="#FFFFFF")

        # ------------------------- SELECCIONAR MATRIZ -------------------------

        
        self.l1 = Label(self.ventana,text="Seleccione la Matriz:")
        self.l1.grid(row=2,column=0)
        self.l1.config(padx=10,pady=10)

        self.valor_=StringVar()
        self.combo = ttk.Combobox(self.ventana,value=self.cargar_archivo.ejemplo,width=10, textvariable=self.valor_)
        self.combo.grid(row=3,column=0)

        # ------------------------- LOGICA -------------------------

        
        self.panel= Label(self.ventana)
        self.panel.grid(row=3, column=1, padx=30, pady=30)
        self.panel.config(background="black")

        self.matriz1 = Label(self.panel)
        self.matriz1.grid(row=0, column=0, padx=30, pady=30)
        self.matriz1.config(background="blue" ,width=40, height=20)

        self.matriz2 = Label(self.panel)
        self.matriz2.grid(row=0, column=2, padx=30, pady=30)
        self.matriz2.config(background="blue" ,width=40, height=20)


        '''
        panel = Text(ventana,x=100,y=50,width=50, height=20)
        panel.pack()
        '''
        ttk.Label(self.ventana, textvariable=self.valor_).grid()
        
        self.root.mainloop()

        
        