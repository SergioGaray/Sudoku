import tkinter as tk
from tkinter import messagebox

def imprimir_tablero(tablero):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(tablero[i][j])
            else:
                print(str(tablero[i][j]) + " ", end="")

def buscar_celda_vacia(tablero, vacio):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                vacio[0] = fila
                vacio[1] = columna
                return True
    return False

def usado_en_fila(tablero, fila, numero):
    return numero in tablero[fila]

def usado_en_columna(tablero, columna, numero):
    for i in range(9):
        if tablero[i][columna] == numero:
            return True
    return False

def usado_en_caja(tablero, fila, columna, numero):
    iniciar_fila = fila - fila % 3
    iniciar_columna = columna - columna % 3
    for i in range(3):
        for j in range(3):
            if tablero[i + iniciar_fila][j + iniciar_columna] == numero:
                return True
    return False

def es_seguro(tablero, fila, columna, numero):
    return not usado_en_fila(tablero, fila, numero) and not usado_en_columna(tablero, columna, numero) and not usado_en_caja(tablero, fila, columna, numero)

def guardar_sudoku(tablero):
    vacio = [0, 0]
    if not buscar_celda_vacia(tablero, vacio):
        return True
    fila, columna = vacio[0], vacio[1]
    for numero in range(1, 10):
        if es_seguro(tablero, fila, columna, numero):
            tablero[fila][columna] = numero
            if guardar_sudoku(tablero):
                return True
            tablero[fila][columna] = 0
    return False

def tablero_valido(tablero):
    for fila in range(9):
        for columna in range(9):
            numero = tablero[fila][columna]
            if numero != 0:
                tablero[fila][columna] = 0
                if not es_seguro(tablero, fila, columna, numero):
                    return False
                tablero[fila][columna] = numero
    return True

def verificar_sudoku():
    try:
        tablero = [[int(celdas[i][j].get() if celdas[i][j].get() else 0) for j in range(9)] for i in range(9)]
        if any(0 in fila for fila in tablero):
            messagebox.showwarning("Celdas vacías", "Por favor, llene todas las celdas del Sudoku.")
        elif tablero_valido(tablero) and guardar_sudoku(tablero):
            messagebox.showinfo("Resultado", "¡Sudoku resuelto correctamente!")
        else:
            messagebox.showerror("Resultado", "Sudoku incorrecto o sin solución.")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, ingrese solo números entre 1 y 9.")

# Crear la ventana principal
root = tk.Tk()
root.title("Sudoku Solver")

# Crear la cuadrícula de entradas
celdas = [[tk.Entry(root, width=5, font=('Arial', 18), justify='center') for j in range(9)] for i in range(9)]
for i in range(9):
    for j in range(9):
        celdas[i][j].grid(row=i, column=j, padx=4, pady=4)

# Ejemplo de tablero de Sudoku con números preestablecidos (0 representa celdas vacías)
tablero_inicial = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Rellenar la cuadrícula con los números preestablecidos
for i in range(9):
    for j in range(9):
        if tablero_inicial[i][j] != 0:
            celdas[i][j].insert(0, str(tablero_inicial[i][j]))
            celdas[i][j].config(state='disabled')

# Botón para verificar el Sudoku
verificar_btn = tk.Button(root, text="Verificar Sudoku", command=verificar_sudoku, font=('Arial', 18))
verificar_btn.grid(row=9, column=0, columnspan=9, pady=20)

# Ejecutar la aplicación
root.mainloop()
