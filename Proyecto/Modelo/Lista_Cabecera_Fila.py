from Modelo.Nodo_Cabecera_Fila import Nodo_Cabecera_Fila
class Lista_Cabecera_Fila():

    def __init__(self,primero=None,ultimo=None):
        self.primero = primero
        self.ultimo = ultimo
        self.size_LCF = 0


    def __vacia__(self):
        if (self.get_primero() == None):
            return True
        return False



    def agregar(self,y):
        nodo_nuevo = Nodo_Cabecera_Fila(y)
        if (self.__vacia__()==True):
            self.set_primero(nodo_nuevo)
            self.set_ultimo(nodo_nuevo)
        else:

            if int(nodo_nuevo.get_y()) < int(self.get_primero().get_y()):
               
                self.get_primero().set_anterior(nodo_nuevo)
                nodo_nuevo.set_siguiente(self.get_primero())
                self.set_primero(nodo_nuevo)

            elif int(nodo_nuevo.get_y()) > int(self.get_ultimo().get_y()):
                
                self.get_ultimo().set_siguiente(nodo_nuevo)
                nodo_nuevo.set_anterior(self.get_ultimo())
                self.set_ultimo(nodo_nuevo)
                
            else:
                aux1 = None
                aux2 = None
                aux1 = self.get_primero()
            
                while int(aux1.get_y()) <= int(nodo_nuevo.get_y()):
                    aux1 = aux1.get_siguiente()

                aux2 = aux1.get_anterior()

                aux2.set_siguiente(nodo_nuevo)
                nodo_nuevo.set_siguiente(aux1)
                aux1.set_anterior(nodo_nuevo)
                nodo_nuevo.set_anterior(aux2)
        self.size_LCF += 1


    def mostrar(self):
        if (self.__vacia__() != True):
            aux = self.get_primero()

            while aux is not None:
                print(f'Cabecera y: {aux}')
                aux = aux.get_siguiente()
    
    def buscar(self,y):
        if (self.__vacia__() != True):
            aux = self.get_primero()
            while aux is not None:
                if (int(aux.get_y()) == int(y)):
                    return aux
                aux = aux.get_siguiente()

        return None


    
    def get_primero(self):
        return self.primero
    def set_primero(self,primero):
        self.primero = primero
    def get_ultimo(self):
        return self.ultimo
    def set_ultimo(self,ultimo):
        self.ultimo = ultimo

