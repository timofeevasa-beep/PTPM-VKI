import sqlite3


class TriangleDB:
    def __init__(self, db_name="triangle.db"):
        self.conn = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS triangles (
                side1 REAL, side2 REAL, side3 REAL,
                type TEXT, error TEXT,
                PRIMARY KEY (side1, side2, side3)
            )
        ''')
        self.conn.commit()

    def add(self, s1, s2, s3, t_type, error):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO triangles (side1, side2, side3, type, error)
            VALUES (?, ?, ?, ?, ?)
        ''', (s1, s2, s3, t_type, error))
        self.conn.commit()

    def get(self, s1, s2, s3):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT type, error FROM triangles 
            WHERE side1=? AND side2=? AND side3=?
        ''', (s1, s2, s3))
        return cursor.fetchone()

    def delete(self, s1, s2, s3):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM triangles WHERE side1=? AND side2=? AND side3=?', (s1, s2, s3))
        self.conn.commit()

    def close(self):
        self.conn.close()