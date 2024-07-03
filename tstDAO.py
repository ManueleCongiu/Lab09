from database.DAO import DAO
from model.model import Model

res = DAO.get_all_airports()
model = Model()

conn = DAO.get_all_connessioni(model._idMap)

print(len(res))
print(conn[0])
