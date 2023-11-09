velcar = int(input("Informe a velocidade do carro: "))
multakm = 20
limitevelocidade = 80

if velcar > limitevelocidade:
    valorExcedido = velcar - limitevelocidade
    totalmulta = multakm * valorExcedido
    print("você excedeu o limite de velocidade e foi MULTADO")
    print("Esse é o valor da multa: ", totalmulta)
else:
    print("Você esta dentro da velocidade permitida", "\n diriga com cuidado" , "\n respeite as leis de transito")

