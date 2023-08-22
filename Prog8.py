h=float(input("Enter the height = "))
b=float(input("Enter the breadth = "))
l=float(input("Enter the lenght = "))
s=(l+b+h)/2
A=(s*(s-l)*(s-b)*(s-h))*0.5
print("The Semi Perimeter of Triangle =%2f"%s)
print("The Area of Triangle =%0.2f"%A)
