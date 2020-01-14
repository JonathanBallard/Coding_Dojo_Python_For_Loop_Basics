
#Basic
for i in range(150):
    print("num", i)

#Multiples of 5
for v in range(0,1000,5):
    print("num: ", v)

#Counting the Dojo Way
for i in range(1,100,1):
    if(i%10 == 0):
        print("Coding Dojo")
    elif(i%5 == 0):
        print("Coding")
    else:
        print("num", i)

#Whoa that sucker's huge
sum = 0
for i in range(1,500000,2):
    sum += i
print(sum)

#Countdown by Fours
for i in range(2018,0,-4):
    print(i)

#Flexible Counter
lowNum = 5
highNum = 155
mult = 5

for i in range(lowNum, highNum, mult):
    print(i)










