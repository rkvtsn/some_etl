# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName(_fromUtf8("LoginWindow"))
        LoginWindow.resize(288, 122)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setWindowOpacity(1.0)
        LoginWindow.setAutoFillBackground(False)
        LoginWindow.setStyleSheet(_fromUtf8("* {\n"
"    font-size: 12px;\n"
"    font-family: \"Century Gothic\";\n"
"    border: none;\n"
"}\n"
".QLabel {\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#frame \n"
"{\n"
"    width: 100%;\n"
"    height: 100%;\n"
"    background: #00cc99;\n"
"}\n"
"\n"
"#btn_login {\n"
"    background: #fff;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"} #btn_login:hover {\n"
"    background: #ececec;\n"
"}"))
        self.centralwidget = QtGui.QWidget(LoginWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 290, 130))
        self.frame.setMinimumSize(QtCore.QSize(290, 130))
        self.frame.setMaximumSize(QtCore.QSize(290, 130))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.btn_login = QtGui.QPushButton(self.frame)
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.gridLayout.addWidget(self.btn_login, 2, 1, 1, 1)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Форма входа", None))
        self.label.setText(_translate("LoginWindow", "Имя пользователя", None))
        self.label_2.setText(_translate("LoginWindow", "Пароль", None))
        self.btn_login.setText(_translate("LoginWindow", "Войти", None))

