# imports
import os, sys

sys.path.append(os.path.dirname(__file__)[0:-10])

from interface import menu
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication([])
    window = menu.Menu()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
