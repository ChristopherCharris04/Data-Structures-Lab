nterms=int(input("How many terms?"))
n1,n2=0,1
count=0
if nterms<=0:
    print("Enter positive number")
elif nterms==1:
    print("Fibonacci Sequence upto",nterms,"=")
    print(n1)
else:
    print("Fibonacci series")
    while count < nterms:
        print(n1) 
        nth=n1+n2
        n1=n2
        n2=nth
        count += 1