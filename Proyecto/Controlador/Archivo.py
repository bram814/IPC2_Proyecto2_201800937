import xml.etree.ElementTree as ET 
from tkinter import filedialog
from io import open

class Archivo():


    def __init__(self):
        self.contador_datos = 0
        self.fila = 0
        self.columna = 0
        self.imagen = ''

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
                            print(f"Dato: {image}")
                            contador_imagen += 1

                    total_datos = int(self.fila)*int(self.columna)

                    if (int(contador_imagen)==int(total_datos)):
                        print(f"CONCUERDA LA CANTIDAD DE FILA Y COLUMNA {contador_imagen} - {total_datos}")
                    else:
                        print(f'ocurrio algo {contador_imagen} - {total_datos}')

                


                
