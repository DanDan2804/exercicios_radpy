import tkinter as tk
import random

def janela_divertida():
        cores =['red', 'blue', 'green', 'pink', 'purple', 'orange']
        segunda_janela = tk.Tk()
        segunda_janela.title ("Sobre")
        segunda_janela.geometry("300x200")

        texto = tk.Label(segunda_janela, text="Mude a cor!", font=("Arial", 12))
        texto.pack(pady=20)

        def mudar_cor():
            cor_aletoria = random.choice(cores)
            segunda_janela.configure(bg=cor_aletoria)

        botao_cor = tk.Button(segunda_janela, text="Mudar Cor", command=mudar_cor)
        botao_cor.pack(pady=10)

        segunda_janela.mainloop()

if __name__ == "__main__":
    janela_divertida()