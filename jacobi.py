#Importación de librerías
import numpy as np
import tkinter as tk
import validations as v

def show_equations(matrix):
        # Verificamos que la matriz tenga dimensiones 3x4
    if len(matrix) != 3 or any(len(fila) != 4 for fila in matrix):
        raise ValueError("La matriz debe ser de dimensiones 3x4.")
    
    ecuaciones = []
    
    for fila in matrix:
        # Extraemos los coeficientes y el resultado
        a, b, c, d = fila
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        # Construimos la ecuación
        terminos = []
        
        # Agregamos el término para x
        if a != 0:
            if abs(a) == 1:
                terminos.append(f"x" if a > 0 else f"-x")
            else:
                terminos.append(f"{a}x" if a > 0 else f"- {-a}x")
        
        # Agregamos el término para y
        if b != 0:
            if abs(b) == 1:
                terminos.append(f"+y" if b > 0 or terminos else f"-y")
            elif b > 0 and terminos:
                terminos.append(f"+ {b}y")
            else:
                terminos.append(f"{b}y" if b < 0 or not terminos else f"+ {b}y")
        
        # Agregamos el término para z
        if c != 0:
            if abs(c) == 1:
                terminos.append(f"+z" if c > 0 or terminos else f"-z")
            elif c > 0 and terminos:
                terminos.append(f"+ {c}z")
            else:
                terminos.append(f"{c}z" if c < 0 or not terminos else f"+ {c}z")
        
        # Agregamos el resultado
        ecuacion = " ".join(terminos) + f" = {d}"
        ecuaciones.append(ecuacion)
    
    return "\n".join(ecuaciones)

def jacobi_method(k,output_text, equations, tolerance=0.05):

    # Vector inicial de Jacobi (0,0,0)
    Xi = np.array([[0],[0],[0]])

    #Matriz A de coeficientes del sistema de ecuación.
    A = np.array([
        [equations[0,0],equations[0,1],equations[0,2]],
        [equations[1,0],equations[1,1],equations[1,2]],
        [equations[2,0],equations[2,1],equations[2,2]]])
    
    #Matriz b de igualdad del sistema de ecuación.
    b = np.array([[equations[0,3]],[equations[1,3]],[equations[2,3]]])

    #Matriz U estrictamente triangular superior.
    U = (-1)*np.triu(A,k=1)

    #Matriz L estrictamente triangular inferior.
    L = (-1)*np.tril(A,k=-1)

    # Matriz Diagonal de A (D)
    D = A + L + U

    # Matriz Diagonal de A (INVERSA DInv)
    DInv = np.linalg.inv(D)

    # Inicializamos la tolerancia
    tolerance_value = float('inf')  # Valor inicial alto para entrar en el bucle

    iteration = 0
    while tolerance_value >= tolerance:
        x1 = np.matmul(DInv, b) + np.matmul(DInv, (np.matmul(L + U, Xi)))
        
        # Calcular la tolerancia
        tolerance_value = np.sqrt(np.sum((x1 - Xi) ** 2)) 
        
        print(f"Iteración número {iteration + 1}") 
        print(x1)
        print(tolerance_value)
        print()

        # Mostrar la iteración en el área de texto
        x_value = x1[0, 0]  #Valor de x
        y_value = x1[1, 0]  #Valor de y
        z_value = x1[2, 0]  #Valor de z

        # Insertar los valores en output_text
        output_text.insert(tk.END, 
            f"Iteración número {iteration + 1}:\n"
            f"x = {x_value:.6f}\n"
            f"y = {y_value:.6f}\n"
            f"z = {z_value:.6f}\n"
            f"- Tolerancia: {tolerance_value:.6f}\n\n"
        )
        
        Xi = x1
        iteration += 1

def reorder_matrix(matrix):
     # Creamos una copia de la matriz para reordenar
    reordered_matrix = np.array(matrix)

    for i in range(3):
        # Encontramos el índice del elemento con el mayor valor absoluto en la fila i
        abs_values = [abs(reordered_matrix[i][j]) for j in range(3)]
        max_index = abs_values.index(max(abs_values))

        # Intercambiamos filas si es necesario
        if max_index != i:
            reordered_matrix[[i, max_index]] = reordered_matrix[[max_index, i]]

    return reordered_matrix
