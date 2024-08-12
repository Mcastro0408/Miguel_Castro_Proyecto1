class Personajes:
    def __init__(self, nombre, planeta_origen, titulos, genero, especie, nave, vehiculos):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
        self.titulos = titulos
        self.genero = genero
        self.especie = especie
        self.nave = nave
        self.vehiculos = vehiculos
    def show_attr(self):
        print(f'nombre: {self.nombre}')
        print(f'planeta de origen: {self.planeta_origen}')
        print(f'titulos: {self.titulos}')
        print(f'genero: {self.genero}')
        print(f'especie: {self.especie}')
        print(f'nave: {self.nave}')
        print(f'vehiculos de usados: {self.vehiculos}')