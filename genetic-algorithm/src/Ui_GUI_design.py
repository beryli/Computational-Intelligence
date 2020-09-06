# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\我的資料夾\NCU\資工大三課程_下\3_計算型智慧\HW2\workspace\GUI_all.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
import rbfn
import car
import ga
import threading
# 
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import time
import random
import copy
parent = os.path.dirname(os.getcwd())


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(65, 65, 65);\n"
        "font: 12pt \"Arial\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("font: 12pt \"Arial\";\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(65, 65, 65);")
        self.centralwidget.setObjectName("centralwidget")
        self.trainFormFrame = QtWidgets.QFrame(self.centralwidget)
        self.trainFormFrame.setGeometry(QtCore.QRect(9, 70, 481, 341))
        self.trainFormFrame.setStyleSheet("border: 1px solid rgb(127, 127, 127);\n"
        "font: 12pt \"Arial\";\n"
        "\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(65, 65, 65);")
        self.trainFormFrame.setObjectName("trainFormFrame")
        self.formLayout = QtWidgets.QFormLayout(self.trainFormFrame)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(20, 5, 20, 5)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.getTrainLabel = QtWidgets.QLabel(self.trainFormFrame)
        self.getTrainLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.getTrainLabel.setObjectName("getTrainLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.getTrainLabel)
        self.getTraincomboBox = QtWidgets.QComboBox(self.trainFormFrame)
        self.getTraincomboBox.setStyleSheet("border: 1px solid rgb(50, 50, 50);\n"
        "background-color:  rgb(50, 50, 50);")
        self.getTraincomboBox.setMaxVisibleItems(3)
        self.getTraincomboBox.setObjectName("getTraincomboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.getTraincomboBox)
        self.reLabel = QtWidgets.QLabel(self.trainFormFrame)
        self.reLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.reLabel.setObjectName("reLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.reLabel)
        self.iterLabel = QtWidgets.QLabel(self.trainFormFrame)
        self.iterLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.iterLabel.setObjectName("iterLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.iterLabel)
        self.iterTimesSpinBox = QtWidgets.QSpinBox(self.trainFormFrame)
        self.iterTimesSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.iterTimesSpinBox.setToolTip("")
        self.iterTimesSpinBox.setStyleSheet("border: 1px solid rgb(50, 50, 50);\n"
        "background-color:  rgb(50, 50, 50);")
        self.iterTimesSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.iterTimesSpinBox.setMinimum(1)
        self.iterTimesSpinBox.setMaximum(10000)
        self.iterTimesSpinBox.setSingleStep(10)
        self.iterTimesSpinBox.setProperty("value", 100)
        self.iterTimesSpinBox.setObjectName("iterTimesSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.iterTimesSpinBox)
        self.populationLabel = QtWidgets.QLabel(self.trainFormFrame)
        self.populationLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.populationLabel.setObjectName("populationLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.populationLabel)
        self.populationSpinBox = QtWidgets.QSpinBox(self.trainFormFrame)
        self.populationSpinBox.setStyleSheet("border: 1px solid rgb(50, 50, 50);\n"
        "background-color:  rgb(50, 50, 50);")
        self.populationSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.populationSpinBox.setMinimum(2)
        self.populationSpinBox.setMaximum(1000)
        self.populationSpinBox.setSingleStep(10)
        self.populationSpinBox.setProperty("value", 100)
        self.populationSpinBox.setObjectName("populationSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.populationSpinBox)
        self.p_cLabel = QtWidgets.QLabel(self.trainFormFrame)
        self.p_cLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.p_cLabel.setObjectName("p_cLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.p_cLabel)
        self.p_cdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.trainFormFrame)
        self.p_cdoubleSpinBox.setAutoFillBackground(False)
        self.p_cdoubleSpinBox.setStyleSheet("border: 1px solid rgb(50, 50, 50);\n"
        "background-color:  rgb(50, 50, 50);")
        self.p_cdoubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.p_cdoubleSpinBox.setReadOnly(False)
        self.p_cdoubleSpinBox.setAccelerated(False)
        self.p_cdoubleSpinBox.setMaximum(1.0)
        self.p_cdoubleSpinBox.setSingleStep(0.1)
        self.p_cdoubleSpinBox.setProperty("value", 0.5)
        self.p_cdoubleSpinBox.setObjectName("p_cdoubleSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.p_cdoubleSpinBox)
        self.p_mLabel = QtWidgets.QLabel(self.trainFormFrame)
        self.p_mLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.p_mLabel.setObjectName("p_mLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.p_mLabel)
        self.p_mDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.trainFormFrame)
        self.p_mDoubleSpinBox.setStyleSheet("border: 1px solid rgb(50, 50, 50);\n"
        "background-color:  rgb(50, 50, 50);")
        self.p_mDoubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.p_mDoubleSpinBox.setMaximum(1.0)
        self.p_mDoubleSpinBox.setSingleStep(0.1)
        self.p_mDoubleSpinBox.setProperty("value", 0.5)
        self.p_mDoubleSpinBox.setObjectName("p_mDoubleSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.p_mDoubleSpinBox)
        self.num_nLabel = QtWidgets.QLabel(self.trainFormFrame)
        self.num_nLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.num_nLabel.setTextFormat(QtCore.Qt.PlainText)
        self.num_nLabel.setObjectName("num_nLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.num_nLabel)
        self.num_nSpinBox = QtWidgets.QSpinBox(self.trainFormFrame)
        self.num_nSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.num_nSpinBox.setToolTip("")
        self.num_nSpinBox.setStyleSheet("border: 1px solid rgb(50, 50, 50);\n"
        "background-color:  rgb(50, 50, 50);")
        self.num_nSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.num_nSpinBox.setMinimum(1)
        self.num_nSpinBox.setMaximum(1000)
        self.num_nSpinBox.setSingleStep(1)
        self.num_nSpinBox.setProperty("value", 12)
        self.num_nSpinBox.setObjectName("num_nSpinBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.num_nSpinBox)
        self.reFrame = QtWidgets.QFrame(self.trainFormFrame)
        self.reFrame.setStyleSheet("border:0px;\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(65, 65, 65);\n"
        "")
        self.reFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reFrame.setObjectName("reFrame")
        self.wheel = QtWidgets.QRadioButton(self.reFrame)
        self.wheel.setGeometry(QtCore.QRect(0, 0, 81, 19))
        self.wheel.setObjectName("wheel")
        self.tournament = QtWidgets.QRadioButton(self.reFrame)
        self.tournament.setGeometry(QtCore.QRect(90, 0, 141, 20))
        self.tournament.setObjectName("tournament")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.reFrame)
        self.headTrainLabel = QtWidgets.QLabel(self.centralwidget)
        self.headTrainLabel.setGeometry(QtCore.QRect(10, 20, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.headTrainLabel.setFont(font)
        self.headTrainLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.headTrainLabel.setStyleSheet("font: 18pt \"Arial\";\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(65, 65, 65);")
        self.headTrainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headTrainLabel.setObjectName("headTrainLabel")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(270, 440, 141, 24))
        self.Save.setStyleSheet("QPushButton{\n"
        "border: 1px solid rgb(50, 50, 50); border-radius:10px; padding:2px 4px;\n"
        "background-color: rgb(50, 50, 50);\n"
        "}\n"
        "QPushButton:hover{background-color: rgb(170, 170, 170); color: black;}\n"
        "QPushButton:pressed{background-color:rgb(200, 200, 200); border-style: inset; }"
        "QPushButton:disabled{background-color:rgb(200, 200, 200); border-style: inset; }")
        self.Save.setCheckable(False)
        self.Save.setAutoDefault(False)
        self.Save.setObjectName("Save")
        self.Go = QtWidgets.QPushButton(self.centralwidget)
        self.Go.setGeometry(QtCore.QRect(60, 440, 151, 24))
        self.Go.setStyleSheet("QPushButton{\n"
        "border: 1px solid rgb(50, 50, 50); border-radius:10px; padding:2px 4px;\n"
        "background-color: rgb(50, 50, 50);\n"
        "}\n"
        "QPushButton:hover{background-color: rgb(170, 170, 170); color: black;}\n"
        "QPushButton:pressed{background-color:rgb(200, 200, 200); border-style: inset; }"
        "QPushButton:disabled{background-color:rgb(200, 200, 200); border-style: inset; }")
        self.Go.setObjectName("Go")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(510, 20, 481, 451))
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
        "QPushButton:pressed{background-color:rgb(200, 200, 200); border-style: inset; }"
        "QPushButton:disabled{background-color:rgb(200, 200, 200); border-style: inset; }")
        self.showPushButton.setObjectName("showPushButton")
        self.getParamLabel = QtWidgets.QLabel(self.frame)
        self.getParamLabel.setGeometry(QtCore.QRect(0, 50, 161, 26))
        self.getParamLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.getParamLabel.setObjectName("getParamLabel")
        self.getParamcomboBox = QtWidgets.QComboBox(self.frame)
        self.getParamcomboBox.setGeometry(QtCore.QRect(160, 50, 211, 26))
        self.getParamcomboBox.setStyleSheet("border: 1px solid rgb(50, 50, 50);\n"
        "background-color:  rgb(50, 50, 50);")
        self.getParamcomboBox.setMaxVisibleItems(3)
        self.getParamcomboBox.setObjectName("getParamcomboBox")
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
        self.trainFrame = QtWidgets.QFrame(self.centralwidget)
        self.trainFrame.setGeometry(QtCore.QRect(0, 500, 511, 101))
        self.trainFrame.setStyleSheet("font: 12pt \"Arial\";\n"
        "background-color: rgb(50, 50, 50);")
        self.trainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trainFrame.setObjectName("trainFrame")
        self.IterLabel = QtWidgets.QLabel(self.trainFrame)
        self.IterLabel.setGeometry(QtCore.QRect(80, 30, 111, 26))
        self.IterLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.IterLabel.setObjectName("IterLabel")
        self.errorLabel = QtWidgets.QLabel(self.trainFrame)
        self.errorLabel.setGeometry(QtCore.QRect(290, 30, 71, 26))
        self.errorLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.errorLabel.setObjectName("errorLabel")
        self.IterNumLabel = QtWidgets.QLabel(self.trainFrame)
        self.IterNumLabel.setGeometry(QtCore.QRect(170, 30, 41, 26))
        self.IterNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.IterNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.IterNumLabel.setObjectName("IterNumLabel")
        self.errorNumLabel = QtWidgets.QLabel(self.trainFrame)
        self.errorNumLabel.setGeometry(QtCore.QRect(350, 30, 51, 26))
        self.errorNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.errorNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorNumLabel.setObjectName("errorNumLabel")
        self.headFrame = QtWidgets.QFrame(self.centralwidget)
        self.headFrame.setGeometry(QtCore.QRect(510, 500, 491, 101))
        self.headFrame.setStyleSheet("font: 12pt \"Arial\";\n"
        "background-color: rgb(50, 50, 50);")
        self.headFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headFrame.setObjectName("headFrame")
        self.xLabel = QtWidgets.QLabel(self.headFrame)
        self.xLabel.setGeometry(QtCore.QRect(0, 20, 21, 26))
        self.xLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.xLabel.setObjectName("xLabel")
        self.yLabel = QtWidgets.QLabel(self.headFrame)
        self.yLabel.setGeometry(QtCore.QRect(170, 20, 31, 26))
        self.yLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.yLabel.setObjectName("yLabel")
        self.xNumLabel = QtWidgets.QLabel(self.headFrame)
        self.xNumLabel.setGeometry(QtCore.QRect(40, 20, 51, 26))
        self.xNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.xNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xNumLabel.setObjectName("xNumLabel")
        self.degLabel = QtWidgets.QLabel(self.headFrame)
        self.degLabel.setGeometry(QtCore.QRect(320, 20, 61, 26))
        self.degLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.degLabel.setObjectName("degLabel")
        self.fdLabel = QtWidgets.QLabel(self.headFrame)
        self.fdLabel.setGeometry(QtCore.QRect(0, 50, 121, 26))
        self.fdLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.fdLabel.setObjectName("fdLabel")
        self.ldLabel = QtWidgets.QLabel(self.headFrame)
        self.ldLabel.setGeometry(QtCore.QRect(170, 50, 121, 26))
        self.ldLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.ldLabel.setObjectName("ldLabel")
        self.rdLabel = QtWidgets.QLabel(self.headFrame)
        self.rdLabel.setGeometry(QtCore.QRect(320, 50, 121, 26))
        self.rdLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.rdLabel.setObjectName("rdLabel")
        self.yNumLabel = QtWidgets.QLabel(self.headFrame)
        self.yNumLabel.setGeometry(QtCore.QRect(210, 20, 51, 26))
        self.yNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.yNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.yNumLabel.setObjectName("yNumLabel")
        self.degNumLabel = QtWidgets.QLabel(self.headFrame)
        self.degNumLabel.setGeometry(QtCore.QRect(390, 20, 51, 26))
        self.degNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.degNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.degNumLabel.setObjectName("degNumLabel")
        self.fdNumLabel = QtWidgets.QLabel(self.headFrame)
        self.fdNumLabel.setGeometry(QtCore.QRect(100, 50, 41, 26))
        self.fdNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.fdNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fdNumLabel.setObjectName("fdNumLabel")
        self.ldNumLabel = QtWidgets.QLabel(self.headFrame)
        self.ldNumLabel.setGeometry(QtCore.QRect(260, 50, 41, 26))
        self.ldNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.ldNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ldNumLabel.setObjectName("ldNumLabel")
        self.rdNumLabel = QtWidgets.QLabel(self.headFrame)
        self.rdNumLabel.setGeometry(QtCore.QRect(420, 50, 41, 26))
        self.rdNumLabel.setStyleSheet("border: 0px solid rgb(255, 255, 255)")
        self.rdNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rdNumLabel.setObjectName("rdNumLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ############################              initialization               ############################
        self.initialization()
        ############################              initialization               ############################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Genetic Algorithm"))
        self.getTrainLabel.setText(_translate("MainWindow", "Training File"))
        self.reLabel.setText(_translate("MainWindow", "Reproduction"))
        self.iterLabel.setText(_translate("MainWindow", "Iteration Times"))
        self.populationLabel.setText(_translate("MainWindow", "Population Size"))
        self.p_cLabel.setText(_translate("MainWindow", "Crossover Probability"))
        self.p_mLabel.setText(_translate("MainWindow", "Mutation Probability"))
        self.num_nLabel.setText(_translate("MainWindow", "Number of Neuron"))
        self.wheel.setText(_translate("MainWindow", "Wheel"))
        self.tournament.setText(_translate("MainWindow", "Tournament"))
        self.headTrainLabel.setText(_translate("MainWindow", "Train"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.Go.setText(_translate("MainWindow", "Go"))
        self.showPushButton.setText(_translate("MainWindow", "Show"))
        self.getParamLabel.setText(_translate("MainWindow", "Load Parameters"))
        self.runLabel.setText(_translate("MainWindow", "Run"))
        self.IterLabel.setText(_translate("MainWindow", "Iteration : "))
        self.errorLabel.setText(_translate("MainWindow", "Error : "))
        self.IterNumLabel.setText(_translate("MainWindow", "0"))
        self.errorNumLabel.setText(_translate("MainWindow", "Inf"))
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
        # radioButton
        self.wheel.setChecked(True)
        # getTraincomboBox
        comboList = os.listdir(parent+'/data/')
        self.getTraincomboBox.addItems(comboList)
        self.getTraincomboBox.setEditable(True)
        self.getTraincomboBox.lineEdit().setReadOnly(True)
        self.getTraincomboBox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        for i in range(self.getTraincomboBox.count()):
            self.getTraincomboBox.setItemData(i, QtCore.Qt.AlignCenter, QtCore.Qt.TextAlignmentRole)
        # getTraincomboBox
        comboList = os.listdir(parent+'/weights/')
        self.getParamcomboBox.addItems(comboList)
        self.getParamcomboBox.setEditable(True)
        self.getParamcomboBox.lineEdit().setReadOnly(True)
        self.getParamcomboBox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        for i in range(self.getParamcomboBox.count()):
            self.getParamcomboBox.setItemData(i, QtCore.Qt.AlignCenter, QtCore.Qt.TextAlignmentRole)
        # buttons
        self.Go.clicked.connect(self.go)
        self.Save.clicked.connect(self.save)
        self.showPushButton.clicked.connect(self.show)
        # graph
        self.c = car.Car()
        self.fig = self.c.draw()
        self.resetFigure()
        # 
        self.plotWidget = FigureCanvas(self.fig)
        self.lay = QtWidgets.QVBoxLayout(self.frame)
        self.lay.setGeometry(QtCore.QRect(25, 101, 431, 341))
        self.lay.setContentsMargins(100, 100, 100, 10) # left, up, right, down
        self.lay.addWidget(self.plotWidget)

    def go(self):
        self.Go.setEnabled(False)
        # thread
        if self.populationSpinBox.value() % 2 == 0:
            self.thread = threading.Thread(target = self.goThread)
            self.thread.start()
        else:
            print('please set population size with enev numbers')
            self.Go.setEnabled(True)
    
    def goThread(self):
        # get params
        filename = self.getTraincomboBox.currentText()
        num_iter, num_neuron = self.iterTimesSpinBox.value(), self.num_nSpinBox.value()
        population = self.populationSpinBox.value()
        p_c = self.p_cdoubleSpinBox.value()
        p_m = self.p_mDoubleSpinBox.value()
        self.errorNumLabel.setText('Inf')
        # print(filename, num_iter, num_neuron, population, p_c, p_m)
        
        # ga
        self.stop_threads = False
        self.g = ga.GA(num_iter, population, p_m, p_c, num_neuron, filename, self.wheel.isChecked())
        for i in range(num_iter):
            if self.stop_threads:
                break
            self.IterNumLabel.setText(str(i+1))
            self.g.evolution()
            if self.g.BestRBFN:
                self.errorNumLabel.setText('{:2.2f}'.format(self.g.BestRBFN.error))
            QtWidgets.QApplication.processEvents()
        # print(self.g.BestRBFN.mu)
        self.g.BestRBFN.saveParams()
        # reset getParamcomboBox
        self.getParamcomboBox.clear()
        comboList = os.listdir(parent+'/weights/')
        self.getParamcomboBox.addItems(comboList)
        self.Go.setEnabled(True)
        
    def save(self):
        self.stop_threads = True
        self.Go.setEnabled(True)
        pass

    def show(self):
        # get engine
        filename = self.getParamcomboBox.currentText()
        engine = rbfn.RBFN()
        engine.loadParams(filename)
        # set car
        self.c = car.Car()
        self.c.setEngine(engine)
        self.c.run()
        # self.c.saveResult()
        
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
            time.sleep(0.035)
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