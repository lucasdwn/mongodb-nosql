import config as config

def findSort():
    mydb = config.connect()
    mycol = mydb.Vendedor
    print("\n===========================")
    print("==== TODOS OS VENDEDORES ====") 
    print("===========================\n")
    mydoc = mycol.find({}, {
        "_id": 0,
        "nome": 1,
        "cpf": 1
    }).sort("nome")
    for x in mydoc:
        print(x)

def findQuery(name):
    mydb = config.connect()
    mycol = mydb.Vendedor
    print("\n=========================")
    print("==== VENDEDOR BUSCADO ====") 
    print("=========================\n")
    myquery = { "nome": name }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def update(cnpj, newName):
    mydb = config.connect()
    mycol = mydb.Vendedor
    print("\n============================")
    print("==== VENDEDOR ATUALIZADO ====") 
    print("============================\n")
    myquery = { "cnpj": cnpj }
    newvalues = { "$set":   { "nome": newName } }
    mycol.update_one(myquery, newvalues)
    print("Vendedor atualizado com sucesso.")

def delete(cnpj):
    mydb = config.connect()
    mycol = mydb.Vendedor
    print("\n==========================")
    print("==== VENDEDOR DELETADO ====") 
    print("==========================\n")
    myquery = { "cnpj": cnpj }
    mycol.delete_one(myquery)
    print("Vendedor deletado com sucesso.")

def insert(name, cnpj):
    mydb = config.connect()
    mycol = mydb.Vendedor
    print("\n=========================")
    print("=== VENDEDOR INSERIDO ===") 
    print("=========================\n")
    mydict = { "nome": name, "cnpj": cnpj }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    print("Vendedor cadastrado com sucesso.")