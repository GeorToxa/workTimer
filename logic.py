# imports
import database

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QHBoxLayout

# Logic class
class Logic:
    db = database.TasksDB()
    def loadList(self, window, vbox, data):
        from interface.timer import TimerTask
        from interface.editTask import EditTask

        for i in range(len(data)):
            numberLbl = QLabel()
            numberLbl.setText(str(data[i][0]))
            numberLbl.setMaximumHeight(30)
            numberLbl.setMinimumHeight(30)
            nameLine = QLineEdit(data[i][1])
            nameLine.setMaximumHeight(30)
            nameLine.setMinimumHeight(30)
            nameLine.setDisabled(True)
            descriptionLine = QLineEdit()
            descriptionLine.setMaximumHeight(30)
            descriptionLine.setMinimumHeight(30)
            descriptionLine.setMinimumWidth(180)
            descriptionLine.setMinimumWidth(180)
            descriptionLine.setDisabled(True)
            descriptionLine.setMaxLength(30)
            if len(data[i][2]) > 26:
                descriptionLine.setText(data[i][2][0:26] + "...")
            else:
                descriptionLine.setText(data[i][2][0:26])

            # Time
            time_in_seconds = data[i][3]
            hours, minutes, seconds = Logic.seconds_to_hms(time_in_seconds)
            timerLine = QLineEdit(f"{hours:02}:{minutes:02}:{seconds:02}")
            timerLine.setMaximumHeight(30)
            timerLine.setMinimumHeight(30)
            timerLine.setDisabled(True)
            editBtn = QPushButton("Edit")
            editBtn.setMaximumHeight(30)
            editBtn.setMinimumHeight(30)
            editBtn.clicked.connect(lambda _, index=i: Logic.moveToAnotherWindow(window, EditTask(data[index][0])))
            timerBtn = QPushButton("Timer")
            timerBtn.setMaximumHeight(30)
            timerBtn.setMinimumHeight(30)
            timerBtn.clicked.connect(lambda _, index=i: Logic.moveToAnotherWindow(window, TimerTask(data[index][0])))

            hbox = QHBoxLayout()
            hbox.addWidget(numberLbl)
            hbox.addWidget(nameLine)
            hbox.addWidget(descriptionLine)
            hbox.addWidget(timerLine)
            hbox.addWidget(editBtn)
            hbox.addWidget(timerBtn)

            vbox.addLayout(hbox)

        return vbox

    # Start timer
    @staticmethod
    def start_timer(time):
        if not time.isActive():
            time.start(1000)

    # Pause timer
    @staticmethod
    def pause_timer(time):
        if time.isActive():
            time.stop()

    # Called every second method for updating label and data in db
    def update_time(self, task_id, timerLbl):
        time_in_seconds = Logic.db.selectById_table(task_id)
        time_in_seconds = time_in_seconds[3]
        self.timerLbl = timerLbl
        time_in_seconds += 1
        hours, minutes, seconds = Logic.seconds_to_hms(time_in_seconds)
        self.timerLbl.setText(f'{hours:02}:{minutes:02}:{seconds:02}')
        Logic.saveTime(task_id, time_in_seconds)

    # Saving task time by adding him to db
    @staticmethod
    def saveTime(taskId, time_in_seconds):
        Logic.db.updateTime_table(id=taskId, time=time_in_seconds)

    # Second to hours:minutes:seconds
    @staticmethod
    def seconds_to_hms(seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return hours, minutes, seconds

    # Deleting task by deleting him from db
    def deleteTask(self, window, target_window, id):
        Logic.db.deleteTask_table(id)
        self.moveToAnotherWindow(window, target_window)

    # Saving task by adding him to db
    def updateTask(self, window, target_window, id, title, description):
        Logic.db.update_table(id, title, description)
        self.moveToAnotherWindow(window, target_window)

    # Saving task by adding him to db
    def saveTask(self, window, target_window, title, description):
        Logic.db.insert_table(title, description)
        self.moveToAnotherWindow(window, target_window)

    # Loading css styles
    @staticmethod
    def cssLoader():
        with open("../../styles/styles.css", "r", encoding="utf-8") as read:
            style = read.read()
            read.close()
        if style == "":
            with open("../styles/styles.css", "r", encoding="utf-8") as read:
                style = read.read()
                read.close()
        return style

    # Additional method for setting window icon
    def setWindowIcon_(self):
        try:
            from PyQt5.QtWinExtras import QtWin

            myappid = 'geortoxa.bigproject.workTimer.1'
            QtWin.setCurrentProcessExplicitAppUserModelID(myappid)

        except ImportError:
            pass

    # Settings windows
    @staticmethod
    def windowSettings(window, title):
        window.setWindowIcon(QtGui.QIcon("../timer.ico"))

        Logic.setWindowIcon_(window)
        window.setWindowTitle(title)
        window.setMinimumSize(700, 500)
        window.setStyleSheet(Logic.cssLoader())

    # Changing windows
    def moveToAnotherWindow(self, window, target_window):
        self.window = window
        self.target_window = target_window

        self.target_window.show()
        self.window.close()

