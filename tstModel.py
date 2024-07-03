from model.model import Model

myModel = Model()

myModel.crea_grafo()

archi = myModel.get_all_edges()

print(archi.values())
