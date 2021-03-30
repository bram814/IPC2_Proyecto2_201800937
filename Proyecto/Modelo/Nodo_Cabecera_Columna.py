from Modelo.Lista_Vertical import Lista_Vertical

class Nodo_Cabecera_Columna():

    def __init__(self,x,siguiente=None,anterior=None):
        self.x = x
        self.siguiente = siguiente
        self.anterior = anterior
        self.columna = Lista_Vertical()
    
    def get_x(self):
        return self.x
    def set_x(self,x):
        self.x = x
    
    def get_columna(self):
        return self.columna
    def set_columna(self,columna):
        self.columna = columna

    def get_siguiente(self):
        return self.siguiente
    def set_siguiente(self,siguiente):
        self.siguiente = siguiente
    
    def get_anterior(self):
        return self.anterior
    def set_anterior(self,anterior):
        self.anterior = anterior

    def __str__(self):
        return f"{self.x} - {self.columna}" 