# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\我的資料夾\NCU\資工大三課程_下\3_計算型智慧\HW1\New Ver\GUI_all.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
import autoCarClass
import threading
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
parent = os.path.dirname(os.getcwd())


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(65, 65, 65);\n"
        "font: 12pt \"Arial\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("font: 12pt \"Arial\";\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(65, 65, 65);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 480, 451))
        self.frame.setStyleSheet("font: 12pt \"Arial\";\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(65, 65, 65);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.showPushButton = QtWidgets.QPushButton(self.frame)
        self.showPushButton.setGeometry(QtCore.QRect(390, 50, 81, 28))
        self.showPushButton.setStyleSheet("QPushButton{\n"
        "border: 1px solid rgb(50, 50, 50); border-radius:10px; padding:2px 4px;\n"
        "background-color: rgb(50, 50, 50);\n"
        "}\n"
        "QPushButton:hover{background-color: rgb(170, 170, 170); color: black;}\n"
        "QPushButton:pressed{background-color:rgb(200, 200, 200); border-style: inset; }")
        self.showPushButton.setObjectName("showPushButton")
        self.runLabel = QtWidgets.QLabel(self.frame)
        self.runLabel.setGeometry(QtCore.QRect(0, 0, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.runLabel.setFont(font)
        self.runLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.runLabel.setStyleSheet("font: 18pt \"Arial\";")
        self.runLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.runLabel.setObjectName("runLabel")
        self.getCasecomboBox = QtWidgets.QComboBox(self.frame)
        self.getCasecomboBox.setGeometry(QtCore.QRect(110, 50, 261, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getCasecomboBox.sizePolicy().hasHeightForWidth())
        self.getCasecomboBox.setSizePolicy(sizePolicy)
        self.getCasecomboBox.setStyleSheet("border: 1px solid rgb(50, 50, 50);\n"
        "background-color:  rgb(50, 50, 50);")
        self.getCasecomboBox.setMaxVisibleItems(3)
        self.getCasecomboBox.setObjectName("getCasecomboBox")
        self.getCaseLabel = QtWidgets.QLabel(self.frame)
        self.getCaseLabel.setGeometry(QtCore.QRect(40, 50, 46, 23))
        self.getCaseLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.getCaseLabel.setObjectName("getCaseLabel")
        self.headFrame = QtWidgets.QFrame(self.centralwidget)
        self.headFrame.setGeometry(QtCore.QRect(0, 500, 501, 101))
        self.headFrame.setStyleSheet("font: 12pt \"Arial\";\n"
        "background-color: rgb(50, 50, 50);")
        self.headFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headFrame.setObjectName("headFrame")
        self.xLabel = QtWidgets.QLabel(self.headFrame)
        self.xLabel.setGeometry(QtCore.QRect(20, 20, 21, 26))
        self.xLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.xLabel.setObjectName("xLabel")
        self.yLabel = QtWidgets.QLabel(self.headFrame)
        self.yLabel.setGeometry(QtCore.QRect(190, 20, 31, 26))
        self.yLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.yLabel.setObjectName("yLabel")
        self.xNumLabel = QtWidgets.QLabel(self.headFrame)
        self.xNumLabel.setGeometry(QtCore.QRect(60, 20, 51, 26))
        self.xNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.xNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xNumLabel.setObjectName("xNumLabel")
        self.degLabel = QtWidgets.QLabel(self.headFrame)
        self.degLabel.setGeometry(QtCore.QRect(340, 20, 61, 26))
        self.degLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.degLabel.setObjectName("degLabel")
        self.fdLabel = QtWidgets.QLabel(self.headFrame)
        self.fdLabel.setGeometry(QtCore.QRect(20, 50, 121, 26))
        self.fdLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.fdLabel.setObjectName("fdLabel")
        self.ldLabel = QtWidgets.QLabel(self.headFrame)
        self.ldLabel.setGeometry(QtCore.QRect(190, 50, 121, 26))
        self.ldLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.ldLabel.setObjectName("ldLabel")
        self.rdLabel = QtWidgets.QLabel(self.headFrame)
        self.rdLabel.setGeometry(QtCore.QRect(340, 50, 121, 26))
        self.rdLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.rdLabel.setObjectName("rdLabel")
        self.yNumLabel = QtWidgets.QLabel(self.headFrame)
        self.yNumLabel.setGeometry(QtCore.QRect(230, 20, 51, 26))
        self.yNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.yNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.yNumLabel.setObjectName("yNumLabel")
        self.degNumLabel = QtWidgets.QLabel(self.headFrame)
        self.degNumLabel.setGeometry(QtCore.QRect(410, 20, 51, 26))
        self.degNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.degNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.degNumLabel.setObjectName("degNumLabel")
        self.fdNumLabel = QtWidgets.QLabel(self.headFrame)
        self.fdNumLabel.setGeometry(QtCore.QRect(120, 50, 41, 26))
        self.fdNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.fdNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fdNumLabel.setObjectName("fdNumLabel")
        self.ldNumLabel = QtWidgets.QLabel(self.headFrame)
        self.ldNumLabel.setGeometry(QtCore.QRect(280, 50, 41, 26))
        self.ldNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.ldNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ldNumLabel.setObjectName("ldNumLabel")
        self.rdNumLabel = QtWidgets.QLabel(self.headFrame)
        self.rdNumLabel.setGeometry(QtCore.QRect(440, 50, 41, 26))
        self.rdNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.rdNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rdNumLabel.setObjectName("rdNumLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ############################              initialization               ############################
        self.initialization()
        ######################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fuzzy System"))
        self.showPushButton.setText(_translate("MainWindow", "Show"))
        self.runLabel.setText(_translate("MainWindow", "Run"))
        self.getCaseLabel.setText(_translate("MainWindow", "Case"))
        self.xLabel.setText(_translate("MainWindow", "X:"))
        self.yLabel.setText(_translate("MainWindow", "Y : "))
        self.xNumLabel.setText(_translate("MainWindow", "0"))
        self.degLabel.setText(_translate("MainWindow", "Deg : "))
        self.fdLabel.setText(_translate("MainWindow", "Front Dist."))
        self.ldLabel.setText(_translate("MainWindow", "Left Dist."))
        self.rdLabel.setText(_translate("MainWindow", "Right Dist."))
        self.yNumLabel.setText(_translate("MainWindow", "0"))
        self.degNumLabel.setText(_translate("MainWindow", "90"))
        self.fdNumLabel.setText(_translate("MainWindow", "0"))
        self.ldNumLabel.setText(_translate("MainWindow", "0"))
        self.rdNumLabel.setText(_translate("MainWindow", "0"))

    def initialization(self):
        # getCasecomboBox
        comboList = os.listdir('case/')
        self.getCasecomboBox.addItems(comboList)
        self.getCasecomboBox.setEditable(True)
        self.getCasecomboBox.lineEdit().setReadOnly(True)
        self.getCasecomboBox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        for i in range(self.getCasecomboBox.count()):
            self.getCasecomboBox.setItemData(i, QtCore.Qt.AlignCenter, QtCore.Qt.TextAlignmentRole)
        self.showPushButton.clicked.connect(self.show)
        # graph
        self.c = autoCarClass.autoCar()
        self.fig = self.c.draw()
        self.resetFigure()
        # 
        self.plotWidget = FigureCanvas(self.fig)
        self.lay = QtWidgets.QVBoxLayout(self.frame)
        self.lay.setGeometry(QtCore.QRect(25, 101, 431, 341))
        self.lay.setContentsMargins(100, 100, 100, 10) # left, up, right, down
        self.lay.addWidget(self.plotWidget)

    def show(self):
        self.c.x_rec, self.c.y_rec, self.c.f_rec, self.c.r_rec, self.c.l_rec, self.c.dir_rec = [], [], [], [], [], []
        filename = self.getCasecomboBox.currentText()
        self.c.loadMap(filename)
        self.c.run()
        
        self.thread1 = threading.Thread(target = self.updateShow)
        self.thread1.start()
        
        self.resetFigure()
        ims = []
        for i in range(len(self.c.x_rec)):
            move = list(zip([self.c.x_rec[i],self.c.y_rec[i]], [self.c.x_rec[i],self.c.y_rec[i]]))
            im = plt.plot(move[0], move[1], marker='o', markersize=20, color = 'b')
            ims.append(im)
        self.ani = animation.ArtistAnimation(self.fig, ims, interval=20, repeat=False)
        self.lay.setGeometry(QtCore.QRect(25, 101, 431, 341))
        self.lay.setContentsMargins(100, 100, 100, 10) # left, up, right, down
        self.lay.update()
        
    def updateShow(self):
        self.showPushButton.setEnabled(False)
        # time.sleep(0.4)
        for i in range(len(self.c.x_rec)):
            time.sleep(0.03)
            # update label
            self.xNumLabel.setText('{:2.2f}'.format(self.c.x_rec[i]))
            self.yNumLabel.setText('{:2.2f}'.format(self.c.y_rec[i]))
            self.degNumLabel.setText('{:2.2f}'.format(self.c.dir_rec[i]))
            self.fdNumLabel.setText('{:2.1f}'.format(self.c.f_rec[i]))
            self.rdNumLabel.setText('{:2.1f}'.format(self.c.r_rec[i]))
            self.ldNumLabel.setText('{:2.1f}'.format(self.c.l_rec[i]))
            # 
            # self.resetFigure()
            # plt.scatter(self.c.x_rec[i], self.c.y_rec[i], s = 300, color = 'c')
            # self.lay.setGeometry(QtCore.QRect(25, 101, 431, 341))
            # self.lay.setContentsMargins(100, 100, 100, 10) # left, up, right, down
            # self.lay.update()
            # 
        self.showPushButton.setEnabled(True)


    def resetFigure(self):
        self.fig.clear()
        # self.figure = plt.figure()
        # start point
        plt.scatter(0, 0, s = 300, color = 'c')
        # end
        end = list(zip(self.c.end1, self.c.end2))
        plt.plot(end[0], end[1], color = 'r')
        # start
        start = list(zip(self.c.walls[-1], self.c.walls[-2]))
        plt.plot(start[0], start[1], color = 'k')
        # walls
        for i in range(len(self.c.walls)-2):
            wall = list(zip(self.c.walls[i], self.c.walls[i+1]))
            plt.plot(wall[0], wall[1], color = 'b')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())