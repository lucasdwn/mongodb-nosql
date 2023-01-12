import config as config

def findSort():
    mydb = config.connect()
    mycol = mydb.Compra
    print("\n===========================")
    print("==== TODAS AS COMPRAS ====") 
    print("===========================\n")
    mydoc = mycol.find().sort("_id")
    for x in mydoc:
        print(x)

def findQuery(id):
    mydb = config.connect()
    mycol = mydb.Compra
    print("\n=========================")
    print("==== COMPRA BUSCADA ====") 
    print("=========================\n")
    myquery = { "_id": id }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def delete(id):
    mydb = config.connect()
    mycol = mydb.Compra
    print("\n==========================")
    print("==== COMPRA DELETADA ====") 
    print("==========================\n")
    myquery = { "_id": id }
    mycol.delete_one(myquery)
    print("Compra deletada com sucesso.")

def insert(nomeProduto, emailUsuario):
    mydb = config.connect()
    columnUsuarios = mydb.Usuario
    columnProdutos = mydb.Produto
    columnCompras = mydb.Compra
    myqueryUsers = { "email": emailUsuario }
    myqueryProdutos = { "nome": nomeProduto }
    findUsuario = columnUsuarios.find(myqueryUsers)
    findProduto = columnProdutos.find(myqueryProdutos)
    createDictUser = {}
    createDictProduto = {}
    for comprador in findUsuario:
        createDictUser.update(comprador)
    
    for produto in findProduto:
        createDictProduto.update(produto)

    if not createDictUser or not createDictProduto:
        print("Usuario ou Produto não existe, por favor coloque um existente")
    else:
        novaCompra = {
            "Usuario": createDictUser,
            "Produto": createDictProduto
        }
        
        insert = columnCompras.insert_one(novaCompra)
        
        print("Compra Inserido com ID: ", insert.inserted_id)
       
        myqueryCompra = {"_id" : insert.inserted_id}
        findCompra = columnCompras.find(myqueryCompra)

        createDictCompra = {}

        for compra in findCompra:
            createDictCompra.update(compra)

        newvalues = { "$addToSet":   { "Compra": createDictCompra } }
        update = columnUsuarios.update_one(myqueryUsers, newvalues)
        print("Compra inserida no usuario com sucesso!")
