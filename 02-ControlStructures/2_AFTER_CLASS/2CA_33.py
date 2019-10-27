import sys
a = str(input("Wprowadź liczbę"))
tab=[]

for i in range(len(a)):
    if(a[i] == "1"):
        tab.append("jeden")
    elif(a[i] == "2"):
        tab.append("dwa")
    elif(a[i] == "3"):
        tab.append("trzy")
    elif(a[i] == "4"):
        tab.append("cztery")
    elif(a[i] == "5"):
        tab.append("pięć")
    elif(a[i] == "6"):
        tab.append("sześć")
    elif(a[i] == "7"):
        tab.append("siedem")
    elif(a[i] == "8"):
        tab.append("osiem")
    elif(a[i] == "9"):
        tab.append("dziewięć")
    else:
        print("Nieprawidłowa cyfra!")
        break

for i in tab:
    print(i,end=' ')

        
    
