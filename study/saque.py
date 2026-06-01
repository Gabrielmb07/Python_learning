nome=input("Qual o seu nome? ")
cpf=input("Qual o seu CPF? ")
saldo=3000.75
print(f'O seu saldo e de {saldo:.2f}')
saque=float(input("Qual o valor de seu saque? "))
if saque<=0:
    print("Saque invalido")
elif saque>saldo:
    print("Saldo menor que saque")
else:
    saldo-=saque
    print(f'Seu novo saldo e de {saldo:.2f}')