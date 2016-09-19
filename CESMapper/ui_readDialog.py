# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_readDialog.ui'
#
# Created: Mon Jul 20 16:05:06 2015
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_readDialog(object):
    def setupUi(self, readDialog):
        readDialog.setObjectName(_fromUtf8("readDialog"))
        readDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        readDialog.resize(350, 155)
        readDialog.setMinimumSize(QtCore.QSize(350, 155))
        readDialog.setMaximumSize(QtCore.QSize(350, 155))
        readDialog.setSizeGripEnabled(False)
        readDialog.setModal(True)
        self.input = QtGui.QLineEdit(readDialog)
        self.input.setGeometry(QtCore.QRect(10, 40, 251, 21))
        self.input.setReadOnly(True)
        self.input.setObjectName(_fromUtf8("input"))
        self.label = QtGui.QLabel(readDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.inputButton = QtGui.QPushButton(readDialog)
        self.inputButton.setGeometry(QtCore.QRect(270, 40, 75, 23))
        self.inputButton.setObjectName(_fromUtf8("inputButton"))
        self.cancelButton = QtGui.QPushButton(readDialog)
        self.cancelButton.setGeometry(QtCore.QRect(240, 100, 101, 32))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.OKButton = QtGui.QPushButton(readDialog)
        self.OKButton.setGeometry(QtCore.QRect(120, 100, 114, 32))
        self.OKButton.setObjectName(_fromUtf8("OKButton"))

        self.retranslateUi(readDialog)
        QtCore.QMetaObject.connectSlotsByName(readDialog)

    def retranslateUi(self, readDialog):
        readDialog.setWindowTitle(QtGui.QApplication.translate("readDialog", "Coastal Mapping Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("readDialog", "Load or Create shapefile:", None, QtGui.QApplication.UnicodeUTF8))
        self.inputButton.setText(QtGui.QApplication.translate("readDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("readDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.OKButton.setText(QtGui.QApplication.translate("readDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

