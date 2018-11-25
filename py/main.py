''' this is the program tochekck if my machine is understanding the user kkd
sd'''
def readf(fname,permission='r'):
    try:
        
        with open("C:/Users/Administrator/Desktop/ever/files/"+fname+".txt",permission) as f:
            a=(f.read().split("\n"))
    except:
        return "specify the name properly"
    else:
        return a
def writef(data="",fname="basic",permission='a+'):
    try:
        
        with open("C:/Users/Administrator/Desktop/ever/db/"+fname+".txt",permission) as f:
            a=f.write(data+"\n")
    except:
        return "specify the name properly"
    else:
        return a

