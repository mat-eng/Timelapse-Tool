# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        MainWindow.setBaseSize(QtCore.QSize(400, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(50, 270, 300, 192))
        self.log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.log.setObjectName("log")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 470, 300, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_folderSelection = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_folderSelection.setGeometry(QtCore.QRect(50, 30, 300, 21))
        self.pushButton_folderSelection.setObjectName("pushButton_folderSelection")
        self.pushButton_musicSelection = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_musicSelection.setGeometry(QtCore.QRect(50, 60, 300, 21))
        self.pushButton_musicSelection.setObjectName("pushButton_musicSelection")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 90, 300, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_duration = QtWidgets.QLabel(self.frame)
        self.label_duration.setGeometry(QtCore.QRect(10, 55, 280, 19))
        self.label_duration.setObjectName("label_duration")
        self.label_1 = QtWidgets.QLabel(self.frame)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 280, 16))
        self.label_1.setObjectName("label_1")
        self.horizontalSlider_duration = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_duration.setGeometry(QtCore.QRect(10, 35, 280, 22))
        self.horizontalSlider_duration.setMinimum(1)
        self.horizontalSlider_duration.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_duration.setObjectName("horizontalSlider_duration")
        self.pushButton_build = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_build.setGeometry(QtCore.QRect(50, 240, 300, 21))
        self.pushButton_build.setObjectName("pushButton_build")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 210, 300, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_openTimelapse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openTimelapse.setGeometry(QtCore.QRect(50, 510, 300, 21))
        self.pushButton_openTimelapse.setObjectName("pushButton_openTimelapse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timelapse Tool"))
        self.pushButton_folderSelection.setText(_translate("MainWindow", "1. Choose pictures folder"))
        self.pushButton_musicSelection.setText(_translate("MainWindow", "2. Choose music file (optional)"))
        self.label_duration.setText(_translate("MainWindow", "Duration: 00:00:00 (hh:mm:ss)"))
        self.label_1.setText(_translate("MainWindow", "3. Define Timelapse duration"))
        self.pushButton_build.setText(_translate("MainWindow", "4. Build Timelapse"))
        self.pushButton_openTimelapse.setText(_translate("MainWindow", "5. Open Timelapse"))