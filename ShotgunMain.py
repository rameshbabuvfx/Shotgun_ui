'''
SCRIPT AUTHOR : RAMESHKANNA
'''
try:
    from PySide2.QtWidgets import *
except:
    from pySide.QtWidgets import *
from ShotgunUI import UiMainWindow
import sys
import subprocess


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()
        self.Project1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.Project2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.Project3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.Project4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.Project5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.Project6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_4))
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_3))
        self.pushButton_4.clicked.connect(self.nukeApp)
        self.pushButton_7.clicked.connect(self.mayaApp)

    @staticmethod
    def nukeApp():
        cmd = r"C:\Program Files\Nuke12.2v2\./Nuke12.2 --nukex"
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        process.communicate()

    @staticmethod
    def mayaApp():
        cmd = r"C:\Program Files\Autodesk\Maya2018\bin\maya.exe"
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        process.communicate()


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec_())
