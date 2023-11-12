# imports
import os

os.chdir(os.path.dirname(__file__))

import database, logic

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout


# Menu window class
class Menu(QWidget):
    def __init__(self):
        super().__init__()

        # Interface imports
        from interface.createTask import CreateTask
        from interface.tasksList import TasksList

        # Class instance
        self.logic = logic.Logic()
        self.db = database.TasksDB()

        # Init db and tables
        # self.db.drop_table()
        # self.db.delete_table()
        self.db.create_table()
        # self.db.fill_table(100)


        self.logic.windowSettings(self, "Menu")    # Window settings


        # Widgets
        # Creating
        self.tasksBtn = QPushButton("Tasks list")
        self.createBtn = QPushButton("Create")

        # Settings
        self.tasksBtn.setMinimumSize(50, 30)
        self.createBtn.setMinimumSize(50, 30)


        # Layouts
        # Creating
        self.hbox = QHBoxLayout()
        self.vboxMain = QVBoxLayout()

        # Placement
        self.hbox.addWidget(self.tasksBtn)
        self.hbox.addWidget(self.createBtn)
        self.vboxMain.addLayout(self.hbox)

        self.setLayout(self.vboxMain)


        # Connecting buttons with methods
        self.tasksBtn.clicked.connect(lambda: self.logic.moveToAnotherWindow(self, TasksList()))
        self.createBtn.clicked.connect(lambda: self.logic.moveToAnotherWindow(self, CreateTask()))

