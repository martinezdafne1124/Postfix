class PilaHanoi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def insertar(self, disco):
        # Validar regla de Hanoi: no poner un disco más grande sobre uno más pequeño
        if self.elementos and self.elementos[-1] < disco:
            raise ValueError(f"Movimiento ilegal: No se puede poner el disco {disco} sobre {self.elementos[-1]}")
        self.elementos.append(disco)

    def eliminar(self):
        if not self.elementos:
            raise IndexError(f"La torre {self.nombre} está vacía.")
        return self.elementos.pop()

    def __str__(self):
        return f"Torre {self.nombre}: {self.elementos}"

def hanoi_con_pilas(n_discos, origen, destino, auxiliar):
    # Función auxiliar recursiva que utiliza los métodos de la Pila
    def mover_discos(n, tor_origen, tor_destino, tor_aux):
        if n == 1:
            disco = tor_origen.eliminar()
            tor_destino.insertar(disco)
            print(f"Mover disco {disco} de {tor_origen.nombre} ➔ {tor_destino.nombre}")
            print(f"   [{tor_origen}], [{tor_aux}], [{tor_destino}]")
            return
        
        mover_discos(n - 1, tor_origen, tor_aux, tor_destino)
        
        disco = tor_origen.eliminar()
        tor_destino.insertar(disco)
        print(f"Mover disco {disco} de {tor_origen.nombre} ➔ {tor_destino.nombre}")
        print(f"   [{tor_origen}], [{tor_aux}], [{tor_destino}]")
        
        mover_discos(n - 1, tor_aux, tor_destino, tor_origen)

    # Inicializar las torres
    torre_A = PilaHanoi("A (Origen)")
    torre_B = PilaHanoi("B (Auxiliar)")
    torre_C = PilaHanoi("C (Destino)")

    # Colocar los discos en la torre de origen (el disco más grande abajo, el 1 más arriba)
    for disco in range(n_discos, 0, -1):
        torre_A.insertar(disco)

    print(f"Estado inicial:")
    print(f"   [{torre_A}], [{torre_B}], [{torre_C}]\n")
    print("--- Comienzan los movimientos ---")
    
    mover_discos(n_discos, torre_A, torre_C, torre_B)
    
    print("\n--- ¡Juego completado con éxito! ---")
    print(f"Estado final:")
    print(f"   [{torre_A}], [{torre_B}], [{torre_C}]")

# --- Ejemplo de uso con 3 discos ---
if __name__ == "__main__":
    hanoi_con_pilas(n_discos=3, origen="A", destino="C", auxiliar="B")