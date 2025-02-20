class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente
            
class Mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo

    def __str__(self):
        return f"Fecha: {self.fecha}, Descripción: {self.descripcion}, Costo: ${self.costo}"

class Vehiculo:
    def __init__(self, placa, marca, modelo, año, kilometraje):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.historial_mantenimientos = ListaEnlazadaSimple()

    def agregar_mantenimiento(self, fecha, descripcion, costo):
        mantenimiento = Mantenimiento(fecha, descripcion, costo)
        self.historial_mantenimientos.agregar(mantenimiento)

    def consultar_historial(self):
        print(f"Historial de mantenimientos para el vehículo {self.placa}:")
        self.historial_mantenimientos.recorrer()

    def calcular_costo_total(self):
        total = 0
        actual = self.historial_mantenimientos.cabeza
        while actual:
            total += actual.dato.costo
            actual = actual.siguiente
        return total

    def __str__(self):
        return f"Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje}"
            