# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_displayOptions.ui'
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

class Ui_displayOptions(object):
    def setupUi(self, displayOptions):
        displayOptions.setObjectName(_fromUtf8("displayOptions"))
        displayOptions.setWindowModality(QtCore.Qt.NonModal)
        displayOptions.resize(375, 369)
        displayOptions.setModal(False)
        self.label = QtGui.QLabel(displayOptions)
        self.label.setGeometry(QtCore.QRect(15, 15, 350, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.showButton = QtGui.QPushButton(displayOptions)
        self.showButton.setGeometry(QtCore.QRect(20, 260, 200, 35))
        self.showButton.setAutoDefault(False)
        self.showButton.setObjectName(_fromUtf8("showButton"))
        self.closeButton = QtGui.QPushButton(displayOptions)
        self.closeButton.setGeometry(QtCore.QRect(230, 310, 120, 35))
        self.closeButton.setAutoDefault(False)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayoutWidget = QtGui.QWidget(displayOptions)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 281, 141))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.retranslateUi(displayOptions)
        QtCore.QMetaObject.connectSlotsByName(displayOptions)

    def retranslateUi(self, displayOptions):
        displayOptions.setWindowTitle(_translate("displayOptions", "CESMapper", None))
        self.label.setText(_translate("displayOptions", "Select level of components to display:", None))
        self.showButton.setText(_translate("displayOptions", "Show ", None))
        self.closeButton.setText(_translate("displayOptions", "Close", None))

