from tkinter import filedialog,Tk,Frame,Entry,Button,Label,Text, ttk, StringVar
from Controlador.Archivo import Archivo
from Modelo.Nodo import Nodo
class main():


    def __init__(self):
        self.cargar_archivo = Archivo()
        self.valor_ = ""


    def __menu__(self):

        #entero = IntVar()  # Declara variable de tipo entera
        #flotante = DoubleVar()  # Declara variable de tipo flotante
        #cadena = StringVar()  # Declara variable de tipo cadena
        #booleano = BooleanVar()  # Declara variable de tipo booleana

        root = Tk()
        root.title("Proyecto2_201800937")

        ventana = Frame(root)
        ventana.pack()
        

        # ------------------------- BARRA DEL MENU -------------------------
        barra = Entry(ventana)
        barra.grid(row=1, column=1, padx=30, pady=30)
        barra.config(background="black", fg="#FFE400")


        boton_cargar_archivo = Button(barra, text="Cargar Archivo", width=20, height=1, command=lambda:self.cargar_archivo.open_File())
        boton_cargar_archivo.grid(row=0 , column=0)
        boton_cargar_archivo.config(background="#685E5E", fg="#FFFFFF")

        boton_operacion = Button(barra, text="Operaciones", width=20, height=1)
        boton_operacion.grid(row=0 , column=1)
        boton_operacion.config(background="#685E5E", fg="#FFFFFF")

        boton_reporte = Button(barra, text="Reportes", width=20, height=1)
        boton_reporte.grid(row=0 , column=2)
        boton_reporte.config(background="#685E5E", fg="#FFFFFF")

        boton_ayuda = Button(barra, text="Ayuda", width=20, height=1)
        boton_ayuda.grid(row=0 , column=3)
        boton_ayuda.config(background="#685E5E", fg="#FFFFFF")

        # ------------------------- SELECCIONAR MATRIZ -------------------------

        ejemplo = []

        i = 0
        j = 10
        fila = 1
        columna = 1 
        while i < j:
            guardar = Nodo(i+1,fila,columna,f'posicion({fila},{columna})')
            ejemplo.append(guardar)
            columna+=1
            if (i == 4):
                columna = 1
                fila += 1
            
            i+=1
        
          
        i = 0 
        while i < len(ejemplo):
            print(ejemplo[i])
            i+=1
        
        l1 = Label(ventana,text="Seleccione la Matriz:")
        l1.grid(row=2,column=0)
        l1.config(padx=10,pady=10)

        self.valor_=StringVar()
        combo = ttk.Combobox(ventana,value=ejemplo,width=10, textvariable=self.valor_)
        combo.grid(row=3,column=0)

        # ------------------------- LOGICA -------------------------

        
        panel= Label(ventana)
        panel.grid(row=3, column=1, padx=30, pady=30)
        panel.config(background="black")

        matriz1 = Label(panel)
        matriz1.grid(row=0, column=0, padx=30, pady=30)
        matriz1.config(background="blue" ,width=40, height=20)

        matriz2 = Label(panel)
        matriz2.grid(row=0, column=2, padx=30, pady=30)
        matriz2.config(background="blue" ,width=40, height=20)


        '''
        panel = Text(ventana,x=100,y=50,width=50, height=20)
        panel.pack()
        '''
        ttk.Label(ventana, textvariable=self.valor_).grid()
        
        root.mainloop()

        


    def open_File(self):
            try:
                #root = Tk()
                ruta =  ""
                filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TXT files","*.txt"),("all files","*.*")))
                ruta = filename
                if ruta != "":
                    return ruta
                else:
                    
                    return None

            except IndexError as e:
                print(e)  



if __name__ == "__main__":
    instance = main()
    instance.__menu__()