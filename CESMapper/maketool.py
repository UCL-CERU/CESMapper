# -*- coding: utf-8 -*-
"""
/***************************************************************************
CESMapper             : Coastal and Estuarine System Mapping
                              CESMapper QGIS plugin
                              -------------------
        begin           : 2012-07-05
        copyright       : 2012-2016 G Thornhill, H Burningham, JR French,
                          and University College London (UCL) Coastal and 
                          Estuarine Research Unit
        original author : Gillian Thornhill (UCL)
        maintainer      : Helene Burningham (UCL - h.burningham@ucl.ac.uk)
        maintainer      : Jon French (UCL - j.french@ucl.ac.uk)
        version         : 1.5.2
        date            : 07-07-2016
        
        acknowledgement : This software was developed by UCL Coastal and 
                          Estuarine Research Unit as part of the NERC-funded
        				  Integrating COAstal Sediment sySTems (iCOASST) 
                          project (NE/J005541/1)   
        																		
Purpose:
 1. CESMapper implements the Coastal and Estuarine System Mapping (CESM) method
    as a plugin for the open-source QGIS
 2. CESM is described more fully in:
    French JR, Burningham H, Thornhill G, Whitehouse R & Nicholls R.J (2016) 
    Conceptualizing and mapping coupled estuary, coast and inner shelf sediment 
    systems. Geomorphology 256, 17-35 http://dx.doi.org/10.1016/j.geomorph.2015.10.006
    
Notes:
 1. This version of CESMapper is compatible with CESOML ontologies (libraries)
    at specification 1.6
 2. This version has been tested with QGIS 2.14.3 and may not function 
    correctly (or at all) with earlier builds
     
Acknowledgements:
 1.  Parts of the CESMapper code have been adapted from  the Rectangles Ovals 
     Digitizing plugin for QGIS (Copyright (C) 2011 - 2012 Pavol Kapusta)
 2.  This work has been funded by NERC as part of the Integrating COAstal 
     Sediment sySTems (iCOASST) project (NE/J005541/1) - www.icoasst.net   

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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

                        
                        
from PyQt4 import QtCore, QtGui
import math
from coastmap import *

# Initialize Qt resources from file resources.py
import resources_rc

                                                                                          
# This is the class for drawing the Rectangles, which eventually will have the 
# feature names
# This is subclassed from the QgsMapTool class, so has additional features.
    
class FeatureTool(QgsMapTool):
    releaseBut = QtCore.pyqtSignal(str)
    
    def __init__(self, canvas):
        # QgsMessageLog.logMessage("** FeatureTool:init")
        QgsMapTool.__init__(self, canvas)
        self.canvas=canvas
        self.x = 0
        self.y = 0
        self.name = ""
        self.pointMap = QgsPoint()
        self.screenPoint = QgsPoint()
        self.currentLevel = -1
        self.levelName = ""
        
    
    def canvasReleaseEvent(self,event):
        layer = self.canvas.currentLayer()
        self.pointScreen = event.pos()
        self.pointMap = self.toMapCoordinates(self.pointScreen)
        
        # QgsMessageLog.logMessage("Map  "+str(self.pointMap))
        # QgsMessageLog.logMessage("Raw  "+str(self.pointScreen))

        
        self.x = self.pointMap.x()
        self.y = self.pointMap.y()
        startPoint = QgsPoint(self.x, self.y)
        self.releaseBut.emit(self.name)
    
    def getPoint(self):
        return self.pointMap
    
    def getScreenPoint(self):
        return self.pointScreen
    
    def setName(self, nameIn):
        self.name = nameIn
    
    def getName(self):
        return self.name
    
    def setLevel(self, level):
        self.currentLevel = level
    
    def getLevel(self):
        return self.currentLevel
    
    
    def setLevelName(self, levelName):
        self.levelName = levelName

    def getLevelName(self):
        return self.levelName
    
    
    def isEditTool(self):
        return True

    def isZoomTool(self):
        return True
    
    def isTransient(self):
        return False

    def activate(self):
        pass
    
    def deactivate(self):
        pass
    

# ***************************************************************************
# ***************************************************************************

# This is the class that implements a selection tool.
# This is subclassed from the QgsMapToolEmitPoint class, so has additional features.
# Taken from QGIS Workshop
# Or have separate 'ClickTool' implementations for the different selection 
# requirements (or subclass it)


class ClickTool(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        # QgsMessageLog.logMessage("** ClickTool:init")
        QgsMapTool.__init__(self, canvas)
        self.canvas=canvas
        self.count = 0
        self.x = 0
        self.y = 0
        self.name = ""
        # These are for connecting, and could be separated into Linktool if we make it work.
        self.dir = 1
        self.type = "Mass flux" # (Other values are "Influence" or "Mixed")
        self.pointMap = QgsPoint()
        self.screenPoint = QgsPoint()
        self.selectId = []
        self.selectList = []
        self.selectFeat = []
    
    
    # Finds features on single selection
    def makeSelectList(self, point, button):
        QgsMessageLog.logMessage("** ClickTool:makeSelectList")
        # Should check if feature is in list - if it is, remove it.
        # reset selection list on each new selection
        # setup the provider select to filter results based on a rectangle
        self.layer = self.canvas.currentLayer()
        self.provider = self.layer.dataProvider()
        pntGeom = QgsGeometry.fromPoint(point)
        startingPoint = point
        # scale-dependent buffer of 10 pixels-worth of map units
        pntBuff = pntGeom.buffer( (self.canvas.mapUnitsPerPixel() * 10),0)
        rect = pntBuff.boundingBox()
        
        feat = QgsFeature()
        
        # create the select statement
        request=QgsFeatureRequest()
        request.setFilterRect(rect)
        
        for feat in self.layer.getFeatures(request):
            featBuff = feat.geometry().buffer((self.canvas.mapUnitsPerPixel() * 100),0)
            #  buffer((self.canvas.mapUnitsPerPixel() * 100),0)
            
            # if the feat geom returned from the selection intersects our point then put it in a list
            if featBuff.intersects(pntGeom):
                if feat.id() in self.selectId:
                    self.selectId.remove(feat.id())
                else:
                    self.selectId.append(feat.id())
                    self.selectFeat.append(feat)
        
        if self.selectId:
            # make the actual selection
            self.layer.setSelectedFeatures(self.selectId)



#   QMessageBox.information( self.iface.mainWindow(),"Info", "No layer currently selected in TOC" )
    def getSelectIdList(self):
        return self.selectId
    

    def getSelectFeatList(self):
        return self.selectFeat
    
    def clearSelectList(self):
        self.layer = self.canvas.currentLayer()
        self.provider = self.layer.dataProvider()
        self.selectId = []
        self.selectFeat = []
        self.layer.setSelectedFeatures(self.selectId)
        self.layer.editEnabled = True
        self.activate()
    
    def setName(self, nameIn):
        self.name = nameIn
    
    def getName(self):
        return self.name
    
    def getPoint(self):
        return self.pointMap
    
    def isEditTool(self):
        return True
    
    def isZoomTool(self):
        return False
    
    def isTransient(self):
        return False
    
    
    def activate(self):
        pass
    
    def deactivate(self):
        pass


# ******************** Code for rectangle extent - can have this or point selection, then do selection check separately.
            
#    def canvasPressEvent(self,event):
#            layer = self.canvas.currentLayer()
#            color = QColor(255,0,0)
#            self.rb = QgsRubberBand(self.canvas, True)
#            self.rb.setColor(color)
#            self.rb.setWidth(1)
#            x = event.pos().x()
#            y = event.pos().y()
#            point = self.toLayerCoordinates(layer,event.pos())
#            pointMap = self.toMapCoordinates(layer, point)
#            self.x0 = pointMap.x()
#            self.y0 = pointMap.y()
#            if self.rb:return
#                
#    def canvasMoveEvent(self,event):
#        if not self.rb:return
#        currpoint = self.toMapCoordinates(event.pos())
#        currx = currpoint.x()
#        curry = currpoint.y()
#        self.rb.reset(True)
#        pt1 = (self.x0, self.y0)
#        pt2 = (self.x0, curry)
#        pt3 = (currx, curry)
#        pt4 = (currx, self.y0)
#        points = [pt1, pt2, pt3, pt4]
#        polygon = [QgsPoint(i[0],i[1]) for i in points]
#        [self.rb.addPoint( point ) for point in polygon]
#
#
#    def canvasReleaseEvent(self,event):
#        if not self.rb:return		
#        if self.rb.numberOfVertices() > 2:
#            geom = self.rb.asGeometry()
#            self.emit(SIGNAL("rbFinished(PyQt_PyObject)"), geom)
#        
#        self.rb.reset(True)
#        self.rb=None
#        self.canvas.refresh()
#
#    
# ******************** Code for Group tool **************************************
            
class GroupTool(ClickTool):
    def __init__(self, canvas):
        QgsMapTool.__init__(self, canvas)
        self.canvas=canvas
        self.count = 0
        self.x = 0
        self.y = 0
        self.name = ""
        self.pointMap = QgsPoint()
        self.selectId = []
        self.selectList = []
        self.selectFeat = []

# ******************** Code for Link tool **************************************
# This is the class for drawing the links, but currently using the clicktool for the selections.
# This is subclassed from the QgsMapTool class, so has inherits from that.
# It has no real fundtionality yet...

class LinkTool(ClickTool):
    def __init__(self, canvas):
        QgsMapTool.__init__(self, canvas)
        self.canvas=canvas
        self.count = 0
        self.x = 0
        self.y = 0
        self.pointMap = QgsPoint()
        self.selectList = []
        self.selectId = []
        self.selectFeat = []
        self.dir = 1
        self.type = "Mass flux" # (Other values are "Influence" or "Mixed")

            
    def setDir(self, dirIn):
        if dirIn == "Bidirectional":
            self.dir = 2
        if dirIn == "Unidirectional":
            self.dir = 1
        if dirIn == "Uncertain":
            self.dir = 0

    def getDir(self):
        return self.dir

    def setType(self, typeIn):
        self.type = typeIn

    def getType(self):
        return self.type

# ******************** Code for Edit tool **************************************

class MoveTool(ClickTool, QgsMapTool):
    
    releaseMouse = QtCore.pyqtSignal(str)
    
    def __init__(self, canvas):
        QgsMapTool.__init__(self, canvas)
        self.canvas=canvas
        self.count = 0
        self.x = 0
        self.y = 0
        self.name = ""
        self.pointMap = QgsPoint()
        self.pointScreen = QgsPoint()
        self.selectId = []
        self.selectList = []
        self.selectFeat = []


    def canvasMoveEvent(self, event):
        #QgsMessageLog.logMessage("In processClick")
        if event.buttons() == Qt.LeftButton:
            if event.type() == QEvent.MouseMove:
                pos = event.pos()
                self.x = pos.x()
                self.y = pos.y()
                self.pointScreen = event.pos()
                self.pointMap = self.canvas.getCoordinateTransform().toMapCoordinates(self.x, self.y)
        else:
            pass

    def canvasReleaseEvent(self, event):
        self.releaseMouse.emit("Emitted")
    

    def getPoint(self):
        return self.pointMap
    
    def getScreenPoint(self):
        return self.pointScreen


# ******************** Code for Delete tool **************************************

class DelCompTool(ClickTool):
    
    releaseDel = QtCore.pyqtSignal(str)
    
    def __init__(self, canvas):
        QgsMapTool.__init__(self, canvas)
        self.canvas=canvas
        self.count = 0
        self.x = 0
        self.y = 0
        self.name = ""
        self.pointMap = QgsPoint()
        self.selectId = []
        self.selectList = []
        self.selectFeat = []


    def canvasReleaseEvent(self, event):
        self.releaseDel.emit("Delete")


           
