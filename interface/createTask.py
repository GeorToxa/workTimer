# imports
import os

os.chdir(os.path.dirname(__file__))

import database, logic

from PyQt5.QtWidgets import QWidget, QLineEdit, QTextEdit, QPushButton, QLabel, QHBoxLayout, QVBoxLayout


class CreateTask(QWidget):
    def __init__(self):
        super().__init__()

        # Interface imports
        from interface.menu import Menu
        from interface.tasksList import TasksList

        # Class instance
        self.logic = logic.Logic()


        self.logic.windowSettings(self, "Create task")  # Window settings


        # Widgets
        # Creating
        self.taskNameLbl = QLabel("Title:")
        self.taskDescriptionLbl = QLabel("Description:")
        self.taskTimerLbl = QLabel("Time:")
        self.taskNameLineEdit = QLineEdit()
        self.taskTimerLineEdit = QLineEdit()
        self.taskDescriptionTextEdit = QTextEdit()
        self.toMenuBtn = QPushButton("Menu")
        self.toTasksBtn = QPushButton("Tasks")
        self.saveBtn = QPushButton("Save")

        # Settings
        self.taskNameLineEdit.setPlaceholderText("Title...")
        self.taskDescriptionTextEdit.setPlaceholderText("Description...")
        self.taskTimerLineEdit.setText("00:00:00")
        self.taskTimerLineEdit.setEnabled(False)
        self.taskNameLbl.setMinimumSize(50, 30)
        self.taskDescriptionLbl.setMinimumSize(50, 30)
        self.taskTimerLbl.setMinimumSize(50, 30)
        self.taskNameLineEdit.setMinimumSize(150, 30)
        self.taskTimerLineEdit.setMinimumSize(150, 30)
        self.taskDescriptionTextEdit.setMinimumSize(150, 200)
        self.toMenuBtn.setMinimumSize(50, 30)
        self.toTasksBtn.setMinimumSize(50, 30)
        self.saveBtn.setMinimumSize(50, 30)


        # Layouts
        # Creating
        self.hbox = QHBoxLayout()
        self.vboxMain = QVBoxLayout()

        # Placement
        self.vboxMain.addWidget(self.taskNameLbl)
        self.vboxMain.addWidget(self.taskNameLineEdit)
        self.vboxMain.addWidget(self.taskDescriptionLbl)
        self.vboxMain.addWidget(self.taskDescriptionTextEdit)
        self.vboxMain.addWidget(self.taskTimerLbl)
        self.vboxMain.addWidget(self.taskTimerLineEdit)

        self.hbox.addWidget(self.toMenuBtn)
        self.hbox.addWidget(self.toTasksBtn)
        self.hbox.addWidget(self.saveBtn)

        self.vboxMain.addLayout(self.hbox)

        self.setLayout(self.vboxMain)

        # Connecting buttons with methods
        self.toMenuBtn.clicked.connect(lambda: self.logic.moveToAnotherWindow(self, Menu()))
        self.toTasksBtn.clicked.connect(lambda: self.logic.moveToAnotherWindow(self, TasksList()))
        self.saveBtn.clicked.connect(lambda: self.logic.saveTask(self, Menu(), self.taskNameLineEdit.text(), self.taskDescriptionTextEdit.toPlainText()))