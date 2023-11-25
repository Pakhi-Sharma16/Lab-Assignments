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

3.
#taking input
n=int(input("enter number"))
#initialization variable
sum=0
#condition
while n!=0:
    sum=sum+(n%10)
    n=n//10
##printing the sum of the digits
print("sum of digits is:",sum)

4.    
#taking positive number
num=int(input("enter number:"))
#initialise counters
divisible_count=0
indivisible_count=0
#looping till the user enters -999
n=int(input("enter number:"))
while num!=-999:
    if n%num==0:
        divisible_count=divisible_count+1
    else:
        indivisible_count=indivisible_count+1
        #get another number
    num=int(input("enter number:"))
#printing the counts 
print("The divisible count is:",divisible_count)
print("The indivisible count is:",indivisible_count)

5.
#taking input
n=int(input("Enter the value:"))
#initilization variables
i=1
fact=1
#condition if number is less than zero
if n<0:
    print("error")
#if no is 0 
if n==0:
    print("Factorial is 1")
#till initialization variable is less than given number
while i<=n:
    fact=fact*i
    i=i+1
#output
print(fact)
       
6.
#taking input
n=int(input("Enter a  number:"))
#storing value in another variable
temp=n
#initialization
re=0
#looping
while(n>0):
    dig=n%10
    re=(re*10)+dig
    n=n//10
#checking if they are equal
if(temp==re):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

7.
# taking input
n = int(input("enter value :"))
#intialization variable
a = 1
b = 1
#sum
sum = a + b
#count variable
count = 1
print("Fibonacci series is: ")     
while (count <= n):           #looping to save fibonacci series
	count += 1
	print(a)
	a = b
	b = sum
	sum = a + b

8.
#taking input
num = int(input("Enter a number:"))  
#initialization variables
i = 2
f=0
#checking
if num<0:
    print("invalid input")
if num==1:
    print("1 is neither prime nor composite")
##looping
while i <= num:
    if num % i == 0:
        f=1  
    break
if f==1:
    print("The entered number is not a  PRIME number")
else:
    print("The entered number is  a PRIME number")
i=i+1

9.
#taking input
X=input("enter a sentence")
#initialization
upp=0
lower=0
dig=0
spec=0
ind=0
##looping
while ind<len(X):
    cha=X[ind]
    #conditions
    if 'A'<=cha<='Z':
        upp+=1
    elif 'a'<=cha<='z':
        lower+=1
    elif '0'<=cha<='9':
        dig+=1
    else:
        spec+=1 
    ind+=1   
#output      
print(upp)
print(lower) 
print(dig)
print(spec)

10.
#taking the values of the coefficients
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
#calculating discrimant
d=(b**2)-(4*a*c)
#a is 0 then the equation is not quadratic eqn
if a==0:
    print("equation is invalid")
#checking if the roots are real, equal or distinct or imaginary
if d<0:
    print("Imaginary roots")
elif d==0:
    print("Real and equal roots")
    Y=((-b/(2*a)))
    print(Y)
elif d>0:
    print("Real and distinct roots")
    x1=((-b+(d**0.5)/(2*a)))
    x2=((-b-(d**0.5)/(2*a)))
    print("The roots are:", x1,x2)