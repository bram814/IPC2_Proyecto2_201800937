from graphviz import Digraph
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class Graphviz():


    def __init__(self):
        self.matriz_ortogonal = None
        self.matriz_ortogonal_nombre = None
        self.fila_matriz1 = 0
        self.fila_matriz2 = 0
        self.columna_matriz1 = 0
        self.columna_matriz2 = 0

    def generar_imagen(self,matriz,matriz2,cont_matriz_uno,cont_matriz_dos):
        self.matriz_ortogonal = matriz
        self.matriz_ortogonal_nombre = matriz2
        print('\n DATOS')
        #self.matriz_ortogonal_nombre.mostrar_matriz()
        #self.matriz_ortogonal.mostrar_matriz()

        print(f'\n SELECCIONA LA MATRIZ 1 -> {cont_matriz_uno} = SELECCIONA LA MATRIZ 2 -> {cont_matriz_dos}')

        
        if (0 < int(cont_matriz_uno)):
            
            if (int(cont_matriz_dos) == 0):
                self.una_imagen(cont_matriz_uno)
            elif (0< int(cont_matriz_dos)):
                self.dos_imagenes(cont_matriz_uno,cont_matriz_dos)


        self.imagen_original = ImageTk.PhotoImage(Image.open('imagen.gv.png'))
        self.label_imagen_original = Label(image=self.imagen_original)
        self.label_imagen_original.grid(row=5, column=0)
        
            
       

    def una_imagen(self,contador):
        g = Digraph('g', format='png',filename='imagen.gv',node_attr={'shape': 'plaintext'})
        
        #<td PORT="f1> port -> SIRVE PARA APUNTAR 
    
        g.node('node01', f'''<
        <table border="0" cellborder="1" cellspacing="0">
        {str(self.generar_tabla_nombre(contador))}
        {str(self.generar_tabla_datos(contador,self.fila_matriz1,self.columna_matriz1))}
        </table>>''')
         
        #g.edges([('node01:f1', 'node02:f0'), ('node03:f2', 'node04:f3')]) # esta condicion crea los punteros
        g.view()

    def dos_imagenes(self,contador,contador2):
        g = Digraph('g', format='png',filename='imagen.gv',node_attr={'shape': 'plaintext'})
        
    
        g.node('struct1', f'''<
        <table border="0" cellborder="1" cellspacing="0">
        {str(self.generar_tabla_nombre(contador))}
        {str(self.generar_tabla_datos(contador,self.fila_matriz1,self.columna_matriz1))}
        </table>>''')

        g.node('struct2', f'''<
        <table border="0" cellborder="1" cellspacing="0">
        {str(self.generar_tabla_nombre(contador2))}
        {str(self.generar_tabla_datos(contador2,self.fila_matriz1,self.columna_matriz1))}
        </table>>''')
        
        g.view()

    def generar_tabla_nombre(self,contador):
        tabla = ''
        aux = self.matriz_ortogonal_nombre.get_fila().get_primero()
        longitud_fila = self.matriz_ortogonal_nombre.get_fila().size_LCF
        i = 0

        while i < longitud_fila:
            
            j = 0
            longitud_lista = aux.get_fila().size_LH
            aux2 = aux.get_fila().get_primero()
            while j < longitud_lista:
                
                if (int(aux2.get_contador()) == int(contador)):
                    self.fila_matriz1 = aux2.get_x()
                    self.columna_matriz1 = aux2.get_y()
                    tabla += f'<tr>\n\t<td>{aux2.get_dato()}</td>\n'
                    x = 0
                    while x < int(aux2.get_x()):
                        tabla += f'\t<td>{x+1}</td>\n'
                        x += 1
                    tabla += "</tr>\n"
                    print(tabla)
                    return tabla
                aux2 = aux2.get_derecha()
                j += 1 

            aux = aux.get_siguiente()
            i += 1

        return tabla

    def generar_tabla_datos(self,contador,fila,columna):
        tabla = ''
        i = 0
        longitud = int(fila)*int(columna)
        fila_temp = 1
        columna_temp = 1
        print(f'longitud: {longitud}')
        while i < longitud:

            if (int(columna_temp) < columna):

                if (int(columna_temp == 1)):
                    tabla += f"<tr>\n\t<td>{fila_temp}</td>\n"
                dato = self.matriz_ortogonal.encontrar_posicion(contador,fila_temp,columna_temp)

                if (dato.get_dato() == '-'):
                    tabla += "\t<td> </td>\n"
                elif (dato.get_dato() == '*'):
                    tabla += "\t<td>*</td>\n"
                #print(f'{contador}.- ({fila_temp},{columna_temp}) Dato: {dato}')
                columna_temp += 1

            elif (int(columna_temp) == columna):
                dato = self.matriz_ortogonal.encontrar_posicion(contador,fila_temp,columna_temp)
                if (dato.get_dato() == '-'):
                    tabla += "\t<td> </td>\n"
                elif (dato.get_dato() == '*'):
                    tabla += "\t<td>*</td>\n"
                #print(f'{contador}.- ({fila_temp},{columna_temp}) Dato: {dato}')
                tabla += "</tr>\t"
                fila_temp += 1
                columna_temp = 1


            i += 1
        print(tabla)
        return tabla

    # ----------------------------------------------------- PARA UNA IMAGEN -----------------------------------------------------
    def rotacion_horizontal(self,contador):
        tabla = ""
        tabla_temp = ""
        tabla_final = ""
        aux = self.matriz_ortogonal_nombre.get_fila().get_primero()
        longitud_fila = self.matriz_ortogonal_nombre.get_fila().size_LCF
        i = 0

        while i < longitud_fila:
            
            j = 0
            longitud_lista = aux.get_fila().size_LH
            aux2 = aux.get_fila().get_primero()
            while j < longitud_lista:
                
                if (int(aux2.get_contador()) == int(contador)):
                    self.fila_matriz1 = aux2.get_x()
                    self.columna_matriz1 = aux2.get_y()
                    tabla += f'<tr>\n\t<td>{aux2.get_dato()}</td>\n'
                    x = 0
                    while x < int(aux2.get_x()):
                        tabla += f'\t<td>{x+1}</td>\n'
                        x += 1
                    tabla += "</tr>\n"

                    fila_separacion = 0
                    if self.fila_matriz1 % 2 == 0: # par
                        fila_separacion = int(self.fila_matriz1) / 2
                        print(f"fila par: {str(fila_separacion)}")
                        fila = 1
                        fila_ultimo = self.fila_matriz1
                        columna = 1
                        #columna_ultima = self.columna_matriz1
                        longitud = int(self.fila_matriz1) * int(self.columna_matriz1)

                        x = 0
                        while x < longitud:
                            
                            if (int(columna) < int(self.columna_matriz1)):
                                
                                temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                temp2 = self.matriz_ortogonal.encontrar_posicion(contador,fila_ultimo,columna).get_dato()
                                if temp1 == "-":
                                    temp1 = " "
                                if (temp2 == "-"):
                                    temp2 = " "

                                if (int(columna == 1)):
                                    tabla_temp = ""
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                                    tabla_temp += f"<tr>\n\t<td>{fila_ultimo}</td>\n"
                                
                                tabla += f"\t<td>{temp2}</td>\n"
                                tabla_temp += f"\t<td>{temp1}</td>\n" 

                                columna += 1
                                
                            elif (int(columna) == int(self.columna_matriz1)):

                                temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                temp2 = self.matriz_ortogonal.encontrar_posicion(contador,fila_ultimo,columna).get_dato()
                                if temp1 == "-":
                                    temp1 = " "
                                if (temp2 == "-"):
                                    temp2 = " "

                                
                                tabla += f"\t<td>{temp2}</td>\n</tr>"
                                tabla_temp += f"\t<td>{temp1}</td>\n</tr>\n" 
                                tabla_final = f"{tabla_temp} {tabla_final}"

                                if (int(fila) == int(fila_separacion)):
                                    print("llgamos a la mitad - terminar")
                                    tabla = f"{tabla} {tabla_final}"
                                    print(tabla)

                                    g = Digraph('g', format='png',filename='rotacion_horizontal.gv',node_attr={'shape': 'plaintext'})
                                    g.node('node01', f'''<
                                    <table border="0" cellborder="1" cellspacing="0">
                                    {str(tabla)}
                                    </table>>''')
                                    g.view()

                                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('rotacion_horizontal.gv.png'))
                                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                    break

                                columna = 1
                                fila += 1
                                fila_ultimo -= 1

                            x += 1

                        break
                    else: # impar

                        fila_separacion = (int(self.fila_matriz1) / 2) + 0.5
                        print(f"fila impar {fila_separacion}")
                        fila = 1
                        fila_ultimo = self.fila_matriz1
                        columna = 1
                        #columna_ultima = self.columna_matriz1
                        longitud = int(self.fila_matriz1) * int(self.columna_matriz1)

                        x = 0
                        while x < longitud:
                            
                            if (int(columna) < int(self.columna_matriz1)):
                                
                                temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                temp2 = self.matriz_ortogonal.encontrar_posicion(contador,fila_ultimo,columna).get_dato()

                                if temp1 == "-":
                                    temp1 = " "
                                if (temp2 == "-"):
                                    temp2 = " "


                                if (int(columna == 1)):
                                
                                    tabla_temp = ""
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                                    if fila < fila_separacion:
                                        tabla_temp += f"<tr>\n\t<td>{fila_ultimo}</td>\n"
                                
                                if (int(fila) == int(fila_separacion)):
                                    tabla += f"\t<td>{temp1}</td>\n"
                                else:
                                    tabla += f"\t<td>{temp2}</td>\n"
                                    tabla_temp += f"\t<td>{temp1}</td>\n" 

                                columna += 1
                                


                            elif (int(columna) == int(self.columna_matriz1)):

                                temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                temp2 = self.matriz_ortogonal.encontrar_posicion(contador,fila_ultimo,columna).get_dato()
                                if temp1 == "-":
                                    temp1 = " "
                                if (temp2 == "-"):
                                    temp2 = " "

                                
                                tabla += f"\t<td>{temp2}</td>\n</tr>"
                                

                                if (int(fila) == int(fila_separacion)):
                                    print("llgamos a la mitad - terminar")
                                    tabla = f"{tabla} {tabla_final}"
                                    #print(tabla)

                                    g = Digraph('g', format='png',filename='rotacion_horizontal.gv',node_attr={'shape': 'plaintext'})
        
                                    g.node('node01', f'''<
                                    <table border="0" cellborder="1" cellspacing="0">
                                    {str(tabla)}
                                    </table>>''')
                                    
                                    g.view()

                                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('rotacion_horizontal.gv.png'))
                                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                    break

                                tabla_temp += f"\t<td>{temp1}</td>\n</tr>\n" 
                                tabla_final = f"{tabla_temp} {tabla_final}"

                                columna = 1
                                fila += 1
                                fila_ultimo -= 1

                            x += 1

                        break
                    
                   
                aux2 = aux2.get_derecha()
                j += 1 

            aux = aux.get_siguiente()
            i += 1

    # ---------------------------------------------------------------- ROTACION VERTICAL --------------------------------------------------------------------------
    def rotacion_vertical(self,contador):
        tabla = ""
        tabla_temp = ""
        #tabla_final = ""
        aux = self.matriz_ortogonal_nombre.get_fila().get_primero()
        longitud_fila = self.matriz_ortogonal_nombre.get_fila().size_LCF
        i = 0

        while i < longitud_fila:
            
            j = 0
            longitud_lista = aux.get_fila().size_LH
            aux2 = aux.get_fila().get_primero()
            while j < longitud_lista:
                
                if (int(aux2.get_contador()) == int(contador)):
                    self.fila_matriz1 = aux2.get_x()
                    self.columna_matriz1 = aux2.get_y()
                    tabla += f'<tr>\n\t<td>{aux2.get_dato()}</td>\n'
                    x = 0
                    while x < int(aux2.get_x()):
                        tabla += f'\t<td>{x+1}</td>\n'
                        x += 1
                    tabla += "</tr>\n"

                    columna_separacion = 0
                    if self.columna_matriz1 % 2 == 0: # par
                        columna_separacion = int(self.columna_matriz1) / 2
                        print(f"Columna par: {str(columna_separacion)}")
                        
                        fila = 1
                        #fila_ultimo = self.fila_matriz1
                        columna = 1
                        columna_ultima = self.columna_matriz1
                        longitud = int(self.fila_matriz1) * int(self.columna_matriz1)

                        x = 0
                        while x < longitud:
                            
                            if (int(columna) < int(columna_separacion)):
                                
                                temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                temp2 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna_ultima).get_dato()
                                if temp1 == "-":
                                    temp1 = " "
                                if (temp2 == "-"):
                                    temp2 = " "

                                if (int(columna == 1)):
                                    tabla_temp = ""
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                                
                                tabla += f"\t<td>{temp2}</td>\n"
                                tabla_temp = f"\t<td>{temp1}</td>\n {tabla_temp}" 

                                columna += 1
                                columna_ultima -= 1
                                
                            elif (int(columna) == int(columna_separacion)):

                                temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                temp2 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna_ultima).get_dato()
                                if temp1 == "-":
                                    temp1 = " "
                                if (temp2 == "-"):
                                    temp2 = " "

                                
                                tabla += f"\t<td>{temp2}</td>\n"
                                tabla_temp = f"\t<td>{temp1}</td>\n {tabla_temp}" 

                                if (int(columna) == int(columna_separacion)): 
                                    print("llgamos a la mitad - terminar")
                                    tabla = f"{tabla} {tabla_temp}\n</tr>"
                                    print(tabla)

                                    if (int(fila) == int(self.fila_matriz1)):

                                        g = Digraph('g', format='png',filename='rotacion_vertical.gv',node_attr={'shape': 'plaintext'})
                                        g.node('node01', f'''<
                                        <table border="0" cellborder="1" cellspacing="0">
                                        {str(tabla)}
                                        </table>>''')
                                        g.view()

                                        self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('rotacion_vertical.gv.png'))
                                        self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                        self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                        break

                                

                                columna = 1
                                columna_ultima = self.columna_matriz1
                                fila += 1

                            x += 1

                        break
                    else: # impar

                        columna_separacion = (int(self.columna_matriz1) / 2) + 0.5
                        print(f"Columna impar {columna_separacion}")
                        fila = 1
                        #fila_ultimo = self.fila_matriz1
                        columna = 1
                        columna_ultima = self.columna_matriz1
                        longitud = int(self.fila_matriz1) * int(self.columna_matriz1)

                        x = 0
                        while x < longitud:
                            
                            
                            if (int(columna) < int(columna_separacion)):
                                
                                temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                temp2 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna_ultima).get_dato()
                                if temp1 == "-":
                                    temp1 = " "
                                if (temp2 == "-"):
                                    temp2 = " "

                                if (int(columna == 1)):
                                    tabla_temp = ""
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                                
                                tabla += f"\t<td>{temp2}</td>\n"
                                tabla_temp = f"\t<td>{temp1}</td>\n {tabla_temp}" 

                                columna += 1
                                columna_ultima -= 1
                                
                            elif (int(columna) == int(columna_separacion)):

                                temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                temp2 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna_ultima).get_dato()
                                if temp1 == "-":
                                    temp1 = " "
                                if (temp2 == "-"):
                                    temp2 = " "

                                
                                tabla += f"\t<td>{temp1}</td>\n"
                                #tabla_temp = f"\t<td>{temp1}</td>\n {tabla_temp}" 

                                if (int(columna) == int(columna_separacion)): #$ error
                                    print("llgamos a la mitad - terminar")
                                    tabla = f"{tabla} {tabla_temp}\n</tr>"
                                    print(tabla)

                                    if (int(fila) == int(self.fila_matriz1)):

                                        g = Digraph('g', format='png',filename='rotacion_vertical.gv',node_attr={'shape': 'plaintext'})
                                        g.node('node01', f'''<
                                        <table border="0" cellborder="1" cellspacing="0">
                                        {str(tabla)}
                                        </table>>''')
                                        g.view()

                                        self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('rotacion_vertical.gv.png'))
                                        self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                        self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                        break

                                

                                columna = 1
                                columna_ultima = self.columna_matriz1
                                fila += 1

                            x += 1

                        break
                    
                   
                aux2 = aux2.get_derecha()
                j += 1 

            aux = aux.get_siguiente()
            i += 1

    def transpuesta(self,contador):
        pass
    def limpiar_zona(self,contador):
        pass
    def agregar_linea_horizontal(self,contador):
        pass
    def agregar_linea_vertical(self,contador):
        pass
    def agregar_rectaungulo(self,contador):
        pass
    def agregar_triangulo_rectangulo(self,contador):
        pass
    # ----------------------------------------------------- PARA DOS IMAGENES -----------------------------------------------------
    def union(self,contador1,contador2):
        pass
    def interseccion(self,contador1,contador2):
        pass
    def diferencia(self,contador1,contador2):
        pass
    def diferencia_simetra(self,contador1,contador2):
        pass