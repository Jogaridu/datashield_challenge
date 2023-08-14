import pymongo

uri = "localhost"
uri = "mongodb+srv://dtsld:ka7HwyA7bjsBSJki@cluster0.lr1zeas.mongodb.net/?retryWrites=true&w=majority"

def instanciar_processos():
    client = pymongo.MongoClient(uri, 27017)
    db = client["datashield_com_br"]
    colecao = db["processos"]
    return colecao


def instanciar_analise():
    client = pymongo.MongoClient(uri, 27017)
    db = client["datashield_com_br"]
    colecao = db["analise"]
    return colecao
