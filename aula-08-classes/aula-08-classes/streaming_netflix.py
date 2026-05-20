# Sistema de Streaming

class Filme:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria

    def exibir_filme(self):
        print(f"Filme: {self.nome}")
        print(f"Categoria: {self.categoria}")


filme1 = Filme("Interestelar", "Ficção Científica")
filme1.exibir_filme()
