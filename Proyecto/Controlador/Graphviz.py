from graphviz import Digraph, nohtml
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
        self.matriz_ortogonal_nombre.mostrar_matriz()
        #self.matriz_ortogonal.mostrar_matriz()

        print(f'\n SELECCIONA LA MATRIZ 1 -> {cont_matriz_uno} = SELECCIONA LA MATRIZ 2 -> {cont_matriz_dos}')

        
        if (0 < int(cont_matriz_uno)):
            
            if (int(cont_matriz_dos) == 0):
                self.una_imagen(cont_matriz_uno)
            elif (0< int(cont_matriz_dos)):
                self.dos_imagenes(cont_matriz_uno,cont_matriz_dos)
            

       
    def una_imagen(self,contador):
        g = Digraph('g', format='svg',filename='imagen.gv',node_attr={'shape': 'plaintext'})
        
        #<td PORT="f1> port -> SIRVE PARA APUNTAR 
    
        g.node('node01', f'''<
        <table border="0" cellborder="1" cellspacing="0">
        {str(self.generar_tabla_nombre(contador))}
        {str(self.generar_tabla_datos(contador,self.fila_matriz1,self.columna_matriz1))}
        </table>>''')
         
        #g.edges([('node01:f1', 'node02:f0'), ('node03:f2', 'node04:f3')]) # esta condicion crea los punteros
        g.view()

    def dos_imagenes(self,contador,contador2):
        g = Digraph('g', format='svg',filename='imagen.gv',node_attr={'shape': 'plaintext'})
        
    
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
        print('ENTRO1')
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
        print('entro 2')
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


    def generar_tabla_nombre2(self,contador):
        print('ENTRO1')
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

    def generar_tabla_datos2(self,contador,fila,columna):
        print('entro 2')
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

