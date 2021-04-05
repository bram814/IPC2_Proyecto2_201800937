from graphviz import Digraph

from tkinter import ttk, Label, StringVar, Entry, messagebox, Scrollbar
from PIL import ImageTk, Image

class Graphviz():


    def __init__(self):
        self.contador_datos = 0
        self.matriz_ortogonal = None
        self.matriz_ortogonal_nombre = None
        self.nombre_matriz = ""
        self.fila_matriz1 = 0
        self.fila_matriz2 = 0
        self.columna_matriz1 = 0
        self.columna_matriz2 = 0


    def generar_imagen(self,contador,matriz,matriz2,cont_matriz_uno,cont_matriz_dos):
        self.matriz_ortogonal = matriz
        self.matriz_ortogonal_nombre = matriz2
        if self.contador_datos == 0:
            self.contador_datos = contador
        #print('\n DATOS')
        #self.matriz_ortogonal_nombre.mostrar_matriz()
        #print("<<<<<<<<<<<")
        #self.matriz_ortogonal.mostrar_matriz2(int(cont_matriz_uno))

        print(f'\n SELECCIONA LA MATRIZ 1 -> {cont_matriz_uno} = SELECCIONA LA MATRIZ 2 -> {cont_matriz_dos}')

        
        if (0 < int(cont_matriz_uno)):
            
            if (int(cont_matriz_dos) == 0):
                self.una_imagen(cont_matriz_uno)
            elif (0< int(cont_matriz_dos)):
                self.dos_imagenes(cont_matriz_uno,cont_matriz_dos)


        self.imagen_original = ImageTk.PhotoImage(Image.open('imagen.gv.png'))
        self.label_imagen_original = Label(image=self.imagen_original)
        self.label_imagen_original.grid(row=5, column=0)
        self.nombre_label_original = Label(text="Imagen Matriz Original")
        self.nombre_label_original.grid(row=6, column=0)


        
            
       

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
                    while x < int(aux2.get_y()):
                        tabla += f'\t<td>{x+1}</td>\n'
                        x += 1
                    tabla += "</tr>\n"
                    #print(tabla)
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
        #print(f'longitud: {longitud}')
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
        #print(tabla)
        return tabla

    # ----------------------------------------------------- PARA UNA IMAGEN -----------------------------------------------------
    def rotacion_horizontal(self,contador,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2):
        #print(f"CONTADOR_TEMP {contador_datos_temp} LLAMADO {self.contador_datos}")
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos

        #print(f"$CONTADOR_TEMP {contador_datos_temp} LLAMADO {self.contador_datos}")
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
                    self.nombre_matriz = aux2.get_dato()
                    tabla += f'<tr>\n\t<td>{aux2.get_dato()}</td>\n'
                    x = 0
                    while x < int(aux2.get_y()):
                        tabla += f'\t<td>{x+1}</td>\n'
                        x += 1
                    tabla += "</tr>\n"

                    fila_separacion = 0
                    if self.fila_matriz1 % 2 == 0: # par
                        fila_separacion = int(self.fila_matriz1) / 2
                        #print(f"fila par: {str(fila_separacion)}")
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
                                if (temp2 == " "):
                                    aux2 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,str(aux2))
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp2)
                                if (temp1 == " "):
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila_ultimo,columna,aux1)
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila_ultimo,columna,temp1)
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
                                if (temp2 == " "):
                                    aux2 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,str(aux2))
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp2)
                                if (temp1 == " "):
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila_ultimo,columna,aux1)
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila_ultimo,columna,temp1)

                                if (int(fila) == int(fila_separacion)):
                                    #print("llgamos a la mitad - terminar")
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
                                    
                                    self.nombre_label = Label(text="Imagen Matriz Rotación Horizontal")
                                    self.nombre_label.grid(row=6, column=3)
                                    self.nombre_matriz = f"{self.nombre_matriz} Rotación Horizontal {contador_datos_temp}"
                                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(self.fila_matriz1),int(self.columna_matriz1),str(self.nombre_matriz))
                                    #matriz_ortogonal_temp.mostrar_matriz()
                                    temp = []
                                    i = 0
                                    temp.append(i)
                                    while i < contador_datos_temp:
                                        temp.append(i+1)
                                        i +=1
                                    combo["values"] = temp
                                    combo2["values"] = temp
                                    break

                                columna = 1
                                fila += 1
                                fila_ultimo -= 1

                            x += 1

                        break
                    else: # impar

                        fila_separacion = (int(self.fila_matriz1) / 2) + 0.5
                        #print(f"fila impar {fila_separacion}")
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
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila_ultimo,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila_ultimo,columna,temp1)
                                else:
                                    tabla += f"\t<td>{temp2}</td>\n"
                                    tabla_temp += f"\t<td>{temp1}</td>\n" 
                                    if (temp2 == " "):
                                        aux2 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,str(aux2))
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp2)
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila_ultimo,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila_ultimo,columna,temp1)

                                columna += 1
                                


                            elif (int(columna) == int(self.columna_matriz1)):

                                temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                temp2 = self.matriz_ortogonal.encontrar_posicion(contador,fila_ultimo,columna).get_dato()
                                if temp1 == "-":
                                    temp1 = " "
                                if (temp2 == "-"):
                                    temp2 = " "

                                
                                tabla += f"\t<td>{temp2}</td>\n</tr>"
                                if (temp2 == " "):
                                    aux2 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,str(aux2))
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp2)
                                   

                                if (int(fila) == int(fila_separacion)):
                                    #print("llgamos a la mitad - terminar")
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
                                    
                                    self.nombre_label = Label(text="Imagen Matriz Rotación Horizontal")
                                    self.nombre_label.grid(row=6, column=3)
                                    #matriz_ortogonal_temp.mostrar_matriz()
                                    self.nombre_matriz = f"{self.nombre_matriz} Rotación Horizontal {contador_datos_temp}"
                                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(self.fila_matriz1),int(self.columna_matriz1),str(self.nombre_matriz))
                                    temp = []
                                    i = 0
                                    temp.append(i)
                                    while i < contador_datos_temp:
                                        temp.append(i+1)
                                        i +=1
                                    combo["values"] = temp
                                    combo2["values"] = temp

                                    break

                                tabla_temp += f"\t<td>{temp1}</td>\n</tr>\n" 
                                tabla_final = f"{tabla_temp} {tabla_final}"
                                if (temp1 == " "):
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila_ultimo,columna,aux1)
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila_ultimo,columna,temp1)

                                columna = 1
                                fila += 1
                                fila_ultimo -= 1

                            x += 1

                        break
                    
                   
                aux2 = aux2.get_derecha()
                j += 1 

            aux = aux.get_siguiente()
            i += 1

        return contador_datos_temp

    # ---------------------------------------------------------------- ROTACION VERTICAL --------------------------------------------------------------------------
    def rotacion_vertical(self,contador,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2):
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos

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
                    self.nombre_matriz = aux2.get_dato()
                    tabla += f'<tr>\n\t<td>{aux2.get_dato()}</td>\n'
                    x = 0
                    while x < int(aux2.get_y()):
                        tabla += f'\t<td>{x+1}</td>\n'
                        x += 1
                    tabla += "</tr>\n"

                    columna_separacion = 0
                    if self.columna_matriz1 % 2 == 0: # par
                        columna_separacion = int(self.columna_matriz1) / 2
                        
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

                                if (temp2 == " "):
                                    aux2 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,str(aux2))
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp2)
                                if (temp1 == " "):
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna_ultima,aux1)
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna_ultima,temp1)

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
                                
                                if (temp2 == " "):
                                    aux2 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,str(aux2))
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp2)
                                if (temp1 == " "):
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna_ultima,str(aux1))
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna_ultima,temp1) 

                                if (int(columna) == int(columna_separacion)): 
                                    tabla = f"{tabla} {tabla_temp}\n</tr>"
                                   

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
                                        
                                        self.nombre_label = Label(text="Imagen Matriz Rotación Vertical")
                                        self.nombre_label.grid(row=6, column=3)

                                        self.nombre_matriz = f"{self.nombre_matriz} Rotación Vertical {contador_datos_temp}"
                                        matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(self.fila_matriz1),int(self.columna_matriz1),str(self.nombre_matriz))
                                        temp = []
                                        i = 0
                                        temp.append(i)
                                        while i < contador_datos_temp:
                                            temp.append(i+1)
                                            i +=1
                                        combo["values"] = temp
                                        combo2["values"] = temp

                                        break

                                

                                columna = 1
                                columna_ultima = self.columna_matriz1
                                fila += 1

                            x += 1

                        break
                    else: # impar

                        columna_separacion = (int(self.columna_matriz1) / 2) + 0.5
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

                                
                                if (temp2 == " "):
                                    aux2 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,str(aux2))
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp2)
                                if (temp1 == " "):
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna_ultima,aux1)
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna_ultima,temp1) 

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
                                
                                if (temp1 == " "):
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna_ultima,aux1)
                                else:
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna_ultima,temp1)

                                if (int(columna) == int(columna_separacion)): 
                                    tabla = f"{tabla} {tabla_temp}\n</tr>"

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
                                        
                                        self.nombre_label = Label(text="Imagen Matriz Rotación Vertical")
                                        self.nombre_label.grid(row=6, column=3)
                                        
                                        self.nombre_matriz = f"{self.nombre_matriz} Rotación Vertical {contador_datos_temp}"
                                        matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(self.fila_matriz1),int(self.columna_matriz1),str(self.nombre_matriz))
                                        temp = []
                                        i = 0
                                        temp.append(i)
                                        while i < contador_datos_temp:
                                            temp.append(i+1)
                                            i +=1
                                        combo["values"] = temp
                                        combo2["values"] = temp

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
    # ---------------------------------------------------------------- TRANSPUESTA --------------------------------------------------------------------------
   
    def transpuesta(self,contador,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2):
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos

        tabla = ""
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
                    self.nombre_matriz = aux2.get_dato()
                    tabla += f'<tr>\n\t<td>{aux2.get_dato()}</td>\n'
                    x = 0
                    while x < int(aux2.get_x()):
                        tabla += f'\t<td>{x+1}</td>\n'
                        x += 1
                    tabla += "</tr>\n"
                    longitud = int(self.fila_matriz1) * int(self.columna_matriz1)
                    x = 0
                    columna = 1
                    fila = 1

                    if int(self.fila_matriz1) == int(self.columna_matriz1):

                        while x < longitud:

                            
                            if int(columna) < int(self.columna_matriz1):
                            
                                if int(columna) == 1:
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                            
                                if (0 < int(fila) <= int(self.columna_matriz1)) and 0 < int(columna) <=int(self.fila_matriz1):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,columna,fila).get_dato()
                                    if temp1 == "-":
                                        temp1 = " "
        

                                    tabla += f"\t<td>{temp1}</td>\n"

                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 
                                else:
                                    
                                    tabla += "\t<td> </td>\n"
                                   
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 
                                    
                                columna += 1

                            elif int(columna) == int(self.columna_matriz1):
                                
                                if (0 < int(fila) <= int(self.columna_matriz1) and  0 < int(columna) <=int(self.fila_matriz1)):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,columna,fila).get_dato()
                                    if temp1 == "-":
                                        temp1 = " "
                                    tabla += f"\t<td>{temp1}</td>\n</tr>"
                                    
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 
                                else:
                                    
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 
                                    tabla += "\t<td> </td>\n</tr>"

                                if int(fila) == int(self.columna_matriz1):
                                    g = Digraph('g', format='png',filename='transpuesta.gv',node_attr={'shape': 'plaintext'})
                                    g.node('node01', f'''<
                                    <table border="0" cellborder="1" cellspacing="0">
                                    {str(tabla)}
                                    </table>>''')
                                    g.view()

                                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('transpuesta.gv.png'))
                                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                    
                                    self.nombre_label = Label(text="Imagen Matriz Transpuesta")
                                    self.nombre_label.grid(row=6, column=3)

                                    self.nombre_matriz = f"{self.nombre_matriz} Transpuesta {contador_datos_temp}"
                                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(self.fila_matriz1),int(self.columna_matriz1),str(self.nombre_matriz))
                                    temp = []
                                    i = 0
                                    temp.append(i)
                                    while i < contador_datos_temp:
                                        temp.append(i+1)
                                        i +=1
                                    combo["values"] = temp
                                    combo2["values"] = temp


                                    break
                                
                                columna = 1
                                fila += 1
                            

                            x += 1
                    elif self.columna_matriz1 < self.fila_matriz1:
                        while x < longitud:

                            
                            if int(columna) < int(self.columna_matriz1):
                            
                                if int(columna) == 1:
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                            
                                if (0 < int(fila) <= int(self.columna_matriz1)) and 0 < int(columna) <=int(self.fila_matriz1):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,columna,fila).get_dato()
                                    if temp1 == "-":
                                        temp1 = " "
        

                                    tabla += f"\t<td>{temp1}</td>\n"

                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1)

                                else:
                                    
                                    tabla += "\t<td> </td>\n"
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1) 
                                    
                                columna += 1

                            elif int(columna) == int(self.columna_matriz1):
                                
                                if (0 < int(fila) <= int(self.columna_matriz1) and  0 < int(columna) <=int(self.fila_matriz1)):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,columna,fila).get_dato()
                                    if temp1 == "-":
                                        temp1 = " "
                                        
                                    if int(self.columna_matriz1) < int(self.fila_matriz1):
                                        tabla += f"\t<td>{temp1}</td>\n"
                                        
                                        if (temp1 == " "):
                                            aux1 = "-"
                                            matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                        else:
                                            matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 

                                        cont_temp = columna

                                        while cont_temp < self.fila_matriz1:

                                            temp2 = self.matriz_ortogonal.encontrar_posicion(contador,cont_temp+1,fila).get_dato()
                                            
                                            if temp2 == "-":
                                                temp2 = " "
                                            tabla += f"\t<td>{temp2}</td>\n"

                                            if (temp2 == " "):
                                                aux2 = "-"
                                                matriz_ortogonal_temp.agregar(contador_datos_temp,fila,cont_temp+1,aux2)
                                            else:
                                                matriz_ortogonal_temp.agregar(contador_datos_temp,fila,cont_temp+1,temp2) 

                                            cont_temp += 1
                                
                                   
                                else:
                                   
                                    tabla += "\t<td> </td>\n"
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)

                                tabla += "</tr>\n"

                                

                                #if int(fila) == int(self.columna_matriz1) or int(columna) == (self.fila_matriz1):
                                if int(fila) == int(self.columna_matriz1):
                                    g = Digraph('g', format='png',filename='transpuesta.gv',node_attr={'shape': 'plaintext'})
                                    g.node('node01', f'''<
                                    <table border="0" cellborder="1" cellspacing="0">
                                    {str(tabla)}
                                    </table>>''')
                                    g.view()

                                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('transpuesta.gv.png'))
                                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                    
                                    self.nombre_label = Label(text="Imagen Matriz Transpuesta")
                                    self.nombre_label.grid(row=6, column=3)
                                    self.nombre_matriz = f"{self.nombre_matriz} Transpuesta {contador_datos_temp}"
                                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(self.columna_matriz1),int(self.fila_matriz1),str(self.nombre_matriz))
                                    temp = []
                                    i = 0
                                    temp.append(i)
                                    while i < contador_datos_temp:
                                        temp.append(i+1)
                                        i +=1
                                    combo["values"] = temp
                                    combo2["values"] = temp


                                    break
                                
                                columna = 1
                                fila += 1
                            

                            x += 1
                    elif self.columna_matriz1 > self.fila_matriz1:
                        
                        
                        while x < longitud:

                            
                            if int(columna) < int(self.fila_matriz1):
                            
                                if int(columna) == 1:
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                            
                                if (0 < int(fila) <= int(self.columna_matriz1)) and 0 < int(columna) <=int(self.fila_matriz1):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,columna,fila).get_dato()
                                    if temp1 == "-":
                                        temp1 = " "
        

                                    tabla += f"\t<td>{temp1}</td>\n"
                                
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 
                                else:
                                    
                                    tabla += "\t<td> </td>\n"
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1) 
                                    
                                columna += 1

                            elif int(columna) == int(self.fila_matriz1):
                                
                                if (0 < int(fila) <= int(self.columna_matriz1) and  0 < int(columna) <=int(self.fila_matriz1)):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,columna,fila).get_dato()
                                    if temp1 == "-":
                                        temp1 = " "
                                    tabla += f"\t<td>{temp1}</td>\n"

                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 
                                else:
                                   
                                    tabla += "\t<td> </td>\n"
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1) 

                                tabla += "</tr>\n"

                        
                                if int(fila) == int(self.columna_matriz1):
                                    g = Digraph('g', format='png',filename='transpuesta.gv',node_attr={'shape': 'plaintext'})
                                    g.node('node01', f'''<
                                    <table border="0" cellborder="1" cellspacing="0">
                                    {str(tabla)}
                                    </table>>''')
                                    g.view()

                                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('transpuesta.gv.png'))
                                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                    
                                    self.nombre_label = Label(text="Imagen Matriz Transpuesta")
                                    self.nombre_label.grid(row=6, column=3)
                                    self.nombre_matriz = f"{self.nombre_matriz} Transpuesta {contador_datos_temp}"
                                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(self.columna_matriz1),int(self.fila_matriz1),str(self.nombre_matriz))
                                    temp = []
                                    i = 0
                                    temp.append(i)
                                    while i < contador_datos_temp:
                                        temp.append(i+1)
                                        i +=1
                                    combo["values"] = temp
                                    combo2["values"] = temp


                                    break
                                
                                columna = 1
                                fila += 1
                            

                            x += 1
                    
                   
                aux2 = aux2.get_derecha()
                j += 1 

            aux = aux.get_siguiente()
            i += 1

 # ---------------------------------------------------------------- LIMPIAR ZONA DE UNA IMAGEN --------------------------------------------------------------------------
   
    def limpiar_zona(self,contador,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2,texto):
       
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos
        aceptacion = False

        tabla = ""
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
                    self.nombre_matriz = aux2.get_dato()
                    
            
                    print(aceptacion)
                    if aceptacion == False:
                        estado = 1
                        fila_inicial = 0
                        columna_inicial = 0
                        fila_final = 0
                        columna_final = 0
                    
                        for text in texto:
                            print(text)
                            if (estado==1): # Guarda fila_inicial
                                if (0 < int(text) <= int(self.fila_matriz1)):
                                    fila_inicial = int(text)
                                    estado += 1
                                else:
                                    estado = 8

                            elif (estado==2): # Comprueba si es una coma [,]
                                if (text == ","):
                                    estado += 1
                                else:
                                    estado = 8

                            elif (estado==3): # Guarda columna_inicial
                                if (0 < int(text) <= int(self.columna_matriz1)):
                                    columna_inicial = int(text)
                                    estado += 1
                                else:
                                    estado = 8

                            elif (estado==4): # Comprueba si es un punto coma [;]
                                if (text == ";"):
                                    estado += 1
                                else:
                                    estado = 8

                            elif (estado==5): # Guardar Fila final
                                if (fila_inicial <= int(text) <= int(self.fila_matriz1)):
                                    fila_final = int(text)
                                    estado += 1
                                else:
                                    estado = 8

                            elif (estado==6): # Comprueba si es punto coma [,]
                                if (text == ","):
                                    estado += 1
                                else:
                                    estado = 8

                            elif (estado==7): #  Guardar Columna Final
                                if (int(columna_final) <= int(text) <= int(self.columna_matriz1)):
                                    columna_final = int(text)

                                    if (int(fila_inicial) <= int(fila_final) <= int(self.fila_matriz1) and int(columna_inicial) <= int(columna_final) <= int(self.fila_matriz1)):

                                        aceptacion = True
                                        print(f"Inicio a Limpiar({fila_inicial},{columna_inicial}) ; ({fila_final},{columna_final})")
                                    else:
                                        aceptacion = False
                                    break
                                else:
                                    estado = 8
                            else:
                                aceptacion = False
                                break

                    if (aceptacion == False):
                        messagebox.showinfo(message="Estructura Incorrecta -> filaInicial,columnaInicial;filaFinal,columnaFinal")

                    else:
                        
                        tabla += f'<tr>\n\t<td>{aux2.get_dato()}</td>\n'
                        x = 0
                        while x < int(aux2.get_y()):
                            tabla += f'\t<td>{x+1}</td>\n'
                            x += 1
                        tabla += "</tr>\n"
                        longitud = int(self.fila_matriz1) * int(self.columna_matriz1)
                        x = 0
                        columna = 1
                        fila = 1


                        while x < longitud:
                                
                            if int(columna) < int(self.columna_matriz1):
                                
                                if int(columna) == 1:
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                                temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                if (temp1 == "-"):
                                    temp1 = " "

                                if (int(fila_inicial) <= int(fila) <= int(fila_final) and int(columna_inicial) <= columna <= int(columna_final)):
                                    tabla += f"\t<td> </td>\n"
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                else:
                                    tabla += f"\t<td>{temp1}</td>\n"
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 

                                columna += 1

                            elif int(columna) == int(self.columna_matriz1):
                                
                                temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                if (temp1 == "-"):
                                    temp1 = " "

                                if (int(fila_inicial) <= int(fila) <= int(fila_final) and int(columna_inicial) <= columna <= int(columna_final)):
                                    tabla += f"\t<td> </td>\n"
                                    aux1 = "-"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                else:
                                    tabla += f"\t<td>{temp1}</td>\n"
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 
                                tabla += "</tr>\n"

                                if int(fila) == int(self.fila_matriz1):
                                    
                                    g = Digraph('g', format='png',filename='limpiar_zona.gv',node_attr={'shape': 'plaintext'})
                                    g.node('node01', f'''<
                                    <table border="0" cellborder="1" cellspacing="0">
                                    {str(tabla)}
                                    </table>>''')
                                    g.view()

                                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('limpiar_zona.gv.png'))
                                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                    
                                    self.nombre_label = Label(text=f"Limpiar Zona {fila_inicial},{columna_inicial};{fila_final}{columna_final}")
                                    self.nombre_label.grid(row=6, column=3)
                                        
                                    self.nombre_matriz = f"{self.nombre_matriz} Limpiar Zona {contador_datos_temp}"
                                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(self.fila_matriz1),int(self.columna_matriz1),str(self.nombre_matriz))
                                    temp = []
                                    i = 0
                                    temp.append(i)
                                    while i < contador_datos_temp:
                                        temp.append(i+1)
                                        i +=1
                                    combo["values"] = temp
                                    combo2["values"] = temp
                                    
                                    break
                                columna = 1
                                fila += 1
                                

                            x += 1
                    
                   
                aux2 = aux2.get_derecha()
                j += 1 

            aux = aux.get_siguiente()
            i += 1
        
        
 # ---------------------------------------------------------------- AGREGAR LINEA HORIZONTAL A UNA IMAGEN --------------------------------------------------------------------------
          
    def agregar_linea_horizontal(self,contador,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2,texto):
       
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos
        aceptacion = False

        tabla = ""
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
                    self.nombre_matriz = aux2.get_dato()
                    
            
                    #print(aceptacion)
                    if aceptacion == False:
                        total = 1
                        for text_temp in texto:
                            print(text_temp)
                            total += 1

                        estado = 1
                        fila_inicial = 0
                        columna_inicial = 0
                        cantidad_elementos = 0
                        fila_final = 0
                        columna_final = 0
                        concatenar_fila = ""
                        total_temp = 1

                        for text in texto:
                            total_temp += 1

                            if (estado==1): # Guarda fila_inicial
                                if (0 < int(text) <= int(self.fila_matriz1)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    estado += 1
                                else:
                                    estado = 8

                            elif (estado==2): # Comprueba si es una coma [,]
                                if (text == ","):
                                    fila_inicial = int(concatenar_fila)
                                    concatenar_fila = ""
                                    estado += 1
                                else:
                                    if (0 <= int(text) <= int(self.fila_matriz1)):
                                        concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                        estado = 2
                                    else:
                                        estado = 8

                            elif (estado==3): # Guarda columna_inicial
                                if (0 < int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    estado += 1
                                else:
                                    estado = 8

                            elif (estado==4): # Comprueba si es un punto coma [;]
                                
                                if (text == ";"):
                                    columna_inicial = int(concatenar_fila)
                                    concatenar_fila = ""
                                    estado += 1
                                
                                else:
                                    if (0 <= int(text)):
                                        concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                        estado = 4
                                    else:
                                        estado = 8

                            elif (estado==5): # Guardar Cantidad
                                if (0 <= int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    if (int(total_temp) == int(total)):
                                        cantidad_elementos = int(concatenar_fila)
                                        fila_final = fila_inicial
                                        columna_final = int(columna_inicial) + int(cantidad_elementos) - 1
                                        if (columna_final <= 0):
                                            columna_final = columna_inicial
                                        print(f"O({fila_inicial},{columna_inicial}) -- F({fila_final},{columna_final})") 

                                        aceptacion = True
                                        break
                                    else:
                                        estado = 5
                                else:
                                    aceptacion = False
                                    break
                            else:
                                aceptacion = False
                                break
                            

                    if (aceptacion == False):
                        messagebox.showinfo(message="Estructura Incorrecta -> filaInicial,columnaInicial;cantidadAgregar")

                    else:
                        
                        tabla += f'<tr>\n\t<td>{aux2.get_dato()}</td>\n'
                        x = 0
                        while x < int(aux2.get_y()):
                            tabla += f'\t<td>{x+1}</td>\n'
                            x += 1
                        if (int(columna_final) > int(self.columna_matriz1)): # agregando mas espacio en columna
                            i = 0
                            cont_temp_cantidad = int(columna_final) - int(self.columna_matriz1)
                            while i < cont_temp_cantidad:
                                tabla += f'\t<td>{x+1}</td>\n'
                                x += 1
                                i += 1
                        tabla += "</tr>\n"
                        
                        x = 0
                        columna = 1
                        fila = 1
                        cont_final = 0
                        if (int(columna_final) > int(self.columna_matriz1)):
                            cont_final = columna_final
                        elif (int(self.columna_matriz1) >= int(columna_final)):
                            cont_final = self.columna_matriz1
                        longitud = int(self.fila_matriz1) * int(cont_final)
                        while x < longitud:
                                
                            if int(columna) < int(cont_final):
                                
                                if int(columna) == 1:
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                                
                                if (int(self.columna_matriz1) < int(columna)):
                                    temp1 = " "
                                elif (int(columna) <= int(self.columna_matriz1) ):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                    if (temp1 == "-"):
                                        temp1 = " "

                                if (int(fila_inicial) == int(fila)):
                                    if (int(columna_inicial) <= int(columna) <= int(columna_final)):
                                        print(f"{fila}{columna} ----------- {columna_inicial}<{columna}<{columna_final}")
                                        tabla += f"\t<td>*</td>\n"
                                        aux1 = "*"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        tabla += f"\t<td>{temp1}</td>\n"
                                        if (temp1 == " "):
                                            aux1 = "-"
                                            matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                        else:
                                            matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 
                                else:
                                    tabla += f"\t<td>{temp1}</td>\n"
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 

                                columna += 1

                            elif int(columna) == int(cont_final):
                                
                                if (int(self.columna_matriz1) < int(columna)):
                                    temp1 = " "
                                elif (int(self.columna_matriz1) >= int(columna)):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                    if (temp1 == "-"):
                                        temp1 = " "

                                if (int(fila_inicial) == int(fila)):
                                    if (int(columna_inicial) <= int(columna) <= int(columna_final)):
                                        print(f"{fila}{columna} ----------- {columna_inicial}<{columna}<{columna_final}")
                                        tabla += f"\t<td>*</td>\n"
                                        aux1 = "*"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        tabla += f"\t<td>{temp1}</td>\n"
                                        if (temp1 == " "):
                                            aux1 = "-"
                                            matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                        else:
                                            matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 
                                else:
                                    tabla += f"\t<td>{temp1}</td>\n"
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 

                                tabla += "</tr>\n"
                                if int(fila) == int(self.fila_matriz1):
                                    
                                    g = Digraph('g', format='png',filename='Lhorizontal.gv',node_attr={'shape': 'plaintext'})
                                    g.node('node01', f'''<
                                    <table border="0" cellborder="1" cellspacing="0">
                                    {str(tabla)}
                                    </table>>''')
                                    g.view()

                                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('Lhorizontal.gv.png'))
                                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                    
                                    self.nombre_label = Label(text=f"Linea Horizontal {fila_inicial},{columna_inicial};{fila_final}{columna_final}")
                                    self.nombre_label.grid(row=6, column=3)
                                        
                                    self.nombre_matriz = f"{self.nombre_matriz} Linea_horizontal {contador_datos_temp}"
                                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(self.fila_matriz1),int(cont_final),str(self.nombre_matriz))
                                    temp = []
                                    i = 0
                                    temp.append(i)
                                    while i < contador_datos_temp:
                                        temp.append(i+1)
                                        i +=1
                                    combo["values"] = temp
                                    combo2["values"] = temp
                                    
                                    break
                                columna = 1
                                fila += 1
                                

                            x += 1
                    
                   
                aux2 = aux2.get_derecha()
                j += 1 

            aux = aux.get_siguiente()
            i += 1
# ---------------------------------------------------------------- AGREGAR LINEA VERTICAL A UNA IMAGEN --------------------------------------------------------------------------
         
    def agregar_linea_vertical(self,contador,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2,texto):
       
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos
        aceptacion = False

        tabla = ""
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
                    self.nombre_matriz = aux2.get_dato()
                    
            
                    print(aceptacion)
                    if aceptacion == False:
                        total = 1
                        for text_temp in texto:
                            print(text_temp)
                            total += 1
                        print(f"TOTAL {total}")

                        estado = 1
                        fila_inicial = 0
                        columna_inicial = 0
                        cantidad_elementos = 0
                        fila_final = 0
                        columna_final = 0
                        concatenar_fila = ""
                        total_temp = 1

                        for text in texto:
                            total_temp += 1
                            print(text)
                            print(f'estado: {estado}')
                            if (estado==1): # Guarda fila_inicial
                                if (0 < int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    estado += 1
                                else:
                                    estado = 8

                            elif (estado==2): # Comprueba si es una coma [,]
                                if (text == ","):
                                    fila_inicial = int(concatenar_fila)
                                    concatenar_fila = ""
                                    estado += 1
                                else:
                                    if (0 <= int(text)):
                                        concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                        estado = 2
                                    else:
                                        estado = 8

                            elif (estado==3): # Guarda columna_inicial
                                if (0 < int(text) <= self.columna_matriz1):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    estado += 1
                                else:
                                    estado = 8

                            elif (estado==4): # Comprueba si es un punto coma [;]
                                
                                if (text == ";"):
                                    columna_inicial = int(concatenar_fila)
                                    
                                    concatenar_fila = ""
                                    estado += 1
                                
                                else:
                                    if (0 <= int(text) <= self.columna_matriz1):
                                        concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                        estado = 4
                                    else:
                                        estado = 8

                            elif (estado==5): # Guardar Cantidad
                                if (0 <= int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    if (int(total_temp) == int(total)):
                                        cantidad_elementos = int(concatenar_fila)
                                        columna_final = columna_inicial
                                        fila_final = int(fila_inicial) + int(cantidad_elementos) - 1
                                        if (fila_final <= 0):
                                            fila_final = fila_inicial
                                        print(f"O({fila_inicial},{columna_inicial}) -- F({fila_final},{columna_final})") 

                                        aceptacion = True
                                        break
                                    else:
                                        estado = 5
                                else:
                                    aceptacion = False
                                    break
                            else:
                                aceptacion = False
                                break
                            

                    if (aceptacion == False):
                        messagebox.showinfo(message="Estructura Incorrecta -> filaInicial,columnaInicial;cantidadAgregar")

                    else:
                        
                        tabla += f'<tr>\n\t<td>{aux2.get_dato()}</td>\n'
                        x = 0
                        while x < int(aux2.get_y()):
                            tabla += f'\t<td>{x+1}</td>\n'
                            x += 1
                        tabla += "</tr>\n"
                        
                        x = 0
                        columna = 1
                        fila = 1
                        cont_final = 0
                        if (int(fila_final) > int(self.fila_matriz1)):
                            cont_final = fila_final
                        elif (int(self.fila_matriz1) >= int(fila_final)):
                            cont_final = self.fila_matriz1

                        longitud = int(self.columna_matriz1) * int(cont_final)
                        while x < longitud:
                                
                            if int(columna) < int(self.columna_matriz1):
                                
                                if int(columna) == 1:
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                                
                                if (int(self.fila_matriz1) < int(fila)):
                                    temp1 = " "
                                elif (int(fila) <= int(self.fila_matriz1)):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                    if (temp1 == "-"):
                                        temp1 = " "

                                if (int(columna_inicial) == int(columna)):
                                    if (int(fila_inicial) <= int(fila) <= int(fila_final)):
                                        print(f"{fila}{columna} ----------- {fila_inicial}<{fila}<{fila_final}")
                                        tabla += f"\t<td>*</td>\n"
                                        aux1 = "*"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        tabla += f"\t<td>{temp1}</td>\n"
                                        if (temp1 == " "):
                                            aux1 = "-"
                                            matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                        else:
                                            matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 
                                else:
                                    tabla += f"\t<td>{temp1}</td>\n"
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 

                                columna += 1

                            elif int(columna) == int(self.columna_matriz1):
                                
                                if (int(self.fila_matriz1) < int(fila)):
                                    temp1 = " "
                                elif (int(fila) <= int(self.fila_matriz1)):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                    if (temp1 == "-"):
                                        temp1 = " "

                                if (int(columna_inicial) == int(columna)):
                                    if (int(fila_inicial) <= int(fila) <= int(fila_final)):
                                        print(f"{fila}{columna} ----------- {fila_inicial}<{fila}<{fila_final}")
                                        tabla += f"\t<td>*</td>\n"
                                        aux1 = "*"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        tabla += f"\t<td>{temp1}</td>\n"
                                        if (temp1 == " "):
                                            aux1 = "-"
                                            matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                        else:
                                            matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 
                                else:
                                    tabla += f"\t<td>{temp1}</td>\n"
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 

                                tabla += "</tr>\n"
                                if int(fila) == int(cont_final):
                                    
                                    g = Digraph('g', format='png',filename='Lvertical.gv',node_attr={'shape': 'plaintext'})
                                    g.node('node01', f'''<
                                    <table border="0" cellborder="1" cellspacing="0">
                                    {str(tabla)}
                                    </table>>''')
                                    g.view()

                                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('Lvertical.gv.png'))
                                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                    
                                    self.nombre_label = Label(text=f"Linea Vertical {fila_inicial},{columna_inicial};{fila_final},{columna_final}")
                                    self.nombre_label.grid(row=6, column=3)
                                        
                                    self.nombre_matriz = f"{self.nombre_matriz} Linea_Vertical {contador_datos_temp}"
                                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(cont_final),int(self.columna_matriz1),str(self.nombre_matriz))
                                    temp = []
                                    i = 0
                                    temp.append(i)
                                    while i < contador_datos_temp:
                                        temp.append(i+1)
                                        i +=1
                                    combo["values"] = temp
                                    combo2["values"] = temp
                                    
                                    break
                                columna = 1
                                fila += 1
                                

                            x += 1
                    
                   
                aux2 = aux2.get_derecha()
                j += 1 

            aux = aux.get_siguiente()
            i += 1
# ----------------------------------------------------- AGREGAR RECTANGULO PARA UNA IMAGEN -----------------------------------------------------
    def agregar_rectaungulo(self,contador,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2,texto):
       
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos
        aceptacion = False

        tabla = ""
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
                    self.nombre_matriz = aux2.get_dato()
                    
            
                    print(aceptacion)
                    if aceptacion == False:
                        total = 1
                        for text_temp in texto:
                            print(text_temp)
                            total += 1
                        print(f"TOTAL {total}")

                        estado = 1
                        fila_inicial = 0
                        columna_inicial = 0
                        fila_final = 0
                        columna_final = 0
                        concatenar_fila = ""
                        total_temp = 1

                        cont_fila = 0
                        cont_columna = 0

                        for text in texto:
                            total_temp += 1
                            print(text)
                            print(f'estado: {estado}')
                            if (estado==1): # Guarda fila_inicial
                                if (0 < int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    estado += 1
                                else:
                                    estado = 9

                            elif (estado==2): # Comprueba si es una coma [,]
                                if (text == ","):
                                    fila_inicial = int(concatenar_fila)
                                    concatenar_fila = ""
                                    estado += 1
                                else:
                                    if (0 <= int(text)):
                                        concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                        estado = 2
                                    else:
                                        estado = 9

                            elif (estado==3): # Guarda columna_inicial
                                if (0 < int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    estado += 1
                                else:
                                    estado = 9

                            elif (estado==4): # Comprueba si es un punto coma [;]
                                
                                if (text == ";"):
                                    columna_inicial = int(concatenar_fila)
                                    
                                    concatenar_fila = ""
                                    estado += 1
                                
                                else:
                                    if (0 <= int(text)):
                                        concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                        estado = 4
                                    else:
                                        estado = 9

                            elif (estado==5): # Guarda fila_final
                                if (0 < int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    estado += 1
                                else:
                                    estado = 9

                            elif (estado==6): # Comprueba si es una coma [,]
                                if (text == ","):
                                    fila_final = int(concatenar_fila)
                                    concatenar_fila = ""
                                    estado += 1
                                else:
                                    if (0 <= int(text)):
                                        concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                        estado = 6
                                    else:
                                        estado = 9
                            elif (estado==7): # Guarda columna_final
                                if (0 <= int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    
                                    if (int(total_temp) == int(total)):
                                        columna_final = int(concatenar_fila)
                                        if (int(fila_final)>int(columna_final) or int(fila_final)<int(columna_final)):
                                            cont_fila = int(fila_inicial) + int(fila_final) - 1
                                            if (int(cont_fila) <= 0):
                                                cont_fila = fila_inicial
                                            if (int(cont_columna) <= 0):
                                                cont_columna = columna_inicial
                                            cont_columna = int(columna_inicial) + int(columna_final) - 1 
                                            aceptacion = True
                                            break
                                            
                                        else:
                                            estado = 9
                                            aceptacion = False
                                            break
                                    else:
                                        estado = 7
                                else:
                                    estado = 9
                                    aceptacion = False
                                    break
                            else:
                                aceptacion = False
                                break
                            

                    if (aceptacion == False):
                        messagebox.showinfo(message="Estructura Incorrecta -> filaInicial,columnaInicial;filaFinal,columnaFinal filaFinal<columnaFinal - filaFinal>columnaFinal ")

                    else:
                        
                        tabla += f'<tr>\n\t<td>{aux2.get_dato()}</td>\n'
                        x = 0
                        while x < int(aux2.get_y()):
                            tabla += f'\t<td>{x+1}</td>\n'
                            x += 1
                        if (int(cont_columna) > int(self.columna_matriz1)): # agregando mas espacio en columna
                            i = 0
                            cont_temp_cantidad = int(cont_columna) - int(self.columna_matriz1)
                            while i < cont_temp_cantidad:
                                tabla += f'\t<td>{x+1}</td>\n'
                                x += 1
                                i += 1
                        tabla += "</tr>\n"

                        
                        x = 0
                        columna = 1
                        fila = 1
                        max_fila = 0
                        max_columna =0
                        if (int(cont_fila) > int(self.fila_matriz1)):
                            max_fila = cont_fila
                        elif (int(self.fila_matriz1) >= int(fila_final)):
                            max_fila = self.fila_matriz1
                        
                        if (int(cont_columna) > int(self.columna_matriz1)):
                            max_columna = cont_columna
                        elif (int(self.columna_matriz1) >= int(cont_columna)):
                            max_columna = self.columna_matriz1

                        longitud = int(max_fila) * int(max_columna)
                        while x < longitud:
                                
                            if int(columna) < int(max_columna):
                                
                                if int(columna) == 1:
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                                
                                if (int(self.fila_matriz1) < int(fila) or int(self.columna_matriz1) < int(columna)):
                                    temp1 = " "
                                elif (int(fila) <= int(self.fila_matriz1) and int(columna) <= int(self.columna_matriz1)):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                    if (temp1 == "-"):
                                        temp1 = " "

                                if (int(columna_inicial) <= int(columna) <= int(cont_columna) and int(fila_inicial) <= int(fila) <= int(cont_fila)):
                                    print(f"{fila}{columna} ----------- {fila_inicial}<{fila}<{fila_final}")
                                    tabla += f"\t<td>*</td>\n"
                                    aux1 = "*"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                else:
                                    tabla += f"\t<td>{temp1}</td>\n"
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 

                                columna += 1

                            elif int(columna) == int(max_columna):
                                 
                                if (int(self.fila_matriz1) < int(fila) or int(self.columna_matriz1) < int(columna)):
                                    temp1 = " "
                                elif (int(fila) <= int(self.fila_matriz1) and int(columna) <= int(self.columna_matriz1)):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                    if (temp1 == "-"):
                                        temp1 = " "

                                if (int(columna_inicial) <= int(columna) <= int(cont_columna) and int(fila_inicial) <= int(fila) <= int(cont_fila)):
                                    print(f"{fila}{columna} ----------- {fila_inicial}<{fila}<{fila_final}")
                                    tabla += f"\t<td>*</td>\n"
                                    aux1 = "*"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                else:
                                    tabla += f"\t<td>{temp1}</td>\n"
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 

                                tabla += "</tr>\n"
                                if int(fila) == int(max_fila):
                                    
                                    g = Digraph('g', format='png',filename='rectangulo.gv',node_attr={'shape': 'plaintext'})
                                    g.node('node01', f'''<
                                    <table border="0" cellborder="1" cellspacing="0">
                                    {str(tabla)}
                                    </table>>''')
                                    g.view()

                                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('rectangulo.gv.png'))
                                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                    
                                    self.nombre_label = Label(text=f"Rectangulo {fila_inicial},{columna_inicial};{fila_final}x{columna_final}")
                                    self.nombre_label.grid(row=6, column=3)
                                        
                                    self.nombre_matriz = f"{self.nombre_matriz} Rectangulo {contador_datos_temp}"
                                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(max_fila),int(max_columna),str(self.nombre_matriz))
                                    temp = []
                                    i = 0
                                    temp.append(i)
                                    while i < contador_datos_temp:
                                        temp.append(i+1)
                                        i +=1
                                    combo["values"] = temp
                                    combo2["values"] = temp
                                    
                                    break
                                columna = 1
                                fila += 1
                                

                            x += 1
                    
                   
                aux2 = aux2.get_derecha()
                j += 1 

            aux = aux.get_siguiente()
            i += 1

    
    # ----------------------------------------------------- AGREGAR TRIANGULO RECTANGULO PARA UNA IMAGEN -----------------------------------------------------
    def agregar_triangulo_rectangulo(self,contador,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2,texto):
       
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos
        aceptacion = False

        tabla = ""
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
                    self.nombre_matriz = aux2.get_dato()
                    
            
                    print(aceptacion)
                    if aceptacion == False:
                        total = 1
                        for text_temp in texto:
                            print(text_temp)
                            total += 1
                        print(f"TOTAL {total}")

                        estado = 1
                        fila_inicial = 0
                        columna_inicial = 0
                        fila_final = 0
                        columna_final = 0
                        concatenar_fila = ""
                        total_temp = 1

                        cont_fila = 0
                        cont_columna = 0

                        for text in texto:
                            total_temp += 1
                            print(text)
                            print(f'estado: {estado}')
                            if (estado==1): # Guarda fila_inicial
                                if (0 < int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    estado += 1
                                else:
                                    estado = 9

                            elif (estado==2): # Comprueba si es una coma [,]
                                if (text == ","):
                                    fila_inicial = int(concatenar_fila)
                                    concatenar_fila = ""
                                    estado += 1
                                else:
                                    if (0 <= int(text)):
                                        concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                        estado = 2
                                    else:
                                        estado = 9

                            elif (estado==3): # Guarda columna_inicial
                                if (0 < int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    estado += 1
                                else:
                                    estado = 9

                            elif (estado==4): # Comprueba si es un punto coma [;]
                                
                                if (text == ";"):
                                    columna_inicial = int(concatenar_fila)
                                    
                                    concatenar_fila = ""
                                    estado += 1
                                
                                else:
                                    if (0 <= int(text)):
                                        concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                        estado = 4
                                    else:
                                        estado = 9

                            elif (estado==5): # Guarda fila_final
                                if (0 < int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    estado += 1
                                else:
                                    estado = 9

                            elif (estado==6): # Comprueba si es una coma [,]
                                if (text == ","):
                                    fila_final = int(concatenar_fila)
                                    concatenar_fila = ""
                                    estado += 1
                                else:
                                    if (0 <= int(text)):
                                        concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                        estado = 6
                                    else:
                                        estado = 9
                            elif (estado==7): # Guarda columna_final
                                if (0 <= int(text)):
                                    concatenar_fila = f"{str(concatenar_fila)}{str(text)}"
                                    
                                    if (int(total_temp) == int(total)):
                                        columna_final = int(concatenar_fila)
                                        cont_fila = int(fila_inicial) + int(fila_final) - 1
                                        if (int(cont_fila) <= 0):
                                            cont_fila = fila_inicial
                                        if (int(cont_columna) <= 0):
                                            cont_columna = columna_inicial
                                        cont_columna = int(columna_inicial) + int(columna_final) - 1 
                                        aceptacion = True
                                        break
                                            
                                    else:
                                        estado = 7
                                else:
                                    estado = 9
                                    aceptacion = False
                                    break
                            else:
                                aceptacion = False
                                break
                            

                    if (aceptacion == False):
                        messagebox.showinfo(message="Estructura Incorrecta -> filaInicial,columnaInicial;filaFinal,columnaFinal filaFinal<columnaFinal - filaFinal>columnaFinal ")

                    else:
                        
                        tabla += f'<tr>\n\t<td>{aux2.get_dato()}</td>\n'
                        x = 0
                        while x < int(aux2.get_y()):
                            tabla += f'\t<td>{x+1}</td>\n'
                            x += 1
                        if (int(cont_columna) > int(self.columna_matriz1)): # agregando mas espacio en columna
                            i = 0
                            cont_temp_cantidad = int(cont_columna) - int(self.columna_matriz1)
                            while i < cont_temp_cantidad:
                                tabla += f'\t<td>{x+1}</td>\n'
                                x += 1
                                i += 1
                        tabla += "</tr>\n"

                        
                        x = 0
                        columna = 1
                        fila = 1
                        max_fila = 0
                        max_columna =0
                        if (int(cont_fila) > int(self.fila_matriz1)):
                            max_fila = cont_fila
                        elif (int(self.fila_matriz1) >= int(fila_final)):
                            max_fila = self.fila_matriz1
                        
                        if (int(cont_columna) > int(self.columna_matriz1)):
                            max_columna = cont_columna
                        elif (int(self.columna_matriz1) >= int(cont_columna)):
                            max_columna = self.columna_matriz1

                        longitud = int(max_fila) * int(max_columna)
                        while x < longitud:
                                
                            if int(columna) < int(max_columna):
                                
                                if int(columna) == 1:
                                    tabla += f"<tr>\n\t<td>{fila}</td>\n"
                                
                                if (int(self.fila_matriz1) < int(fila) or int(self.columna_matriz1) < int(columna)):
                                    temp1 = " "
                                elif (int(fila) <= int(self.fila_matriz1) and int(columna) <= int(self.columna_matriz1)):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                    if (temp1 == "-"):
                                        temp1 = " "

                                if (int(columna_inicial) <= int(columna) <= int(cont_columna) and int(fila_inicial) <= int(fila) <= int(cont_fila)):
                                    print(f"{fila}{columna} ----------- {fila_inicial}<{fila}<{fila_final}")
                                    tabla += f"\t<td>*</td>\n"
                                    aux1 = "*"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                else:
                                    tabla += f"\t<td>{temp1}</td>\n"
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 

                                columna += 1

                            elif int(columna) == int(max_columna):
                                 
                                if (int(self.fila_matriz1) < int(fila) or int(self.columna_matriz1) < int(columna)):
                                    temp1 = " "
                                elif (int(fila) <= int(self.fila_matriz1) and int(columna) <= int(self.columna_matriz1)):
                                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador,fila,columna).get_dato()
                                    if (temp1 == "-"):
                                        temp1 = " "

                                if (int(columna_inicial) <= int(columna) <= int(cont_columna) and int(fila_inicial) <= int(fila) <= int(cont_fila)):
                                    print(f"{fila}{columna} ----------- {fila_inicial}<{fila}<{fila_final}")
                                    tabla += f"\t<td>*</td>\n"
                                    aux1 = "*"
                                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                else:
                                    tabla += f"\t<td>{temp1}</td>\n"
                                    if (temp1 == " "):
                                        aux1 = "-"
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                                    else:
                                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,temp1) 

                                tabla += "</tr>\n"
                                if int(fila) == int(max_fila):
                                    
                                    g = Digraph('g', format='png',filename='triangulo_rectangulo.gv',node_attr={'shape': 'plaintext'})
                                    g.node('node01', f'''<
                                    <table border="0" cellborder="1" cellspacing="0">
                                    {str(tabla)}
                                    </table>>''')
                                    g.view()

                                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('triangulo_rectangulo.gv.png'))
                                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                                    
                                    self.nombre_label = Label(text=f"Triangulo Rectangulo {fila_inicial},{columna_inicial};{fila_final}x{columna_final}")
                                    self.nombre_label.grid(row=6, column=3)
                                        
                                    self.nombre_matriz = f"{self.nombre_matriz} Triangulo Rectangulo {contador_datos_temp}"
                                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(max_fila),int(max_columna),str(self.nombre_matriz))
                                    temp = []
                                    i = 0
                                    temp.append(i)
                                    while i < contador_datos_temp:
                                        temp.append(i+1)
                                        i +=1
                                    combo["values"] = temp
                                    combo2["values"] = temp
                                    
                                    break
                                columna = 1
                                fila += 1
                                

                            x += 1
                    
                   
                aux2 = aux2.get_derecha()
                j += 1 

            aux = aux.get_siguiente()
            i += 1
    # ----------------------------------------------------- PARA DOS IMAGENES -----------------------------------------------------
    def union(self,contador1,contador2,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2,texto):
        
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos
        tabla = ""

        print(self.matriz_ortogonal_nombre.encontrar_contador(int(contador1)).__str__())
        print(self.matriz_ortogonal_nombre.encontrar_contador(int(contador2)).__str__())

        aux1 = self.matriz_ortogonal_nombre.encontrar_contador(int(contador1))
        aux2 = self.matriz_ortogonal_nombre.encontrar_contador(int(contador2))
        contador_uno = aux1.get_contador()
        contador_dos = aux2.get_contador()

        fila_uno = int(aux1.get_x())
        fila_dos = int(aux2.get_x())
        max_fila = 1
        columna_uno = int(aux1.get_y())
        columna_dos = int(aux2.get_y())
        max_columna = 1


        if (int(aux1.get_x()) > int(aux2.get_x())):
            print(f'ES MAYOR LA FILA DEL CONTADOR {aux1.get_contador()} {aux1.get_x()}>{aux2.get_x()} --- > {aux1.get_x()}')
            max_fila = int(aux1.get_x())
        else:
            print(f'ES MAYOR LA FILA DEL CONTADOR {aux2.get_contador()} {aux1.get_x()}<{aux2.get_x()} --- > {aux2.get_x()}')
            max_fila = int(aux2.get_x())
        
        if (int(aux1.get_y()) > int(aux2.get_y())):
            print(f'ES MAYOR LA COLUMNA DEL CONTADOR {aux1.get_contador()} {aux1.get_y()}>{aux2.get_y()}')
            max_columna = int(aux1.get_y())
        else:
            print(f'ES MAYOR LA COLUMNA DEL CONTADOR {aux2.get_contador()} {aux1.get_y()}<{aux2.get_y()}')
            max_columna = int(aux2.get_y())

        self.nombre_matriz = f"Union {contador1},{contador2}"

        tabla += f"<tr>\n\t<td>{self.nombre_matriz}</td>\n"
        x = 0 
        while x < max_columna:
            tabla += f"\t<td>{x+1}</td>\n"
            x += 1
        tabla += f"</tr>\n"
        longitud = int(max_fila)*int(max_columna)
        i = 0
        columna = 1
        fila = 1
        while i < longitud:

            if int(columna) < int(max_columna):

                if int(columna) == 1:
                    tabla += f"<tr>\n\t<td>{fila}</td>\n"

                if int(fila) <= int(fila_uno) and int(columna) <= int(columna_uno):
                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador_uno,fila,columna).get_dato()
                    if (temp1 == "-"):
                        temp1 = " "
                else:
                    temp1 = " "
                
                if int(fila) <= int(fila_dos) and int(columna) <= int(columna_dos):
                    temp2 = self.matriz_ortogonal.encontrar_posicion(contador_dos,fila,columna).get_dato()
                    if (temp2 == "-"):
                        temp2 = " "
                else:
                    temp2 = " "
                

                if temp1 == "*" or temp2 == "*":
                    tabla += f"\t<td>*</td>\n"
                    aux1 = "*"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                else:
                    tabla += f"\t<td> </td>\n"
                    aux1 = "-"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)


                columna += 1
            elif int(columna) == int(columna):
                
                if int(fila) <= int(fila_uno) and int(columna) <= int(columna_uno):
                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador_uno,fila,columna).get_dato()
                    if (temp1 == "-"):
                        temp1 = " "
                else:
                    temp1 = " "
                
                if int(fila) <= int(fila_dos) and int(columna) <= int(columna_dos):
                    temp2 = self.matriz_ortogonal.encontrar_posicion(contador_dos,fila,columna).get_dato()
                    if (temp2 == "-"):
                        temp2 = " "
                else:
                    temp2 = " "
                

                if temp1 == "*" or temp2 == "*":
                    tabla += f"\t<td>*</td>\n</tr>\n"
                    aux1 = "*"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                else:
                    tabla += f"\t<td> </td>\n</tr>"
                    aux1 = "-"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)

                if int(fila) == int(max_fila):
                    #print(tabla)
                    g = Digraph('g', format='png',filename='union.gv',node_attr={'shape': 'plaintext'})
                    g.node('node01', f'''<
                    <table border="0" cellborder="1" cellspacing="0">
                    {str(tabla)}
                    </table>>''')
                    g.view()

                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('union.gv.png'))
                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                    
                    self.nombre_label = Label(text=f"Union")
                    self.nombre_label.grid(row=6, column=3)
                                        
                    self.nombre_matriz = f"{self.nombre_matriz} - {contador_datos_temp}"
                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(max_fila),int(max_columna),str(self.nombre_matriz))
                    temp = []
                    i = 0
                    temp.append(i)
                    while i < contador_datos_temp:
                        temp.append(i+1)
                        i +=1
                    combo["values"] = temp
                    combo2["values"] = temp
                                    
                    break

                fila += 1
                columna = 1

            i += 1


    # ----------------------------------------------------- INTERSECCION PARA DOS IMAGENES -----------------------------------------------------

    def interseccion(self,contador1,contador2,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2,texto):
      
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos
        tabla = ""

        print(self.matriz_ortogonal_nombre.encontrar_contador(int(contador1)).__str__())
        print(self.matriz_ortogonal_nombre.encontrar_contador(int(contador2)).__str__())

        aux1 = self.matriz_ortogonal_nombre.encontrar_contador(int(contador1))
        aux2 = self.matriz_ortogonal_nombre.encontrar_contador(int(contador2))
        contador_uno = aux1.get_contador()
        contador_dos = aux2.get_contador()

        fila_uno = int(aux1.get_x())
        fila_dos = int(aux2.get_x())
        max_fila = 1
        columna_uno = int(aux1.get_y())
        columna_dos = int(aux2.get_y())
        max_columna = 1


        if (int(aux1.get_x()) > int(aux2.get_x())):
            print(f'ES MAYOR LA FILA DEL CONTADOR {aux1.get_contador()} {aux1.get_x()}>{aux2.get_x()} --- > {aux1.get_x()}')
            max_fila = int(aux1.get_x())
        else:
            print(f'ES MAYOR LA FILA DEL CONTADOR {aux2.get_contador()} {aux1.get_x()}<{aux2.get_x()} --- > {aux2.get_x()}')
            max_fila = int(aux2.get_x())
        
        if (int(aux1.get_y()) > int(aux2.get_y())):
            print(f'ES MAYOR LA COLUMNA DEL CONTADOR {aux1.get_contador()} {aux1.get_y()}>{aux2.get_y()}')
            max_columna = int(aux1.get_y())
        else:
            print(f'ES MAYOR LA COLUMNA DEL CONTADOR {aux2.get_contador()} {aux1.get_y()}<{aux2.get_y()}')
            max_columna = int(aux2.get_y())

        self.nombre_matriz = f"Intersección {contador1},{contador2}"

        tabla += f"<tr>\n\t<td>{self.nombre_matriz}</td>\n"
        x = 0 
        while x < max_columna:
            tabla += f"\t<td>{x+1}</td>\n"
            x += 1
        tabla += f"</tr>\n"
        longitud = int(max_fila)*int(max_columna)
        i = 0
        columna = 1
        fila = 1
        while i < longitud:

            if int(columna) < int(max_columna):

                if int(columna) == 1:
                    tabla += f"<tr>\n\t<td>{fila}</td>\n"

                if int(fila) <= int(fila_uno) and int(columna) <= int(columna_uno):
                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador_uno,fila,columna).get_dato()
                    if (temp1 == "-"):
                        temp1 = " "
                else:
                    temp1 = " "
                
                if int(fila) <= int(fila_dos) and int(columna) <= int(columna_dos):
                    temp2 = self.matriz_ortogonal.encontrar_posicion(contador_dos,fila,columna).get_dato()
                    if (temp2 == "-"):
                        temp2 = " "
                else:
                    temp2 = " "
                

                if temp1 == "*" and temp2 == "*":
                    tabla += f"\t<td>*</td>\n"
                    aux1 = "*"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                else:
                    tabla += f"\t<td> </td>\n"
                    aux1 = "-"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)


                columna += 1
            elif int(columna) == int(columna):
                
                if int(fila) <= int(fila_uno) and int(columna) <= int(columna_uno):
                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador_uno,fila,columna).get_dato()
                    if (temp1 == "-"):
                        temp1 = " "
                else:
                    temp1 = " "
                
                if int(fila) <= int(fila_dos) and int(columna) <= int(columna_dos):
                    temp2 = self.matriz_ortogonal.encontrar_posicion(contador_dos,fila,columna).get_dato()
                    if (temp2 == "-"):
                        temp2 = " "
                else:
                    temp2 = " "
                

                if temp1 == "*" and temp2 == "*":
                    tabla += f"\t<td>*</td>\n</tr>\n"
                    aux1 = "*"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                else:
                    tabla += f"\t<td> </td>\n</tr>"
                    aux1 = "-"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)

                if int(fila) == int(max_fila):
                    #print(tabla)
                    g = Digraph('g', format='png',filename='interseccion.gv',node_attr={'shape': 'plaintext'})
                    g.node('node01', f'''<
                    <table border="0" cellborder="1" cellspacing="0">
                    {str(tabla)}
                    </table>>''')
                    g.view()

                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('interseccion.gv.png'))
                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                    
                    self.nombre_label = Label(text=f"Interseccion")
                    self.nombre_label.grid(row=6, column=3)
                                        
                    self.nombre_matriz = f"{self.nombre_matriz} - {contador_datos_temp}"
                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(max_fila),int(max_columna),str(self.nombre_matriz))
                    temp = []
                    i = 0
                    temp.append(i)
                    while i < contador_datos_temp:
                        temp.append(i+1)
                        i +=1
                    combo["values"] = temp
                    combo2["values"] = temp
                                    
                    break

                fila += 1
                columna = 1

            i += 1



    # ----------------------------------------------------- DIFERENCIA PARA DOS IMAGENES -----------------------------------------------------
    
    def diferencia(self,contador1,contador2,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2,texto):
      
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos
        tabla = ""

        print(self.matriz_ortogonal_nombre.encontrar_contador(int(contador1)).__str__())
        print(self.matriz_ortogonal_nombre.encontrar_contador(int(contador2)).__str__())

        aux1 = self.matriz_ortogonal_nombre.encontrar_contador(int(contador1))
        aux2 = self.matriz_ortogonal_nombre.encontrar_contador(int(contador2))
        contador_uno = aux1.get_contador()
        contador_dos = aux2.get_contador()

        fila_uno = int(aux1.get_x())
        fila_dos = int(aux2.get_x())
        max_fila = 1
        columna_uno = int(aux1.get_y())
        columna_dos = int(aux2.get_y())
        max_columna = 1


        if (int(aux1.get_x()) > int(aux2.get_x())):
            print(f'ES MAYOR LA FILA DEL CONTADOR {aux1.get_contador()} {aux1.get_x()}>{aux2.get_x()} --- > {aux1.get_x()}')
            max_fila = int(aux1.get_x())
        else:
            print(f'ES MAYOR LA FILA DEL CONTADOR {aux2.get_contador()} {aux1.get_x()}<{aux2.get_x()} --- > {aux2.get_x()}')
            max_fila = int(aux2.get_x())
        
        if (int(aux1.get_y()) > int(aux2.get_y())):
            print(f'ES MAYOR LA COLUMNA DEL CONTADOR {aux1.get_contador()} {aux1.get_y()}>{aux2.get_y()}')
            max_columna = int(aux1.get_y())
        else:
            print(f'ES MAYOR LA COLUMNA DEL CONTADOR {aux2.get_contador()} {aux1.get_y()}<{aux2.get_y()}')
            max_columna = int(aux2.get_y())

        self.nombre_matriz = f"Intersección {contador1},{contador2}"

        tabla += f"<tr>\n\t<td>{self.nombre_matriz}</td>\n"
        x = 0 
        while x < max_columna:
            tabla += f"\t<td>{x+1}</td>\n"
            x += 1
        tabla += f"</tr>\n"
        longitud = int(max_fila)*int(max_columna)
        i = 0
        columna = 1
        fila = 1
        while i < longitud:

            if int(columna) < int(max_columna):

                if int(columna) == 1:
                    tabla += f"<tr>\n\t<td>{fila}</td>\n"

                if int(fila) <= int(fila_uno) and int(columna) <= int(columna_uno):
                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador_uno,fila,columna).get_dato()
                    if (temp1 == "-"):
                        temp1 = " "
                else:
                    temp1 = " "
                
                if int(fila) <= int(fila_dos) and int(columna) <= int(columna_dos):
                    temp2 = self.matriz_ortogonal.encontrar_posicion(contador_dos,fila,columna).get_dato()
                    if (temp2 == "-"):
                        temp2 = " "
                else:
                    temp2 = " "
                

                if temp1 == "*" and temp2 == "*":
                    tabla += f"\t<td> </td>\n"
                    aux1 = "-"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                else:
                    tabla += f"\t<td>{temp1}</td>\n"
                    if temp1 == " ":
                        aux1 = "-"
                    else:
                        aux1 = "*"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)


                columna += 1
            elif int(columna) == int(columna):
                
                if int(fila) <= int(fila_uno) and int(columna) <= int(columna_uno):
                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador_uno,fila,columna).get_dato()
                    if (temp1 == "-"):
                        temp1 = " "
                else:
                    temp1 = " "
                
                if int(fila) <= int(fila_dos) and int(columna) <= int(columna_dos):
                    temp2 = self.matriz_ortogonal.encontrar_posicion(contador_dos,fila,columna).get_dato()
                    if (temp2 == "-"):
                        temp2 = " "
                else:
                    temp2 = " "
                

                if temp1 == "*" and temp2 == "*":
                    tabla += f"\t<td> </td>\n</tr>\n"
                    aux1 = "-"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                else:
                    tabla += f"\t<td>{temp1}</td>\n</tr>\n"
                    if temp1 == " ":
                        aux1 = "-"
                    else:
                        aux1 = "*"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)


                if int(fila) == int(max_fila):
                    #print(tabla)
                    g = Digraph('g', format='png',filename='interseccion.gv',node_attr={'shape': 'plaintext'})
                    g.node('node01', f'''<
                    <table border="0" cellborder="1" cellspacing="0">
                    {str(tabla)}
                    </table>>''')
                    g.view()

                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('interseccion.gv.png'))
                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                    
                    self.nombre_label = Label(text=f"Interseccion")
                    self.nombre_label.grid(row=6, column=3)
                                        
                    self.nombre_matriz = f"{self.nombre_matriz} - {contador_datos_temp}"
                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(max_fila),int(max_columna),str(self.nombre_matriz))
                    temp = []
                    i = 0
                    temp.append(i)
                    while i < contador_datos_temp:
                        temp.append(i+1)
                        i +=1
                    combo["values"] = temp
                    combo2["values"] = temp
                                    
                    break

                fila += 1
                columna = 1

            i += 1


    # ----------------------------------------------------- DIFERENCIA SIMETRICA PARA DOS IMAGENES -----------------------------------------------------
    def diferencia_simetra(self,contador1,contador2,contador_datos_temp,matriz_ortogonal_temp,matriz_ortogonal_nombre_temp,combo,combo2,texto):
      
        self.nombre_matriz = ""
        if self.contador_datos == 0:
            self.contador_datos = contador_datos_temp
        else:
            self.contador_datos += 1
            contador_datos_temp = self.contador_datos
        tabla = ""

        print(self.matriz_ortogonal_nombre.encontrar_contador(int(contador1)).__str__())
        print(self.matriz_ortogonal_nombre.encontrar_contador(int(contador2)).__str__())

        aux1 = self.matriz_ortogonal_nombre.encontrar_contador(int(contador1))
        aux2 = self.matriz_ortogonal_nombre.encontrar_contador(int(contador2))
        contador_uno = aux1.get_contador()
        contador_dos = aux2.get_contador()

        fila_uno = int(aux1.get_x())
        fila_dos = int(aux2.get_x())
        max_fila = 1
        columna_uno = int(aux1.get_y())
        columna_dos = int(aux2.get_y())
        max_columna = 1


        if (int(aux1.get_x()) > int(aux2.get_x())):
            print(f'ES MAYOR LA FILA DEL CONTADOR {aux1.get_contador()} {aux1.get_x()}>{aux2.get_x()} --- > {aux1.get_x()}')
            max_fila = int(aux1.get_x())
        else:
            print(f'ES MAYOR LA FILA DEL CONTADOR {aux2.get_contador()} {aux1.get_x()}<{aux2.get_x()} --- > {aux2.get_x()}')
            max_fila = int(aux2.get_x())
        
        if (int(aux1.get_y()) > int(aux2.get_y())):
            print(f'ES MAYOR LA COLUMNA DEL CONTADOR {aux1.get_contador()} {aux1.get_y()}>{aux2.get_y()}')
            max_columna = int(aux1.get_y())
        else:
            print(f'ES MAYOR LA COLUMNA DEL CONTADOR {aux2.get_contador()} {aux1.get_y()}<{aux2.get_y()}')
            max_columna = int(aux2.get_y())

        self.nombre_matriz = f"Dif Simetrica {contador1},{contador2}"

        tabla += f"<tr>\n\t<td>{self.nombre_matriz}</td>\n"
        x = 0 
        while x < max_columna:
            tabla += f"\t<td>{x+1}</td>\n"
            x += 1
        tabla += f"</tr>\n"
        longitud = int(max_fila)*int(max_columna)
        i = 0
        columna = 1
        fila = 1
        while i < longitud:

            if int(columna) < int(max_columna):

                if int(columna) == 1:
                    tabla += f"<tr>\n\t<td>{fila}</td>\n"

                if int(fila) <= int(fila_uno) and int(columna) <= int(columna_uno):
                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador_uno,fila,columna).get_dato()
                    if (temp1 == "-"):
                        temp1 = " "
                else:
                    temp1 = " "
                
                if int(fila) <= int(fila_dos) and int(columna) <= int(columna_dos):
                    temp2 = self.matriz_ortogonal.encontrar_posicion(contador_dos,fila,columna).get_dato()
                    if (temp2 == "-"):
                        temp2 = " "
                else:
                    temp2 = " "
                

                if temp1 == "*" and temp2 == "*":
                    tabla += f"\t<td> </td>\n"
                    aux1 = "-"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                else:
                    if temp1 == "*" or temp2 == "*":
                        tabla += f"\t<td>*</td>\n"
                        aux1 = "*"
                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                    else:
                        tabla += f"\t<td> </td>\n"
                        aux1 = "-"
                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)


                columna += 1
            elif int(columna) == int(columna):
                
                if int(fila) <= int(fila_uno) and int(columna) <= int(columna_uno):
                    temp1 = self.matriz_ortogonal.encontrar_posicion(contador_uno,fila,columna).get_dato()
                    if (temp1 == "-"):
                        temp1 = " "
                else:
                    temp1 = " "
                
                if int(fila) <= int(fila_dos) and int(columna) <= int(columna_dos):
                    temp2 = self.matriz_ortogonal.encontrar_posicion(contador_dos,fila,columna).get_dato()
                    if (temp2 == "-"):
                        temp2 = " "
                else:
                    temp2 = " "
                

                if temp1 == "*" and temp2 == "*":
                    tabla += f"\t<td> </td>\n</tr>\n"
                    aux1 = "-"
                    matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                else:
                    if temp1 == "*" or temp2 == "*":
                        tabla += f"\t<td>*</td>\n</tr>\n"
                        aux1 = "*"
                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)
                    else:
                        tabla += f"\t<td> </td>\n</tr>\n"
                        aux1 = "-"
                        matriz_ortogonal_temp.agregar(contador_datos_temp,fila,columna,aux1)


                if int(fila) == int(max_fila):
                    #print(tabla)
                    g = Digraph('g', format='png',filename='interseccion.gv',node_attr={'shape': 'plaintext'})
                    g.node('node01', f'''<
                    <table border="0" cellborder="1" cellspacing="0">
                    {str(tabla)}
                    </table>>''')
                    g.view()

                    self.imagen_rotacion_horizontal = ImageTk.PhotoImage(Image.open('interseccion.gv.png'))
                    self.label_imagen_rotacion_horizontal = Label(image=self.imagen_rotacion_horizontal)
                    self.label_imagen_rotacion_horizontal.grid(row=5, column=3)
                    
                    self.nombre_label = Label(text=f"Interseccion")
                    self.nombre_label.grid(row=6, column=3)
                                        
                    self.nombre_matriz = f"{self.nombre_matriz} - {contador_datos_temp}"
                    matriz_ortogonal_nombre_temp.agregar(int(contador_datos_temp),int(max_fila),int(max_columna),str(self.nombre_matriz))
                    temp = []
                    i = 0
                    temp.append(i)
                    while i < contador_datos_temp:
                        temp.append(i+1)
                        i +=1
                    combo["values"] = temp
                    combo2["values"] = temp
                                    
                    break

                fila += 1
                columna = 1

            i += 1

  