from app.config.database import connection as con
from app.models.about import About 


class Home:
    def get_data(pertama, kedua):
        try:
            cur = con.cursor()
            cur.execute("SELECT * FROM schedules")
            myresult = cur.fetchall()
            con.commit()
            cur.close()
            res = []
            for i in myresult:
                res.append(
                    {
                        "id": i[0],
                        "waktu_penebaran": str(i[1]),
                        "k1": pertama,
                        "k2": kedua,
                        "m3": About.contoh(),
                    }
                )
            return res
        except:
            return "no"
