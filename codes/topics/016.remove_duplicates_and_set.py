n=input("Enter a number split with comma: ").split(',')
m=[]
for number in n:
    if number not in m:
        m.append(number)
print(m)
#or we can use set
n1=input("Enter a number split with comma: ").split(',')
m=list(set(n1))
print(m)