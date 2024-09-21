import mysql.connector


class Database:
    pass


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tugas_akhir",
)
