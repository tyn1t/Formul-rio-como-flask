import sqlite3 as sql 

class Models:
    
    def __init__(self) -> None:
        self.conn = None
        self.cur = None
        
        
        
        
    def db(self):
        try:
            self.conn = sql.connect("Banco_dados.db")
            self.cur = self.conn.cursor()
            self.cur.execute('''CREATE TABLE IF NOT EXISTS Usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    idade TEXT, 
                    rua TEXT,
                    cidade TEXT,
                    numero TEXT,
                    estado TEXT, 
                    email TEXT)''')
            self.conn.commit()
            self.conn.close()
        except sql.OperationalError as err:
            print(err)
       
    def run(self):
        self.db()

dados = Models()
dados.run()