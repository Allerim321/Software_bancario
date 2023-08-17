class Cliente:

    def __init__(self, nome, cpf, idade, saldo):
        self.nome=nome
        self.cpf=cpf
        self.idade=idade
        self.saldo=saldo

    def sacar(self,valor):
        if valor > self.saldo:
            print("Não é possível sacar esse valor")
        else:
            self.saldo = self.saldo - valor
            print("Valor sacado com sucesso! Seu saldo agora é de R$",self.saldo)