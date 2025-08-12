class Livro:
    def __init__(self, titulo, autores, editora, isbn, num_paginas):
        self.titulo = titulo
        self.autores = autores
        self.editora = editora
        self.isbn = isbn
        self.num_paginas = num_paginas
    
    def display_details(self):
        print("Detalhes do Livro:")
        print(f"Título: {self.titulo}")
        print(f"Autor(es): {', '.join(self.autores)}")
        print(f"Editora: {self.editora}")
        print(f"ISBN: {self.isbn}")
        print(f"Número de páginas: {self.num_paginas}")
        print("-" * 40)


class Revista:
    def __init__(self, titulo, autores, editora, issn, volume, edicao):
        self.titulo = titulo
        self.autores = autores
        self.editora = editora
        self.issn = issn
        self.volume = volume
        self.edicao = edicao
    
    def display_details(self):
        print("Detalhes da Revista:")
        print(f"Título: {self.titulo}")
        print(f"Autor(es): {', '.join(self.autores)}")
        print(f"Editora: {self.editora}")
        print(f"ISSN: {self.issn}")
        print(f"Volume: {self.volume}")
        print(f"Edição: {self.edicao}")
        print("-" * 40)


class Jornal:
    def __init__(self, titulo, autores, editora, data_publicacao, secao):
        self.titulo = titulo
        self.autores = autores
        self.editora = editora
        self.data_publicacao = data_publicacao
        self.secao = secao
    
    def display_details(self):
        print("Detalhes do Jornal:")
        print(f"Título: {self.titulo}")
        print(f"Autor(es): {', '.join(self.autores)}")
        print(f"Editora: {self.editora}")
        print(f"Data de publicação: {self.data_publicacao}")
        print(f"Seção: {self.secao}")
        print("-" * 40)


# Testando as classes
if __name__ == "__main__":
    # Criando objetos de cada tipo de publicação
    livro = Livro(
        titulo="Python para Iniciantes",
        autores=["John Smith", "Maria Silva"],
        editora="Tech Books",
        isbn="978-3-16-148410-0",
        num_paginas=350
    )
    
    revista = Revista(
        titulo="Ciência Moderna",
        autores=["Carlos Eduardo", "Ana Paula"],
        editora="Editora Científica",
        issn="1234-5678",
        volume=15,
        edicao=3
    )
    
    jornal = Jornal(
        titulo="Diário Nacional",
        autores=["Redação"],
        editora="Grupo Mídia",
        data_publicacao="15/06/2023",
        secao="Ciência e Tecnologia"
    )
    
    # Exibindo os detalhes de cada publicação
    livro.display_details()
    revista.display_details()
    jornal.display_details()