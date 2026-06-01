clientes=[]
contas=[]

while True:
    cliente_ou_conta=int(input("Digite 1 para ver as contas dos clientes ou digite 2 para ver as contas no banco ou pressione 0 para cancelar: "))
    if cliente_ou_conta == 1:
        while True:
            crud=input("Digite 1 para cadastrar um novo cliente. Digite 2 para buscar um cliente. Digite 3 para atualizar um cliente. Digite 4 para excluir um cliente. Digite 5 para mostrar todos os clientes. DIgite 0 para encerrar o programa. ")
            if crud=="1":
                nome=input("Digite o nome de seu novo cliente: ")
                idade=int(input("Digite a idade de seu novo cliente: "))
                cpf=input("Digite o CPF de seu cliente: ")
                cidade=input("Digite a cidade de seu cliente: ")
                cpf_existente=False
                for i in range(len(clientes)):
                    if cpf==clientes[i]['cpf']:
                        cpf_existente=True
                        print("Nao e possivel criar uma nova conta com um CPF ja existente")
                        break
                if cpf_existente==False:
                    cliente={
                        'nome':nome,
                        'idade':idade,
                        'cpf':cpf,
                        'cidade':cidade
                    }
                    clientes.append(cliente)

            elif crud=="2":
                cpf_da_busca=input("Qual o CPF do cliente que voce esta buscando? ") #alterar para melhor busca
                for cli in clientes:
                    if cli['cpf']==cpf_da_busca:
                        print(cli)
                    elif cli['cpf']!=cpf_da_busca:
                        print("Nao foi possivel encontrar este cliente, ou o cliente foi excluido. Certifique-se que botou o CPF corretamente")
                        break

            elif crud=="3":
                cpf_da_busca=input("Digite o CPF do cliente que voce esta atualizando: ")
                for i in range(len(clientes)):
                     if cpf_da_busca==clientes[i]['cpf']:
                         novo_nome=input("Digite o nome atualizado do cliente: ")
                         nova_idade=int(input("Digite a nova idade do cliente: "))
                         nova_cidade=input("Digite a nova cidade do cliente: ")
                         clientes[i]['nome']=novo_nome
                         clientes[i]['idade']=nova_idade
                         clientes[i]['cidade']=nova_cidade
                         break
                     else:
                        print("Nao foi possivel encontrar este cliente. Certifique-se que colocou o CPF corretamente.")
                    
            elif crud=="4":
                cpf_da_busca=input("Digite o CPF do cliente que deseje excluir: ")
                for i in range(len(clientes)):
                    if cpf_da_busca==clientes[i]['cpf']:
                        del clientes[i]
                        print("Cliente excluido")
                        break
                    else:
                        print("Nao foi possivel encontrar este cliente. Certifique-se que colocou o CPF corretamente.")

            elif crud=="5":
                print(clientes)

            elif crud=="0":
                print("Operacao finalizada.")
                break

    elif cliente_ou_conta ==2:
        while  True:
            crud=int(input("Pressione 1 para adicionar uma conta de um cliente. Pressione 2 para ver uma conta do cliente. Pressione 3 para alterar a conta de um cliente. Pressione 4 para excluir a conta de um cliente. Precione 5 para ver todas as contas de cliente. Pressione 0 para encerrar a atividade"))
            if crud==1:
                nome=input("Digite o nome de seu novo cliente: ")
                idade=int(input("Digite a idade de seu novo cliente: "))
                cpf_c=input("Digite o CPF de seu cliente: ")
                id=input("Digite ID da conta: ")
                tipo=input("Digite o tipo de conta: ")
                conta={
                    'nome':nome,
                    'idade':idade,
                    'cpf':cpf_c,
                    'id':id,
                    'tipo':tipo
                }
                for i in range(len(clientes)):
                    if cpf_c==clientes[i]['cpf']:
                        contas.append(conta)
                    

            elif crud==2:
                cpf_da_busca=input("Digite o CPF do cliente que deseje ver a conta: ")
                for i in range(len(contas)):
                    if cpf_da_busca==contas[i]['cpf'] and cpf_da_busca==clientes[i]['cpf']:
                        print(contas)
                        break
                    elif cpf_da_busca!=contas[i]['cpf'] or cpf_da_busca!=clientes[i]['cpf']:
                        print("Nao foi possivel achar a conta do cliente que voce digiou o CPF. Verifique se o CPF indicado esta correto.")

            elif crud==3:
                cpf_da_busca=input("Digite o CPF do cliente que deseje alterar a conta: ")
                for i in range(len(contas)):
                    if cpf_da_busca==contas[i]['cpf'] and cpf_da_busca==clientes[i]['cpf']:
                        novo_nome=input("Digite o nome atualizado do cliente: ")
                        nova_idade=int(input("Digite a nova idade do cliente: "))
                        novo_id=input("Digite o novo ID do cliente: ")
                        novo_tipo=input("Digite o novo tipo de conta do cliente: ")
                        clientes[i]['nome']=novo_nome
                        clientes[i]['idade']=nova_idade
                        clientes[i]['id']=novo_id
                        clientes[i]['novo id']=novo_tipo
                        break
                    elif cpf_da_busca!=contas[i]['cpf'] or cpf_da_busca!=clientes[i]['cpf']:
                        print("Nao foi possivel achar a conta do cliente que voce digiou o CPF. Verifique se o CPF indicado esta correto.")

            elif crud==4:
                cpf_da_busca=input("Digite o CPF do cliente que deseje alterar a conta: ")
                for i in range(len(contas)):
                    if cpf_da_busca==contas[i]['cpf'] and cpf_da_busca==clientes[i]['cpf']:
                        del contas[i]
                        print("Conta de cliente excluida")
                        break
                    elif cpf_da_busca!=contas[i]['cpf'] or cpf_da_busca!=clientes[i]['cpf']:
                        print("Nao foi possivel achar a conta do cliente que voce digiou o CPF. Verifique se o CPF indicado esta correto.")

            elif crud ==5:
                print(contas)

            elif crud==0:
                print("Operacao finalizada")
                break
    elif cliente_ou_conta ==0:
        print("Operacao terminada")
        break