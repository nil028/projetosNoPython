fatorial = int(input("Insira um número: "))

for i in range(fatorial, 1, -1):
    fatorial *= i
    print(fatorial)

print(f"Resultado = {fatorial}")