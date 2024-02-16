import random


# Definición de la clase base para las células del sistema inmunológico
class Celula:
    def __init__(self, id):
        self.id = id

    def interactuar(self, otra):
        pass


# Subclase para representar los antígenos
class Antigeno(Celula):
    def __init__(self, id):
        super().__init__(id)
        self.tasa_mutacion = 0.1  # Tasa de mutación del antígeno

    # Método para simular la mutación del antígeno
    def mutar(self):
        if random.random() < self.tasa_mutacion:
            self.id += "_mutado"

    # Método para la interacción entre células
    def interactuar(self, otra):
        # Si la otra célula es un anticuerpo, el antígeno es reconocido
        if isinstance(otra, Anticuerpo):
            print(f"{self.id} es reconocido por {otra.id}.")
            return True
        return False


# Subclase para representar los anticuerpos
class Anticuerpo(Celula):
    def __init__(self, id):
        super().__init__(id)
        self.memoria_reconocimiento = set()  # Memoria de reconocimiento de antígenos

    # Método para la interacción entre células
    def interactuar(self, otra):
        # Si la otra célula es un antígeno, se agrega a la memoria de reconocimiento
        if isinstance(otra, Antigeno):
            self.memoria_reconocimiento.add(otra.id)
            print(f"{self.id} reconoce {otra.id}.")
            return True
        return False


# Subclase para representar las células T
class CelulaT(Celula):
    def interactuar(self, otra):
        # Si la otra célula es un antígeno, la célula T se activa y lo mata
        if isinstance(otra, Antigeno):
            print(f"{self.id} se activa y mata a {otra.id}.")
            return True
        return False


# Subclase para representar las células B
class CelulaB(Celula):
    def interactuar(self, otra):
        # Si la otra célula es un antígeno, la célula B se activa y produce anticuerpos contra él
        if isinstance(otra, Antigeno):
            print(f"{self.id} se activa y produce anticuerpos contra {otra.id}.")
            return True
        return False


# Clase que representa el sistema inmunológico
class SistemaInmunologico:
    def __init__(self):
        self.celulas = []  # Lista para almacenar las células del sistema

    # Método para agregar células al sistema
    def agregar_celula(self, celula):
        self.celulas.append(celula)

    # Método para simular interacciones entre células
    def interactuar_celulas(self):
        for i in range(len(self.celulas)):
            for j in range(i + 1, len(self.celulas)):
                celula1 = self.celulas[i]
                celula2 = self.celulas[j]
                # Verifica la interacción entre cada par de células
                if celula1.interactuar(celula2):
                    print(f"Interacción: {celula1.id} <-> {celula2.id}")


# Crear el sistema inmunológico
sistema_inmunologico = SistemaInmunologico()
# Agregar anticuerpos al sistema
for i in range(5):
    sistema_inmunologico.agregar_celula(Anticuerpo(id=f"Anticuerpo_{i + 1}"))
# Agregar antígenos al sistema
for i in range(3):
    sistema_inmunologico.agregar_celula(Antigeno(id=f"Antígeno_{i + 1}"))

# Simular interacciones entre células
print("Interacciones:")
sistema_inmunologico.interactuar_celulas()

