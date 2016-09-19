# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_coastmap.ui'
#
# Created: Tue Aug 16 23:41:19 2016
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

class Ui_CoastMap(object):
    def setupUi(self, CoastMap):
        CoastMap.setObjectName(_fromUtf8("CoastMap"))
        CoastMap.setWindowModality(QtCore.Qt.NonModal)
        CoastMap.resize(500, 400)
        CoastMap.setWindowOpacity(0.9)
        CoastMap.setModal(False)
        self.linkButton = QtGui.QPushButton(CoastMap)
        self.linkButton.setGeometry(QtCore.QRect(300, 80, 150, 35))
        self.linkButton.setAutoDefault(False)
        self.linkButton.setObjectName(_fromUtf8("linkButton"))
        self.saveButton = QtGui.QPushButton(CoastMap)
        self.saveButton.setGeometry(QtCore.QRect(300, 280, 150, 35))
        self.saveButton.setAutoDefault(False)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.label = QtGui.QLabel(CoastMap)
        self.label.setGeometry(QtCore.QRect(120, 15, 170, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.cancelButton = QtGui.QPushButton(CoastMap)
        self.cancelButton.setGeometry(QtCore.QRect(350, 330, 100, 35))
        self.cancelButton.setAutoDefault(False)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.verticalLayoutWidget = QtGui.QWidget(CoastMap)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 221, 231))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.editButton = QtGui.QPushButton(CoastMap)
        self.editButton.setEnabled(True)
        self.editButton.setGeometry(QtCore.QRect(300, 160, 150, 35))
        self.editButton.setAutoDefault(False)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.analyseButton = QtGui.QPushButton(CoastMap)
        self.analyseButton.setEnabled(False)
        self.analyseButton.setGeometry(QtCore.QRect(300, 200, 150, 35))
        self.analyseButton.setObjectName(_fromUtf8("analyseButton"))
        self.displayButton = QtGui.QPushButton(CoastMap)
        self.displayButton.setEnabled(True)
        self.displayButton.setGeometry(QtCore.QRect(15, 330, 150, 35))
        self.displayButton.setAutoDefault(False)
        self.displayButton.setObjectName(_fromUtf8("displayButton"))
        self.loadMapButton = QtGui.QPushButton(CoastMap)
        self.loadMapButton.setGeometry(QtCore.QRect(300, 240, 150, 35))
        self.loadMapButton.setObjectName(_fromUtf8("loadMapButton"))
        self.groupButton = QtGui.QPushButton(CoastMap)
        self.groupButton.setGeometry(QtCore.QRect(300, 120, 150, 35))
        self.groupButton.setAutoDefault(False)
        self.groupButton.setObjectName(_fromUtf8("groupButton"))
        self.label_2 = QtGui.QLabel(CoastMap)
        self.label_2.setGeometry(QtCore.QRect(300, 15, 50, 50))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/CESM50.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(CoastMap)
        QtCore.QMetaObject.connectSlotsByName(CoastMap)

    def retranslateUi(self, CoastMap):
        CoastMap.setWindowTitle(_translate("CoastMap", "CESMapper", None))
        self.linkButton.setText(_translate("CoastMap", "Link Components", None))
        self.saveButton.setText(_translate("CoastMap", "Save/Create Map", None))
        self.label.setText(_translate("CoastMap", "CESMapper", None))
        self.cancelButton.setText(_translate("CoastMap", "Exit", None))
        self.editButton.setText(_translate("CoastMap", "Edit Map", None))
        self.analyseButton.setText(_translate("CoastMap", "Analyse", None))
        self.displayButton.setText(_translate("CoastMap", "Display Options", None))
        self.loadMapButton.setText(_translate("CoastMap", "Load Map", None))
        self.groupButton.setText(_translate("CoastMap", "Group Components", None))

