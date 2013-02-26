__author__ = 'juliewe'

class MyVector:

    def __init__(self,entrytag,entry,tag):
        self.entrytag=entrytag
        self.entry=entry
        self.tag=tag
        self.vector={}
        self.total=0


    def add(self,feature,count):
        if feature in self.vector.keys():
            self.vector[feature] += count
        else:
            self.vector[feature] = count
        self.total+=count

    def display(self):
        print self.entrytag,self.entry,self.tag,self.total
        print self.vector

    def writefiles(self,outmat,outrow,outrowcounts):
        for feature in self.vector.keys():
            outmat.write(self.entrytag+'\t'+feature+'\t'+str(self.vector[feature])+'\n')
        outrow.write(self.entrytag+'\n')
        outrowcounts.write(self.entrytag+'\t'+str(self.total)+'\n')