soma = 0
qtd_num = 0
while True:
    num = int(input("Digite um número: "))
    print("Caso digite 0 o programa sera parado")
    if num == 0:
        break
    else: 
        soma += num
        qtd_num += 1

if qtd_num > 0:
    media = soma / qtd_num
    print("A quantidade de numeros digitados foi de: ", qtd_num)
    print("A soma de todos os numeros digitados é: ", soma)
    print("A media dos numeros digitados é de: ", media)
