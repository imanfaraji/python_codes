# Function

def myFunc():
    print ("Func called")

def add(a, b, c):
    a = b + c
    return a
def addRef(ar1, ar2, ar3):
    ar1[0] = ar2[0] + ar3[0]

for i in range(3):
    myFunc()

a = 1
print add(a, 2, 3)

ar1 = [1, 2, 3]
ar2 = [2, 3, 4]
ar3 = [3, 4, 5]
addRef(ar1, ar2, ar3)
print (ar1[0], ar1[1])
