import sqlite3


class TasksDB:
    def __init__(self):
        self.connect = sqlite3.connect("../database.db")
        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            timer INTEGER
        )""")
        self.connect.commit()

    def insert_table(self, name, description):
        timer = 0
        self.cursor.execute("""INSERT INTO tasks (name, description, timer) VALUES (?, ?, ?)""", [name, description, timer])
        self.connect.commit()

    def select_table(self):
        self.cursor.execute("SELECT * FROM tasks")

        return self.cursor.fetchall()

    def selectById_table(self, id):
        self.cursor.execute("SELECT * FROM tasks WHERE id = ?", [id])

        return self.cursor.fetchone()

    def updateTime_table(self, id, time):
        self.cursor.execute("UPDATE tasks SET timer = ? WHERE id = ?", [time, id])
        self.connect.commit()

    def update_table(self, id, name, description):
        self.cursor.execute("UPDATE tasks SET name = ?, description = ? WHERE id = ?", [name, description, id])
        self.connect.commit()

    def deleteTask_table(self, id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", [id])
        self.connect.commit()

    def delete_table(self):
        self.cursor.execute("DELETE * FROM tasks")
        self.connect.commit()

    def drop_table(self):
        self.cursor.execute("DROP TABLE tasks")
        self.connect.commit()

    def close_table(self):
        self.connect.close()

    def fill_table(self, lenght):
        for i in range(lenght):
            self.insert_table(name = str(lenght) + "name", description = lenght)