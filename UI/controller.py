import flet as ft
from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        self._view._txt_result.controls.clear()
        self._model.crea_grafo()
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.get_num_nodes()} aeroporti"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.get_num_edges()} connessioni\n"))
        self._view.update_page()

        distanza = self._view._txtIn.value

        try:
            dist = float(distanza)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Devi inserire un valore numerico"))
            self._view.update_page()
            return

        archi = DAO.get_all_connessioni(self._model._idMap)

        cont = 0
        list = []
        for e in archi:
            if e.peso >= dist:
                cont = cont + 1
                list.append(e)

        if cont == 0:
            self._view._txt_result.controls.append(ft.Text(f"Non ci sono aeroporti con distanza uguale o "
                                                           f"superiore a {dist} km!"))
        elif cont == 1:
            self._view._txt_result.controls.append(ft.Text(f"C'è solo un areoporto con distanza uguale o "
                                                           f"superiore a {dist} km!"))
        else:
            self._view._txt_result.controls.append(ft.Text(f"Gli aeroporti con distanza uguale o superiore"
                                                           f" a {dist} km sono {cont}:"))

        for i in list:
            self._view._txt_result.controls.append(ft.Text(f"La distanza tra {i.v1.IATA_CODE} "
                                                           f"e {i.v2.IATA_CODE} è di {i.peso.__round__(0)} km"))

        self._view.update_page()
