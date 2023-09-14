word=input('Enter a string = ')
D=L=0
for s in word:
    if s.isdigit():
        D=D+1
    elif s.isalpha():
        L=L+1
    else:
        pass
print("Letters",L,"\ndigists",D)
