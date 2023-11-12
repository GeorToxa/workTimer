# imports
import os

os.chdir(os.path.dirname(__file__))

import database, logic

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QTextEdit, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QScrollArea
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui


class EditTask(QWidget):
    def __init__(self, id):
        super().__init__()

        self.taskId = id

        # Interface imports
        from interface.menu import Menu
        from interface.tasksList import TasksList

        # Class instance
        self.logic = logic.Logic()
        self.db = database.TasksDB()

        # Select data from db
        self.data = self.db.selectById_table(str(self.taskId))

        self.logic.windowSettings(self, f"Editing: {self.data[1]}")  # Window settings


        # Time
        self.time_in_seconds = self.data[3]
        hours, minutes, seconds = self.logic.seconds_to_hms(self.time_in_seconds)


        # Widgets
        # Creating widgets
        self.nameLbl = QLabel("Task name:")
        self.nameLineEdit = QLineEdit(str(self.data[1]))
        self.descriptionLbl = QLabel("Task description:")
        self.descriptionTextEdit = QTextEdit(str(self.data[2]))
        self.timerLbl = QLabel("Task time:")
        self.timerLineEdit = QLineEdit(f"{hours:02}:{minutes:02}:{seconds:02}")
        self.toMenuBtn = QPushButton("Menu")
        self.toTasksBtn = QPushButton("Tasks")
        self.saveBtn = QPushButton("Save")
        self.deleteBtn = QPushButton("Delete")

        # Setting widgets
        self.timerLineEdit.setDisabled(True)
        self.nameLbl.setMinimumHeight(30)
        self.nameLineEdit.setMinimumHeight(30)
        self.descriptionLbl.setMinimumHeight(30)
        self.descriptionTextEdit.setMinimumHeight(30)
        self.timerLbl.setMinimumHeight(30)
        self.timerLineEdit.setMinimumHeight(30)
        self.toMenuBtn.setMinimumHeight(30)
        self.toTasksBtn.setMinimumHeight(30)
        self.saveBtn.setMinimumHeight(30)
        self.deleteBtn.setMinimumHeight(30)


        # Layouts
        # Creating layouts
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hboxMain = QHBoxLayout()

        # Placement
        self.vbox.addWidget(self.nameLbl)
        self.vbox.addWidget(self.nameLineEdit)
        self.vbox.addWidget(self.descriptionLbl)
        self.vbox.addWidget(self.descriptionTextEdit)
        self.vbox.addWidget(self.timerLbl)
        self.vbox.addWidget(self.timerLineEdit)

        self.hbox.addWidget(self.toMenuBtn)
        self.hbox.addWidget(self.toTasksBtn)
        self.hbox.addWidget(self.saveBtn)
        self.hbox.addWidget(self.deleteBtn)

        self.vbox.addLayout(self.hbox)

        self.hboxMain.addLayout(self.vbox)

        self.setLayout(self.hboxMain)


        # Connect buttons with methods
        self.toMenuBtn.clicked.connect(lambda: self.logic.moveToAnotherWindow(self, Menu()))
        self.toTasksBtn.clicked.connect(lambda: self.logic.moveToAnotherWindow(self, TasksList()))
        self.saveBtn.clicked.connect(lambda: self.logic.updateTask(self, Menu(), self.taskId, self.nameLineEdit.text(), self.descriptionTextEdit.toPlainText()))
        self.deleteBtn.clicked.connect(lambda: self.logic.deleteTask(self, Menu(), self.taskId))
