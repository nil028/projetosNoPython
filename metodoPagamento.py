print("Olá!")
print("Qual será o seu metódo de pagamento?")
print("[1] - Cartão de débito ou crédito | [2] - Pix")
opcao = int(input("Insira aqui: "))
if opcao == 1:
    cartao = (input('Digite o seu cartão: '))
    digitos = cartao[-4:]
    print(f"Seu cartão termina em: XXXXXXXXXXXX{digitos}")
    print("Deseja continuar? [S] - Sim ou [N] - Não")
    opc = (input(""))
    print("Ok!" if opc == 'S' else "Tente novamente.")
elif opcao == 2:
    print("Estamos trabalhando nessa opção!")
while opcao >= 3 or opcao <= 0:
    print("Olá!")
    print("Qual será o seu metódo de pagamento?")
    print("[1] - Cartão de débito ou crédito | [2] - Pix")
    opcao = int(input("Insira aqui: "))
    if opcao == 1:
        cartao = (input('Digite o seu cartão: '))
        digitos = cartao[-4:]
        print(f"Seu cartão termina em: XXXXXXXXXXXX{digitos}")
        print("Deseja continuar? [S] - Sim ou [N] - Não")
        opc = (input(""))
        print("Ok!" if opc == 'S' else "Tente novamente.")
    elif opcao == 2:
        print("Estamos trabalhando nessa opção!")