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

def jacobi_method():
    pass