from    ordenador   import  Ordenador
from    perifericos import  Perifericos
from    perifericos import  Mouse
from    perifericos import  Teclado
from    perifericos import  Audifonos
from    pantalla    import  Pantalla
from    componentes import  Componentes
from    componentes import  Procesador
from    componentes import  Grafica
from    componentes import  Mainboard
from    componentes import  Memoria
from    componentes import  Almacenamiento
from    combo       import  Combo

class   Setup:
    tamanio     =   str
    ordenador   =   Ordenador("", "")
    combo       =   Combo("", "", "", "")
    pantalla    =   Pantalla("", "", "", "", "", "", "", "", "", "", "")
    procesador  =   Procesador("", "", "", "", "", "", "")
    grafica     =   Grafica("", "", "", "", "", "", "")
    mb          =   Mainboard("", "", "", "", "")
    mem         =   Memoria("", "", "", "", "", "")
    almac       =   Almacenamiento("", "", "", "", "", "")
    
    def __init__(self, tamanio, ordenador, combo, pantalla, procesador, grafica, mb, mem, almac):
        self.tamanio        =   tamanio
        self.ordenador      =   ordenador
        self.pantalla       =   pantalla
        self.procesador     =   procesador
        self.grafica        =   grafica
        self.mb             =   mb
        self.mem            =   mem
        self.almac          =   almac
    
