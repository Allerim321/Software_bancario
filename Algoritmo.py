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

            op = int(input("Digite o numero equivalente a opção que deseja: "))

            if op == 1:
                print("Você escolheu a opção 1")
            elif op == 2:
                print("Você escolheu a opção 2")
            elif op == 3:
                print("Você escolheu a opção 3")
            elif op == 4: 
                print("Saindo...")
                os.system("pause")
                exit()
            else:
                print("Essa opção não consta na lista.")
        except Exception as erro:
            print("Algo deu errado")
            print(erro.__class__.__name__)
