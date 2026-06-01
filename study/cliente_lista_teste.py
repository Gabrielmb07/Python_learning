clientes=[]
cliente1={
    'nome':"Antonio",
    'idade':'24',
    'cpf':'20910929892',
    'cidade':'Sao Paolo'
}
cliente2={
    'nome':"Gabriel",
    'idade':'18',
    'cpf':'21909837685',
    'cidade':'Rio de Janeiro'
}
clientes.append(cliente1)
clientes.append(cliente2)
# for i in range(len(clientes)): 
#   print(clientes[i])
#    print(clientes[i]['nome'])
clientes[0]['nome']="Marcos"
print(clientes[0]["nome"])