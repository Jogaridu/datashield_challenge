# Site com o conteúdo: https: //code.tutsplus.com/pt/tutorials/introduction-to-machine-learning-in-python--cms-30623

from sklearn import tree #importa o módulo "tree"' do Sklearn Árvore de Decisão

# Régua para uso de dados (labels)
# MAX_HANDLE_COUNT = 1000
# MAX_PAGE_FAULTS = 52000
# MAX_PAGE_FILE_USAGE = 90000
# MAX_PEAK_PAGE_FILE_USAGE = 110000
# MAX_WORKING_SET_SIZE = 105243072
# MAX_THREAD_COUNT = 35
# MAX_PRIORITY = 12
# MAX_PRIVATE_PAGE_COUNT = 70000000
# processos seguros sao representados por 0, enquanto uma ameaca por 1
# Convertendo os dados JSON em um formato adequado para scikit-learn

classif = tree.DecisionTreeClassifier() #Classificador

classif.fit (features, labels)

#funcao de analise dos dados
MHC = float(input("digite o valor: "))
MPF = float(input("digite o valor: "))
MPFU = float(input("digite o valor: "))
MPPFU = float(input("digite o valor: "))
MWSS = float(input("digite o valor: "))
MTC = float(input("digite o valor: "))
MP = float(input("digite o valor: "))
MPPC = float(input("digite o valor: "))

media = classif.predict ([[MHC,MPF, MPFU, MPPFU, MWSS, MTC, MP, MPPC]])

#decisao se é seguro ou ameaca
if media == 0:

    print("processo é seguro")
else:
    print("ameaca detectada, fechando processo!")