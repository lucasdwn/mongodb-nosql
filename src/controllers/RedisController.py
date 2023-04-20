import config as config
import json
import controllers.ProdutoController as produtoController

# REDIS

def listProdutos():
    mydbRedis= config.connectRedis()
    produtos = mydbRedis.hgetall('produtos')
    print("\n===========================")
    print("==== TODOS OS PRODUTOS ====") 
    print("===========================\n")
    print(produtos)

def importProduto():
    mydbRedis= config.connectRedis()
    produtoController.findSort()
    alvo = input("Digite o codigo do produto que deseja importar: ")
    produto = json.dumps(findProduto(alvo))
    mydbRedis.hset('produtos', alvo, produto)
    print('Produto inserido com sucesso!')

def updateProduto():
    mydbRedis= config.connectRedis()
    #
    print("\n===========================")
    print("==== PRODUTOS ====") 
    print("===========================\n")
    print(mydbRedis.hgetall('produtos'))
    #
    print('Qual produto deseja editar?')
    codigo = input('código do produto: ')
    newName= input("Novo nome: ")
    newPrice= input("Novo preço: ")
    #
    produto = {"codigo": f"{codigo}", "nome": newName, "preco": newPrice}
    mydbRedis.hset('produtos', codigo, json.dumps(produto))
    #
    print("Produto editado com sucesso!")

def exportProduto():
    mydbRedis= config.connectRedis()
    #
    print("\n===========================")
    print("==== PRODUTOS ====") 
    print("===========================\n")
    print(mydbRedis.hgetall('produtos'))
    #
    codigo = input('código do produto: ')
    produto = mydbRedis.hget('produtos', codigo)
    updateProdutoMongo(codigo, produto.decode())

def deleteProduto():
    mydbRedis= config.connectRedis()
    print("\n===========================")
    print("==== DELETAR PRODUTO ====") 
    print("===========================\n")
    codigo = input('código do produto: ')
    res = mydbRedis.hdel('produtos', codigo)
    if(res == 1):
        print("Produto deletado com sucesso!")
    elif(res == 0):
        print("Produto não foi deletado!")

# MONGODB

def findProduto(codigo):
    mydbMongo = config.connect()
    mycol = mydbMongo.Produto
    myquery = { "codigo": codigo }
    mydoc = mycol.find(myquery, {
        "_id": 0,
        "codigo": 1,
        "nome": 1,
        "preco": 1
    })
    myDict = {}
    for produto in mydoc:
        myDict.update(produto)
    return myDict

def updateProdutoMongo(codigo, produto):
    mydb = config.connect()
    mycol = mydb.Produto
    dictProd = json.loads(produto)
    newvalues = { "$set":   { "nome": dictProd["nome"], "preco": dictProd["preco"] } }
    myquery = { "codigo": codigo }
    mycol.update_one(myquery, newvalues)
    print("Produto exportado para o MongoDB com sucesso!")

# TESTES

def listKeys():
    mydbRedis= config.connectRedis()
    # print(mydb.get('user:name').decode())
    print(mydbRedis.keys())
