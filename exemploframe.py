import tkinter as tk

class ExemploFrame:
    def __init__(self):
        self.janela = tk.Tk()
        for i in range(3):
            self.janela.columnconfigure(i, weight=1, minsize=75)
            self.janela.rowconfigure(i, weight=1, minsize=50)
            for j in range(3):
                frame = tk.Frame(master=self.janela, relief=tk.RAISED, borderwidth=1)
                frame.grid(row=i, column=j, padx=5, pady=5)
                label = tk.Label(master=frame, text=f"Linha {i}\nColuna {j}")
                label.pack()
            self.janela.mainloop()

if __name__ == "__main__":
    ExemploFrame()