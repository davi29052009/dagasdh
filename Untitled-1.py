class animal:
def __init__ (self, name, sound) :
    self.name = name
    self.sound = sound
    def fazer_som (self)
        exibe qual som o animal fazer_som

        print (f"{self.name}  faz: {self.sound} ")

        class cachorro (Animal)
            
            sub classe que representa um cachorro 
            atributos
            name(str) : nome do cachorro 
            sound (str): som fixo "au au "

            def __init__ (self, name) :

                inicializa um cachorro com um nome pre definido 

                parametros 

                name (str): nome do cachorro 

                super(). __init__(name, sound = "au au") #chama o construtor da classe pai com som especifico 

                class Gato (animal):
                    subclasse que representa um gato 

                    atributos

                    name (str): nome do gato 
                    sound (str): som fixo "miau" (sobrescrito base da classe).

                    def __init__(self, name):

                        parametros
            nome(str): nome do gato.

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


                