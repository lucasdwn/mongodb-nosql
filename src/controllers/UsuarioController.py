import config as config

def findSort():
    mydb = config.connect()
    mycol = mydb.Usuario
    print("\n===========================")
    print("==== TODOS OS USUARIOS ====") 
    print("===========================\n")
    mydoc = mycol.find({}, {
        "_id": 0,
        "nome": 1,
        "email": 1,
        "Compra": 1,
        "Favorito": 1
    }).sort("nome")
    for x in mydoc:
        print(x)

def findQuery(name):
    mydb = config.connect()
    mycol = mydb.Usuario
    print("\n=========================")
    print("==== USUARIO BUSCADO ====") 
    print("=========================\n")
    myquery = { "nome": name }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def update(email, newName):
    mydb = config.connect()
    mycol = mydb.Usuario
    print("\n============================")
    print("==== USUARIO ATUALIZADO ====") 
    print("============================\n")
    myquery = { "email": email }
    newvalues = { "$set":   { "nome": newName } }
    mycol.update_one(myquery, newvalues)
    print("Usuario atualizado com sucesso.")

def delete(email):
    mydb = config.connect()
    mycol = mydb.Usuario
    print("\n==========================")
    print("==== USUARIO DELETADO ====") 
    print("==========================\n")
    myquery = { "email": email }
    mycol.delete_one(myquery)
    print("Usuario deletado com sucesso.")

def insert(name, email):
    mydb = config.connect()
    mycol = mydb.Usuario
    print("\n=========================")
    print("=== USUARIO INSERIDO ===") 
    print("=========================\n")
    mydict = { "nome": name, "email": email }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    print("Usuario cadastrado com sucesso.")

def insertFavoritos(nomeProduto, emailUsuario):
    mydb = config.connect()
    columnUsuarios = mydb.Usuario
    columnProdutos = mydb.Produto
    myqueryUsers = { "email": emailUsuario }
    myqueryProdutos = { "nome": nomeProduto }
    findUsuario = columnUsuarios.find(myqueryUsers)
    findProduto = columnProdutos.find(myqueryProdutos)
    createDictUser = {}
    createDictProduto = {}

    for usuario in findUsuario:
        createDictUser.update(usuario)
    
    for produto in findProduto:
        createDictProduto.update(produto)

    if not createDictUser or not createDictProduto:
        print("Usuario ou Produto não existe, por favor coloque um existente")
    else:
    
        newvalues = { "$addToSet":   { "Favorito": produto } }
        update = columnUsuarios.update_one(myqueryUsers, newvalues)
        print("Favorito inserido no usuario com sucesso!")
        