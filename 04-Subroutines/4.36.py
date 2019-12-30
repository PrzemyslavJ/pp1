tab = [7,5,3,[3,6,[2]],7,[1,[2,3,[4]],9,2],4]
tabN = [1,2,3,[4,5]]

def SUM(tabL):
    S = 0
    for i in tabL:
        if(isinstance(i,list)):
            S+=SUM(i)
        else:
            S+=i
           
    return S

print(SUM(tab))
        
