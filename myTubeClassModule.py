# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:22:50 2020

@author: apuap
"""

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import sys

class Tube:

###########################################
# _init_ function
###########################################
    
    def __init__(self):
        
        plt.close('all')

        self.G = nx.Graph()
                
        return

###########################################
# loading stations csv into nodesdata
        
# storing number of rows in csv 
###########################################
        
    def load_tubeNamesFile(self, stations):
        
        self.nodesdata = pd.read_csv(stations)
        self.length_nodes = len(self.nodesdata.index)
        
        return

###########################################
# loading connections csv into edgedata
        
# storing number of rows in csv 
###########################################
        
    def load_ConnectionsFile(self, connections):
        
        self.edgedata = pd.read_csv(connections)
        self.length_edges = len(self.edgedata.index)
        
        return 

###########################################
# loading lines csv into linedata
        
# storing number of rows in csv 
###########################################
        
    def load_lineNamesFile(self, lines):
        
        self.linedata = pd.read_csv(lines)
        self.length_lines = len(self.linedata.index)
        
        return    
    
###########################################
# creating nodes
        # list of station names: station_list
    
# creating edges
        # list of edge pairs: name_pairs
    
# adding edge attributes (line, time/weight)
        # attribute dictionary: MainDict_edge
                # Dict of dict
       
# adding node attributes (latitude, longitude)
        # attribute dictionary: MainDict_node
                # Dict of dict
    
#creating dict where,
        # line numbers as keys and line colours as values
###########################################
        
    def allocateDatatoGraph(self):
                
        self.station_list = self.nodesdata["name"]
        self.G.add_nodes_from(self.station_list)
        
        self.id_dict = {}
        
        keyx = self.nodesdata["id"]
        valx = self.nodesdata["name"]
        
        for i in range(len(keyx)):
            self.id_dict[keyx[i]] = valx[i]
        
        self.name_pairs = []

        for i in range(self.length_edges):
            temp1 = self.edgedata['station1'][i]
            temp2 = self.edgedata['station2'][i]
            station1_name = self.id_dict[temp1]
            station2_name = self.id_dict[temp2]
            tuple_temp = (station1_name, station2_name)
            self.name_pairs.append(tuple_temp)
            
        self.G.add_edges_from(self.name_pairs, time = self.edgedata['time'])
        
        self.MainDict_edge = {}
        row_name_edge = ['line', 'time']

        for i in range(self.length_edges):
   
            edgeDict = {}
            edge_name = self.name_pairs[i]
        
            for j in range(2):     
                keyx = row_name_edge[j]
                valx = self.edgedata[row_name_edge[j]][i]        
                edgeDict[keyx] = valx
        
            self.MainDict_edge[edge_name] = edgeDict
            
        nx.set_edge_attributes(self.G, self.MainDict_edge)
        
        
        self.MainDict_node = {}
        row_name_node = ['latitude', 'longitude']
        
        for i in range(self.length_nodes):
   
            nodeDict = {}
            node_name = self.station_list[i]
        
            for j in range(2):     
                keyx = row_name_node[j]
                valx = self.nodesdata[row_name_node[j]][i]        
                nodeDict[keyx] = valx
        
            self.MainDict_node[node_name] = nodeDict
            
        nx.set_node_attributes(self.G, self.MainDict_node)
            
        self.Dict_line = {}
        keyx = self.linedata['line']
        valx = self.linedata['colour']
        for j in range(self.length_lines):
            self.Dict_line[keyx[j]] = valx[j]
            
        return

###########################################
# plot whole london tube map as figure 1
###########################################    
        
    def plot_wholeTubeMap(self, tranpBack, en_labBack, fignumBack):

        plt.figure(fignumBack, figsize = (16, 9))
        plt.grid(True)

        for i in range(self.length_nodes):          #plotting nodes as points
            
            temp_lat1 = self.MainDict_node[self.station_list[i]]['latitude']    
            temp_lon1 = self.MainDict_node[self.station_list[i]]['longitude']
            plt.scatter(temp_lon1, temp_lat1, alpha = tranpBack, facecolors='none', edgecolors='black', s = 80)
            if en_labBack:
                plt.text(temp_lon1, temp_lat1, self.station_list[i], alpha = 0.8)
        
        for i in range(self.length_edges):          #plotting edge lines      
            
            whole_x1 = self.MainDict_node[self.name_pairs[i][0]]['longitude']
            whole_y1 = self.MainDict_node[self.name_pairs[i][0]]['latitude']
            whole_x2 = self.MainDict_node[self.name_pairs[i][1]]['longitude']
            whole_y2 = self.MainDict_node[self.name_pairs[i][1]]['latitude']

            line_num = self.G.edges[self.name_pairs[i]]['line']
            self.line_col = self.Dict_line[line_num]
                
            plt.plot((whole_x1, whole_x2), (whole_y1, whole_y2), color = self.line_col, lw = 4, alpha = tranpBack)
            
        return

###########################################
# creating list pair_path

# pairs of edges involved in shortest path
###########################################
    
    def compute_shortest_path(self, StationFrom, StationTo):
        
        self.short_path = nx.shortest_path(self.G, StationFrom, StationTo, weight = 'time')
        self.pair_path = []
        
        for i in range(len(self.short_path)-1):
            temp_tuple=(self.short_path[i], self.short_path[i+1])
            self.pair_path.append(temp_tuple)
            
        return

###########################################
# check input
###########################################
    
    def input_check(self, StationFrom, StationTo):
        
        if  not (StationFrom in self.G.nodes):
            print("First input is incorrect. Check for spelling and try again. \n\nProgram will exit now.")
            sys(exit)
            
        elif not (StationTo in self.G.nodes):
            print("Second input is incorrect. Check for spelling and try again. \n\nProgram will exit now.")
            sys.exit()
        
        else:
            print("Inputs found. \nProceeding to plot your shortest recommended path from " + StationFrom + " to " + StationTo + ".")
            
        return
    
###########################################
# plot fore and background path in map as figure 2
###########################################
        
    def plot_mypath_wrapper(self):
        
        tranpBack = 0.05
        en_labBack = False
        
        tranpFore = 1
        en_labFore = True
        fignumFore = 2
        
        self.plot_wholeTubeMap(tranpBack, en_labBack, fignumFore)
        self.plot_highlight_path(tranpFore, en_labFore, fignumFore)
        
        return
    
###########################################
# plot recommended path in map as figure 2
###########################################
        
    def plot_highlight_path(self, tranpFore, en_labFore, fignumFore):
        
        for i in range(len(self.short_path)):
            
            temp_lat2 = self.MainDict_node[self.short_path[i]]['latitude']    
            temp_lon2 = self.MainDict_node[self.short_path[i]]['longitude']
            plt.scatter(temp_lon2, temp_lat2, facecolors='none', edgecolors='black', s = 80)
            plt.text(temp_lon2, temp_lat2, self.short_path[i], alpha = 0.8)
        
        for i in range(len(self.pair_path)):          #plotting edge lines      
            
            highlght_x1 = self.MainDict_node[self.pair_path[i][0]]['longitude']
            highlght_y1 = self.MainDict_node[self.pair_path[i][0]]['latitude']
            highlght_x2 = self.MainDict_node[self.pair_path[i][1]]['longitude']
            highlght_y2 = self.MainDict_node[self.pair_path[i][1]]['latitude']

            highlght_line_num = self.G.edges[self.pair_path[i]]['line']
            self.highlght_line_col = self.Dict_line[highlght_line_num]
                
            plt.plot((highlght_x1, highlght_x2), (highlght_y1, highlght_y2), color = self.highlght_line_col, lw = 4, alpha = tranpFore)

###########################################
# display details of map
###########################################
            
    def detail_display(self):
        
        self.station1_list = []
        self.station2_list = []
        self.listName = []
        
        for i in range(len(self.pair_path)):
            
            self.station1_list.append(self.pair_path[i][0])
            self.station2_list.append(self.pair_path[i][1])
            self.listName.append(self.linedata['name'][self.G.edges[self.pair_path[i]]['line']])
        
        self.cum_list = []
        self.jnd_list = []
        self.cum_list = [x+', ' +y+': '+z for x,y,z in zip(self.station1_list,self.station2_list,self.listName)]
        self.jnd_list = '\n'.join(self.cum_list)
            
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax= plt.subplot()
        plt.axis([-0.8, +0.9, 51.3, 51.8])
        plt.text(0.63, 0.96, self.jnd_list, transform = ax.transAxes, fontsize=10, verticalalignment='top', bbox = props)
        
        return    
            