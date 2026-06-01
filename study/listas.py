produtos=['banana','maca']
produtos.append('abacate')
produtos.append('abacaxi')
print(produtos)
print(produtos[0:2])
print(produtos[2:])
produtos.pop(2)
print(produtos)
print(produtos[2])
nome:str="Gabriel"
print(nome[0])
for p in produtos:
    print(p)
for i in range(len(produtos)):
    print(produtos[i])
print("-------")
for a in produtos:
    if a[0]=="a":
        print(a)
produtos2=('banana','maca')

