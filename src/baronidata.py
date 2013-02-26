__author__ = 'juliewe'


from myvector import MyVector

class BaroniData:



    def __init__(self,filename):
        self.inputfile=filename
        self.linesread=0
        self.vectordict={} #dictionary of dictionaries to store vectors
        self.tags={}  #different tags in file
        self.features={}  #totals for features
        self.suffixes=[]
        for i in range(1,9):
            self.suffixes.append(str(i))
        self.suffixes.reverse()
        self.tagcodes={}

        self.readfile()
        self.writefiles()


    def readfile(self):
        instream=open(self.inputfile,'r')

        for line in instream:
            self.processline(line.rstrip())
            self.linesread+=1
        instream.close()
        print "Read "+self.inputfile


    def processline(self,line):
        parts = line.split('\t')
        entrypos=parts[0]
        entryparts=entrypos.split('/')
        entry=entryparts[0]
        pos=entryparts[1]

        if pos in self.tagcodes.keys():
            self.tags[pos]+=1 #record each distinct pos seen for file splitting
        else:
            self.tags[pos]=1
            self.tagcodes[pos]=self.suffixes.pop()

        if entrypos in self.vectordict.keys():
            self.check=True
            print "Will add to vector for "+entrypos
        else:
            self.vectordict[entrypos]=MyVector(entrypos,entry,pos)
            print "Created new vector for "+entrypos
        #print parts[1],parts[2],parts[3]

        for i in range(1,len(parts)):
            feature=parts[i]
            self.vectordict[entrypos].add(feature,1)
            if (feature,pos) in self.features.keys():
                self.features[(feature,pos)]+=1
            else:
                self.features[(feature,pos)]=1

    def writefiles(self):
        outmatrix={}
        outrow={}
        outcol={}
        outrowcounts={}
        outcolcounts={}

        #open files
        for tag in self.tagcodes.keys():
            outmatrix[tag]=open(self.inputfile+'_'+self.tagcodes[tag]+'.sm','w')
            outrow[tag]=open(self.inputfile+'_'+self.tagcodes[tag]+'.rows','w')
            outcol[tag]=open(self.inputfile+'_'+self.tagcodes[tag]+'.cols','w')
            outrowcounts[tag]=open(self.inputfile+'_'+self.tagcodes[tag]+'.rowcounts','w')
            outcolcounts[tag]=open(self.inputfile+'_'+self.tagcodes[tag]+'.colcounts','w')

        #write files

        #process vectors to produce sparse matrix and row files
        for entrypos in self.vectordict.keys():
            tag = self.vectordict[entrypos].tag
            self.vectordict[entrypos].writefiles(outmatrix[tag],outrow[tag],outrowcounts[tag])

        #process features to produce col files
        for (feature,tag) in self.features.keys():
            outcol[tag].write(feature)
            outcolcounts[tag].write(feature+'\t'+str(self.features[(feature,tag)])+'\n')

        #close files
        for tag in self.tagcodes.keys():
            outmatrix[tag].close()
            outrow[tag].close()
            outcol[tag].close()
            outrowcounts[tag].close()
            outcolcounts[tag].close()