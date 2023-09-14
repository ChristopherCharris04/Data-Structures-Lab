Dict={}
n=int(input('Enter no of terms = '))

for i in range(0,n):
    Key_Value=int(input('Enter key and value = '))
    Dict.append(Key_Value)

for i in Dict:
    print(i,':',Dict[i])