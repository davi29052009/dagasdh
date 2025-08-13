class contaBancaria
"""
classe que indica conta bancaria
 

 def __init__(self, titular, saldo_inicial=0 , numero= ""):

    """
    iniciializa a conta bancaria.

    Parametros

    """

    self.titular = titular
    self.saldo = saldo_inicial
    self.numero = numero

    def depositar (self, valor)
    """

    Adiciona um valor ao saldo da conta 

    Parametros

      valor (float): valor a ser depositado

      retorna:

      float: novo saldo 

      if valor >0:
        self.saldo += valor
        return self.saldo