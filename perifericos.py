class Perifericos:
    marca       =   str
    modelo      =   str
    wired       =   bool
    wireless    =   bool
    rgb         =   bool
    descripcion =   str
    
    def __init__(self, marca, modelo, wired, wireless, rgb, descripcion):
        self.marca      =   marca
        self.modelo     =   modelo
        self.wired      =   wired
        self.wireless   =   wireless
        self.rgb        =   rgb
        self.descripcion=   descripcion
    
class   Mouse(Perifericos):
    ambidiestro =   bool
    dpimax      =   int
    vidateclas  =   int
    
    def __init__(self, marca, modelo, wired, wireless, rgb, descripcion, ambidiestro, dpimax, vidateclas):
        super().__init__(marca, modelo, wired, wireless, rgb, descripcion)
        self.ambidiestro    =   ambidiestro
        self.dpimax         =   dpimax
        self.vidateclas     =   vidateclas

class   Teclado(Perifericos):
    tipopulsa   =   str
    tiposwitch  =   str
    
    def __init__(self, marca, modelo, wired, wireless, rgb, descripcion, tipopulsa, tiposwitch):
        super().__init__(marca, modelo, wired, wireless, rgb, descripcion)
        self.tipopulsa  =   tipopulsa
        self.tiposwitch =   tiposwitch

class   Audifonos(Perifericos):
    potenciaw   =   int
    
    def __init__(self, marca, modelo, wired, wireless, rgb, descripcion, tipopulsa, tiposwitch, potenciaw):
        super().__init__(marca, modelo, wired, wireless, rgb, descripcion)
        self.potenciaw  =   potenciaw
    def aclararpot(self):
        
        print+'La potencia de estos audifonos no es rms'
