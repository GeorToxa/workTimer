# imports
import os

os.chdir(os.path.dirname(__file__))

import database, logic

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer


class TimerTask(QWidget):
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

        # Timer
        self.time = QTimer()
        self.time_in_seconds = int(self.data[3])
        hours, minutes, seconds = self.logic.seconds_to_hms(self.time_in_seconds)


        self.logic.windowSettings(self, f"Timer: {self.data[1]}")  # Window settings


        # Widgets
        # Creating widgets
        self.taskNameLbl = QLabel("Task name: " + str(self.data[1]))
        self.timerLbl = QLabel(f'{hours:02}:{minutes:02}:{seconds:02}')
        self.startTimeBtn = QPushButton("Start timer")
        self.pauseTimeBtn = QPushButton("Pause timer")
        self.toMenuBtn = QPushButton("Menu")
        self.toTasksBtn = QPushButton("Tasks")

        # Settings
        self.taskNameLbl.setMinimumHeight(30)
        self.timerLbl.setMinimumHeight(30)
        self.startTimeBtn.setMinimumHeight(30)
        self.pauseTimeBtn.setMinimumHeight(30)
        self.toMenuBtn.setMinimumHeight(30)
        self.toTasksBtn.setMinimumHeight(30)

        # Layouts
        # Creating layouts
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hboxMain = QHBoxLayout()

        # Placement
        self.vbox.addWidget(self.taskNameLbl)
        self.vbox.addWidget(self.timerLbl)
        self.hbox1.addWidget(self.startTimeBtn)
        self.hbox1.addWidget(self.pauseTimeBtn)

        self.hbox2.addWidget(self.toMenuBtn)
        self.hbox2.addWidget(self.toTasksBtn)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)

        self.hboxMain.addLayout(self.vbox)

        self.setLayout(self.hboxMain)

        # Connect buttons with methods
        self.toMenuBtn.clicked.connect(lambda: self.logic.pause_timer(self.time))
        self.toMenuBtn.clicked.connect(lambda: self.logic.moveToAnotherWindow(self, Menu()))
        self.toTasksBtn.clicked.connect(lambda: self.logic.pause_timer(self.time))
        self.toTasksBtn.clicked.connect(lambda: self.logic.moveToAnotherWindow(self, TasksList()))
        self.startTimeBtn.clicked.connect(lambda: self.logic.start_timer(self.time))
        self.pauseTimeBtn.clicked.connect(lambda: self.logic.pause_timer(self.time))

        self.time.timeout.connect(lambda: self.logic.update_time(self.taskId, self.timerLbl))
