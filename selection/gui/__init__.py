import sys
from PyQt4 import QtGui, QtCore
from main_form import MainForm

app = QtGui.QApplication(sys.argv)
translator = QtCore.QTranslator(app)
locale = QtCore.QLocale.system().name()
path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
translator.load('qt_%s' % locale, path)
app.installTranslator(translator)
form = MainForm()
form.show()
