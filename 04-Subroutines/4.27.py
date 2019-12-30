Text = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi,Prosto, długo, daleko, jako morza brzegi."
CountA = 0
CountAn = 0
CountE = 0
CountEn = 0
CountI = 0
CountO = 0
CountU = 0
CountY = 0

for i in Text:
    if(i=="A" or i=="a"):
        CountA+=1
    elif(i=="ą"):
        CountAn+=1
    elif(i=="e" or i=="E"):
        CountE+=1
    elif(i=="ę"):
        CountEn+=1
    elif(i=="I" or i=="i"):
        CountI+=1
    elif(i=="O" or i=="o"):
        CountO+=1
    elif(i=="U" or i=="u"):
        CountU+=1
    elif(i=="Y" or i=="y"):
        CountY+=1

print("Ilość wystąpień samogłoski a: {} ą: {} e: {}, ę: {} i: {} o: {} u: {} y: {}".format(CountA,CountAn,CountE,CountEn,CountI,CountO,CountU,CountY))
