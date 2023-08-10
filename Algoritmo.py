import os

def main():
    while True:
        try:
            print("Bem Vindo ao PazBank")
            print("[1] - Cadastrar cliente")
            print("[2] - Excluir cliente")
            print("[3] - Alterar cliente")
            print("[4] - Realizar saque")
            print("[5] - Realizar depósito")
            print("[6] - Sair")

            op = int(input("Digite o número equivalente à opção que deseja:\n"))

            if op == 1:
                print("")
            elif op == 2:
                print("")
            elif op == 3:
                print("")
            elif op == 4:
                print("")
            elif op == 5:
                print("")
            elif op == 6: 
                print("Saindo...")
                os.system("pause")
                exit()
            else:
                print("Essa opção não consta na lista.")
        except Exception as erro:
            print("Algo deu errado. Tente novamente.")
            print(erro.__class__.__name__)
