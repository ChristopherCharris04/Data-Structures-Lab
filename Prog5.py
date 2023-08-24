x=int(input("Enter first no ="))
y=int(input("Enter second no ="))
z=int(input("Enter third no ="))
if x>y and x>z:
    print(x,"is biggest")
if y>z and y>x:
    print(y,"is biggest")
else:
    print(z,"is biggest")