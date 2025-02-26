import tkinter as tk
from tkinter import messagebox
import random
import string

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            messagebox.showerror("Erro", "Digite um número maior que zero.")
            return
        
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")

def copiar_senha():
    janela.clipboard_clear()
    janela.clipboard_append(entry_senha.get())
    janela.update()
    messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")

janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x250")
janela.resizable(False, False)

tk.Label(janela, text="Tamanho da Senha:", font=("Arial", 12)).pack(pady=5)
entry_tamanho = tk.Entry(janela, font=("Arial", 12), width=10)
entry_tamanho.pack()

btn_gerar = tk.Button(janela, text="Gerar Senha", font=("Arial", 12), command=gerar_senha)
btn_gerar.pack(pady=10)

entry_senha = tk.Entry(janela, font=("Arial", 14), width=25, justify="center")
entry_senha.pack(pady=5)

btn_copiar = tk.Button(janela, text="Copiar Senha", font=("Arial", 12), command=copiar_senha)
btn_copiar.pack(pady=10)

janela.mainloop()
