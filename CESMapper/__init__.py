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

 ***************************************************************************/
 
 
 /***************************************************************************
 *  This script initializes the CESMapper plugin, making it known to QGIS   *
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

def classFactory(iface):
    # load CESMtool class from file coastmap
    from coastmap import CESMtool
    return CESMtool(iface)

