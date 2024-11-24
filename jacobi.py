#Importación de librerías
import numpy as np

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
                terminos.append(f"y" if b > 0 or terminos else f"-y")
            elif b > 0 and terminos:
                terminos.append(f"+ {b}y")
            else:
                terminos.append(f"{b}y" if b < 0 or not terminos else f"+ {b}y")
        
        # Agregamos el término para z
        if c != 0:
            if abs(c) == 1:
                terminos.append(f"z" if c > 0 or terminos else f"-z")
            elif c > 0 and terminos:
                terminos.append(f"+ {c}z")
            else:
                terminos.append(f"{c}z" if c < 0 or not terminos else f"+ {c}z")
        
        # Agregamos el resultado
        ecuacion = " ".join(terminos) + f" = {d}"
        ecuaciones.append(ecuacion)
    
    return "\n".join(ecuaciones)

def jacobi_method(k,equations):

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

    #=================== JACOBI POR ITERACIONES===================
    for i in range(k):
        x1 = np.matmul(DInv,b) + np.matmul(DInv,(np.matmul(L+U,Xi)))
        print(f"Interación número {i+1}")
        print(x1)
        print()
        Xi = x1