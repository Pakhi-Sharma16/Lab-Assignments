# 1.
p = str(input('Enter your paragraph: '))
p =p.lower()
p=p.replace('',' ')
s=p.split()
print(s)
d={'a':0,'e':0,'i':0,'o':0,'u':0} # creating a dictionary of vowels.
for i in s:
    if i=='a':
        d['a']+= 1
    elif i=='e':
        d['e'] +=1
    elif i=='i':
        d['i']+= 1
    elif i=='o':
        d['o']+= 1
    elif i=='u':
        d['u']+= 1

print(d)
print(max(d.values()))

sd = dict(sorted(d.items(), key=lambda item: item[1])) # sorting the dictionary according to the values.

# displaying the result.
for key, value in sd.items():
    print(key, value)

# 2.(a)
import random

# First function for the list of outcomes.
def roll(n):
    l = []
    for i in range(n):
        x = random.randint(1, 6)
        l.append(x)
    return l

# Second function for finding the frequency count of the outcomes.
def fco(lst):
    fc = {}
    for i in lst:
        if i in fc:
            fc[i] += 1
        else:
            fc[i] = 1
    return fc

# Third function for displaying the frequency count.
def d_fc(fc):
    for i, j in fc.items():
        print(f'{i}: {j}')

# Last bit of code for calling the functions
N = int(input('Enter a number greater than 10000: '))
if N < 10000:
    print('Enter a number > 10000.')
else:
    r = roll(N)
    f = fco(r)
    print('Frequency Count: ')
    d_fc(f)

# (b)
import random

# First function for the list of outcomes.
# i just added a new parameter for the sides of the dice.
def roll(n,sides):
    l = []
    for i in range(n):
        x = random.randint(1, sides)
        l.append(x)
    return l

# Second function for finding the frequency count of the outcomes.
def fco(lst):
    fc = {}
    for i in lst:
        if i in fc:
            fc[i] += 1
        else:
            fc[i] = 1
    return fc

# Third function for displaying the frequency count.
def d_fc(fc):
    for i, j in fc.items():
        print(f'{i}: {j}')

# Last bit of code for calling the functions
N = int(input('Enter a number greater than 10000: '))
if N < 10000:
    print('Enter a number > 10000.')
else:
    s= int(input('Enter no. of sides of dice: '))
    r = roll(N,s)
    f = fco(r)
    print('Frequency Count: ')
    d_fc(f)

# 3.
Odd = {}
Even = {}
while 1==1:
    x= str(input('over or not? '))
    if x=='over':
        break
    else:
        n= int(input())
        s= n*n
        c=n*n*n

    if n%2==0:
        Even[n]=[s,c]
    else:
        Odd[n]=[s,c] 
print(Even)
print(Odd)

# 4.
Odd = {}
Even = {}
while 1==1:
    x= str(input('over or not? '))
    if x=='over':
        break
    else:
        n= int(input())
        s= n*n
        c=n*n*n

    if n%2==0:
        Even[n]=[s,c]
    else:
        Odd[n]=[s,c] 
print(Even)
print(Odd)

# 5.
def shift(lst,k):
    if not lst:
        return lst
    else:
        n= len(lst)
        if k>n or k<0:
            print('invalid')
        else:
            return lst[k:] + lst[:k]
    
l= [0,1,2,3,4,5,6,7,8,9]
k=4
r = shift(l,k)
print(r)


def shift_d(lst,k,direction='left'):
    if not lst:
        return lst
    else:
        n= len(lst)
        if k>n or k<0:
            print('invalid')
        if direction == 'left':
            return lst[k:] + lst[:k]
        elif direction == 'right':
            return lst[-k:] + lst[:-k]
        else:
            print("Use 'left' or 'right'.")

l=[0,1,2,3,4,5,6,7,8,9]
k=4
r1= shift_d(l,k,'left')
r2= shift_d(l,k,'right')
print(r1)
print(r2)

# 6.(a)
# function for factorial.
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
x = int(input('enter the no. :'))
print(f'The factorial of {x} is {fact(x)}.')

# (b)
# function for finding sum of numbers.
def su(n):
    if n==0:
        return 0
    else:
        return n+su(n-1)

x= int(input('enter the no. you want the sum of: '))
print(f'The sum of {x} numbers is {su(x)}.')

# (c)
# function for fibonacci series
def fib(n):
    if n==1 or n==0:
        return n
    else:
        return fib(n-1)+fib(n-2)

x= int(input('Enter the no. of terms in the series: '))
print('Fibonacci series: ')
for i in range(x):
    print(fib(i), end=',')
