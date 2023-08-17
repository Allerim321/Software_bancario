import os

def def_cadastro():
    x = 1
    while x == 1:
        os.system("cls")
        os.system("pause")
        x = 2

def def_excluir():
    x = 1
    while x == 1:
        os.system("cls")
        os.system("pause")
        x = 2

def def_alterar():
    x = 1
    while x == 1:
        os.system("cls")
        os.system("pause")
        x = 2

def def_saque():
    x = 1
    while x == 1:
        os.system("cls")
        os.system("pause")
        x = 2

def def_deposito():
    x = 1
    while x == 1:
        os.system("cls")
        os.system("pause")
        x = 2
    
def def_transferencia():
    x = 1
    while x == 1:
        os.system("cls")
        os.system("pause")
        x = 2

def main():
    while True:
        try:
            
            print("Bem Vindo ao PazBank")
            print("[1] - Cadastrar cliente")
            print("[2] - Excluir cliente")
            print("[3] - Alterar cliente")
            print("[4] - Realizar saque")
            print("[5] - Realizar depósito")
            print("[6] - Realizar transferência")
            print("[7] - Sair")

            op = int(input("Digite o número equivalente à opção que deseja:\n"))
            match op:
                case 1:
                    print("")
                case 2:
                    print("")
                case 3:
                    print("")
                case 4:
                    print("")
                case 5:
                    print("")
                case 6:
                    print("")
                case 7: 
                    print("Saindo...")
                    os.system("pause")
                    exit()
                case _:
                    print("Essa opção não consta na lista.")
        except Exception as erro:
            print("Algo deu errado. Tente novamente.")
            print(erro.__class__.__name__)
