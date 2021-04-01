from Modelo.Nodo import Nodo

class Lista_Vertical():


    def __init__(self,primero=None,ultimo=None):
        self.primero = primero
        self.ultimo = ultimo
        self.size_LV = 0


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

            if int(nodo_nuevo.get_y()) < int(self.get_primero().get_y()):
               
                self.get_primero().set_arriba(nodo_nuevo)
                nodo_nuevo.set_abajo(self.get_primero())
                self.set_primero(nodo_nuevo)

            elif int(nodo_nuevo.get_y()) > int(self.get_ultimo().get_y()):
                
                self.get_ultimo().set_abajo(nodo_nuevo)
                nodo_nuevo.set_arriba(self.get_ultimo())
                self.set_ultimo(nodo_nuevo)
                
            else:
                aux1 = None
                aux2 = None
                aux1 = self.get_primero()
            
                while int(aux1.get_y()) <= int(nodo_nuevo.get_y()):
                    if  int(aux1.get_y()) == self.get_ultimo().get_y():
                        print("ojito")
                        break
                    aux1 = aux1.get_abajo()

                if  int(aux1.get_y()) == self.get_ultimo().get_y():
                    self.get_ultimo().set_abajo(nodo_nuevo)
                    nodo_nuevo.set_arriba(self.get_ultimo())
                    self.set_ultimo(nodo_nuevo)
                
                else:
                    aux2 = aux1.get_arriba()

                    aux2.set_abajo(nodo_nuevo)
                    nodo_nuevo.set_abajo(aux1)
                    aux1.set_arriba(nodo_nuevo)
                    nodo_nuevo.set_arriba(aux2)

        self.size_LV += 1



    def mostar(self):

        aux = self.get_primero()

        while aux is not None:
            print(aux)
            aux = aux.get_abajo()
        
    def get_primero(self):
        return self.primero
    def set_primero(self,primero):
        self.primero = primero
    def get_ultimo(self):
        return self.ultimo
    def set_ultimo(self,ultimo):
        self.ultimo = ultimo


