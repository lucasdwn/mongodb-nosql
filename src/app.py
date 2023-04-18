import os
import controllers.ProdutoController as produtoController
import controllers.UsuarioController as usuarioController
import controllers.VendedorController as vendedorController
import controllers.CompraController as compraController
import controllers.RedisController as redisController


def clearConsole(): return os.system('cls'
                                     if os.name in ('nt', 'dos') else 'clear')

# $- OPÇÕES INICIAIS

def main():
    clearConsole()
    print("==== 1 - MONGODB ====")
    print("==== 2 - REDIS ====")
    select = input("Qual opção deseja?: ")
    if select == "1":
        mongoStart()
    elif select == "2":
        redisStart()
    else:
        print("Opção Não entendida")

# MONGODB START
def mongoStart():
    clearConsole()
    on = True
    while on:
        print("\n===========================")
        print("==== OPÇÕES ====")
        print("==== 1 - USUARIO ====")
        print("==== 2 - VENDEDOR ====")
        print("==== 3 - PRODUTO ====")
        print("==== 4 - COMPRA ====")
        print("==== CLS - CLEAR CONSOLE ====")
        print("==== X - FECHAR ====")
        print("===========================\n")
        select = input("Qual opção deseja?: ")
        if select == "1":
            usuarioStart()
        elif select == "2":
            vendedorStart()
        elif select == "3":
            produtoStart()
        elif select == "4":
            compraStart()
        elif select == "CLS":
            clearConsole()
            return mongoStart()
        elif select == "X":
            clearConsole()
            return main()
        else:
            print("Opção Não entendida")

# 1- OPÇÕES DE USUARIOS
def usuarioStart():
    clearConsole()
    on = True
    while on:
        print("\n===========================")
        print("==== OPÇÕES ====")
        print("==== 1 - BUSCAR USUARIOS ====")
        print("==== 2 - BUSCAR USUARIO ====")
        print("==== 3 - NOVO USUARIO ====")
        print("==== 4 - EDITAR USUARIO ====")
        print("==== 5 - ADICIONAR FAVORITOS ====")
        print("==== 6 - DELETAR USUARIO ====")
        print("==== CLS - CLEAR CONSOLE ====")
        print("==== X - FECHAR ====")
        print("===========================\n")
        select = input("Qual opção deseja?: ")
        if select == "1":
            usuarioController.findSort()
        elif select == "2":
            nome = input("Digite o nome que deseja buscar: ")
            usuarioController.findQuery(nome)
        elif select == "3":
            print("Insira Nome e E-mail do novo usuario")
            nome = input("nome: ")
            email = input("email: ")
            usuarioController.insert(nome, email)
        elif select == "4":
            print("Insira E-mail do usuario que deseja editar e o novo nome.")
            email = input("email: ")
            novoNome = input("Novo nome: ")
            usuarioController.update(email, novoNome)
        elif select == "5":
            print("Insira o e-mail do usuario que deseja adicionar favorito e o nome do Produto")
            emailUser = input("E-mail do usuario: ")
            nomeProduto = input("Nome do produto: ")    
            usuarioController.insertFavoritos(nomeProduto, emailUser)
        elif select == "6":
            email = input("Insira o e-mail do usuario que deseja deletar: ")
            usuarioController.delete(email)
        elif select == "CLS":
            clearConsole()
            return mongoStart()
        elif select == "X":
            on = False
            mongoStart()
        else:
            print("Opção Não entendida")


# 2- OPÇÕES DE VENDEDOR
def vendedorStart():
    clearConsole()
    on = True
    while on:
        print("\n===========================")
        print("==== OPÇÕES ====")
        print("==== 1 - BUSCAR VENDEDORES ====")
        print("==== 2 - BUSCAR VENDEDOR ====")
        print("==== 3 - NOVO VENDEDOR ====")
        print("==== 4 - EDITAR VENDEDOR ====")
        print("==== 5 - DELETAR VENDEDOR ====")
        print("==== CLS - CLEAR CONSOLE ====")
        print("==== X - FECHAR ====")
        print("===========================\n")
        select = input("Qual opção deseja?: ")
        if select == "1":
            vendedorController.findSort()
        elif select == "2":
            nome = input("Digite o nome que deseja buscar: ")
            vendedorController.findQuery(nome)
        elif select == "3":
            print("Insira Nome e CNPJ do novo vendedor")
            nome = input("nome: ")
            cnpj = input("cnpj: ")
            vendedorController.insert(nome, cnpj)
        elif select == "4":
            print("Insira cnpj do usuario que deseja editar e o novo nome.")
            cnpj = input("cnpj: ")
            novoNome = input("Novo nome: ")
            vendedorController.update(cnpj, novoNome)
        elif select == "5":
            cnpj = input("Insira o cnpj do vendedor que deseja deletar: ")
            vendedorController.delete(cnpj)
        elif select == "CLS":
            clearConsole()
            return mongoStart()
        elif select == "X":
            on = False
            mongoStart()
        else:
            print("Opção Não entendida")


# 3- OPÇÕES DE PRODUTO
def produtoStart():
    clearConsole()
    on = True
    while on:
        print("\n===========================")
        print("==== OPÇÕES ====")
        print("==== 1 - BUSCAR PRODUTOS ====")
        print("==== 2 - BUSCAR PRODUTO ====")
        print("==== 3 - NOVO PRODUTO ====")
        print("==== 4 - EDITAR PRODUTO ====")
        print("==== 5 - DELETAR PRODUTO ====")
        print("==== CLS - CLEAR CONSOLE ====")
        print("==== X - FECHAR ====")
        print("===========================\n")
        select = input("Qual opção deseja?: ")
        if select == "1":
            produtoController.findSort()
        elif select == "2":
            nome = input("Digite o nome do produto que deseja buscar: ")
            produtoController.findQuery(nome)
        elif select == "3":
            print("Insira nome, preço e vendedor do produto: ")
            nome = input("nome: ")
            preco = input("preço: ")
            vendedor = input("Nome do vendedor: ")
            produtoController.insert(nome, preco, vendedor)
        elif select == "4":
            print("Insira nome do produto que deseja editar e o novo preço.")
            nome = input("nome: ")
            novoPreco = input("Novo preço: ")
            produtoController.update(nome, novoPreco)
        elif select == "5":
            nome = input("Insira o nome do produto que deseja deletar: ")
            produtoController.delete(nome)
        elif select == "CLS":
            clearConsole()
            return mongoStart()
        elif select == "X":
            on = False
            mongoStart()
        else:
            print("Opção Não entendida")    


# 4- OPÇÕES DE COMPRA
def compraStart():
    clearConsole()
    on = True
    while on:
        print("\n===========================")
        print("==== OPÇÕES ====")
        print("==== 1 - BUSCAR COMPRAS ====")
        print("==== 2 - BUSCAR COMPRA ====")
        print("==== 3 - NOVA COMPRA ====")
        print("==== 4 - DELETAR COMPRA ====")
        print("==== CLS - CLEAR CONSOLE ====")
        print("==== X - FECHAR ====")
        print("===========================\n")
        select = input("Qual opção deseja?: ")
        if select == "1":
            compraController.findSort()
        elif select == "2":
            id = input("Digite o id da compra que deseja buscar: ")
            compraController.findQuery(id)
        elif select == "3":
            print("Insira nome do produto e o e-mail do usuario")
            nomeProduto = input("Nome do produto: ")
            emailUsuario = input("E-mail do usuario: ")
            compraController.insert(nomeProduto, emailUsuario)
        elif select == "4":
            nome = input("Insira o id da compra que deseja deletar: ")
            compraController.delete(nome)
        elif select == "CLS":
            clearConsole()
            return mongoStart()
        elif select == "X":
            on = False
            mongoStart()
        else:
            print("Opção Não entendida")

# REDIS START

def redisStart():
    clearConsole()
    on = True
    while on:
        print("\n===========================")
        print("==== OPÇÕES ====")
        print("==== 1 - IMPORTAR PRODUTO ====")
        print("==== 2 - EDITAR PRODUTO ====")
        print("==== 3 - EXPORTAR PRODUTO ====")
        print("==== CLS - CLEAR CONSOLE ====")
        print("==== X - FECHAR ====")
        print("===========================\n")
        select = input("Qual opção deseja?: ")
        if select == "1":
            redisController.importProduto()
        elif select == "2":
            redisController.getUserName()
        elif select == "CLS":
            clearConsole()
            return redisStart()
        elif select == "X":
            on = False
            main()
        else:
            print("Opção Não entendida")

# INICIANDO OPÇÕES
main()
