import math

#Create the evenNumbers list
evenNumbers = []
for i in range(1,299):
    if (i%2==0):
        evenNumbers.append(i)

print(len(evenNumbers))
for num in evenNumbers:
    if(num==int(math.sqrt(num)+0.5)**2):
        print(num)
