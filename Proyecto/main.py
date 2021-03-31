from Vista.Menu import Menu
from Vista.Pantalla import Pantalla



from Modelo.Lista_Vertical import Lista_Vertical
from Modelo.Lista_Horizontal import Lista_Horizontal
from Modelo.Lista_Cabecera_Columna import Lista_Cabecera_Columna
from Modelo.Lista_Cabecera_Fila import Lista_Cabecera_Fila
from Modelo.Matriz_Ortogonal import Matriz_Ortogonal
from Modelo.Nodo import Nodo



class main():


    def __init__(self):
        
        #self.llamar = Menu()
        #entero = IntVar()  # Declara variable de tipo entera
        #flotante = DoubleVar()  # Declara variable de tipo flotante
        #cadena = StringVar()  # Declara variable de tipo cadena
        #booleano = BooleanVar()  # Declara variable de tipo booleana
        self.vista = Pantalla()
        

if __name__ == "__main__":
    '''
    matriz = Matriz_Ortogonal()

    matriz.agregar(1,1,1,11)
    matriz.agregar(1,1,2,12)
    matriz.agregar(1,1,3,13)

    matriz.agregar(1,2,1,14)
    matriz.agregar(1,2,2,15)
    matriz.agregar(1,2,3,16)

    matriz.agregar(1,3,1,17)
    matriz.agregar(1,3,2,18)
    matriz.agregar(1,3,3,19)
    
    matriz.agregar(2,1,1,20)
    matriz.agregar(2,1,2,21)
    matriz.agregar(2,2,1,22)
    matriz.agregar(2,2,2,23)

    print('Buscar por Fila: ->')
    print(matriz.get_fila().get_primero().get_fila().get_primero())
    print('Buscar por Columna: v')
    print(matriz.get_columna().get_primero().get_siguiente().get_siguiente().get_columna().get_primero().get_abajo().get_abajo())

    print('BUSCANDO DATOS')
    print(matriz.encontrar_posicion(2,2,2))

    '''
    instance = main()
    instance.vista