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
        MainWindow.resize(372, 151)
        MainWindow.setStyleSheet(_fromUtf8("#sch_frame {\n"
"    border: 1px solid #ccc;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_request = QtGui.QPushButton(self.centralwidget)
        self.btn_request.setGeometry(QtCore.QRect(10, 10, 75, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_request.sizePolicy().hasHeightForWidth())
        self.btn_request.setSizePolicy(sizePolicy)
        self.btn_request.setObjectName(_fromUtf8("btn_request"))
        self.sch_frame = QtGui.QFrame(self.centralwidget)
        self.sch_frame.setGeometry(QtCore.QRect(12, 96, 201, 43))
        self.sch_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sch_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.sch_frame.setObjectName(_fromUtf8("sch_frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.sch_frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btn_set_interval = QtGui.QPushButton(self.sch_frame)
        self.btn_set_interval.setEnabled(True)
        self.btn_set_interval.setObjectName(_fromUtf8("btn_set_interval"))
        self.gridLayout_2.addWidget(self.btn_set_interval, 0, 4, 1, 1)
        self.label_4 = QtGui.QLabel(self.sch_frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.sch_frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.spin_interval = QtGui.QSpinBox(self.sch_frame)
        self.spin_interval.setMinimum(1)
        self.spin_interval.setMaximum(3600)
        self.spin_interval.setObjectName(_fromUtf8("spin_interval"))
        self.gridLayout_2.addWidget(self.spin_interval, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(12, 76, 81, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.btn_request.raise_()
        self.sch_frame.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Форма запуска задач", None))
        self.btn_request.setText(_translate("MainWindow", "Выполнить", None))
        self.btn_set_interval.setText(_translate("MainWindow", "Установить", None))
        self.label_4.setText(_translate("MainWindow", "сек.", None))
        self.label_3.setText(_translate("MainWindow", "Раз в", None))
        self.label_5.setText(_translate("MainWindow", "По расписанию:", None))

