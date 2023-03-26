class VersionManager:
    
    def __init__(self, version="0.0.1"):
        self.history=[]
        if version=="":
            version="0.0.1"
        #if version.isdigit():
        splited_version=version.split(".",2)
        self.maj=int(splited_version[0])
        try:
            self.min=int(splited_version[1])
        except:
            self.min=0
        try:
            self.pat=int(splited_version[2][0])
        except:
            self.pat=0
        
        self.history.append([self.maj,self.min, self.pat])
        

    def major(self):
        self.maj+=1
        self.min=0
        self.pat=0
        self.history.append([self.maj,self.min, self.pat])
        return self
        
    def minor(self):
        self.min+=1
        self.pat=0
        self.history.append([self.maj,self.min, self.pat])
        return self
        
    
    def patch(self):
        self.pat+=1
        self.history.append([self.maj,self.min, self.pat])
        return self
        

    def rollback(self):
        self.maj=self.history[-1][0]
        self.min=self.history[-1][1]
        self.pat=self.history[-1][2]
        del self.history[-1]
        return self

    def release(self):
        return ".".join(map(str,self.history[-1]))
    
VersionManager().major().release()
VersionManager("").release()
VersionManager("1.2.3").release()
VersionManager("1.2.3.4").release()
VersionManager("1.2.3.d").release()
VersionManager("1").release()
VersionManager("1.1").release()


    

