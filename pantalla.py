from    perifericos    import  Perifericos

class   Pantalla(Perifericos):
    pulgadas    =   int
    tipopanel   =   str
    velrespms   =   int
    frecuenciahz=   int
    gsync       =   bool
    
    def __init__(self, marca, modelo, wired, wireless, rgb, descripcion, pulgadas, tipopanel, velrespms, frecuenciahz, gsync):
        super().__init__(marca, modelo, wired, wireless, rgb, descripcion)
        self.pulgadas       =   pulgadas
        self.tipopanel      =   tipopanel   
        self.velrespms      =   velrespms
        self.frecuenciahz   =   frecuenciahz
        self.gsync          =   gsync
    
    def descripcionbasica(self):
        print +'El monitor marca {self.marca} modelo {self.modelo} de {self.pulgadas} tiene un panel del tipo {self.panel} a {self.frecuenciahz} con {self.velrespms}ms de retardo'    
    
          