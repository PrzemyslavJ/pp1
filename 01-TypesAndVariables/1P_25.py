number = input("Podaj nr rachunku bankowego: ")
temp = ''
try:
    int(number)
    print(f'Nr rachunku: {number[0:2]} {number[2:6]} {number[6:10]} {number[10:14]} {number[14:18]} {number[18:22]} {number[22:26]}')
except:
    print("Podaj tylko cyfry!")
