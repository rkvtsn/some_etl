# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(398, 179)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 30, 251, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.spinInterval = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.spinInterval.setMinimum(1)
        self.spinInterval.setMaximum(3600)
        self.spinInterval.setObjectName(_fromUtf8("spinInterval"))
        self.horizontalLayout_2.addWidget(self.spinInterval)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.btnSetRequestTime = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnSetRequestTime.setEnabled(True)
        self.btnSetRequestTime.setObjectName(_fromUtf8("btnSetRequestTime"))
        self.horizontalLayout_2.addWidget(self.btnSetRequestTime, QtCore.Qt.AlignRight)
        self.btnRequest = QtGui.QPushButton(self.centralwidget)
        self.btnRequest.setGeometry(QtCore.QRect(90, 100, 201, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRequest.sizePolicy().hasHeightForWidth())
        self.btnRequest.setSizePolicy(sizePolicy)
        self.btnRequest.setObjectName(_fromUtf8("btnRequest"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 140, 381, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.btnRequest.raise_()
        self.progressBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Каждую", None))
        self.label_2.setText(_translate("MainWindow", "сек.", None))
        self.btnSetRequestTime.setText(_translate("MainWindow", "Установить", None))
        self.btnRequest.setText(_translate("MainWindow", "Запросить", None))

