import sys
from PyQt4 import QtGui, QtCore
from main_form import MainForm
from login_form import LoginForm
from admin_form import AdminForm

app = QtGui.QApplication(sys.argv)
translator = QtCore.QTranslator(app)
locale = QtCore.QLocale.system().name()
path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
translator.load('qt_%s' % locale, path)
app.installTranslator(translator)
login_form = LoginForm()

window = AdminForm()
window.show()
sys.exit(app.exec_())

# if login_form.exec_() == QtGui.QDialog.Accepted:
#     user = login_form.get_user()
#     if user['is_admin']:
#         print 'admin'
#         window = AdminForm(user=user)
#         window.show()
#     else:
#         window = MainForm(user=user)
#         window.show()
#     sys.exit(app.exec_())
