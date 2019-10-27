import random
tab=[]
for i in range(100):
    tab.append(random.randint(1,6))

six = tab.count(6)
five = tab.count(5)
four = tab.count(4)
three = tab.count(3)
two = tab.count(2)
one = tab.count(1)

print("szóstka: {} \npiątka: {} \nczwórka: {} \ntrójka: {} \ndwójka: {} \njedynka: {}".format(six,five,four,three,two,one))
