from Modelo.Nodo import Nodo

class Lista_Horizontal():


    def __init__(self,primero=None,ultimo=None):
        self.primero = primero
        self.ultimo = ultimo
        self.size_LH = 0


    def __vacia__(self):
        if (self.get_primero() == None):
            return True
        return False


    def agregar(self,contador,x,y,dato):
        nodo_nuevo = Nodo(contador,x,y,dato)
        if (self.__vacia__()==True):
            self.set_primero(nodo_nuevo)
            self.set_ultimo(nodo_nuevo)
        else:

            if int(nodo_nuevo.get_x()) < int(self.get_primero().get_x()):
                # al inicio
                self.get_primero().set_izquierda(nodo_nuevo)
                nodo_nuevo.set_derecha(self.get_primero())
                self.set_primero(nodo_nuevo)

            elif int(nodo_nuevo.get_x()) > int(self.get_ultimo().get_x()):
                # al fin
                self.get_ultimo().set_derecha(nodo_nuevo)
                nodo_nuevo.set_izquierda(self.get_ultimo())
                self.set_ultimo(nodo_nuevo)

            else:
                # en medio
                aux1 = None
                aux2 = None
                aux1 = self.get_primero()
            
                while int(aux1.get_x()) <= int(nodo_nuevo.get_x()):
                    aux1 = aux1.get_derecha()

                aux2 = aux1.get_izquierda()

                aux2.set_derecha(nodo_nuevo)
                nodo_nuevo.set_derecha(aux1)
                aux1.set_izquierda(nodo_nuevo)
                nodo_nuevo.set_izquierda(aux2)
        self.size_LH += 1




    def mostar(self):

        aux = self.get_primero()

        while aux is not None:
            print(aux)
            aux = aux.get_derecha()
        
    def get_primero(self):
        return self.primero
    def set_primero(self,primero):
        self.primero = primero
    def get_ultimo(self):
        return self.ultimo
    def set_ultimo(self,ultimo):
        self.ultimo = ultimo


