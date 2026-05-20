# GymTrack - Validador de Treino

print("=== GymTrack ===")

try:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    treino = input("Treino concluído? (sim/não): ")

    if idade < 16:
        print("Usuário não possui idade mínima para alguns treinos.")
    else:
        print(f"Bem-vindo(a), {nome}!")

    if treino.lower() == "sim":
        print("Treino registrado com sucesso!")
    else:
        print("Treino pendente.")

except ValueError:
    print("Erro: Digite valores válidos.")
