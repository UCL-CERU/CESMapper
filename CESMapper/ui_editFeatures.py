# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_editFeatures.ui'
#
# Created: Tue Aug 16 23:41:20 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_editFeatures(object):
    def setupUi(self, editFeatures):
        editFeatures.setObjectName(_fromUtf8("editFeatures"))
        editFeatures.setWindowModality(QtCore.Qt.NonModal)
        editFeatures.resize(300, 300)
        editFeatures.setModal(False)
        self.label = QtGui.QLabel(editFeatures)
        self.label.setGeometry(QtCore.QRect(15, 15, 250, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.moveButton = QtGui.QPushButton(editFeatures)
        self.moveButton.setGeometry(QtCore.QRect(20, 90, 200, 35))
        self.moveButton.setAutoDefault(False)
        self.moveButton.setObjectName(_fromUtf8("moveButton"))
        self.removeButton = QtGui.QPushButton(editFeatures)
        self.removeButton.setGeometry(QtCore.QRect(20, 130, 200, 35))
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.closeButton = QtGui.QPushButton(editFeatures)
        self.closeButton.setGeometry(QtCore.QRect(160, 240, 120, 35))
        self.closeButton.setAutoDefault(False)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.doneButton = QtGui.QPushButton(editFeatures)
        self.doneButton.setGeometry(QtCore.QRect(20, 180, 200, 35))
        self.doneButton.setAutoDefault(False)
        self.doneButton.setObjectName(_fromUtf8("doneButton"))

        self.retranslateUi(editFeatures)
        QtCore.QMetaObject.connectSlotsByName(editFeatures)

    def retranslateUi(self, editFeatures):
        editFeatures.setWindowTitle(_translate("editFeatures", "CESMapper", None))
        self.label.setText(_translate("editFeatures", "Select components to edit:", None))
        self.moveButton.setText(_translate("editFeatures", "Move Component", None))
        self.removeButton.setText(_translate("editFeatures", "Remove Component", None))
        self.closeButton.setText(_translate("editFeatures", "Close", None))
        self.doneButton.setText(_translate("editFeatures", "Done Editing", None))

