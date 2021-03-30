from Modelo.Lista_Horizontal import Lista_Horizontal
class Nodo_Cabecera_Fila():

    def __init__(self,y,siguiente=None,anterior=None):
        self.y = y
        self.siguiente = siguiente
        self.anterior = anterior
        self.fila = Lista_Horizontal()

    
    def get_y(self):
        return self.y
    def set_y(self,y):
        self.y = y

    def get_fila(self):
        return self.fila
    def set_fila(self,fila):
        self.fila = fila

    def get_siguiente(self):
        return self.siguiente
    def set_siguiente(self,siguiente):
        self.siguiente = siguiente
    
    def get_anterior(self):
        return self.anterior
    def set_anterior(self,anterior):
        self.anterior = anterior
    
    def __str__(self):
        return f"{self.y} - {self.fila}" 