##Elizabeth E. Esterly
##The University of New Mexico
##NASA Swarmathon HS Division 2017
##autorun
##last revision 03/08/2017

#INPUT: python swarmathon2017autorun.py -path to folder of submissions to be processed- -path to text file to record results-


from py4j.java_gateway import JavaGateway
from os import listdir
import sys   

def setupRun():
    #set all patches to black and force world size
    bridge.command("setup")
    bridge.command("ask patches [set pcolor black]")
    bridge.command("resize-world -50 50 -50 50") 

def makeRandomDistribution():
    bridge.command("ask n-of 500 patches [if pcolor != yellow [set pcolor yellow]]")

def makeSquareDistribution():
    bridge.command("ask patches with [pxcor > 30 and pycor > 25] [set pcolor yellow]")

def makeNASALogo():
    bridge.command("ask patches with [distancexy 0 0 < 40 and distancexy 0 0 > 39][set pcolor yellow]")  #make circle
    #make N 
    bridge.command("ask patches with [pxcor = -30 and pycor >= -8 and pycor <= 8] [set pcolor yellow]")
    bridge.command("ask patches with [pxcor = -20 and pycor >= -8 and pycor <= 8] [set pcolor yellow]")
    bridge.command("ask patches with [pycor >= -1.6  * pxcor + -40 and pycor <= -1.6 * pxcor - 38 and pycor >= -8 and pycor <= 8][set pcolor yellow]")
    #make A
    bridge.command("ask patches with [pycor >= 2 * (pxcor + 11)  and pycor <= 2 * (pxcor + 12) and pycor >= -8 and pycor <= 8][set pcolor yellow]")
    bridge.command("ask patches with [pycor >= -2 * (pxcor + 4)  and pycor <= -2 * (pxcor + 3) and pycor >= -8 and pycor <= 8][set pcolor yellow]")
    bridge.command("ask patches with [pycor = 0 and pxcor >= -11 and pxcor <= -4][set pcolor yellow]")
    #make S
    bridge.command("ask patches with [pycor = -8 and pxcor >= 3 and pxcor <= 11][set pcolor yellow]")
    bridge.command("ask patches with [pycor = 8 and pxcor >= 3 and pxcor <= 11][set pcolor yellow]")
    bridge.command("ask patches with [pycor <= 8 and pycor >= 1 and pxcor = 3 ][set pcolor yellow]")
    bridge.command("ask patches with [pycor = 0 and pxcor >= 3 and pxcor <= 11][set pcolor yellow]")
    bridge.command("ask patches with [pycor >= -8 and pycor <= 0 and pxcor = 11 ][set pcolor yellow]")
    #make 2nd A
    bridge.command("ask patches with [pycor >= 2 * (pxcor - 20)  and pycor <= 2 * (pxcor - 19) and pycor >= -8 and pycor <= 8][set pcolor yellow]")
    bridge.command("ask patches with [pycor >= -2 * (pxcor - 27)  and pycor <= -2 * (pxcor - 28) and pycor >= -8 and pycor <= 8][set pcolor yellow]")
    bridge.command("ask patches with [pycor = 0 and pxcor <= 28 and pxcor >= 20][set pcolor yellow]")
    bridge.command("while[count patches with [pcolor = yellow] < 500][ask one-of patches [if pcolor != yellow and distancexy 0 0 > 40 [set pcolor yellow]]]")

def runOne():
    setupRun()
    makeRandomDistribution()
    return bridge.report("count patches with [pcolor = yellow]")

def runTwo():
    setupRun()
    makeSquareDistribution()
    return bridge.report("count patches with [pcolor = yellow]")

def runThree():
    setupRun()
    makeNASALogo()
    return bridge.report("count patches with [pcolor = yellow]")
    
d = {}
#open bridge to Netlogo and set random seed
gw = JavaGateway()
bridge = gw.entry_point
bridge.command("random-seed 1337")
path = sys.argv[1] #path to code submissions
files = [c for c in listdir(path) if not (c.startswith('.')) and not c == 'parkinglot.jpg'] #toss .DS_store and img file from list of files


#Competition Loop
for i in range(0, len(files)): #run each file in the path specified in commandline args
    name = files[i]
    p = path + name
    print("opening " + name) #shell notification for convenience

    #write all lines except bitmap extension and import to patch colors command
    print("cleaning" + name)

    cleaned = open(path + 'c' + name, 'w')

    #read lines one at a time. If you see a b, set flag one and gather chars for the length of that string. Same with e.
    #When that's done, print it out and do a string comparison. Only write it if they don't match.
    with open (p, 'r+') as f:
        while (True):
            c = f.readline()
            if c != "  bitmap:copy-to-pcolors bitmap:import \"parkingLot.jpg\" true\n" and c != " extensions[bitmap]\n":
                cleaned.write(c)
            if not c:
                break
    cleaned.close()

    bridge.openModel(path + 'c' + name)
    random = 500 - runOne() #counts remaining
    square = 500 - runTwo()
    logo = 500 - runThree()
    total = random + square + logo

    #export performance
    results = sys.argv[2]#file name to store results
    with open (results, 'a') as f:
        f.write(name + " results\nRandom: " + str(random) + "\nSquare: " + str(square) + "\nNASA logo" + str(logo) + "\nTotal: " + str(total) + "\n\n")
        f.close()
    bridge.closeModel()
    bridge.refresh()



    

 
