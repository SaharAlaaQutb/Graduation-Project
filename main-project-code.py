from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.uic import loadUiType
import sys
import threading
import sqlite3
from datetime import date
import smtplib, ssl
import pdfkit
from os import path







class application_data:

    def __init__(self):

        self.connection_closed = True
        self.cur = None
        self.rows = []

    def open_connection(self):

        if self.connection_closed is True:
            self.sql_connection = sqlite3.connect(
                r"project database.db")
        self.connection_closed = False

    def close_connection(self):

        if self.connection_closed is False:
            self.sql_connection.close()
        self.connection_closed = True

    def select_data(self, sql_statement, sql_parameters):

        self.cur = self.sql_connection.cursor()
        if len(sql_parameters) == 0:
            self.rows = self.cur.execute(sql_statement).fetchall()
        else:
            self.rows = self.cur.execute(sql_statement, sql_parameters).fetchall()
        return self.rows

    def execute_command(self, sql_statement, sql_parameters):

        self.cur = self.sql_connection.cursor()
        if len(sql_parameters) == 0:
            self.cur.execute(sql_statement)
        else:
            self.cur.execute(sql_statement, sql_parameters)
        return self.cur.lastrowid


dal = application_data()


def login(position, email, password):

    parameters = [position, email, password]
    sql_statement = "SELECT* FROM Employee WHERE Position=? AND Email=? AND Password=?"

    dal.open_connection()
    rows = dal.select_data(sql_statement, parameters)
    dal.close_connection()

    if len(rows) == 0:
        return [False, rows]

    return [True, rows]




design , _= loadUiType(path.join(path.dirname(__file__),'project(main).ui'))

class window(QMainWindow , design):
    position = str()
    email = str()
    password = str()
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.openWelcomePage()
        self.handleButtons()
        self.handleMainWindow()

    def handleButtons(self):
        self.objectivesLogoutButton.clicked.connect(self.openLoginPage)
        self.loginButton.clicked.connect(self.get_text)
        self.topManagerSetObjectivesButton.clicked.connect(self.openTopManagerSetObjectivesPage)
        self.topManagerViewGoalsButton.clicked.connect(self.openViewGoalsPage)
        self.topManagerViewActionPlanButton.clicked.connect(self.openViewActionPlanPage)
        self.topManagerEvaluationButton.clicked.connect(self.openTopManagerEvaluationPage)
        self.topManagerMiddleManagerEvaluationButton.clicked.connect(self.openTopManagerManagerEvaluationPage)
        self.topManagerHistoryButton.clicked.connect(self.openTopManagerHistoryPage)
        self.middleManagerViewObjectivesButton.clicked.connect(self.openViewObjectivesPage)
        self.middleManagerSetGoalsButton.clicked.connect(self.openMiddleManagerSetGoalsPage)
        self.middleManagerViewActionPlanButton.clicked.connect(self.openViewActionPlanPage)
        self.middleManagerEvaluationButton.clicked.connect(self.openMiddleManagerEvaluationPage)
        self.middleManagerEmployeeEvaluationButton.clicked.connect(self.openMiddleManagerEmployeeEvaluationPage)
        self.middleManagerPreviousReportButton.clicked.connect(self.openMiddleManagerPreviousEvaluationPage)
        self.middleManagerHistoryButton.clicked.connect(self.openMiddleManagerHistoryPage)
        self.employeeViewObjectivesButton.clicked.connect(self.openViewObjectivesPage)
        self.employeeViewGoalsButton.clicked.connect(self.openViewGoalsPage)
        self.employeeSetActionPlanButton.clicked.connect(self.openEmployeeSetActionPlanPage)
        self.employeeEvaluationButton.clicked.connect(self.openEmployeeEvaluationPage)
        self.employeePreviousReportButton.clicked.connect(self.openEmployeePreviousEvaluationPage)
        self.employeeHistoryButton.clicked.connect(self.openEmployeeHistoryPage)
        self.objectivesHomeButton.clicked.connect(self.openHomeBar)
        self.objectivesEvaluationButton.clicked.connect(self.openEvaluationBar)
        self.objectivesButton.clicked.connect(self.openTopManagerSetObjectivesPage)
        self.objectivesGoalsButton.clicked.connect(self.openMiddleManagerSetGoalsPage)
        self.objectivesActionPlanButton.clicked.connect(self.openEmployeeSetActionPlanPage)





    def handleMainWindow(self):
        self.setWindowTitle('Performance management')
        self.setWindowIcon(QIcon('team (1).png'))


    def openWelcomePage(self):
        self.screens.setCurrentIndex(0)
        self.objectivesLeftFrame.hide()
        self.objectivesUpFrame.hide()
        t = threading.Timer(3 , self.openLoginPage)
        t.start()
    def openLoginPage(self):
        self.setWindowTitle('Performance management - Login')
        self.screens.setCurrentIndex(1)
        self.objectivesLeftFrame.hide()
        self.objectivesUpFrame.hide()
        position_list = [self.tr('Top Manager'), self.tr('Middle Manager'), self.tr('Employee')]
        self.positionList.clear()
        self.positionList.addItems(position_list)
    def get_text(self):
        self.position = str(self.positionList.currentText())
        self.email = str(self.loginEmailInput.text())
        self.password = str(self.loginPasswordInput.text())
        login_result = login(self.position , self.email , self.password)
        if login_result[0] == True:
            self.objectivesNameInput.setText(login_result[1][0])
            self.objectivesPositionInput.setText(login_result[1][2])
            self.objectivesEmailInput.setText(login_result[1][3])
            self.objectivesDepartmentInput.setText(login_result[1][4])
            if self.position == 'Top Manager':
                self.openTopManagerHomePage()
            elif self.position == 'Middle Manager':
                self.openMiddleManagerHomePage()
            elif self.position == 'Employee':
                self.openEmployeeHomePage()
            else:
                print(self.position)
        elif self.email == null:
            pass
        elif self.password == null:
            pass
        else:
            pass
    def openHomeBar(self):
        if self.position == 'Top Manager':
            self.objectivesHomeButton.clicked.connect(self.openTopManagerHomePage)
        elif self.position == 'Middle Manager':
            self.objectivesHomeButton.clicked.connect(self.openMiddleManagerHomePage)
        elif self.position == 'Employee':
            self.objectivesHomeButton.clicked.connect(self.openEmployeeHomePage)
        else:
            print(self.position)
    def openEvaluationBar(self):
        if self.position == 'Top Manager':
            self.objectivesEvaluationButton.clicked.connect(self.openTopManagerEvaluationPage)
        elif self.position == 'Middle Manager':
            self.objectivesEvaluationButton.clicked.connect(self.openMiddleManagerEvaluationPage)
        elif self.position == 'Employee':
            self.objectivesEvaluationButton.clicked.connect(self.openEmployeeEvaluationPage)
        else:
            print(self.position)
    def openTopManagerHomePage(self):
        self.setWindowTitle('Performance management - Home')
        self.screens.setCurrentIndex(2)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesGoalsButton.hide()
        self.objectivesActionPlanButton.hide()
        self.objectivesButton.show()
    def openMiddleManagerHomePage(self):
        self.setWindowTitle('Performance management - Home')
        self.screens.setCurrentIndex(3)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesActionPlanButton.hide()
        self.objectivesButton.hide()
        self.objectivesGoalsButton.show()
    def openEmployeeHomePage(self):
        self.setWindowTitle('Performance management - Home')
        self.screens.setCurrentIndex(4)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesButton.hide()
        self.objectivesGoalsButton.hide()
        self.objectivesActionPlanButton.show()
    def openTopManagerSetObjectivesPage(self):
        self.setWindowTitle('Performance management - Objectives')
        self.screens.setCurrentIndex(5)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesGoalsButton.hide()
        self.objectivesActionPlanButton.hide()
    def openMiddleManagerSetGoalsPage(self):
        self.setWindowTitle('Performance management - Goals')
        self.screens.setCurrentIndex(6)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesActionPlanButton.hide()
        self.objectivesButton.hide()
    def openEmployeeSetActionPlanPage(self):
        self.setWindowTitle('Performance management - Action Plan')
        self.screens.setCurrentIndex(7)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesButton.hide()
        self.objectivesGoalsButton.hide()
    def openViewObjectivesPage(self):
        self.setWindowTitle('Performance management - Objectives')
        self.screens.setCurrentIndex(8)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
    def openViewGoalsPage(self):
        self.setWindowTitle('Performance management - Goals')
        self.screens.setCurrentIndex(9)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
    def openViewActionPlanPage(self):
        self.setWindowTitle('Performance management - Action Plan')
        self.screens.setCurrentIndex(10)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
    def openTopManagerEvaluationPage(self):
        self.setWindowTitle('Performance management - Evaluation')
        self.screens.setCurrentIndex(11)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesGoalsButton.hide()
        self.objectivesActionPlanButton.hide()
    def openMiddleManagerEvaluationPage(self):
        self.setWindowTitle('Performance management - Evaluation')
        self.screens.setCurrentIndex(12)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesActionPlanButton.hide()
        self.objectivesButton.hide()
    def openEmployeeEvaluationPage(self):
        self.setWindowTitle('Performance management - Evaluation')
        self.screens.setCurrentIndex(13)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesButton.hide()
        self.objectivesGoalsButton.hide()
    def openTopManagerManagerEvaluationPage(self):
        self.setWindowTitle('Performance management - Manager Evaluation')
        self.screens.setCurrentIndex(14)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesGoalsButton.hide()
        self.objectivesActionPlanButton.hide()
    def openMiddleManagerEmployeeEvaluationPage(self):
        self.setWindowTitle('Performance management - Employee Evaluation')
        self.screens.setCurrentIndex(15)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesActionPlanButton.hide()
        self.objectivesButton.hide()
    def openEmployeePreviousEvaluationPage(self):
        self.setWindowTitle('Performance management - Previous Evaluation')
        self.screens.setCurrentIndex(17)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesButton.hide()
        self.objectivesGoalsButton.hide()
    def openMiddleManagerPreviousEvaluationPage(self):
        self.setWindowTitle('Performance management - Previous Evaluation')
        self.screens.setCurrentIndex(16)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesActionPlanButton.hide()
        self.objectivesButton.hide()
    def openTopManagerHistoryPage(self):
        self.setWindowTitle('Performance management - History')
        self.screens.setCurrentIndex(18)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesGoalsButton.hide()
        self.objectivesActionPlanButton.hide()
    def openMiddleManagerHistoryPage(self):
        self.setWindowTitle('Performance management - History')
        self.screens.setCurrentIndex(19)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesActionPlanButton.hide()
        self.objectivesButton.hide()
    def openEmployeeHistoryPage(self):
        self.setWindowTitle('Performance management - History')
        self.screens.setCurrentIndex(20)
        self.objectivesLeftFrame.show()
        self.objectivesUpFrame.show()
        self.objectivesButton.hide()
        self.objectivesGoalsButton.hide()





def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    login = window()
    login.show()
    app.exec_()

if __name__ == '__main__':
    main()
