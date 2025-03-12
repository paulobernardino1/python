import tkinter as tk
from tkinter import ttk, messagebox

def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        resultado = (b * c) / a
        entry_x.config(state="normal", background="#2D728F", foreground="white")
        entry_x.delete(0, tk.END)
        entry_x.insert(0, f"{resultado:.2f}")
        entry_x.config(state="readonly")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da interface
tela = tk.Tk()
tela.title("Calculadora de Regra de Três Direta")
tela.geometry("400x250")
tela.resizable(False, False)
tela.configure(bg="#F4F4F4")

frame = tk.Frame(tela, bg="#F4F4F4")
frame.pack(pady=10)

fonte_principal = ("Helvetica", 12, "bold")
fonte_secundaria = ("Helvetica", 10)

entry_a = ttk.Entry(frame, width=12, font=fonte_secundaria)
entry_a.grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame, text="ESTÁ PARA", fg="gray", bg="#F4F4F4", font=fonte_secundaria).grid(row=0, column=1, padx=5)
entry_b = ttk.Entry(frame, width=12, font=fonte_secundaria)
entry_b.grid(row=0, column=2, padx=5, pady=5)

tk.Label(frame, text="ASSIM COMO", font=fonte_principal, bg="#F4F4F4").grid(row=1, column=0, columnspan=3, pady=5)

entry_c = ttk.Entry(frame, width=12, font=fonte_secundaria)
entry_c.grid(row=2, column=0, padx=5, pady=5)
tk.Label(frame, text="ESTÁ PARA", fg="gray", bg="#F4F4F4", font=fonte_secundaria).grid(row=2, column=1, padx=5)
entry_x = tk.Entry(frame, width=12, state="readonly", font=fonte_principal, justify="center", readonlybackground="#2D728F", fg="white")
entry_x.grid(row=2, column=2, padx=5, pady=5)

botao_calcular = tk.Button(tela, text="Calcular", command=calcular, font=fonte_principal, bg="#2D728F", fg="white", padx=10, pady=5, relief="flat")
botao_calcular.pack(pady=10)

tela.mainloop()