tabL = [2,5,4,1,8,7,4,0,9]
def reverse(tab):
    tabN = []
    for i in range(len(tab)-1,-1,-1):
        tabN.append(tab[i])
        
    return tabN

print(list(reverse(tabL)))
