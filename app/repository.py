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
    
    def insertData(self, id: int, date: str, time: str, entry: str):
        self.cursor.execute("INSERT INTO journal(id, date, time, entry) VALUES(?, ?, ?, ?)", (id, date, time, entry))
        self.conn.commit()
        
    def appendData(self, id: int, entry: str):
        self.cursor.execute("UPDATE journal SET entry = entry || ? WHERE id = ?", (entry, id))
        self.conn.commit()
        
    def deleteData(self, id: int):
        self.cursor.execute("DELETE FROM journal WHERE id = ?", (id,))
        self.conn.commit()
        
    def readData(self) -> tuple:
        self.cursor.execute("SELECT * FROM journal")
        rows = self.cursor.fetchall()
        return rows
    
    def findMatch(self, id: int) -> bool:
        self.cursor.execute("SELECT * FROM journal WHERE id = ?", (id,))
        match = self.cursor.fetchall()
        if len(match) > 0:
            return True
        else:
            return False

if __name__ == '__main__':
    s = EntryRepository()
    