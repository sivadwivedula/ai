''' this is the program tochekck if my machine is understanding the user kkd
sd'''
def readf(a,b='r'):
    try:
        
        with open("C:/Users/Administrator/Desktop/files/"+a+".txt",b) as f:
            a=(f.read().split("\n"))
    except:
        return "specify the name properly"
    else:
        return a

