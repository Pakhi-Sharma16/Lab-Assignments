# # 1.
# x = int(input("enter a number:"))
# #checking if number is negative
# if x<0:
#     print("please enter a positive number")
# #checking if number is zero
# if x==0:
#     print("please enter a number greater than zero")
# print(f'Multiplication table \n ')
# #looping through the numbers till the entered number 
# i=1
# while i<=x:
#     y=1
#     while y<=20:
#         print(f'{i}*{y}={i*y}\n')
#         y=y+1
#     i=i+1

# # 2.
# N=int(input("enter the number:"))
# #checking if no is zero or negative
# if N==0:
#     print("enter a non zero number")
# if N<0:
#     print("enter a positive number")
# #initialization
# i=1
# #looping till i is less than or equal to 1000
# while i<=1000:
#     if i%N!=0:
#         print(f'Numbers not divisible by N are \n {i}')
#     else:
#         i=i+1
#         continue
#     i=i+1

# # 3.(a)
# num = int(input('Enter number of rows : '))
# #intializing 
# i = 1
# ##looping through the numbers till the entered number with help of nested while loop
# while i <= num :
#     j = 1
#     while j <= i:
#         print('*', end = " ")
#         j += 1
#     print()
#     i += 1

# # (b)
# rows = int(input("Please Enter the Total Number of Rows  : "))
# #intializing
# i = 1
# #looping through the numbers till the entered number with help of while loop
# while(i <= rows):
#     #output
#     print(f'The pattern is as follows: \n')
#     print(' ' * (rows - i) + '*' * i)
#     i=i+1  

# # (c)
# #taking no of rows as input
# no = int(input("Please enter the amount of rows: "))
# ##intialization variable
# row = 0
# #looping 
# while(row < no):
#     row += 1
#     spaces = no - row
# #intialization variable
#     spaces_counter = 0
#     #looping
#     while(spaces_counter < spaces):
#         print(" ", end='')
#         spaces_counter += 1
# #intialization variable
#     num_stars = 2*row-1
#     #looping
#     while(num_stars > 0):
#         print("*", end='')
#         num_stars -= 1

#     print()

# # 4.
# N= int(input('enter a no.: '))
# c=0
# d = 0
# while 1==1:
#     n = int(input('enter the no.: '))
#     if n == -999:
#         break
#     else:
#         if n%N ==0:
#             c =c+1
#         else:
#             d= d+1

# print(f'No. of numbers divisible by {N} are {c}.')
# print(f'No. of numbers not divisible by {N} are {d}.')

# # 5.
# N = int(input('enetr a no.: ')) # N is the count of +ve numbers.
# hcf = 1
# i = 0
# l=[]

# while i<N:
#     n  = int(input("enter the +ve integer : "))
#     if N<2:
#         print('invaild input.')
#     else:
#         l.append(n)
 
#     i=i+1
# print(l)
# g=l[0]
# c=1
# while c<len(l):
#     x=l[c]
#     while g!=x:
#         if g>x:
#             g = g-x
#         else:
#             x=x-g
#     c=c+1

# lcm = 1
# j=0
# while j<len(l):
#     lcm = lcm*l[j]
#     j=j+1

# LCM = lcm/g
# print(f'the LCM of {N} +ve no. is {LCM}.')

# # 6.
# N = int(input('enetr a no.: ')) # N is the count of +ve numbers.
# hcf = 1
# i = 0
# l=[]

# while i<N:
#     n  = int(input("enter the next +ve integer : "))
#     if N<2:
#         print('invaild input.')
#     else:
#         l.append(n)
#     i=i+1
# print(l)
# g=l[0]
# c=1
# while c<len(l):
#     x=l[c]
#     while g!=x:
#         if g>x:
#             g = g-x
#         else:
#             x=x-g
#     c=c+1

    

# print(f'the GCD of {N} positive numbers is {g}.')

# 7.
N = int(input('enter a number: '))

a= '* '
b = ' '
i=1

while i<=N:
    print(b*(N-i)+ a*i)
    i=i+1

