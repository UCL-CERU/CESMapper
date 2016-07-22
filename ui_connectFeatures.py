# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_connectFeatures.ui'
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

class Ui_connectFeatures(object):
    def setupUi(self, connectFeatures):
        connectFeatures.setObjectName(_fromUtf8("connectFeatures"))
        connectFeatures.setWindowModality(QtCore.Qt.NonModal)
        connectFeatures.resize(325, 388)
        connectFeatures.setModal(False)
        self.label = QtGui.QLabel(connectFeatures)
        self.label.setGeometry(QtCore.QRect(15, 15, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.doneButton = QtGui.QPushButton(connectFeatures)
        self.doneButton.setGeometry(QtCore.QRect(10, 275, 200, 35))
        self.doneButton.setAutoDefault(False)
        self.doneButton.setObjectName(_fromUtf8("doneButton"))
        self.clearButton = QtGui.QPushButton(connectFeatures)
        self.clearButton.setGeometry(QtCore.QRect(10, 305, 200, 35))
        self.clearButton.setAutoDefault(False)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.closeButton = QtGui.QPushButton(connectFeatures)
        self.closeButton.setGeometry(QtCore.QRect(190, 345, 120, 35))
        self.closeButton.setAutoDefault(False)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.TypeButtonBox = QtGui.QGroupBox(connectFeatures)
        self.TypeButtonBox.setGeometry(QtCore.QRect(20, 50, 161, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TypeButtonBox.setFont(font)
        self.TypeButtonBox.setObjectName(_fromUtf8("TypeButtonBox"))
        self.massButton = QtGui.QRadioButton(self.TypeButtonBox)
        self.massButton.setGeometry(QtCore.QRect(20, 30, 102, 20))
        self.massButton.setChecked(True)
        self.massButton.setObjectName(_fromUtf8("massButton"))
        self.typeGroup = QtGui.QButtonGroup(connectFeatures)
        self.typeGroup.setObjectName(_fromUtf8("typeGroup"))
        self.typeGroup.addButton(self.massButton)
        self.influButton = QtGui.QRadioButton(self.TypeButtonBox)
        self.influButton.setGeometry(QtCore.QRect(20, 50, 102, 20))
        self.influButton.setObjectName(_fromUtf8("influButton"))
        self.typeGroup.addButton(self.influButton)
        self.mixedButton = QtGui.QRadioButton(self.TypeButtonBox)
        self.mixedButton.setGeometry(QtCore.QRect(20, 70, 102, 20))
        self.mixedButton.setAutoExclusive(True)
        self.mixedButton.setObjectName(_fromUtf8("mixedButton"))
        self.typeGroup.addButton(self.mixedButton)
        self.directBox = QtGui.QGroupBox(connectFeatures)
        self.directBox.setGeometry(QtCore.QRect(20, 160, 161, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.directBox.setFont(font)
        self.directBox.setObjectName(_fromUtf8("directBox"))
        self.uncertainButton = QtGui.QRadioButton(self.directBox)
        self.uncertainButton.setGeometry(QtCore.QRect(20, 70, 102, 20))
        self.uncertainButton.setObjectName(_fromUtf8("uncertainButton"))
        self.directGroup = QtGui.QButtonGroup(connectFeatures)
        self.directGroup.setObjectName(_fromUtf8("directGroup"))
        self.directGroup.addButton(self.uncertainButton)
        self.uniDirButton = QtGui.QRadioButton(self.directBox)
        self.uniDirButton.setGeometry(QtCore.QRect(20, 30, 131, 20))
        self.uniDirButton.setChecked(True)
        self.uniDirButton.setObjectName(_fromUtf8("uniDirButton"))
        self.directGroup.addButton(self.uniDirButton)
        self.biDirButton = QtGui.QRadioButton(self.directBox)
        self.biDirButton.setGeometry(QtCore.QRect(20, 50, 121, 20))
        self.biDirButton.setObjectName(_fromUtf8("biDirButton"))
        self.directGroup.addButton(self.biDirButton)

        self.retranslateUi(connectFeatures)
        QtCore.QMetaObject.connectSlotsByName(connectFeatures)

    def retranslateUi(self, connectFeatures):
        connectFeatures.setWindowTitle(_translate("connectFeatures", "CESMapper", None))
        self.label.setText(_translate("connectFeatures", "Select components to connect:", None))
        self.doneButton.setText(_translate("connectFeatures", "Connection Completed", None))
        self.clearButton.setText(_translate("connectFeatures", "Clear Selection", None))
        self.closeButton.setText(_translate("connectFeatures", "Close", None))
        self.TypeButtonBox.setTitle(_translate("connectFeatures", "Connection Type", None))
        self.massButton.setText(_translate("connectFeatures", "Mass flux", None))
        self.influButton.setText(_translate("connectFeatures", "Influence", None))
        self.mixedButton.setText(_translate("connectFeatures", "Mixed", None))
        self.directBox.setTitle(_translate("connectFeatures", "Arrow Direction", None))
        self.uncertainButton.setText(_translate("connectFeatures", "Uncertain", None))
        self.uniDirButton.setText(_translate("connectFeatures", "Unidirectional", None))
        self.biDirButton.setText(_translate("connectFeatures", "Bidirectional", None))

