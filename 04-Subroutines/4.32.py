Macierz = [[1,2,0],[0,0,3],[5,1,1]]
for i in Macierz:
    print(i)

def Transp(Mac):
    MacierzT = [[],[],[]]
    for i in range(len(Macierz)):
        MacierzT[0].append(Mac[i][0])
        MacierzT[1].append(Mac[i][1])
        MacierzT[2].append(Mac[i][2])

    return MacierzT
    
print()
for i in Transp(Macierz):
    print(i)
                     
    
               
            
            
    
    


        
