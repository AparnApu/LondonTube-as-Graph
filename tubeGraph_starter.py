# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:59:07 2020

@author: apuap
"""
from myTubeClassModule import Tube

LondonTube = Tube()

###########################################
# File names
###########################################

dataPath = '..\\dataset\\'

tubeNamesFile= 'london.stations.csv'
ConnectionsFile= 'london.connections.csv'
lineNamesFile= 'london.lines.csv'

LondonTube = Tube()

###########################################
# Load database
###########################################

LondonTube.load_tubeNamesFile(tubeNamesFile)
LondonTube.load_ConnectionsFile(ConnectionsFile)
LondonTube.load_lineNamesFile(lineNamesFile)

###########################################
# Allocate all data to graph
###########################################

LondonTube.allocateDatatoGraph()

###########################################
# Plotting whole map
###########################################

tranp = 0.8
en_lab = True
fignum = 1

LondonTube.plot_wholeTubeMap(tranp, en_lab, fignum)

###########################################
# User Input
###########################################

# test case 1

StationFrom = "Chesham"
StationTo = "Morden"

# test case 2

#StationFrom = "Chesham"
#StationTo = "Epping"

###########################################
# Checking Input
###########################################

LondonTube.input_check(StationFrom, StationTo)

###########################################
# Highlight shortest path
###########################################

LondonTube.compute_shortest_path(StationFrom,StationTo)
LondonTube.plot_mypath_wrapper()

###########################################
# display shortest path details
###########################################

LondonTube.detail_display()