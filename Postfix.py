class PilaEvaluador:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def insertar(self, item):
        self.elementos.append(item)

    def eliminar(self):
        if self.esta_vacia():
            raise IndexError("Subdesbordamiento: la pila está vacía")
        return self.elementos.pop()

def evaluar_posfija(expresion):
    pila = PilaEvaluador()
    tokens = expresion.split()
    
    for token in tokens:
        # Si es un número, lo convertimos a entero (o float) y lo metemos a la pila
        if token.replace('.', '', 1).isdigit():
            pila.insertar(float(token))
        # Si es un operador, sacamos los dos operandos correspondientes
        elif token in "+-*/^":
            if len(pila.elementos) < 2:
                raise ValueError("Expresión posfija inválida: faltan operandos.")
            val2 = pila.eliminar()
            val1 = pila.eliminar()
            
            if token == '+':
                resultado = val1 + val2
            elif token == '-':
                resultado = val1 - val2
            elif token == '*':
                resultado = val1 * val2
            elif token == '/':
                if val2 == 0:
                    raise ZeroDivisionError("Error: División entre cero.")
                resultado = val1 / val2
            elif token == '^':
                resultado = val1 ** val2
                
            pila.insertar(resultado)
        else:
            raise ValueError(f"Token no reconocido: {token}")
            
    if len(pila.elementos) != 1:
        raise ValueError("Expresión posfija inválida.")
    
    return pila.eliminar()

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Expresión equivalente a: (5 + 3) * 2 / 4
    expresion_pos = "5 3 + 2 * 4 /"
    print(f"Expresión posfija: {expresion_pos}")
    resultado = evaluar_posfija(expresion_pos)
    print(f"Resultado de la evaluación: {resultado}")