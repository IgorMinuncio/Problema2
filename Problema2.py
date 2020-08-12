import os 
def LimparTela():
    os.system('cls')

listaCategorias = list(['Frutas'])    
dictProduto = dict()        
listaEstoque = list()  

while True:
    LimparTela()
    print("=-==-==-==-==-==-==-==-==-==-==-==-==-MENU-==-==-==-==-==-==-==-==-==-==-==")
    print("( 1 ) Cadastrar Categoria")
    print("( 2 ) Listar Estoque")
    print("( 3 ) Remover Produto do Estoque")
    print("( 4 ) Cadastrar Produto no Estoque")
    print("( 5 ) Sair")
    print("=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==") 
    op = int(input("Escolha uma opção: "))  
    if op == 1:
        print("=-==-==-==-==-==-==-==-==CADASTRO DE CATEGORIA-==-==-==-==-==-==-==-==-=")
        listaCategorias.append(str(input("Nome da nova categoria: ")))
    elif op == 2:
        print("=-==-==-==-==-==-==-==-==-==-==ESTOQUE-==-==-==-==-==-==-==-==-==-==-==")
        for prod in listaEstoque:
            print(f"", prod)
            print("=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==") 
        input("Pressionar Enter para continuar... ")
        print("=-==-==-==-==-==-==-==-==-==-==-==-==-==-=-==-==-==-==-==-==-==-==-==-==")
    elif op == 3:        
        print("=-==-==-==-==-==-==-==-==-==-==ESTOQUE-==-==-==-==-==-==-==-==-==-==-==")
        i = 0
        for prod in listaEstoque:
            print("{} {}".format(i, prod))
            i += 1
        print("=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-") 
        esc = int(input("Escolha produto para será removido: "))
        listaEstoque.pop(esc)
    elif op == 4:        
        print("=-==-==-==-==-==-==-==-=CADASTRO DE PRODUTO=-==-==-==-==-==-==-==-==-==")
        print("=-==-==-==-==-==-==-==-==-==-=CATEGORIAS=-==-==-==-==-==-==-==-==-==-=")
        for c in listaCategorias:
            print(c)
        print("=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=")                     
        verf = False
        while verf == False:
            cat = str(input("Escolha a categoria do produto: "))
            for c in listaCategorias:
                if c == cat:
                    print("Categoria válida!")
                    verf = True 
        nomeProd = str(input("Nome do produto: "))
        valorProd = float(input("Valor do produto: "))    
        dictProduto = {'produto':nomeProd,
                       'valor':valorProd,
                       'categoria':cat
                       }
        listaEstoque.append(dictProduto)
    elif(op == 5):        
        while True:
            esc = str(input("Deseja realmente sair? [S/N]")).upper()[0]
            if esc in 'SN': 
                break
            print('ERRO! Por favor, digite apenas S ou N.')   
        if(esc == 'S'):
            import sys
            sys.exit(0)
    else:
        print('ERRO! Por favor, escolha uma opção válida.')
 