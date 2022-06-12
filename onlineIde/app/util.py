import os

def compre(x):  
    cwd = os.getcwd()  
    
    filehandle1=open(cwd,'file.txt',"r")
    filehandle2=open(cwd,'t2.txt',"r")
    for line1 in filehandle1:
        for line2 in filehandle2:
            if line1==line2:
                return True
            else:
                return False