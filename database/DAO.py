from database.DB_connect import DBConnect
from model.connessioni import Connessione
from model.airports import Airport


class DAO:

    @staticmethod
    def get_all_airports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * 
                   FROM airports a"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_connessioni(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT T1.ORIGIN_AIRPORT_ID as a1, T1.DESTINATION_AIRPORT_ID as a2, (COALESCE(T1.D, 0) + COALESCE(T2.D, 0))/(COALESCE(T1.N, 0) + COALESCE(T2.N, 0)) as peso
                   FROM
                   (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                   FROM flights f
                   GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T1
                   LEFT JOIN
                   (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                   FROM flights f
                   GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T2
                   ON T1.ORIGIN_AIRPORT_ID = T2.DESTINATION_AIRPORT_ID AND T2.ORIGIN_AIRPORT_ID = T1.DESTINATION_AIRPORT_ID
                   WHERE T1.ORIGIN_AIRPORT_ID < T2.ORIGIN_AIRPORT_ID OR T2.ORIGIN_AIRPORT_ID IS NULL OR T2.DESTINATION_AIRPORT_ID IS NULL"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(Connessione(idMap[row["a1"]],
                                      idMap[row["a2"]],
                                      row["peso"]))

        cursor.close()
        conn.close()
        return result
