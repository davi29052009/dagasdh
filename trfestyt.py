class ContaBancaria:
    """
    Classe que representa uma conta bancária com operações básicas, implementando o conceito de encapsulamento.
    
    Atributos privados:
        __titular (str): Nome do titular da conta
        __saldo (float): Saldo atual da conta
    """
    
    def __init__(self, titular, saldo_inicial=0):
        """
        Inicializa uma nova conta bancária.
        
        Parâmetros:
            titular (str): Nome do titular da conta
            saldo_inicial (float): Saldo inicial da conta (padrão: 0)
        """
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado
    
    def depositar(self, valor):
        """
        Realiza um depósito na conta se o valor for positivo.
        
        Parâmetros:
            valor (float): Valor a ser depositado
            
        Retorna:
            str: Mensagem de confirmação com novo saldo
            
        Levanta:
            ValueError: Se o valor for negativo ou zero
        """
        if valor <= 0:
            
        
        self.__saldo += valor
        return f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}"
    
    def sacar(self, valor):
        """
        Realiza um saque da conta se houver saldo suficiente.
        
        Parâmetros:
            valor (float): Valor a ser sacado
            
        Retorna:
            str: Mensagem de confirmação com novo saldo
            
        Levanta:
            ValueError: Se o valor for negativo, zero ou maior que o saldo
        """
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente para realizar o saque")
        
        self.__saldo -= valor
        return f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}"
    
    def get_saldo(self):
        """
        Retorna o saldo atual da conta.
        
        Retorna:
            float: Saldo atual
        """
        return self.__saldo
    
    def get_titular(self):
        """
        Retorna o nome do titular da conta.
        
        Retorna:
            str: Nome do titular
        """
        return self.__titular


# Exemplo de uso da classe
if __name__ == "__main__":
    # Criando uma conta bancária para João com saldo inicial de R$1000
    conta_joao = ContaBancaria("João", 1000)
    
    # Realizando operações (usando apenas os métodos públicos)
    print(conta_joao.depositar(500))  # Depósito de R$500
    print(conta_joao.sacar(200))     # Saque de R$200
    
    # Consultando saldo (usando o método público)
    saldo_atual = conta_joao.get_saldo()
    print(f"Saldo atual da conta do {conta_joao.get_titular()}: R${saldo_atual:.2f}")
    
    # Tentativa de acesso direto aos atributos privados (gerará erro)
    try:
        print(conta_joao.__saldo)  # Isso causará AttributeError
    except AttributeError as e:
        print(f"Erro: {e} - Acesso direto a atributos privados não é permitido.")