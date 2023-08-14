import pymongo

def instanciar_processos():
    client = pymongo.MongoClient("localhost", 27017)
    db = client["datashield_com_br"]
    colecao = db["processos"]
    return colecao


def instanciar_analise():
    client = pymongo.MongoClient("localhost", 27017)
    db = client["datashield_com_br"]
    colecao = db["analise"]
    return colecao
