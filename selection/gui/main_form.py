# coding=utf-8
from PyQt4 import QtGui, QtCore

from selection import IntegrationController
from tinterval import TimeInterval
import design


class MainForm(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.btnRequest.clicked.connect(self.make_request)
        self.btnSetRequestTime.clicked.connect(self.set_interval)
        self.interval = TimeInterval(3600, self.make_request)
        a = IntegrationController()

    def make_request(self):
        print "make request"

    def set_interval(self, checked):
        t = self.spinInterval.value()
        self.interval.set_timeout(t)

    def on_close(self):
        print "closing"
        self.interval.stop()
        print "closed"

    def closeEvent(self, event):
        quit_msg = u"Уверены, что желаете выйти?"
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.Cancel)

        if reply == QtGui.QMessageBox.Yes:
            self.on_close()
            event.accept()
        else:
            event.ignore()