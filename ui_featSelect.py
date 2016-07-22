# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_featSelect.ui'
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

class Ui_featSelect(object):
    def setupUi(self, featSelect):
        featSelect.setObjectName(_fromUtf8("featSelect"))
        featSelect.setWindowModality(QtCore.Qt.NonModal)
        featSelect.resize(350, 646)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(featSelect.sizePolicy().hasHeightForWidth())
        featSelect.setSizePolicy(sizePolicy)
        featSelect.setModal(True)
        self.label = QtGui.QLabel(featSelect)
        self.label.setGeometry(QtCore.QRect(25, 25, 250, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayoutWidget = QtGui.QWidget(featSelect)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 80, 251, 461))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stopButton = QtGui.QPushButton(featSelect)
        self.stopButton.setGeometry(QtCore.QRect(75, 580, 200, 35))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))

        self.retranslateUi(featSelect)
        QtCore.QMetaObject.connectSlotsByName(featSelect)

    def retranslateUi(self, featSelect):
        featSelect.setWindowTitle(_translate("featSelect", "CESMapper", None))
        self.label.setText(_translate("featSelect", "Select complex to map:", None))
        self.stopButton.setText(_translate("featSelect", "Finished Mapping", None))

