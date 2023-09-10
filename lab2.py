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
