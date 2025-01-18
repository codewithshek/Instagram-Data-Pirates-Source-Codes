from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
import requests
from bs4 import BeautifulSoup
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(547, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 331, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 491, 61))
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 491, 71))
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setText("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.get_score(MainWindow)
        # call the get_score() function
        # after every 1000 milliseconds
        # to update score labels
        timer = QtCore.QTimer(MainWindow)
        timer.timeout.connect(lambda:self.get_score(MainWindow))
        timer.start(1000)       
    def get_score(self, MainWindow):
        # cricbuzz url to get score updates
        url="https://www.cricbuzz.com/"
        # request data from cricbuzz
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        # name of first team
        team_1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
        # name of second team
        team_2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
        # scores of first team
        team_1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
        # scores of second team
        team_2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()
        # set the team names to label_2
        self.label_2.setText(f"{team_1}\t\t{team_2}")
        # set the team scores to label_3
        self.label_3.setText(f"{team_1_score}\t{team_2_score}")
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Indian Premier League"))
        self.label.setText("IPL 2022")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())