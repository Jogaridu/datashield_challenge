import pymongo
from urllib.parse import quote_plus

# REMOTO
username = quote_plus('dtsld')
password = quote_plus('ka7HwyA7bjsBSJki')
cluster = 'cluster0.lr1zeas.mongodb.net'
authSource = '<authSource>'
authMechanism = '<authMechanism>'
uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster
print(uri)

# LOCAL
uri = "localhost"

def instanciar_processos():
    client = pymongo.MongoClient(uri)
    db = client["datashield_com_br"]
    colecao = db["processos"]
    return colecao


def instanciar_analise():
    client = pymongo.MongoClient(uri, 27017)
    db = client["datashield_com_br"]
    colecao = db["analise"]
    return colecao






# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# uri = "mongodb+srv://dtsld:ka7HwyA7bjsBSJki@cluster0.lr1zeas.mongodb.net/?authMechanism=DEFAULT"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)