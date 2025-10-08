import sqlite3


class EntryRepository:
    def __init__(self):
        self.conn = sqlite3.connect('app/data/database.db')
        self.cursor = self.conn.cursor()
        stmt = """
        CREATE TABLE IF NOT EXISTS journal(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        time TEXT,
        entry TEXT
        )
        """
        self.conn.execute(stmt)
        self.conn.commit()
    
    def insertData(self, date: str, time: str, entry: str):
        self.cursor.execute("INSERT INTO journal(date, time, entry) VALUES(?, ?, ?)", (date, time, entry))
        self.conn.commit()
        
    def deleteData(self, id: int):
        self.cursor.execute("DELETE FROM journal WHERE id = ?", (id,))
        self.conn.commit()
        
    def readData(self) -> tuple:
        self.cursor.execute("SELECT * FROM journal")
        rows = self.cursor.fetchall()
        return rows
    

if __name__ == '__main__':
    s = EntryRepository()