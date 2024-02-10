import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def guardar_info():
    nombre_libro = entry_nombre_libro.get()
    autor = entry_autor.get()
    genero = ", ".join([genero for genero, var in generos.items() if var.get()])
    editorial = combo_editorial.get()
    isbn = entry_isbn.get()
    tipo_libro = tipo_libro_var.get()
    descripcion = scrolled_text.get("1.0", tk.END)

    with open("biblioteca.txt", "a") as archivo:
        archivo.write(f"Nombre del libro: {nombre_libro}\n")
        archivo.write(f"Autor: {autor}\n")
        archivo.write(f"Género: {genero}\n")
        archivo.write(f"Editorial: {editorial}\n")
        archivo.write(f"ISBN: {isbn}\n")
        archivo.write(f"Tipo de libro: {tipo_libro}\n")
        archivo.write(f"Descripción: {descripcion}\n\n")
    
    limpiar_campos()

def limpiar_campos():
    entry_nombre_libro.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    for var in generos.values():
        var.set(False)
    combo_editorial.set("")
    entry_isbn.delete(0, tk.END)
    tipo_libro_var.set("")
    scrolled_text.delete("1.0", tk.END)

# Crear ventana
ventana = tk.Tk()
ventana.title("Manejo de archivos")
ventana.maxsize(width=400, height=1000)
marco = ttk.Frame(ventana, padding=10)
marco.grid(padx=0, pady=0, sticky="nsew")

marco = ttk.Frame(ventana, padding=10)
marco.grid(padx=0, pady=0)

# Crear y posicionar elementos
lbl_titulo = ttk.Label(marco, text="biblioteca personal", font=("Times New Roman", 14)).grid(padx=50, pady=0, row=0, sticky=tk.W)
tk.Label(ventana, text="Nombre del Libro:").grid(row=2, column=0, sticky="w")
entry_nombre_libro = tk.Entry(ventana, width=57)
entry_nombre_libro.grid(row=3, column=0, padx=0, pady=0, sticky=tk.W)

tk.Label(ventana, text="Autor:").grid(row=4, column=0, sticky="w")
entry_autor = tk.Entry(ventana, width=57)
entry_autor.grid(row=5, column=0, padx=0, pady=5, sticky=tk.W)

tk.Label(ventana, text="Género:").grid(row=6, column=0, sticky="w")
generos = {"Ficción": tk.BooleanVar(), "Novela": tk.BooleanVar(), "Misterio": tk.BooleanVar()}
genero_frame = tk.Frame(ventana)
genero_frame.grid(row=7, column=0, padx=5, pady=5, sticky="w")
columna = 0
for genero, var in generos.items():
    cb = tk.Checkbutton(genero_frame, text=genero, variable=var)
    cb.grid(row=7, column=columna, padx=5, sticky=tk.W)
    columna += 1

tk.Label(ventana, text="Editorial:").grid(row=12, column=0, sticky="w")
editoriales = ["Editorial Naranja", "Editorial Planeta", "Editorial Panamericana"]
combo_editorial = ttk.Combobox(ventana, width=24, values=editoriales, state="readonly")
combo_editorial.grid(row=12, column=0, padx=70, pady=5, sticky=tk.W)

tk.Label(ventana, text="ISBN:").grid(row=14, column=0, sticky="w")
entry_isbn = tk.Entry(ventana, width=30)
entry_isbn.grid(row=14, column=0, padx=50, pady=5, sticky=tk.W)

tk.Label(ventana, text="Tipo de Libro:").grid(row=16, column=0, sticky="w")
tipo_libro_var = tk.StringVar()
tipo_libro_frame = tk.Frame(ventana)
tipo_libro_frame.grid(row=17, column=0, padx=5, pady=5, sticky="w")
radiobutton1 = tk.Radiobutton(tipo_libro_frame, text="De bolsillo", variable=tipo_libro_var, value="bolsillo")
radiobutton1.grid(row=17, column=1, sticky="w", padx=5)
radiobutton2 = tk.Radiobutton(tipo_libro_frame, text="De coleccion", variable=tipo_libro_var, value="coleccion")
radiobutton2.grid(row=17, column=0, sticky="w", padx=5)
tipo_libro_var.set("bolsillo")

tk.Label(ventana, text="Descripción:").grid(row=19, column=0, sticky="w")
scrolled_text = scrolledtext.ScrolledText(ventana, width=40, height=5)
scrolled_text.grid(row=20, column=0, padx=5, pady=5, sticky=tk.W)

boton_guardar = tk.Button(ventana, width=30, text="Guardar", command=guardar_info)
boton_guardar.grid(row=21, column=0, columnspan=2, pady=10)

# Ejecutar ventana
ventana.mainloop()
