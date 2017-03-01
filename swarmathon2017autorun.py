##Elizabeth E. Esterly
##The University of New Mexico
##NASA Swarmathon HS Division 2017
##autorun
##last revised 02/13/2017

from py4j.java_gateway import JavaGateway
from os import listdir
import sys

#open bridge to Netlogo
gw = JavaGateway()
bridge = gw.entry_point

path = sys.argv[1] #get path as command line arg
files = [c for c in listdir(path) if not (c.startswith('.'))] #careful, this might give you .DS_Store first!
    
if files[0] is "parkinglot.jpg": #toss img file if it exists
    files = files[1:]

##!!!later go in and scrub this from files!!!#

for i in range(0, len(files)): #run each file in the path specified in commandline args
    name = files[i]  
    print("opening " + name) #shell notification for convenience 
    p = path + name
    bridge.openModel(p)

    #set slider values for run 1
    bridge.command("set singleRocks 70")
    bridge.command("set clusterRocks 50")
    bridge.command("set largeClusterRocks 0")
        
    #setup the model
    bridge.command("setup")

    while bridge.report("count patches with [pcolor = yellow]") < 510 and bridge.report("count patches with [pcolor = yellow]") > 514:
        bridge.command("setup")
    print(bridge.report("count patches with [pcolor = yellow]"))
    bridge.exportView(name + ".png")
    bridge.closeModel()
    bridge.refresh()
