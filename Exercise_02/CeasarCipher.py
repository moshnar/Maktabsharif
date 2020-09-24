Letters=['abcdefghijklmnopqrstuvwxyz']
cipher = ['defghijklmnopqrstuvwxyzabc']

def sub(l,ci,text):
    indexes=[]
    for i in range(0,len(text)-1):
        indexes=text.find(l[i])
        print(indexes)





print(sub(Letters,cipher,'hello my name is mamad'))
