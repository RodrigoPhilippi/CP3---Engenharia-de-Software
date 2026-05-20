# Biblioteca Digital

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir(self):
        print(f"Livro: {self.titulo} | Autor: {self.autor}")


livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("1984", "George Orwell")

livro1.exibir()
livro2.exibir()
