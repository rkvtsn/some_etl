# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
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

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName(_fromUtf8("LoginDialog"))
        LoginDialog.resize(311, 150)
        self.frame = QtGui.QFrame(LoginDialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 290, 130))
        self.frame.setMinimumSize(QtCore.QSize(290, 130))
        self.frame.setMaximumSize(QtCore.QSize(290, 130))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.edit_password = QtGui.QLineEdit(self.frame)
        self.edit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.edit_password.setObjectName(_fromUtf8("edit_password"))
        self.gridLayout.addWidget(self.edit_password, 1, 1, 1, 1)
        self.btn_login = QtGui.QPushButton(self.frame)
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.gridLayout.addWidget(self.btn_login, 3, 0, 1, 2)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edit_login = QtGui.QLineEdit(self.frame)
        self.edit_login.setObjectName(_fromUtf8("edit_login"))
        self.gridLayout.addWidget(self.edit_login, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)
        LoginDialog.setTabOrder(self.edit_login, self.edit_password)
        LoginDialog.setTabOrder(self.edit_password, self.btn_login)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Форма входа", None))
        self.edit_password.setPlaceholderText(_translate("LoginDialog", "Пароль", None))
        self.btn_login.setText(_translate("LoginDialog", "Войти", None))
        self.label.setText(_translate("LoginDialog", "Имя пользователя:", None))
        self.edit_login.setPlaceholderText(_translate("LoginDialog", "Имя пользователя", None))
        self.label_2.setText(_translate("LoginDialog", "Пароль:", None))

