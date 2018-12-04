# Loops

myArray = ["3", "4", "5"]
myArray2 = [2, 3, 4]

#for myEl in myArray2:
#    print (myEl)

for i in range(-1,len(myArray)):
    print (i)

print ("###########")

i = 3
while (i < 10):
    i += 1
    if (i == 6):
        continue
    elif (i == 8):
        break
    print(i)
