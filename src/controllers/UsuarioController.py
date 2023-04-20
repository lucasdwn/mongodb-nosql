import config as config
import json

def findSort():
    mydb = config.connect()
    mycol = mydb.Usuario
    print("\n===========================")
    print("==== TODOS OS USUARIOS ====") 
    print("===========================\n")
    mydoc = mycol.find({}, {
        "_id": 0,
        "nome": 1,
        "email": 1
    }).sort("nome")
    for x in mydoc:
        print("\n===========================")
        print(x)
        print("===========================\n")

def findQuery(name):
    mydb = config.connect()
    mycol = mydb.Usuario
    print("\n=========================")
    print("==== USUARIO BUSCADO ====") 
    print("=========================\n")
    myquery = { "nome": {"$regex": name} }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print("\n==========================")
        print(x)
        print("==========================\n")

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

def insertFavoritos(codigoProduto, emailUsuario):
    mydb = config.connect()
    columnUsuarios = mydb.Usuario
    columnProdutos = mydb.Produto
    myqueryUsers = { "email": emailUsuario }
    myqueryProdutos = { "codigo": codigoProduto }
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
        