# Date sort:

inputList = ["01-05-2016", "05-08-2016", "07-09-2015", "02-24-2014", "09-30-2012", "01-09-2017"]
print (inputList)

def mySwap(mylst,idx1, idx2):
    temp = mylst[idx1]
    mylst[idx1] = mylst[idx2]
    mylst[idx2] = temp

def getDay(myDate):
    return myDate[3:5]
def getMonth(myDate):
    return myDate[0:2]
def getYear(myDate):
    return myDate[6:10]

def isSmaller(date1, date2):
    if int(getYear(date1)) < int(getYear(date2)):
        return True
    elif int(getYear(date1)) == int(getYear(date2)):
        if int(getMonth(date1)) < int(getMonth(date2)):
            return True
        elif int(getMonth(date1)) == int(getMonth(date2)):
            if int(getDay(date1)) < int(getDay(date2)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

DList = []
MList = []
YList = []

for i in range(0, len(inputList)):
    myStr = inputList[i]
    DList.append(getDay(myStr))
    MList.append(getMonth(myStr))
    YList.append(getYear(myStr))

for i in range(len(inputList)-1, 0, -1):
    for j in range (0, i):
        day1 = inputList[j]
        day2 = inputList[j+1]
        if (isSmaller(day1, day2)):
            mySwap(inputList, j, j+1)
print(inputList)
