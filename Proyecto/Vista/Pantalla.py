import xml.etree.ElementTree as ET 
from tkinter import filedialog
from Modelo.Nodo import Nodo
from io import open


from tkinter import *
from tkinter import ttk
from Controlador.Archivo import Archivo
from PIL import ImageTk, Image

class Pantalla():

    def __init__(self):

        
        self.contador_datos = 1
        self.fila = 0
        self.columna = 0
        self.imagen = ''
        self.ejemplo = []

        self.cargar_archivo = Archivo()
        self.valor_ = ""

        self.root_window = Tk()
        self.root_window.geometry("1350x670+0+0")
        self.root_window.title("Ventana Principal")

        # ------------------------------------ BARRA MENU ------------------------------------ 

        self.barra_menu = Menu(self.root_window)

        # ------------------------------------ CARGAR ARCHIVO ------------------------------------ 
        self.open_file = Menu(self.barra_menu)
        self.open_file.add_command(label="Abrir", command=lambda:self.open_File())

        self.barra_menu.add_cascade(label="Cargar Archivo", menu=self.open_file)

        # ------------------------------------ OPERACIONES ------------------------------------ 

        self.operacion = Menu(self.barra_menu)
        self.operacion.add_command(label="1.- Rotación Horizontal de una Imagen")
        self.operacion.add_command(label="2.- Rotación Vertical de una Imagen")
        self.operacion.add_command(label="3.- Transpuesta de una Imagen")
        self.operacion.add_command(label="4.- Limpiar Zona de una Imagen")
        self.operacion.add_command(label="5.- Agregar Línea Horizontal a una Imagen")
        self.operacion.add_command(label="6.- Agregar Línea Vertical a una Imagen")
        self.operacion.add_command(label="7.- Agregar Rectángulo")
        self.operacion.add_command(label="8.- Agregar Triángulo Rectángulo")

        self.barra_menu.add_cascade(label="Operaciones", menu=self.operacion)

        # ------------------------------------ REPORTES ------------------------------------ 

        self.reporte = Menu(self.barra_menu)
        self.reporte.add_command(label="Abrir")

        self.barra_menu.add_cascade(label="Reportes", menu=self.reporte)

        # ------------------------------------ AYUDA ------------------------------------ 
        
        self.ayuda = Menu(self.barra_menu)
        self.ayuda.add_command(label="Abrir")

        self.barra_menu.add_cascade(label="Ayuda", menu=self.ayuda)

        # ---------------------------------- ESCOGER MATRIZ -------------------------------

        self.l1 = Label(self.root_window,text="Seleccione la Matriz:")
        self.l1.grid(row=2,column=0)
        self.l1.config(padx=10,pady=10)

        self.valor_=StringVar()
        self.combo = ttk.Combobox(self.root_window,value=self.cargar_archivo.ejemplo,width=10)
        self.combo.grid(row=3,column=0)


        self.root_window.config(menu=self.barra_menu)
        self.root_window.mainloop()

    
    def open_File(self):
            try:
                #root = Tk()
                ruta =  ""
                filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TXT files","*.xml"),("all files","*.*")))
                ruta = filename
                if ruta != "":
                    self.cargar_Archivo(ruta)
                    return ruta
                else:
                    
                    return None

            except IndexError as e:
                print(e)   

    def cargar_Archivo(self,rout):
        file_route = ET.parse(rout)
        root = file_route.getroot()
        print('\n')

        for element in root:
            for subelement in element:
                if (subelement.tag == 'filas'):
                    self.fila = subelement.text
                    print(f'aca hay una fila - {self.fila}')
                elif (subelement.tag == 'columnas'):
                    self.columna = subelement.text
                    print(f'aca hay una columna - {self.columna}')
                elif (subelement.tag == 'imagen'):
                    self.imagen = subelement.text
                    print(f'aca hay una imagen - {self.imagen}')
                    contador_imagen = 0
                    for image in self.imagen:
                        if (image == "-" or image == "*"):
                            contador_imagen += 1

                    total_datos = int(self.fila)*int(self.columna)

                    if (int(contador_imagen)==int(total_datos)):
                        print(f"CONCUERDA LA CANTIDAD DE FILA Y COLUMNA {contador_imagen} - {total_datos}")
                        fila = 1
                        columna = 1
                        for image in self.imagen:
                            if (image == "-" or image == "*"):
                                print(f"({self.contador_datos}.- ({fila},{columna}) Dato: {image}")

                                if (int(columna) == int(self.columna)):
                                    columna = 1
                                    fila += 1
                                elif (int(columna) < int(self.columna)):
                                    columna += 1

                    else:
                        print(f'ocurrio algo {contador_imagen} - {total_datos}')

                    self.contador_datos += 1


                
        

        i = 0
        j = 10
        fila = 1
        columna = 1 
        while i < j:
            guardar = Nodo(i+1,fila,columna,f'posicion({fila},{columna})')
            self.ejemplo.append(guardar)
            columna+=1
            if (i == 4):
                columna = 1
                fila += 1
            
            i+=1
        
          
        i = 0 
        while i < len(self.ejemplo):
            print(self.ejemplo[i].get_contador())
            
            i+=1

        self.combo["values"] = self.ejemplo