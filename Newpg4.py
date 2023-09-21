n=int(input('Enter a number = '))
sum1=0
for i in range(1,n):
    if(n%i==0):
        sum1 += i
if (sum1 == n):
    print('The number is Perfect Number!')
else:
    print('The number is not a Perfect Number!')