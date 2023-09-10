1.
print("Table of numbers N till 20")
#enter any positive number
N=int(input("enter any positive integer:"))
i=1
if N<=0:
    print("invalid input")
else:
    while(i<=20):
     print(N, 'X',i,'=',N*i)
     i=i+1

2.
X=int(input("enter any number:"))
Y=int(input("enter any number:"))
N=int(input("enter any number:"))
i=X+1
while (i<=Y):
    if i%N==0:
        print(i)
    else:
        print("invalid input")