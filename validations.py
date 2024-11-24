import re

def verify_entry(num):
    patron = r'^-?\d*\.?\d*$'
    
    if re.match(patron, num):
        return True
    return False

def verify_initial_condition(matrix):
    if len(matrix) != 3 or any(len(fila) != 4 for fila in matrix):
            raise ValueError("La matriz debe ser de dimensiones 3x4.") #Por lo que tenemos en main
        
    for i in range(3):
        # Valor absoluto del elemento en la diagonal principal
        diag_value = abs(matrix[i][i])
        
        # Suma de los valores absolutos de los otros elementos en la fila
        suma_otros = sum(abs(matrix[i][j]) for j in range(3) if j != i)
        
        # Condición
        if diag_value <= suma_otros:
            return False
    
    return True

