class Reader:

    def __init__(self,fname):
        self.fname = fname;
        self.f = open(fname,"rt")

    def close(self):
        self.f.close();


    def read(self):
        self.f.read();
