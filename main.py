import tkinter as tk
import numpy as np
from tkinter import messagebox
import validations as v
import jacobi
from jacobi import *

def solve_equations():
    print("Resolviendo...")
    try:
        equations = np.array([ 
            [float(entry_a11.get() or 0), float(entry_a12.get() or 0), float(entry_a13.get() or 0), float(entry_b1.get() or 0)], 
            [float(entry_a21.get() or 0), float(entry_a22.get() or 0), float(entry_a23.get() or 0), float(entry_b2.get() or 0)], 
            [float(entry_a31.get() or 0), float(entry_a32.get() or 0), float(entry_a33.get() or 0), float(entry_b3.get() or 0)] ])
        initial_guess = [0, 0, 0]
        tolerance = 0.05
        max_iterations = 100

        print(v.verify_initial_condition(equations))

        jacobi_method(5,equations) #Función para resolver el Jacobi con k=iteraciones
        solution = ""

        show_eq = jacobi.show_equations(equations)

        messagebox.showinfo("Entrada", f"Ecuaciones: {show_eq}")

        #solution = jacobi_method(equations, initial_guess, tolerance, max_iterations)
        #messagebox.showinfo("Solución", f"Solución: {solution}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Ecuaciones 3x3 por método de Jacobi")
root.geometry("500x300+800+200")
root.resizable(False, False)
#root.configure(bg="light sky blue")

# Crear un marco para centrar los widgets
frame = tk.Frame(root)
frame.pack(pady=10)

# Instrucciones para el usuario
instructions = tk.Label(frame, text="Ingrese los coeficientes y resultados de cada ecuación:\nSi no hay coeficientes se asumirá un 0")
instructions.grid(row=0, column=0, columnspan=7, pady=5)

# Registrar la función de validación
vcmd = (root.register(v.verify_entry), '%P')

# Crear las etiquetas y entradas para los coeficientes y resultados
tk.Label(frame, text="Ecuación 1").grid(row=1, column=0, columnspan=7)
entry_a11 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_a11.grid(row=2, column=0, sticky="e")
tk.Label(frame, text="x +").grid(row=2, column=1, sticky="w")
entry_a12 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_a12.grid(row=2, column=2, sticky="e")
tk.Label(frame, text="y +").grid(row=2, column=3, sticky="w")
entry_a13 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_a13.grid(row=2, column=4, sticky="e")
tk.Label(frame, text="z =").grid(row=2, column=5, sticky="w")
entry_b1 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_b1.grid(row=2, column=6, sticky="e")

tk.Label(frame, text="Ecuación 2").grid(row=3, column=0, columnspan=7)
entry_a21 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_a21.grid(row=4, column=0, sticky="e")
tk.Label(frame, text="x +").grid(row=4, column=1, sticky="w")
entry_a22 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_a22.grid(row=4, column=2, sticky="e")
tk.Label(frame, text="y +").grid(row=4, column=3, sticky="w")
entry_a23 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_a23.grid(row=4, column=4, sticky="e")
tk.Label(frame, text="z =").grid(row=4, column=5, sticky="w")
entry_b2 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_b2.grid(row=4, column=6, sticky="e")

tk.Label(frame, text="Ecuación 3").grid(row=5, column=0, columnspan=7)
entry_a31 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_a31.grid(row=6, column=0, sticky="e")
tk.Label(frame, text="x +").grid(row=6, column=1, sticky="w")
entry_a32 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_a32.grid(row=6, column=2, sticky="e")
tk.Label(frame, text="y +").grid(row=6, column=3, sticky="w")
entry_a33 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_a33.grid(row=6, column=4, sticky="e")
tk.Label(frame, text="z =").grid(row=6, column=5, sticky="w")
entry_b3 = tk.Entry(frame, width=5, validate="key", validatecommand=vcmd)
entry_b3.grid(row=6, column=6, sticky="e")

# Botón para resolver el sistema de ecuaciones
tk.Button(frame, text="Resolver", command=solve_equations).grid(row=7, column=0, columnspan=7, pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()


