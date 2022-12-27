import config as config

def findSort():
    mydb = config.connect()
    mycol = mydb.Produto
    print("\n===========================")
    print("==== TODOS OS PRODUTOS ====") 
    print("===========================\n")
    mydoc = mycol.find({}, {
        "_id": 0,
        "nome": 1,
        "preco": 1,
        "vendedor": 1
    }).sort("nome")
    for x in mydoc:
        print(x)

def findQuery(name):
    mydb = config.connect()
    mycol = mydb.Produto
    print("\n=========================")
    print("==== PRODUTO BUSCADO ====") 
    print("=========================\n")
    myquery = { "nome": name }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def update(name, newPrice):
    mydb = config.connect()
    mycol = mydb.Produto
    print("\n============================")
    print("==== PRODUTO ATUALIZADO ====") 
    print("============================\n")
    myquery = { "nome": name }
    newvalues = { "$set":   { "preco": newPrice } }
    mycol.update_one(myquery, newvalues)
    print("Produto atualizado com sucesso.")

def delete(nome):
    mydb = config.connect()
    mycol = mydb.Usuario
    print("\n==========================")
    print("==== PRODUTO DELETADO ====") 
    print("==========================\n")
    myquery = { "nome": nome }
    mycol.delete_one(myquery)
    print("Produto deletado com sucesso.")

def insert(nome, preco, vendedor):
    mydb = config.connect()
    columnVendedores = mydb.Vendedor
    columnProdutos = mydb.Produto
    myquery = { "nome": vendedor }
    findVendedor = columnVendedores.find(myquery)
    createDict = {}
    for fornecedor in findVendedor:
        createDict.update(fornecedor)
    if not createDict:
        print("Vendedor não existe, por favor coloque um existente")
    else:
        novoProduto = {
            "nome": nome,
            "preco": preco,
            "vendedor": createDict
        }
        insert = columnProdutos.insert_one(novoProduto)
        print("Produto Inserido com ID: ", insert.inserted_id)
