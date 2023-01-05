from    perifericos import  Mouse
from    perifericos import  Teclado 
from    perifericos import  Audifonos

class   Combo:
    costo   =   int
    mouse       =   Mouse("", "", "", "", "", "", "", "", "")
    teclado     =   Teclado("", "", "", "", "", "", "", "")
    audifonos   =   Audifonos("", "", "", "", "", "", "", "", "")
    
    def __init__(self, costo, mouse, teclado, audifonos):
        self.costo      =   costo
        self.mouse      =   mouse
        self.teclado    =   teclado
        self.audifonos  =   audifonos