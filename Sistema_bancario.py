# ===== DADOS GLOBAIS =====
AGENCIA = "0001"
usuarios = []
contas = []

# ===== FUNÇÕES BANCÁRIAS =====
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n✅ Depósito realizado com sucesso!")
    else:
        print("\n❌ Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\n❌ Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("\n❌ Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("\n❌ Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n✅ Saque realizado com sucesso!")
    else:
        print("\n❌ Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================")


# ===== FUNÇÕES DE CADASTRO =====
def criar_usuario():
    cpf = input("Informe o CPF (apenas números): ")

    usuario = filtrar_usuario(cpf)
    if usuario:
        print("\n⚠️ Já existe usuário com esse CPF!")
        return

    nome = input("Nome completo: ")
    data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nasc": data_nasc,
        "endereco": endereco,
    })

    print("\n✅ Usuário criado com sucesso!")


def filtrar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        numero_conta = len(contas) + 1
        contas.append({
            "agencia": AGENCIA,
            "numero_conta": numero_conta,
            "usuario": usuario,
        })
        print("\n✅ Conta criada com sucesso!!")
    else:
        print("\n❌ Usuário não encontrado. Crie o usuário primeiro.")


# ===== SISTEMA (MENU) =====
def main():
    saldo = 0
    extrato = ""
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
======= MENU =======
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[q] Sair
=> """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario()

        elif opcao == "nc":
            criar_conta()

        elif opcao == "q":
            print("\n✅ Obrigado por usar nosso sistema! Até logo!")
            break

        else:
            print("\n❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
