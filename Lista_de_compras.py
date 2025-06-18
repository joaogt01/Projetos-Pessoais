def menu_compras():
    print('''Digite a opção escolhida:
1 - Adicionar um produto
2 - Excluir um produto
3 - Consultar a lista de compras
4 - Sair''')
lista_de_compras = []
registo_compras = {'produto':[]  , 'quantidade': []}
laco = True
while laco == True:
    menu_compras()
    escolha = int(input())
    if escolha == 1:
        print("Digite o produto a ser adicionado na lista: ")
        produto_add = input()
        print("Digite a quantidade a ser adicionada: ")
        quantidade_add = int(input())
        registo_compras['produto'] = produto_add
        registo_compras['quantidade'] = quantidade_add
        lista_de_compras.append(registo_compras)
        continue
    elif escolha == 2:
        print(lista_de_compras)
        print("Escolha o produto a ser excluido da lista")
        produto_remove = input().lower()
        if produto_remove in lista_de_compras:
            lista_de_compras.remove(registo_compras[produto_remove])
            print(lista_de_compras)
    elif escolha == 3:
        print(lista_de_compras)