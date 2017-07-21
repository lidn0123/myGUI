# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 50, 421, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.price_box = QtWidgets.QTextEdit(self.centralwidget)
        self.price_box.setGeometry(QtCore.QRect(400, 170, 104, 71))
        self.price_box.setObjectName("price_box")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 200, 54, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tax_rate = QtWidgets.QSpinBox(self.centralwidget)
        self.tax_rate.setGeometry(QtCore.QRect(230, 290, 42, 22))
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName("tax_rate")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 290, 54, 12))
        self.label_3.setObjectName("label_3")
        self.calx_tax_button = QtWidgets.QPushButton(self.centralwidget)
        self.calx_tax_button.setGeometry(QtCore.QRect(200, 360, 75, 23))
        self.calx_tax_button.setObjectName("calx_tax_button")
        self.results_window = QtWidgets.QTextEdit(self.centralwidget)
        self.results_window.setGeometry(QtCore.QRect(190, 420, 104, 71))
        self.results_window.setObjectName("results_window")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">Sales Tax Calculator</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Price"))
        self.label_3.setText(_translate("MainWindow", "Tax Tate"))
        self.calx_tax_button.setText(_translate("MainWindow", "Calvulator"))

