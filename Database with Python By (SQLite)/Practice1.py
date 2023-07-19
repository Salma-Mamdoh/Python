# Practice
import sqlite3
def get_all_data():
    try:
        db=sqlite3.connect("app.db")
        print("Connected Successfully")
        cr=db.cursor()
        cr.execute("SELECT * From users")
        results=cr.fetchall()
        print(f"DB has {len(results)} rows")
        print("showing Data : ")
        for i in results:
            print(f"UserID => {i[0]}",end=" ")
            print(f"Username =>{i[1]}")

    except sqlite3.Error as er:
        print(f"Faild connection {er}")
    finally:
        if (db):
            db.close()
            print("DB has closed ")

get_all_data()
