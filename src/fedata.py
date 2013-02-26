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
            self.newpos = '<'+self.headPOS+',det>'

        self.matched=0
        self.matched2=0
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
        print "Matched "+self.headPOS+"_"+self.modPOS+" "+str(self.matched2)+" times"
        return self.outfile

    def processline(self,line,outstream):
        featurelist=line.split('\t')
        head=featurelist[0]
        matchobj=self.headPATT.match(head)
        if matchobj:
            #first word on line matches the required POS so write this line out
            self.matched+=1
            outstream.write(line+'\n')
            for f in featurelist:
                #continue checking after finding mod as there may be more
                #print f
                matchobj2=self.modPATT.match(f)
                if matchobj2:
                    #matched the required dependency so create new head term and write out line

                    featurelist[0]=self.newhead(matchobj.group(1),matchobj2.group(1))
                    #print featurelist
                    newlist=featurelist
                    newlist.remove(f)
                    #print newlist
                    self.writelist(newlist,outstream)
                    self.matched2+=1

    def newhead(self,head,feature):
        return '<'+head+","+feature+'>/'+self.newpos


    def writelist(self,flist,outstream):
        #write out the current feature list

        for f in flist:
            outstream.write(f+'\t')
        outstream.write('\n')

