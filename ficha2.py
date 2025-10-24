import math

# Alínea 1: Calcular hipotenusa
def Alínea1():
    cateto1 = int(input("Comprimento do primeiro cateto: "))
    cateto2 = int(input("Comprimento do segundo cateto: "))
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    print("O valor da hipotenusa é:", hipotenusa)

# Alínea 2: Verificar aprovação
def Alínea2():
    nota1 = int(input("Escreva a primeira nota: "))
    nota2 = int(input("Escreva a segunda nota: "))
    media = (nota1 + nota2) / 2
    if media >= 9.5:
        print("Aprovado. Com média de:", media)
    else:
        print("Reprovado. Com média de:", media)

# Alínea 3: Verificar maior valor
def Alínea3():
    valor1 = int(input("Introduza o primeiro valor: "))
    valor2 = int(input("Introduza o segundo valor: "))
    if valor1 > valor2:
        print("O maior valor é:", valor1)
    elif valor2 > valor1:
        print("O maior valor é:", valor2)
    else:
        print("Os valores são iguais.")

# Alínea 4: Contagem crescente até 15
def Alínea4():
    numero = int(input("Insira um número entre 1 e 15: "))
    if numero < 1 or numero > 15:
        print("Número fora do intervalo.")
        return
    while numero <= 15:
        print("n =", numero)
        numero += 1

# Alínea 5: Soma da contagem até 15
def Alínea5():
    numero = int(input("Insira um número entre 1 e 15: "))
    if numero < 1 or numero > 15:
        print("Número fora do intervalo.")
        return
    soma = 0
    while numero <= 15:
        print("n =", numero)
        soma += numero
        numero += 1
    print("Soma dos números apresentados:", soma)

# Alínea 6: Somatório até atingir 500
def Alínea6():
    soma = 0
    contador = 0
    while soma < 500:
        valor = int(input("Introduza um número inferior a 100: "))
        if valor < 100:
            soma += valor
            contador += 1
            print("Somatório atual:", soma)
        else:
            print("Valor inválido. Deve ser inferior a 100.")
    media = soma / contador
    print("Média dos valores válidos introduzidos:", media)

# Alínea 7: Calcular desconto
def Alínea7():
    preco = float(input("Preço por unidade: "))
    quantidade = int(input("Quantidade a comprar: "))
    if quantidade >= 1000:
        desconto = 0.08
    elif quantidade >= 500:
        desconto = 0.05
    else:
        desconto = 0.0
    total_sem_desconto = preco * quantidade
    valor_desconto = total_sem_desconto * desconto
    total_final = total_sem_desconto - valor_desconto
    print("Desconto aplicado:", desconto * 100, "%")
    print(f"Montante a pagar após desconto: {total_final}")

# Corpo principal do programa
continuar = "s"

while continuar == "s":
    print("\nEscolha a alínea que deseja executar:")
    print("1 - Calcular hipotenusa")
    print("2 - Verificar aprovação")
    print("3 - Verificar maior valor")
    print("4 - Contagem crescente até 15")
    print("5 - Soma da contagem até 15")
    print("6 - Somatório até atingir 500")
    print("7 - Calcular desconto")

    escolha = input("Digite o número da alínea (1 a 7): ")

    if escolha == "1":
        Alínea1()
    elif escolha == "2":
        Alínea2()
    elif escolha == "3":
        Alínea3()
    elif escolha == "4":
        Alínea4()
    elif escolha == "5":
        Alínea5()
    elif escolha == "6":
        Alínea6()
    elif escolha == "7":
        Alínea7()
    else:
        print("Opção inválida. Por favor escolha um número entre 1 e 7.")

    continuar = input("\nDeseja fazer outra alínea? (s/n): ").lower()

print("Programa terminado. Até à próxima!")