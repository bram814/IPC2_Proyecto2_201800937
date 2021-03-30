from Modelo.Lista_Cabecera_Columna import Lista_Cabecera_Columna
from Modelo.Lista_Cabecera_Fila import Lista_Cabecera_Fila
from Modelo.Nodo import Nodo

class Matriz_Ortogonal():


    def __init__(self):
        self.fila = Lista_Cabecera_Fila()
        self.columna = Lista_Cabecera_Columna()
        self.size_ortogonal = 0


    def agregar(self,contador,x,y,dato):

        if (self.get_columna().buscar(x) == None):
            self.get_columna().agregar(x)
            print(f"{x} - {dato}")
        
        if (self.get_fila().buscar(y) == None):
            self.get_fila().agregar(y)
            print(f"{y} - {dato}")

        aux_columna = None
        aux_fila = None

        #aux_columna = self.get_columna().buscar(x)
        #aux_fila = self.get_fila().buscar(y)
        self.get_columna().buscar(x).get_columna().agregar(contador,x,y,dato)
        self.get_fila().buscar(y).get_fila().agregar(contador,x,y,dato)
        #aux_columna.get_columna().agregar(contador,x,y,dato)
        #aux_fila.get_fila().agregar(contador,x,y,dato)
        print(f"Inserto dato: {dato}, pos ({x},{y})")
        self.size_ortogonal += 1


    def encontrar_posicion(self,contador,x,y):
        aux = self.get_fila().get_primero()
        longitud_fila = self.get_fila().size_LCF
        i = 0

        while i < longitud_fila:
            
            j = 0
            longitud_lista = aux.get_fila().size_LH
            aux2 = aux.get_fila().get_primero()
            while j < longitud_lista:
                if (int(aux2.get_contador()) == int(contador) and int(aux2.get_x()) == int(x) and int(aux2.get_y()) == int(y)):
                    return aux2
                aux2 = aux2.get_derecha()
                j += 1 

            aux = aux.get_siguiente()
            i += 1


        

    def get_fila(self):
        return self.fila
    def set_fila(self,fila):
        self.fila = fila
    
    def get_columna(self):
        return self.columna
    def set_columna(self,columna):
        self.columna = columna

    