1.
X=int(input("enter length of parallel side:"))
Y=int(input("enter length of parallel side:"))
H=int(input("enter height of trapezoid:"))
area=((X+Y)/2)*H
print(area)


2.
weight=float(input("enter the weight in kg:")) #get weight in kg
height=float(input("enter the height in m:")) #get height in m
BMI= weight/(height**2)#calculate BMI
print(BMI)
weight=float(input("Enter weight in pounds:"))
height=float(input("Enter height in inches:"))
#converting
#calculate BMI
BMI=(703*weight)/(height**2)
print(BMI)

3.
a=int(input("Enter side1:"))
b=int(input("Enter side2:"))
c=int(input("Enter side3:"))
if (a+b)>c:
    print("Yes, They does form the sides of a triangle")
elif (a+c)>b:
    print("Yes")
else:
    print("No, They does not form a triangle")


4.
a=int(input("enter a three digit number:"))
b= a//100
c=(a//10)%10
d=a%10
sum=b+c+d
print(sum)
if sum%3==0:
    print("it is divisible by 3")
else:
    print("it is not divisible by 3")


5.
x=int(input("enter a five digit number:"))
a= a//10000
b=(a//1000)%10
c=(a//100)%10
d=(a//10)%10
e=a%10
print(e,d,c,b,a)
print("numbers are palindrome")


6.
x=int(input("Enter a no:"))
y=int(input("enter a no:"))
print("Before swapping:",x,y)
x,y=y,x
print("After swapping:",x,y)


7.
x=complex(input("enter first complex number: "))
y=complex(input("enter second complex number: "))
sum=x+y
product=x*y
print(sum)
print(product)

8.
bsal=int(input("enter salary:"))
hra=0.2*bsal
ta=0.05*bsal
da=0.1*bsal
gs=bsal+hra+ta+da
print("Gtoss Salary is:",gs)


9.
bsal=int(input("enter salary:"))
hra=0.2*bsal
ta=0.05*bsal
da=0.1*bsal
gs=bsal+hra+ta+da
print("Gtoss Salary is:",gs)

if gs<300000:
    print("No Income Tax")
if gs>=300000 and gs<1000000:
    inctx=0.1*gs
    print(inctx)
if gs>=1000000 and gs<2500000:
    inctx=0.2*gs
    print(inctx)
if gs>=2500000:
    inctx=0.3*gs
    print(inctx)


10.
a=int(input("Enter a no:"))
b=int(input("Enter a no:"))
c=int(input("Enter a no:"))
if a>b :
    if a>c:
        print("a is largest number")
if b>a:
    if b>c:
        print("b is largest number")
if c>a:
    if c>b:
        print("c is largest number")


11.
x = int(input("Enter the first digit:"))
y = int(input("Enter the second digit:"))
z = int(input("Enter the third digit:"))
xyz= x,y,z
cube = x**3 + y**3 + z**3
print(x,y,z)
print(cube)
if xyz == cube:
    print("It is an armstrong no.")
else:
    print("It is not an armstrong no.")