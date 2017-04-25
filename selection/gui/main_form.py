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
    def __init__(self, parent=None, user=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        if user is None:
            raise Exception("Something wrong with user! Error #100")
        self.btn_request.clicked.connect(self.make_request)
        self.btn_set_interval.clicked.connect(self.set_interval)
        self.interval = TimeInterval(3600, self.request)

    def request(self):
        self.__simulate_work()

    def __simulate_work(self, n=10000000):
        for i in range(n + 1):
            percentage = 100 * float(i) / n
            if percentage % 10 == 0:
                print percentage

    def make_request(self):
        self.btn_request.setEnabled(False)
        self.btn_set_interval.setEnabled(False)
        self.request_thread = Task(self.request)
        self.connect(self.request_thread, SIGNAL("task_done(QString)"), self.done)
        self.request_thread.start()

    def done(self, result):
        self.btn_request.setEnabled(True)
        self.btn_set_interval.setEnabled(True)

    def set_interval(self, checked):
        t = self.spin_interval.value()
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
