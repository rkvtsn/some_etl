# coding=utf-8
from PyQt4 import QtGui, QtCore

import design


class LoginForm(QtGui.QMainWindow, design.Ui_LoginWindow):
    def __init__(self, parent=None, child=None):
        super(LoginForm, self).__init__(parent)
        self.child = child
        self.setupUi(self)
        self.btn_login.clicked.connect(self.login)

    def login(self):
        print "attempted to login"
        self.child.show()
        pass

    def on_close(self):
        pass

    def closeEvent(self, event):
        quit_msg = u"Уверены, что желаете выйти?"
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.Cancel)

        if reply == QtGui.QMessageBox.Yes:
            self.on_close()
            event.accept()
        else:
            event.ignore()
