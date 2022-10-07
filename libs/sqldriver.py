import sqlite3 as sql

if __name__ == '__main__':
    print('No se puede ejecutar directamente.')
else:
    def createDB(name):
        conn = sql.connect(name)
        conn.commit()
        conn.close()
    
    def createTable(bd, name):
        conn = sql.connect(bd)
        cursor = conn.cursor()
        cursor.execute(f"""CREATE TABLE '{name}' (
            mensaje text,
            tiempo text
        )""")
        conn.commit()
        conn.close()
        
    def itemIns(bd, table, mensaje, tiempo):
        try:
            conn = sql.connect(bd)
            cursor = conn.cursor()
            consulta = f"INSERT INTO '{table}' VALUES ('{mensaje}', '{tiempo}')"
            cursor.execute(consulta)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            

    def itemS_all(bd, table):
        conn = sql.connect(bd)
        cursor = conn.cursor()
        consulta = f"SELECT * FROM '{table}'"

        cursor.execute(consulta)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return datos

        
    
    def makeDB():
        createDB('tracker.db')
        createTable('tracker.db', 'tracking_lugar')

            