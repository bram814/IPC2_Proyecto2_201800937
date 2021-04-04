import xml.etree.ElementTree as ET 
from tkinter import filedialog
from Modelo.Nodo import Nodo
from io import open

from Controlador.Graphviz import Graphviz
from Modelo.Matriz_Ortogonal import Matriz_Ortogonal
from Modelo.Lista_Vertical import Lista_Vertical


from tkinter import ttk, Tk, Label, Menu, Button, Entry, StringVar, Scrollbar, Frame
from PIL import ImageTk, Image
from Controlador.Archivo import Archivo


class Pantalla():

    def __init__(self):

        
        
        self.contador_datos = 0
        self.nombre = ''
        self.fila = 0
        self.columna = 0
        self.imagen = ''
        # ------------------- METODOS O FUNCIONES ----------------------
        self.graphivz = Graphviz()

        # ------------------- MATRIZ ORTOGONAL ----------------------
        self.matriz_ortogonal = Matriz_Ortogonal()
        self.matriz_ortogonal_nombre = Matriz_Ortogonal()

        self.cargar_archivo = Archivo()

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
        self.operacion.add_command(label="SOBRE UNA IMAGEN")
        self.operacion.add_command(label="1.- Rotación Horizontal de una Imagen", command=lambda:self.graphivz.rotacion_horizontal(self.combo.get(),self.contador_datos,self.matriz_ortogonal,self.matriz_ortogonal_nombre,self.combo,self.combo2))
        self.operacion.add_command(label="2.- Rotación Vertical de una Imagen", command=lambda:self.graphivz.rotacion_vertical(self.combo.get(),self.contador_datos,self.matriz_ortogonal,self.matriz_ortogonal_nombre,self.combo,self.combo2))
        self.operacion.add_command(label="3.- Transpuesta de una Imagen", command=lambda:self.graphivz.transpuesta(self.combo.get(),self.contador_datos,self.matriz_ortogonal,self.matriz_ortogonal_nombre,self.combo,self.combo2))
        self.operacion.add_command(label="4.- Limpiar Zona de una Imagen -> filaO,columnaO;filaF,columnaF", command=lambda:self.graphivz.limpiar_zona(self.combo.get(),self.contador_datos,self.matriz_ortogonal,self.matriz_ortogonal_nombre,self.combo,self.combo2,self.string_limpiar_zona.get()))
        self.operacion.add_command(label="5.- Agregar Línea Horizontal a una Imagen -> filaO,columnaO;cantidad", command=lambda:self.graphivz.agregar_linea_horizontal(self.combo.get(),self.contador_datos,self.matriz_ortogonal,self.matriz_ortogonal_nombre,self.combo,self.combo2,self.string_limpiar_zona.get()))
        self.operacion.add_command(label="6.- Agregar Línea Vertical a una Imagen -> filaO,columnaO;cantidad", command=lambda:self.graphivz.agregar_linea_vertical(self.combo.get(),self.contador_datos,self.matriz_ortogonal,self.matriz_ortogonal_nombre,self.combo,self.combo2,self.string_limpiar_zona.get()))
        self.operacion.add_command(label="7.- Agregar Rectángulo")
        self.operacion.add_command(label="8.- Agregar Triángulo Rectángulo")
        self.operacion.add_separator()
        self.operacion.add_command(label="SOBRE DOS IMAGENES")
        self.operacion.add_command(label="1.- Union")
        self.operacion.add_command(label="2.- Intersección")
        self.operacion.add_command(label="3.- Diferencia")
        self.operacion.add_command(label="4.- Diferencia Simétrica")

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

        self.l1 = Label(self.root_window,text="Seleccione la Matriz 1:")
        self.l1.grid(row=2,column=0)
        self.l1.config(padx=10,pady=10)
        self.combo = ttk.Combobox(self.root_window,value=self.cargar_archivo.ejemplo,width=10)
        self.combo.grid(row=3,column=0)

        self.l2 = Label(self.root_window,text="Seleccione la Matriz 2:")
        self.l2.grid(row=2,column=1)
        self.l2.config(padx=10,pady=10)

        self.combo2 = ttk.Combobox(self.root_window,value=self.cargar_archivo.ejemplo,width=10)
        self.combo2.grid(row=3,column=1)

        # ---------------------------------- Metodos Agregar -------------------------------
        self.label_limpiar = Label(self.root_window,text="Operaciones Sobre Una Imagen [4-8]")
        self.label_limpiar.grid(row=2,column=3)
        self.label_limpiar.config(padx=10,pady=10)

        self.string_limpiar_zona = StringVar()
        self.limpiar_zona = Entry(self.root_window,width=12,textvariable=self.string_limpiar_zona)
        self.limpiar_zona.grid(row=3,column=3)
        

        # ------------------------------------- BOTON -----------------------------------------

        self.boton_mostrar = Button(self.root_window, text="Mostrar", width=10, height=1, command=lambda:self.graphivz.generar_imagen(self.contador_datos,self.matriz_ortogonal,self.matriz_ortogonal_nombre,self.combo.get(),self.combo2.get()))
        self.boton_mostrar.grid(row=3 , column=2)

        #self.boton_limpiar =  Button(self.root_window, text="Limpiar Resultado", width=15, height=1, command=lambda:self.graphivz.limpiar_resultado())
        #self.boton_limpiar.grid(row=3, column=4)
        
        # ------------------------------------- IMAGEN -----------------------------------------

        #self.imagen_original = ImageTk.PhotoImage(Image.open('imagen.gv.png'))
        #self.label_imagen_original = Label(image=self.imagen_original)
        #self.label_imagen_original.grid(row=5, column=0)
        

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
                if (subelement.tag == 'nombre'):
                    self.nombre = subelement.text
                    print(f'NOMBRE DE LA MATRIZ {self.nombre}')
                elif (subelement.tag == 'filas'):
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
                        self.contador_datos += 1
                        self.matriz_ortogonal_nombre.agregar(int(self.contador_datos),int(self.fila),int(self.columna),str(self.nombre))
                        
                        for image in self.imagen:
                            if (image == "-" or image == "*"):
                                #print(f"({self.contador_datos}.- ({fila},{columna}) Dato: {image}")
                                self.matriz_ortogonal.agregar(int(self.contador_datos),int(fila),int(columna),str(image))
                                
                                if (int(columna) == int(self.columna)):
                                    columna = 1
                                    fila += 1
                                elif (int(columna) < int(self.columna)):
                                    columna += 1

                    else:
                        print(f'ocurrio algo {contador_imagen} - {total_datos}')



                        

        temp = []
        i = 0
        temp.append(i)
        while i < self.contador_datos:
            temp.append(i+1)
            i +=1
        self.combo["values"] = temp
        self.combo2["values"] = temp

        