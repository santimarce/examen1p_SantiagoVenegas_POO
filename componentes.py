from ordenador import Ordenador

class Componentes(Ordenador):
    tipo        =   str
    marca       =   str
    modelo      =   str
    generación  =   int
    
    def __init__(self, socket, fecha, tipo, marca, modelo, generacion):
        super().__init__(socket, fecha)
        self.tipo       =   tipo
        self.marca      =   marca
        self.modelo     =   modelo
        self.generación =   generacion
    
    def __str__(self):
        print("El componente {self.tipo} del modelo {self.modelo} marca {self.marca} pertenece a la {self.generacion} generacion de dispositivos en su clase")

class Grafica(Componentes):
    tamanomemGB     =   str
    gsync           =   bool
    fsync           =   bool
    
    def __init__(self, tipo, marca, modelo, generacion, tamanomemGB, gsync, fsync):
        super().__init__(socket, fecha, tipo, marca, modelo, generacion)
        self.tamanomemGB    =   tamanomemGB
        self.gsync          =   gsync
        self.fsync          =   fsync

    def compatibilidadGSYNC(self, tarjetamem):
        if self.gsync == tarjetamem.gsync:
            print("Existe compatibilidad de la tecnología NVIDIA G-SYNC en su setup")
        else:
            print("Escoja un panel compatible con G-SYNC o una tarjeta envidia para aumentar su performance")

class   Memoria(Componentes):
    tamanomemGB     =   int
    tipoddr            =   int
    
    def __init__(self, tipo, marca, modelo, generacion, tamanomemGB, tipoddr):
        super().__init__(tipo, marca, modelo, generacion)
        self.tamanomemGB    =   tamanomemGB
        self.tipoddr        =   tipoddr

class   Procesador(Componentes):
    nucleos     =   int
    
    def __init__(self, tipo, marca, modelo, generacion, nucleos):
        super().__init__(socket, fecha, tipo, marca, modelo, generacion)
        self.nucleos    =   nucleos   

class   Mainboard(Componentes):
    tamano      =   str
    
    def __init__(self, tipo, marca, modelo, generacion, tamano):
        super().__init__(tipo, marca, modelo, generacion)
        self.tamano =   tamano

class   Almacenamiento(Componentes):
    tamanoGB    =   int
    tipofnc     =   str
    
    def __init__(self, tipo, marca, modelo, generacion, tamanoGB, tipofnc):
        self.tamanoGB   =   tamanoGB
        self.tipofnc    =   tipofnc

    