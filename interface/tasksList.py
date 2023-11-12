# imports
import os

os.chdir(os.path.dirname(__file__))

import database, logic

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QTextEdit, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QScrollArea
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui


class TasksList(QWidget):
    def __init__(self):
        super().__init__()

        # Interface imports
        from interface.menu import Menu
        from interface.createTask import CreateTask
        from interface.timer import TimerTask
        from interface.editTask import EditTask

        # Class instance
        self.logic = logic.Logic()
        self.db = database.TasksDB()

        # Select data from db
        self.data = self.db.select_table()

        # Updating list
        # self.time = QTimer()

        self.logic.windowSettings(self, "Tasks list")  # Window settings


        # Layouts
        # Creating
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.vboxMain = QVBoxLayout()


        # Widgets
        # Creating widgets
        self.toMenuBtn = QPushButton("Menu")
        self.createTaskBtn = QPushButton("Create new task")

        # Settings
        self.toMenuBtn.setMinimumHeight(30)
        self.createTaskBtn.setMinimumHeight(30)

        # Creating task lists
        for i in range(len(self.data)):
            numberLbl = QLabel()
            numberLbl.setText(str(self.data[i][0]))
            numberLbl.setMinimumHeight(30)
            numberLbl.setMinimumWidth(25)
            nameLine = QLineEdit(self.data[i][1])
            nameLine.setMinimumHeight(30)
            nameLine.setDisabled(True)
            descriptionLine = QLineEdit()
            descriptionLine.setMinimumHeight(30)
            descriptionLine.setMinimumWidth(180)
            descriptionLine.setDisabled(True)
            descriptionLine.setMaxLength(30)
            if len(self.data[i][2]) > 26:
                descriptionLine.setText(self.data[i][2][0:26] + "...")
            else:
                descriptionLine.setText(self.data[i][2][0:26])

            # Time
            time_in_seconds = self.data[i][3]
            hours, minutes, seconds = self.logic.seconds_to_hms(time_in_seconds)

            timerLine = QLineEdit(f"{hours:02}:{minutes:02}:{seconds:02}")
            timerLine.setMinimumHeight(30)
            timerLine.setDisabled(True)
            editBtn = QPushButton("Edit")
            editBtn.setMinimumHeight(30)
            editBtn.setMinimumWidth(75)
            editBtn.clicked.connect(lambda _, index=i: self.logic.moveToAnotherWindow(self, EditTask(self.data[index][0])))
            timerBtn = QPushButton("Timer")
            timerBtn.setMinimumHeight(30)
            timerBtn.setMinimumWidth(75)
            timerBtn.clicked.connect(lambda _, index=i: self.logic.moveToAnotherWindow(self, TimerTask(self.data[index][0])))

            hbox = QHBoxLayout()
            hbox.addWidget(numberLbl)
            hbox.addWidget(nameLine)
            hbox.addWidget(descriptionLine)
            hbox.addWidget(timerLine)
            hbox.addWidget(editBtn)
            hbox.addWidget(timerBtn)

            self.vbox.addLayout(hbox)


        # Scroll area for tasks list
        self.content = QWidget()
        self.content.setLayout(self.vbox)
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.content)


        # Layouts
        # Placement
        self.hbox.addWidget(self.toMenuBtn)
        self.hbox.addWidget(self.createTaskBtn)
        self.vboxMain.addWidget(self.scrollArea)
        self.vboxMain.addLayout(self.hbox)
        self.setLayout(self.vboxMain)


        # Connecting buttons with methods
        self.toMenuBtn.clicked.connect(lambda: self.logic.moveToAnotherWindow(self, Menu()))
        self.createTaskBtn.clicked.connect(lambda: self.logic.moveToAnotherWindow(self, CreateTask()))

        # self.time.timeout.connect(lambda: self.logic.updateList(self.taskId))