import config as config

def findSort():
    mydb = config.connect()
    mycol = mydb.Produto
    print("\n===========================")
    print("==== TODOS OS PRODUTOS ====") 
    print("===========================\n")
    mydoc = mycol.find({}, {
        "_id": 0,
        "codigo": 1,
        "nome": 1,
        "preco": 1,
        "vendedor": 1
    }).sort("nome")
    for x in mydoc:
        print(x)
        print("===========================\n")

def findQuery(name):
    mydb = config.connect()
    mycol = mydb.Produto
    print("\n=========================")
    print("==== PRODUTO BUSCADO ====") 
    print("=========================\n")
    myquery = { "nome": {"$regex": name}}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def update(codigo):
    mydb = config.connect()
    mycol = mydb.Produto
    myquery = { "codigo": codigo }

    print("\n============================")
    print("==== EDITAR ====") 
    print("==== 1 - NOME ====")
    print("==== 2 - PREÇO ====")
    print("==== 3 - AMBOS ====")
    print("============================\n")
    select = input('Selecione uma opção:')
    if(select == '1'):
        newName = input('Novo nome: ')
        newvalues = { "$set":   { "nome": newName } }
        print("Nome editado com sucesso!")
    elif(select == '2'):
        newPrice = input('Novo preço: ')
        newvalues = { "$set":   { "nome": newPrice } }
        print("Preço editado com sucesso!")
    elif(select == '3'):
        newName = input('Novo nome: ')
        newPrice = input('Novo preço: ')
        newvalues = { "$set":   { "nome": newName, "preco": newPrice } }
        print("Dados editados com sucesso!")
    else:
        print("Opção não entendida!")

    mycol.update_one(myquery, newvalues)

def delete(codigo):
    mydb = config.connect()
    mycol = mydb.Usuario
    print("\n==========================")
    print("==== PRODUTO DELETADO ====") 
    print("==========================\n")
    myquery = { "codigo": codigo }
    mycol.delete_one(myquery)
    print("Produto deletado com sucesso.")

def insert(codigo, nome, preco, vendedor):
    mydb = config.connect()
    columnVendedores = mydb.Vendedor
    columnProdutos = mydb.Produto
    myquery = { "nome": vendedor }
    findVendedor = columnVendedores.find(myquery)
    createDict = {}
    for fornecedor in findVendedor:
        createDict.update(fornecedor)
    if not createDict:
        print("Vendedor não existe, por favor selecione um existente")
    else:
        novoProduto = {
            "codigo": codigo,
            "nome": nome,
            "preco": preco,
            "vendedor": createDict
        }
        insert = columnProdutos.insert_one(novoProduto)
        print("Produto Inserido com ID: ", insert.inserted_id)
