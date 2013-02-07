__author__ = 'Julie'

#to represent and filter the output of the feature extractor to obtain representations of phrases
#for each line decide whether to output 0,1 or 2 lines
#0 lines if the first word does not match headPOS
#1 line (as input) if line does not contain modPOS
#2 lines (1 as input and 1 where the head word is concatenated with mod to form phrase) if line does contain modPOS
#more lines if multiple modPOS?
import re

class FEData:

    nounPATT = re.compile('(.*)/N')
    detdepPATT = re.compile('det-DEP:(.*)')

    def __init__(self,filename,hpos,mpos):
        self.filename=filename

        self.headPOS=hpos
        self.modPOS=mpos
        self.outfile=filename+"_"+hpos+"_"+mpos
        if self.headPOS =='N':
            self.headPATT =FEData.nounPATT
        else:
            print "Unknown POS for matching"
            exit(1)
        if self.modPOS == 'det-DEP':
            self.modPATT=FEData.detdepPATT

        self.matched=0
        self.linesread=0

    def readfile(self):

        instream=open(self.filename,'r')
        outstream=open(self.outfile,'w')
        print "Processing "+self.filename

        for line in instream:
            self.processline(line.rstrip(),outstream)
            self.linesread+=1
        instream.close()
        outstream.close()
        print "Read "+str(self.linesread)+" lines"
        print "Matched "+self.headPOS+" "+str(self.matched)+" times"


    def processline(self,line,outstream):
        featurelist=line.split('\t')
        matchobj=self.headPATT.match(featurelist[0])
        if matchobj:
            self.matched+=1
            outstream.write(line+'\n')





