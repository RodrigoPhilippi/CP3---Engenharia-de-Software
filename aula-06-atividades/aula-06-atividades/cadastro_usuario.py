# Cadastro e Aprovação de Usuário

usuarios_aprovados = []

try:
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade: "))

    if idade >= 18:
        usuarios_aprovados.append(nome)
        print("Usuário aprovado!")
    else:
        print("Usuário menor de idade.")

    print("\nUsuários aprovados:")

    for usuario in usuarios_aprovados:
        print(usuario)

except ValueError:
    print("Digite uma idade válida.")
