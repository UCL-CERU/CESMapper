# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_initialise.ui'
#
# Created: Tue Aug  2 23:14:17 2016
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

class Ui_initialise(object):
    def setupUi(self, initialise):
        initialise.setObjectName(_fromUtf8("initialise"))
        initialise.setEnabled(True)
        initialise.resize(526, 277)
        initialise.setWindowOpacity(0.9)
        self.Mainlabel = QtGui.QLabel(initialise)
        self.Mainlabel.setGeometry(QtCore.QRect(140, 70, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Mainlabel.setFont(font)
        self.Mainlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Mainlabel.setObjectName(_fromUtf8("Mainlabel"))
        self.loadButton = QtGui.QPushButton(initialise)
        self.loadButton.setEnabled(True)
        self.loadButton.setGeometry(QtCore.QRect(100, 210, 300, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loadButton.setFont(font)
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.Mainlabel_2 = QtGui.QLabel(initialise)
        self.Mainlabel_2.setGeometry(QtCore.QRect(20, 20, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Mainlabel_2.setFont(font)
        self.Mainlabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Mainlabel_2.setObjectName(_fromUtf8("Mainlabel_2"))
        self.label = QtGui.QLabel(initialise)
        self.label.setGeometry(QtCore.QRect(220, 130, 50, 50))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("img/CESM50.png")))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(initialise)
        QtCore.QMetaObject.connectSlotsByName(initialise)

    def retranslateUi(self, initialise):
        initialise.setWindowTitle(_translate("initialise", "CESMapper", None))
        self.Mainlabel.setText(_translate("initialise", "CESMapper", None))
        self.loadButton.setText(_translate("initialise", "Load CESM ontology", None))
        self.Mainlabel_2.setText(_translate("initialise", "Coastal and Estuarine System Mapping", None))

import images_rc
