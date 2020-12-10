import sys, os
import PySide2.QtWidgets as q
from PySide2.QtCore import Slot, Qt, QSize, QThread, QObject, Signal,QAbstractTableModel,QModelIndex
from PySide2 import QtGui

class MyTable(q.QDialog):
    
    def __init__(self, data, parent=None, labels=None, keys=None, sizes=None, th = None):
        
        q.QDialog.__init__(self, parent=parent)
        ssize = q.QApplication.primaryScreen().availableGeometry()
        self.w = ssize.width()
        self.h = ssize.height()-30
        self.setFixedSize(self.w, self.h)
        self.setWindowIcon(QtGui.QIcon("assets/logo.png"))
        self.show()
        self.center()
        self.th = th
        
        # Constroi layouts
        self.layout = q.QVBoxLayout()
        
        
        self.setLayout(self.layout)
        

    def center(self):
        qr = self.frameGeometry()
        cp = q.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
