def classificar_idade ():
  try:
    idade = int(input("Digite sua idade :"))

    if idade < 0:
      print ("Idade não pode ser negativa!")
    elif idade < 13:
      print ("voce é uma criança.")
    elif idade < 18:
      print ("voce é um adolescente.")
    elif idade < 65:
      print ("voce é um adulto.")
    elif idade < 90:
      print ("você é um idoso.")

execept ValueError:

Print ("por favor, digite um numero valido ")

