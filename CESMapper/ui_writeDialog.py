# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_writeDialog.ui'
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

class Ui_writeDialog(object):
    def setupUi(self, writeDialog):
        writeDialog.setObjectName(_fromUtf8("writeDialog"))
        writeDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        writeDialog.resize(350, 155)
        writeDialog.setMinimumSize(QtCore.QSize(350, 155))
        writeDialog.setMaximumSize(QtCore.QSize(350, 155))
        writeDialog.setSizeGripEnabled(False)
        writeDialog.setModal(True)
        self.output = QtGui.QLineEdit(writeDialog)
        self.output.setGeometry(QtCore.QRect(10, 40, 251, 21))
        self.output.setReadOnly(True)
        self.output.setObjectName(_fromUtf8("output"))
        self.label = QtGui.QLabel(writeDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.outputButton = QtGui.QPushButton(writeDialog)
        self.outputButton.setGeometry(QtCore.QRect(270, 40, 75, 23))
        self.outputButton.setObjectName(_fromUtf8("outputButton"))
        self.cancelButton = QtGui.QPushButton(writeDialog)
        self.cancelButton.setGeometry(QtCore.QRect(240, 100, 101, 32))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.createButton = QtGui.QPushButton(writeDialog)
        self.createButton.setGeometry(QtCore.QRect(120, 100, 114, 32))
        self.createButton.setObjectName(_fromUtf8("createButton"))

        self.retranslateUi(writeDialog)
        QtCore.QMetaObject.connectSlotsByName(writeDialog)

    def retranslateUi(self, writeDialog):
        writeDialog.setWindowTitle(QtGui.QApplication.translate("writeDialog", "Coastal Mapping Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("writeDialog", "Output shapefile:", None, QtGui.QApplication.UnicodeUTF8))
        self.outputButton.setText(QtGui.QApplication.translate("writeDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("writeDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.createButton.setText(QtGui.QApplication.translate("writeDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

