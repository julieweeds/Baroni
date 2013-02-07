__author__ = 'Julie'

#application to extract phrasal vectors
from fedata import FEData

at_home=True
on_apollo=False

parent="/Users/juliewe/Documents/workspace/Baroni/data/"

if at_home:
    parent="C:/Users/Julie/Documents/sussex/Baroni/data/"

if on_apollo:
    parent="/mnt/lustre/scratch/inf/juliewe/Baroni/data/"

inputdata=parent+"exp6_tiny" #sample of fe output for gigaword


headPOS="N"
modPOS="det-DEP"

mydata = FEData(inputdata,headPOS,modPOS)
mydata.readfile()