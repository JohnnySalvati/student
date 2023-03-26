class VersionManager:
    def __init__(self, version="0.0.1"):
    
        self.history=[]
    
        if len(version)==0:
            version="0.0.1"
            
        splited_version=version.split(".")
        
        if len(splited_version)>3:
            splited_version=splited_version[0:3]
        else:
            if len(splited_version)==2:
                splited_version.append("0")
                
            elif len(splited_version)==1:
                splited_version.append("0")
                splited_version.append("0")
        
        if not ((splited_version[0]+splited_version[1]+splited_version[2]).isnumeric()):
            raise Exception("Error occured while parsing version!")
            
        self.history.append([int(m) for m in splited_version])

    def major(self):
        major, _, _ = self.history[-1]
        self.history.append([major+1, 0, 0])
        return self
        
    def minor(self):
        major, minor, _ =self.history[-1]
        self.history.append([major, minor+1, 0])
        return self
    
    def patch(self):
        major, minor, patch =self.history[-1]
        self.history.append([major, minor , patch+1])
        return self
        

    def rollback(self):
        if len(self.history)>1:
            self.history.pop()
        else:
            raise Exception("Cannot rollback!")
            
        return self
        
    def release(self):
        return ".".join(map(str,self.history[-1]))
    

    

print(VersionManager("").major().rollback().release())


