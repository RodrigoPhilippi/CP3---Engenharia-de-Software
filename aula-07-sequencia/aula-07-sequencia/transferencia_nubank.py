# Simulação de Transferência Bancária

saldo = 1000

try:
    valor = float(input("Digite o valor da transferência: R$ "))

    if valor <= saldo:
        saldo -= valor
        print("Transferência realizada com sucesso!")
        print(f"Saldo restante: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente.")

except ValueError:
    print("Digite um valor válido.")
