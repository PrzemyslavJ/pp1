tabl = [1,0,3,2,1,4,3,2,0,1,2,3,5,6,0,2]
def BezPowt(tab):
    tabN=[]
    for i in tab:
        tabN.append(i)
        
    for i in tab:
        CountLoc=0
        for x in tab:
            if(x==i):
                CountLoc+=1
        if(CountLoc>1):
            tabN.remove(i)
    
    return tabN

for i in BezPowt(tabl):
    print(i,end=' ')
                
