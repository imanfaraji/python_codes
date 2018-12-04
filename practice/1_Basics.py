# 1st basic program
# String concat
A = "Alice"
B = "Hello"
C = A + B + "!" * 3
print(C)
print (len(A))
print("What is your age:")
myAge = input()
print ("Your age is: " + str(myAge))
if ( not (myAge == 30) ):
    print("Perfect")
elif ( myAge > 30 ):
    print("Old")
else:
    print ("Young")

counter=1
while (counter < 10):
    print (str(counter))
    counter += 1
