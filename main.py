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
from    setup       import  Setup


#Empieza la ejecucion
if __name__=="__main__":

#Inicializacion de objetos

    mouse1      = Mouse("Logitech", "G-305", False, True, True, "Mouse de alta presicion", False, 10000, 30000000)
    teclado1    =   Teclado("Logitech", "T-087", True, True, True, "Buen Teclado", "Mecanico", "Blue")   
    audifonos1  =   Audifonos("Logitech", "G-708", True, True, True, "Buen Audifomno", "", "", 10)
    pantalla1   =   Pantalla("LG", "24fas", True, False, False, "BuenMontor", 24, "IPS", 1, 300, True)
    ordenador1  =   Ordenador("AM4", 20221212)
    procesador1 =   Procesador("AM4", 20221212,"Procesador", "AMD", "R7 7700X", 5, 8)
    grafica1    =   Grafica("TarjetaGrafica", "NVIDIA", "RTX 4080", 4, 16, True, False)
    mainboard1  =   Mainboard("Mainboard", "ASUS", "B650m", 5, ATX)
    memoria1    =   Memoria("MemoriaRAM", "Kingston", "Renegade X", 8, 16, 5)
    almacenamiento1 =   Almacenamiento("Almacenamient", "WD", "Black", 10, 1000, "NVMe 2.0")
    componente1 =   Componentes("Fuente", "Corsair", "AX 750", 9)
# Objetos con objetos dentro 
    combo1      =   Combo(160, mouse1, teclado1, audifonos1)
    combo2      =   Combo(250, mouse1, teclado1, audifonos1)
# Objetos con objetos dentro de objetos
    setup1      =   Setup("Grande", ordenador1, combo1, pantalla1, procesador1, grafica1, mainboard1, memoria1, almacenamiento1)
    setup2      =   Setup("Peque", ordenador1, combo1, pantalla1, procesador1, grafica1, mainboard1, memoria1, almacenamiento1)

#Metodo STR en clase 
    componente1.__str__()

#Metodo de clase en otro archivo con el objeto 
    pantalla1.descripcionbasica()
    
#MEtodo clase hija dentro del mismo archivo
    audifonos1.aclararpot()

# Método 

    
    
    