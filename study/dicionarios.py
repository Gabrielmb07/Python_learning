cliente1={
    'nome':'Gabriel',
    'idade':18,
    'cidade':'Rio de Janeiro'
}
cliente2={
    'nome':'Rafael',
    'idade':'13',
    'cidade':'Maranhao'
}
cliente3={
    'nome':'Gustavo',
    'idade':'20',
    'cidade':'Belo Horizonte'
}
cliente4={
    'nome':'Angelo',
    'idade':'30',
    'cidade':'Roma'
}
clientes=(cliente1,cliente2,cliente3,cliente4)
for cli in clientes:
    if cli['nome'][0]=="A":
        print(cli['nome'])
