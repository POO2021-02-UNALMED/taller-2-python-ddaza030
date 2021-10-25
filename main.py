
class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        if(color in ["rojo","verde","amarillo","negro","blanco"]):
            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        i=0
        for asiento in self.asientos:
            if asiento != None:
                i+=1
        return i

    def verificarIntegridad(self):
        asientosval = []
        a = True
        for asiento in self.asientos:
            if asiento != None:
                asientosval.append(asiento.registro)
        for i in range(len(asientosval)-1):
            if asientosval[i] != asientosval[i+1]:
                a = False
                break
        
        if(self.registro== self.motor.registro and a == True):
            return("Auto original")
        else:
            return("Las piezas no son originales")
            


        
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nregistro):
        self.registro = nregistro
    
    def asignarTipo(self, tipo):
        
        if (tipo in ["electrico","gasolina"]):
            self.tipo = tipo


