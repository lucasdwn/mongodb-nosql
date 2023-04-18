import config as config
import controllers.ProdutoController as produtoController

def importProduto():
    mydbRedis= config.connectRedis()
    produtoController.findSort()
    alvo = input("Digite o nome do produto que deseja importar: ")
   

def getUserName():
    mydb= config.connectRedis()
    print(mydb.get('user:name'))

