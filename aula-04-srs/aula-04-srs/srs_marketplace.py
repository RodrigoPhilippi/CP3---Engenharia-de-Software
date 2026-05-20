# Sistema Marketplace FIAP

print("=== FIAP Marketplace ===")

produtos = []

while True:
    produto = input("Digite o nome do produto: ")

    if produto == "sair":
        break

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

print("\nProdutos cadastrados:")

for item in produtos:
    print(f"- {item}")
