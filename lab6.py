# 1.
s = str(input('enter the sentence: '))
l= len(s)
word =1
i=0
v=0
c=0
V = ['A','E','I','O','U','a','e','i','o','u']
S = [' ']
C = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
for i in range (0,l):
    if s[i] in V:
        v=v+1
    elif s[i] in C:
        c=c+1
    elif s[i] in S:
        word = word+1
        
    else:
        print('there is a invalid input.')
print(f'number of vowels is {v}')
print(f'no. of consonants is {c}')
print(f'no. of words is {word}')

# 2. (a)
n=int(input("ENTER THE NO OF TERMS:"))
sum=0
i=1
while i<=n:
  sum=sum+(1/i)
  i=i+1
print(f"sum of {n} terms is:{sum:.9f}")

# (b)
n=int(input("ENTER THE NO OF TERMS:"))
sum=0
fact=1
i=1
while i<=n:
  fact=fact*i
  i+=1
  sum=sum+(1/fact)
print(f"sum of {n} terms is:{sum:.9f}")

# (c)
n=int(input("ENTER THE NO OF TERMS:"))
x=int(input("enter the vale of x:"))
sum=0
i=1
while i<=n:
  sum=sum+(x**i)/i
  i+=1
print(f"sum of series {n} is:{sum:.9f}")

# 3.
n=int(input("enter the no. of terms:"))
i=1
total=0
while i<=n:
    total+=(1/2)**i
    i+=1
print(f"the sum of the series of {n} terms is:{total}")


n=int(input())
x=int(input())
fact=1
sum=1
i=0
for i in range(n):
    fact=fact*(2*n+1)
    a=((-1)**n)*((x)(2*n+1))/(fact)
    sum=sum+a
print(sum)


n=int(input())
x=int(input())
fact=1
sum=0
i=1
for i in range(n):
    fact=fact*(2*n-2)
    a=(-1)*(n-1)*((x)(2*n-2)/(fact))
    sum=sum+a
print(sum)