print("-----ADVINHE A SENHA-----")
senhaCorreta = {24, 893, 1000000}
senha = int(input("Insira a senha: "))

if senha in senhaCorreta:
    print("Você acertou!")
while senha not in senhaCorreta:
    print("Você errou! Tente novamente.")
    print("-----ADVINHE A SENHA-----")
    senhaCorreta = {24, 893, 1000000}
    senha = int(input("Insira a senha: "))