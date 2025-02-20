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

class FlotaVehiculos:
    def __init__(self):
        self.vehiculos = ListaEnlazadaSimple()

    def registrar_vehiculo(self, placa, marca, modelo, año, kilometraje):
        vehiculo = Vehiculo(placa, marca, modelo, año, kilometraje)
        self.vehiculos.agregar(vehiculo)
        print(f"Vehículo con placa {placa} registrado exitosamente.")

    def buscar_vehiculo(self, placa):
        actual = self.vehiculos.cabeza
        while actual:
            if actual.dato.placa == placa:
                return actual.dato
            actual = actual.siguiente
        return None

    def listar_vehiculos(self):
        print("Lista de vehículos registrados:")
        self.vehiculos.recorrer()
               
def mostrar_menu():
    print("\n--- Menú de Gestión de Flota de Vehículos ---")
    print("1. Registrar un nuevo vehículo")
    print("2. Agregar mantenimiento a un vehículo")
    print("3. Consultar historial de mantenimientos de un vehículo")
    print("4. Calcular costo total de mantenimientos de un vehículo")
    print("5. Listar todos los vehículos")
    print("6. Salir")                    