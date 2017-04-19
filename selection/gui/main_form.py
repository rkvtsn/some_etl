# coding=utf-8
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL

from selection import IntegrationController
from tinterval import TimeInterval
import design

class Task(QtCore.QThread):
    def __init__(self, fn):
        QtCore.QThread.__init__(self)
        self.do_work = fn

    def __del__(self):
        self.wait()

    def run(self):
        result = self.do_work()
        self.emit(SIGNAL('task_done(QString)'), "")


class MainForm(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.btnRequest.clicked.connect(self.make_request)
        self.btnSetRequestTime.clicked.connect(self.set_interval)
        self.interval = TimeInterval(3600, self.request)

    def request(self):
        self.__simulate_work()

    def __simulate_work(self, n=10000000):
        for i in range(n + 1):
            percentage = 100 * float(i) / n
            if percentage % 10 == 0:
                print percentage

    def make_request(self):
        self.btnRequest.setEnabled(False)
        self.btnSetRequestTime.setEnabled(False)
        self.progressBar.setMaximum(5)
        self.progressBar.setValue(0)
        self.progressBar.setValue(3)
        self.request_thread = Task(self.request)
        self.connect(self.request_thread, SIGNAL("task_done(QString)"), self.done)
        self.request_thread.start()

    def done(self, result):
        self.progressBar.setValue(5)
        self.btnRequest.setEnabled(True)
        self.btnSetRequestTime.setEnabled(True)

    def set_interval(self, checked):
        t = self.spinInterval.value()
        self.interval.set_timeout(t)

    def on_close(self):
        self.interval.stop()

    def closeEvent(self, event):
        quit_msg = u"Уверены, что желаете выйти?"
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.Cancel)

        if reply == QtGui.QMessageBox.Yes:
            self.on_close()
            event.accept()
        else:
            event.ignore()
