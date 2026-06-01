saldo=3000.75
movimentos=[]
while True:   
    comando=int(input("Pressione 1 para fazer um deposito, pressione 2 para fazer um saque, pressione 3 para verificar as movimentacoes e pressione 0 para finalizar: "))
    if comando==1:
       print(f'O seu saldo e de {saldo:.2f}')
       saque=float(input("Qual o valor de seu saque? "))
       if saque<=0:
            print("Saque invalido")
       elif saque>saldo:
           print("Saldo menor que saque")
       else:
          saldo-=saque
          print(f'Seu novo saldo e de {saldo:.2f}')
          acoes={
              'tipo':'D',
              'valor':saque
              }
          movimentos.append(acoes)

    elif comando==2:
        print(f'O seu saldo e de {saldo:.2f}')
        deposito=float(input("Qual o valor de seu deposito? "))
        saldo+=deposito
        print(f'Seu novo saldo e de {saldo:.2f}')
        acoes2={
            'tipo':'C',
            'valor':deposito
        }
        movimentos.append(acoes2)

    elif comando==3:
        tipo_de_filtro=int(input("Para filtrar atraves de valor, pressione 1. Para filtrar atraves tipo de acao, pressione 2: "))
        if tipo_de_filtro==1:
            valor=int(input("Digite o valor do filtro que queira utilizar: "))
            grandeza=(input("Use '<' para ver valores menores que o digitado, '>' para ver os valores maiores que o digitado e '=' para ver os valores iguais ao digitado: "))
            if grandeza=="<":
                for moviment in movimentos:
                    if moviment['valor']<valor:
                        print(moviment)
            elif grandeza==">":
                for moviment in movimentos:
                    if moviment['valor']>valor:
                        print(moviment)
            if grandeza=="=":
                for moviment in movimentos:
                    if moviment['valor']==valor:
                        print(moviment)
        elif tipo_de_filtro==2:
             tipo_de_acao=int(input("Pressione 1 para ver filtro atraves de saque. Pressione 2 para ver filtro atraves de deposito: "))
             if tipo_de_acao==1:
                 for moviment in movimentos:
                     if  moviment['tipo']=='D':
                         print(moviment)
             else:
                 for moviment in movimentos:
                     if  moviment['tipo']=='C':
                         print(moviment)


    elif comando==0:
        print("Operacao finalizada")
        break