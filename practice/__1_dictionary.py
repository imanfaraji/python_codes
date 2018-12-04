# Dictionary

myCar = {"model":"corola", "year":"2015", "color":"blue" }

carKeys= myCar.keys()
print (myCar["color"])
print (myCar.values())
print(myCar.get("type"))
myCar.setdefault("type","sedan")
print(myCar)