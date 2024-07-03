import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._airports_list = DAO.get_all_airports()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._airports_list)
        self._idMap = {}
        for v in self._airports_list:
            self._idMap[v.ID] = v

    def crea_grafo(self):
        self._grafo.clear()
        self._grafo.clear_edges()

        all_edges = DAO.get_all_connessioni(self._idMap)
        for edge in all_edges:
            self._grafo.add_edge(edge.v1, edge.v2, weight=edge.peso)

    def get_all_edges(self):
        return self._grafo.edges

    def get_num_nodes(self):
        return len(self._grafo.nodes)

    def get_num_edges(self):
        return len(self._grafo.edges)



'''

Input di una distanza media.
Grafo semplice, non orientato e pesato.
Gli archi devono indicare le rotte tra gli aeroporti collegati
tra di loro da almeno un volo. Il peso dell’arco rappresenta la
distanza media percorsa tra i due aeroporti.
idMap nella query

'''