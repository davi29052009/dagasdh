class Livro:
    def __init__(self, titulo, autor, isbn, disponivel = true ):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel

        def emprestar (self):
          if self.disponivel:
             self.disponivel = false 
             return true 
        return false 
    
    def devolver (self):
       self.disponivel = true 

       class usuario:
   def __init__ (self, nome, id_usuario):
      self.nome = nome 
      self.id_usuario = id_usuario 
      self.livros_emprestados = []

      def emprestar livros (self, livro):
      if livro.emprestar ():
          self.livros_emprestados.append (livro)
          return f "livro ' {livro.titulo} ' emprestado com sucesso 
          return "Livro indisponivel para emprestimo."
      
      def devolver_livro (self, livro):
          if livro in self.livros_emprestados:
              livro.devolver ()
              self.livros_emprestados.remove(livros)

          return f 'Livro'  {livro.titulo}' devolvido com sucesso!"
          return "este livro não foi emprestado por este usuario."
      
      Class biblioteca:

      def __init__(self):
          self.livros = []
          self.usuario = []

          def adicionar_livro (self, livro):
              self.livros.append (livro)

              def cadastrar_usuario (self, usuario):
                  self.usuarios.append (usuario)

        def buscar livro (self, titulo):
      return [livro for livro in self.livros if titulo.lower () in livro.titulo. lower ()]


    def relatorio_disponibilidade(self):
        disponiveis = sum(1 for livro in self.livros if livro.disponivel)
        return f"Livros disponíveis: {disponiveis}/{len(self.livros)}"

# Exemplo de uso do sistema
if __name__ == "__main__":
    # Criando objetos
    biblioteca = Biblioteca()

