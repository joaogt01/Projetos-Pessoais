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
        registo_compras = {
            'produto': produto_add,
            'quantidade': quantidade_add
        }
        lista_de_compras.append(registo_compras)
        continue
    elif escolha == 2:
        print("Lista atual:")
        for i,item in enumerate(lista_de_compras):
            print(f"{i+1}. {item['produto']} - {item['quantidade']}")
        print("Digite o nome do produto a ser removido")
        produto_remove = input().lower()

        encontrado = False
        for item in lista_de_compras:
            if item['produto'].lower() == produto_remove:
                lista_de_compras.remove(item)
                print(f"{produto_remove} removido com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado na lista.")
    elif escolha == 3:
        for item in lista_de_compras:
            print(f"- {item['produto']} (Quantidade: {item['quantidade']})")
    elif escolha == 4:
        laco = False
        print("Encerrando")
    else:
        print("Opção invalida. Tente novamente")