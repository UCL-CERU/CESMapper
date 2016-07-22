# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_initialise.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_initialise(object):
    def setupUi(self, initialise):
        initialise.setObjectName(_fromUtf8("initialise"))
        initialise.setEnabled(True)
        initialise.resize(400, 200)
        initialise.setWindowOpacity(0.9)
        self.Mainlabel = QtGui.QLabel(initialise)
        self.Mainlabel.setGeometry(QtCore.QRect(70, 70, 170, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Mainlabel.setFont(font)
        self.Mainlabel.setObjectName(_fromUtf8("Mainlabel"))
        self.loadButton = QtGui.QPushButton(initialise)
        self.loadButton.setEnabled(True)
        self.loadButton.setGeometry(QtCore.QRect(50, 140, 300, 35))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.Mainlabel_2 = QtGui.QLabel(initialise)
        self.Mainlabel_2.setGeometry(QtCore.QRect(24, 25, 352, 24))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Mainlabel_2.setFont(font)
        self.Mainlabel_2.setObjectName(_fromUtf8("Mainlabel_2"))
        self.label = QtGui.QLabel(initialise)
        self.label.setGeometry(QtCore.QRect(280, 70, 50, 50))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("img/CESM50.png")))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(initialise)
        QtCore.QMetaObject.connectSlotsByName(initialise)

    def retranslateUi(self, initialise):
        initialise.setWindowTitle(_translate("initialise", "CESMapper", None))
        self.Mainlabel.setText(_translate("initialise", "CESMapper", None))
        self.loadButton.setText(_translate("initialise", "Load CESM ontology library file", None))
        self.Mainlabel_2.setText(_translate("initialise", "Coastal and Estuarine System Mapping", None))

