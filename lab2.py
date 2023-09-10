1.
x=float(input("enter length: "))
y=float(input("enter breadth: "))
area=x*y
print(area)

2.
x=float(input("enter length in feet: "))
y=float(input("enter breadth in feet : "))
X=x*0.3048
Y=y*0.3048
area=X*Y
print("area in square metres= ", area)

3.
X=int(input("enter a number x:"))
Y=int(input("enter a number y:"))
if Y%X==0:
  print("Y is divisible by X")
else :
  print("Y is not divisible by X")  

4.
a=int(input("enter a number: "))
if a%2==0:
  print("a is even")
else:
  print("a is odd")

5.
r=int(input("enter radius:"))
if 1<r<100:
  print("area=" , 3.14*(r**2))
else:
  print("invalid input")

6.
C= float(input("enter temp in C:"))
F=(C*1.8)+32
K=C+273.15
print(C,"in fahreheit is", F, "and" ,C , "in kelvin is",K)

7.
C= float(input("enter temp in C:"))
F=(C*1.8)+32
print("C=F at -40 degree celsius")

8.
Year=int(input("enter a year:"))
if Year%400==0 or Year%100!=0 and Year%4==0:
  print("it is a leap year")
else:
  print("it's not a leap year")

9.
money=float(input("enter the monthly investment:"))
time=float(input("enter duration in months:"))
rate=7.1
if money>=500 and time>=6:
  interest = float(money*(rate/time))
  print(interest)
elif time<6:
  print("duration should be more than 6 months")
elif money<500:
  print("minimum amt should be more than Rs.500")
else:
  print("invalid input")

10.
n=int(input("enter the time in seconds:")) #seconds
if n in range(1,86400):
  hours=int(n/3600)
  n%=3600
  minutes=int(n/60)
  n%=60
  print(hours,minutes,n)
else:
  print("invalid input")