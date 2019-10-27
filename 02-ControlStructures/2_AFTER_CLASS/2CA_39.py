import sys
print("pierwszych 50 wyrazów ciągu fibonaciego: ")
tab = []
for i in range(0,50):
    if(i==0):
        tab.append(0)
    elif(i==1):
        tab.append(1)
    elif(i>1):
        tab.append(tab[i-1]+tab[i-2])

for i in range(len(tab)-1):
    print(tab[i],end=' ')

    

    
