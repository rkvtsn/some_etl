import operator
from PyQt4 import QtCore

from PyQt4.QtCore import QAbstractTableModel, SIGNAL
from PyQt4.QtCore import QVariant


class TableModel(QAbstractTableModel):
    def __init__(self, datain, headers, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = headers

    def rowCount(self, parent):
        if parent.isValid():
            return 0
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role == QtCore.Qt.CheckStateRole and index.column() == 3:
            is_admin = self.arraydata[index.row()][index.column()]
            if is_admin:
                return QtCore.Qt.Checked
            else:
                return QtCore.Qt.Unchecked
        elif role != QtCore.Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

    def sort(self, col, order):
        """Sort table by given column number.
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(col))
        if order == QtCore.Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))

    def insertRows(self, items, parent=None, *args, **kwargs):
        self.beginInsertRows(QtCore.QModelIndex(), len(self.arraydata), len(self.arraydata))
        self.arraydata.append(items)
        self.endInsertRows()
        return True

    def removeRows(self, index, parent=None, *args, **kwargs):
        self.beginRemoveRows(QtCore.QModelIndex(), len(self.arraydata), len(self.arraydata))
        self.arraydata.pop(index)
        self.endRemoveRows()
        return True

    def setData(self, index, value, role=None):
        self.arraydata[index.row()][index.column()] = value
        return True

    def get_data(self):
        return self.arraydata

    def reset(self, data, *args, **kwargs):
        self.beginResetModel()
        self.arraydata[:] = []
        self.arraydata = data
        self.endResetModel()
