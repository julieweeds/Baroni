__author__ = 'Julie'

#application to extract phrasal vectors
from fedata import FEData
from baronidata import BaroniData

at_home=False
on_apollo=False

parent="/Users/juliewe/Documents/workspace/Baroni/data/"

if at_home:
    parent="C:/Users/Julie/Documents/sussex/Baroni/data/"

if on_apollo:
    parent="/mnt/lustre/scratch/inf/juliewe/Baroni/data/"

inputdata=parent+"exp6_tiny" #sample of fe output for gigaword


headPOS="N"
modPOS="det-DEP"

#stage 1: extract relevant POS words and phrases from feature extractor output
mydata1 = FEData(inputdata,headPOS,modPOS)
outfile1=mydata1.readfile()
print "Written first stage output file "+outfile1

#stage 2: turn them into vectors and create .rows, .cols and .sm files for Baroni toolkit and count files for analysis

mydata2 = BaroniData(outfile1)
print "Completed vector files for Baroni toolkit and analysis"