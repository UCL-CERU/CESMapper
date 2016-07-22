
"""
/***************************************************************************
CESMapper             : Coastal and Estuarine System Mapping
                              CESMapper QGIS plugin
                              -------------------
 coastmapdialog.py   -  handles generation of the various dialog boxes
  
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 * Copyright (c) <2012,2013,2015,2016>                                     *
 <               <G Thornhill, H Burningham, JR French, and                *
 *                UCL Coastal and Estuarine Research Unit>                 *
 *                                                                         *
 * This file is part of CESMapper                                          *
 *                                                                         *
 *  CESMapper is free software: you can redistribute it and/or modify      *
 *  it under the terms of the GNU General Public License as published by   *
 *  the Free Software Foundation, either version 3 of the License, or      *
 *  (at your option) any later version.                                    *
 *                                                                         *
 *  CESMapper is distributed in the hope that it will be useful,           *
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of         *
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
 *  GNU General Public License for more details.                           *
 *                                                                         *
 *  You should have received a copy of the GNU General Public License      *
 *  along with CESMapper.  If not, see <http://www.gnu.org/licenses/>.     *
 *                                                                         *
 ***************************************************************************/
"""


import os.path
import operator


from PyQt4 import QtCore, QtGui

from qgis.core import *

import sys

from coastmap import *

from ui_initialise import Ui_initialise
from ui_coastmap import Ui_CoastMap
from ui_featSelect import Ui_featSelect
from ui_readDialog import Ui_readDialog
from ui_writeDialog import Ui_writeDialog
from ui_groupFeatures import Ui_groupFeatures
from ui_connectFeatures import Ui_connectFeatures
from ui_editFeatures import Ui_editFeatures
from ui_displayOptions import Ui_displayOptions

# create the dialog for adding layer

class CoastMapDialog(QtGui.QDialog):
    def __init__(self):
        # QgsMessageLog.logMessage("** CoastMapDlg:init")
        # QtGui.QDialog.__init__(self)
        QtGui.QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        # Set up the user interface from Designer.
        self.ui = Ui_CoastMap()
        self.ui.setupUi(self)
        self.ui.layout = self.ui.verticalLayout
        self.ui.buttonGroup = QtGui.QButtonGroup(self.ui.layout)
    
     
    def addNewButton(self, name, level):
        # QgsMessageLog.logMessage("** CoastMapDlg:addNewButton")
        butName = name+"Button"
        self.butNew = QtGui.QPushButton(self)
        self.butNew.setObjectName(butName)
        self.butNew.setText(name)
        self.ui.buttonGroup.addButton(self.butNew, level)
        self.ui.layout.addWidget(self.butNew)
        self.butNew.setEnabled(True)
        

# *********************************************************************

class InitialiseDialog(QtGui.QDialog):
    def __init__(self):
        # QgsMessageLog.logMessage("** InitialiseDlg:init")
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_initialise()
        self.ui.setupUi(self)

# *********************************************************************

class GroupFeatures(QtGui.QDialog):
    def __init__(self):
        # QgsMessageLog.logMessage("** GroupFeaturesDlg:init")
        QtGui.QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        # Set up the user interface from Designer.
        self.ui = Ui_groupFeatures()
        self.ui.setupUi(self)

    def getRadioSelect(self):
        # QgsMessageLog.logMessage("** GroupFeaturesDlg:getRadioSelect")
        button = self.ui.butonGroup.checkedButton()
        choice = button.text()
        return choice

# *********************************************************************

class ConnectFeatures(QtGui.QDialog):
    def __init__(self):
        # QgsMessageLog.logMessage("** ConnectFeaturesDlg:init")
        QtGui.QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        # Set up the user interface from Designer.
        self.ui = Ui_connectFeatures()
        self.ui.setupUi(self)

    def getType(self):
        # QgsMessageLog.logMessage("** ConnectFeaturesDlg:getType")
        button = self.ui.typeGroup.checkedButton()
        retType = button.text()
        return retType

    def getDir(self):
        # QgsMessageLog.logMessage("** ConnectFeaturesDlg:getDir")
        button = self.ui.directGroup.checkedButton()
        retDir = button.text()
        return retDir


# *********************************************************************

class SelectFeature(QtGui.QDialog):
    def __init__(self):
        # QgsMessageLog.logMessage("** SelectFeaturesDlg:init")
        QtGui.QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.ui = Ui_featSelect()
        self.ui.setupUi(self)        
        #self.ui.defButton.setOn(True)
        self.ui.layout = self.ui.verticalLayout
        self.ui.buttonGroup = QtGui.QButtonGroup(self.ui.layout)
    
    def setLevelName(self, levelLabel):
        # QgsMessageLog.logMessage("** SelectFeaturesDlg:setLevelName")
        self.levelName = levelLabel
        self.ui.label.setText("Select "+self.levelName+" to map:")
    
    def addNewLabel(self, subLabel):
        # QgsMessageLog.logMessage("** SelectFeaturesDlg:addNewLabel")
        self.labNew = QtGui.QLabel(self)
        self.labNew.setGeometry(QtCore.QRect(40, 20, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labNew.setFont(font)
        self.labNew.setWordWrap(True)
        self.labNew.setText(subLabel)
        self.ui.layout.addWidget(self.labNew)

    
    def addNewButton(self, name):
        # QgsMessageLog.logMessage("** SelectFeaturesDlg:addNewButton")
        butName = name+"Button"
        self.butNew = QtGui.QRadioButton(self)
        self.butNew.setObjectName(butName)
        self.butNew.setText(name)
        self.ui.layout.addWidget(self.butNew)
        self.ui.buttonGroup.addButton(self.butNew)
    
    def getSelect(self):
        # QgsMessageLog.logMessage("** SelectFeaturesDlg:getSelect")
        button = self.ui.buttonGroup.checkedButton()
        retString = button.text()
        return retString

# *********************************************************************

class EditFeatures(QtGui.QDialog):
    def __init__(self):
        # QgsMessageLog.logMessage("** EditDlg:init")
        QtGui.QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.ui = Ui_editFeatures()
        self.ui.setupUi(self)

# *********************************************************************

class DisplayOptions(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.ui = Ui_displayOptions()
        self.ui.setupUi(self)
        self.ui.layout = self.ui.verticalLayout
        self.ui.buttonGroup = QtGui.QButtonGroup(self.ui.layout)

    
    def getLevel(self):
        button = self.ui.buttonGroup.checkedButton()
        level = button.objectName()
        return level

        
    def addNewButton(self, orderLabel, order):
        # QgsMessageLog.logMessage("** SelectFeaturesDlg:addNewButton")
        butName = str(order)
        self.butNew = QtGui.QRadioButton(self)
        self.butNew.setObjectName(butName)
        self.butNew.setText(orderLabel)
        self.ui.layout.addWidget(self.butNew)
        self.ui.buttonGroup.addButton(self.butNew)


# *********************************************************************

class WriteDialog(QtGui.QDialog):
    def __init__(self):
        # QgsMessageLog.logMessage("** WriteDlg:init")
        QtGui.QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.ui = Ui_writeDialog()
        self.ui.setupUi(self)
                  
    
## *********************************************************************

class ReadDialog(QtGui.QDialog):
    def __init__(self):
        # QgsMessageLog.logMessage("** ReadDlg:init")
        QtGui.QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.ui = Ui_readDialog()
        self.ui.setupUi(self)

