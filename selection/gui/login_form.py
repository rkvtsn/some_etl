# coding=utf-8
from selection.util import account
from PyQt4 import QtGui, QtCore

import design


class LoginForm(QtGui.QDialog, design.Ui_LoginDialog):
    def __init__(self, parent=None):
        super(LoginForm, self).__init__(parent)
        self.setupUi(self)
        self.btn_login.clicked.connect(self.login)
        self.btn_login.setAutoDefault(True)

    def login(self):
        print "attempted to login user: %s" % self.edit_login.text()
        username = str(self.edit_login.text()).strip()
        password = str(self.edit_password.text()).strip()
        user = account.login(username, password)
        print user
        if user is None:
            QtGui.QMessageBox.warning(self, u'Ошибка входа', u'Неверный логин или пароль')
            return
        self.accept()
        self.user = user

    def get_user(self):
        return self.user

    # def on_close(self):
    #     pass
    #
    # def closeEvent(self, event):
    #     quit_msg = u"Уверены, что желаете выйти?"
    #     reply = QtGui.QMessageBox.question(self, 'Message',
    #                                        quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.Cancel)
    #
    #     if reply == QtGui.QMessageBox.Yes:
    #         self.on_close()
    #         event.accept()
    #     else:
    #         event.ignore()
