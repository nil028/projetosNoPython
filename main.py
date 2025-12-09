print("---CALCULADORA---")
calculadora = int(input("Insira um valor: "))
sinal = input("Insira o sinal: ")
teste = int(input("Insira outro valor: "))

sinalzinho = ["/", "*", "+", "-"]

while sinal == "+":
    print(f"Resultado: {calculadora+teste}")
    print("---CALCULADORA---")
    calculadora = int(input("Insira um valor: "))
    sinal = input("Insira o sinal: ")
    teste = int(input("Insira outro valor: "))
while sinal == "-":
    print(f"Resultado: {calculadora-teste}")
    print("---CALCULADORA---")
    calculadora = int(input("Insira um valor: "))
    sinal = input("Insira o sinal: ")
    teste = int(input("Insira outro valor: "))
while sinal == "*":
    print(f"Resultado: {calculadora*teste}")
    print("---CALCULADORA---")
    calculadora = int(input("Insira um valor: "))
    sinal = input("Insira o sinal: ")
    teste = int(input("Insira outro valor: "))
while sinal == "/":
    print(f"Resultado: {calculadora/teste}")
    print("---CALCULADORA---")
    calculadora = int(input("Insira um valor: "))
    sinal = input("Insira o sinal: ")
    teste = int(input("Insira outro valor: "))
while sinal != sinalzinho:
    print("Tente novamente!")
    print("---CALCULADORA---")
    calculadora = int(input("Insira um valor: "))
    sinal = input("Insira o sinal: ")
    teste = int(input("Insira outro valor: "))
