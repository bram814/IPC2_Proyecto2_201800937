class Nodo():

    def __init__(self,contador,x,y,dato,derecha=None,izquierda=None,abajo=None,arriba=None):
        self.contador = contador
        self.x = x
        self.y = y
        self.dato = dato # 0 -> - | 1 -> *
        self.derecha = derecha
        self.izquierda = izquierda
        self.abajo = abajo
        self.arriba = arriba

    def get_contador(self):
        return self.contador
    def set_contador(self,contador):
        self.contador = contador

    def get_x(self):
        return self.x
    def set_x(self,x):
        self.x = x
    
    def get_y(self):
        return self.y
    def set_y(self,y):
        self.y = y

    def get_dato(self):
        return self.dato    
    def set_dato(self,dato):
        self.dato = dato

    def get_derecha(self):
        return self.derecha
    def set_derecha(self,derecha):
        self.derecha = derecha
    
    def get_izquierda(self):
        return self.izquierda
    def set_izquierda(self,izquierda):
        self.izquierda = izquierda

    def get_arriba(self):
        return self.arriba
    def set_arriba(self,arriba):
        self.arriba = arriba
    
    def get_abajo(self):
        return self.abajo
    def set_abajo(self,abajo):
        self.abajo = abajo
    '''
    def __str__(self):
        if self.dato == 1:
            return f"{self.contador}.- ({self.x},{self.y}) Dato: *"
        elif self.dato == 0:
            return f"{self.contador}.- ({self.x},{self.y}) Dato: -"
    '''
    def __str__(self):
        return f"{self.contador}.- ({self.x},{self.y}) Dato: {self.dato}"