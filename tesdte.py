"""
Módulo: UC4 - Herança e Polimorfismo
Objetivo: Demonstrar o uso de herança e substituição de métodos em Python através de uma hierarquia de animais.
Autor: [Seu Nome]
Data: [Data]
"""

class Animal:
    """
    Classe base que representa um animal genérico.

    Atributos:
        name (str): Nome do animal.
        sound (str): Som característico que o animal emite.
    """

    def __init__(self, name, sound):
        """
        Inicializa um animal com nome e som.

        Parâmetros:
            name (str): Nome do animal (ex: "Rex", "Whiskers").
            sound (str): Som do animal (ex: "Au Au", "Miau").
        """
        self.name = name  # Armazena o nome do animal
        self.sound = sound  # Armazena o som do animal

    def fazer_som(self):
        """
        Exibe o som que o animal faz.

        Retorna:
            None (apenas imprime uma mensagem).
        """
        print(f"{self.name} faz: {self.sound}")


class Cachorro(Animal):
    """
    Subclasse que representa um cachorro, herdando de Animal.

    Atributos:
        name (str): Nome do cachorro.
        sound (str): Som fixo "Au Au!" (sobrescrito da classe base).
    """

    def __init__(self, name):
        """
        Inicializa um cachorro com nome e som pré-definido.

        Parâmetros:
            name (str): Nome do cachorro.
        """
        super().__init__(name, sound="Au Au!")  # Chama o construtor da classe pai com som específico


class Gato(Animal):
    """
    Subclasse que representa um gato, herdando de Animal.

    Atributos:
        name (str): Nome do gato.
        sound (str): Som fixo "Miau!" (sobrescrito da classe base).
    """

    def __init__(self, name):
        """
        Inicializa um gato com nome e som pré-definido.

        Parâmetros:
            name (str): Nome do gato.
        """
        super().__init__(name, sound="Miau!")  # Chama o construtor da classe pai com som específico


# --- TESTE DAS CLASSES ---
if __name__ == "__main__":
    """
    Bloco de teste para verificar o funcionamento das classes.
    """
    rex = Cachorro("Rex")  # Cria um cachorro chamado Rex
    whiskers = Gato("Whiskers")  # Cria um gato chamado Whiskers

    rex.fazer_som()  # Saída esperada: "Rex faz: Au Au!"
    whiskers.fazer_som()  # Saída esperada: "Whiskers faz: Miau!"