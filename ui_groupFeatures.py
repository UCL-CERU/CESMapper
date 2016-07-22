# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_groupFeatures.ui'
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

class Ui_groupFeatures(object):
    def setupUi(self, groupFeatures):
        groupFeatures.setObjectName(_fromUtf8("groupFeatures"))
        groupFeatures.setWindowModality(QtCore.Qt.NonModal)
        groupFeatures.setEnabled(True)
        groupFeatures.resize(300, 350)
        groupFeatures.setModal(False)
        self.label = QtGui.QLabel(groupFeatures)
        self.label.setGeometry(QtCore.QRect(15, 15, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.doneButton = QtGui.QPushButton(groupFeatures)
        self.doneButton.setGeometry(QtCore.QRect(15, 210, 160, 35))
        self.doneButton.setAutoDefault(False)
        self.doneButton.setObjectName(_fromUtf8("doneButton"))
        self.clearButton = QtGui.QPushButton(groupFeatures)
        self.clearButton.setGeometry(QtCore.QRect(15, 250, 160, 35))
        self.clearButton.setAutoDefault(False)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.closeButton = QtGui.QPushButton(groupFeatures)
        self.closeButton.setGeometry(QtCore.QRect(190, 300, 100, 35))
        self.closeButton.setAutoDefault(False)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.selectGroup = QtGui.QGroupBox(groupFeatures)
        self.selectGroup.setGeometry(QtCore.QRect(15, 60, 270, 131))
        self.selectGroup.setTitle(_fromUtf8(""))
        self.selectGroup.setObjectName(_fromUtf8("selectGroup"))
        self.newButton = QtGui.QRadioButton(self.selectGroup)
        self.newButton.setGeometry(QtCore.QRect(15, 15, 100, 20))
        self.newButton.setChecked(True)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.grButtonGroup = QtGui.QButtonGroup(groupFeatures)
        self.grButtonGroup.setObjectName(_fromUtf8("grButtonGroup"))
        self.grButtonGroup.addButton(self.newButton)
        self.editButton = QtGui.QRadioButton(self.selectGroup)
        self.editButton.setGeometry(QtCore.QRect(130, 15, 100, 20))
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.grButtonGroup.addButton(self.editButton)
        self.selEditButton = QtGui.QPushButton(self.selectGroup)
        self.selEditButton.setEnabled(False)
        self.selEditButton.setGeometry(QtCore.QRect(140, 60, 120, 35))
        self.selEditButton.setAutoDefault(False)
        self.selEditButton.setObjectName(_fromUtf8("selEditButton"))
        self.unGroupButton = QtGui.QPushButton(self.selectGroup)
        self.unGroupButton.setEnabled(False)
        self.unGroupButton.setGeometry(QtCore.QRect(140, 90, 120, 35))
        self.unGroupButton.setAutoDefault(False)
        self.unGroupButton.setObjectName(_fromUtf8("unGroupButton"))

        self.retranslateUi(groupFeatures)
        QtCore.QMetaObject.connectSlotsByName(groupFeatures)

    def retranslateUi(self, groupFeatures):
        groupFeatures.setWindowTitle(_translate("groupFeatures", "CESMapper", None))
        self.label.setText(_translate("groupFeatures", "Select components to group:", None))
        self.doneButton.setText(_translate("groupFeatures", "Group Completed", None))
        self.clearButton.setText(_translate("groupFeatures", "Clear Selection", None))
        self.closeButton.setText(_translate("groupFeatures", "Close", None))
        self.newButton.setText(_translate("groupFeatures", "New Group", None))
        self.editButton.setText(_translate("groupFeatures", "Edit Group", None))
        self.selEditButton.setText(_translate("groupFeatures", "Select Group", None))
        self.unGroupButton.setText(_translate("groupFeatures", "Ungroup", None))

