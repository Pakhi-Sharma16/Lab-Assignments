1.
#displaying all characters from 'A' to 'Z' 
for i in range(65,91):
    print(chr(i),end=" ")


2.
str = input("Enter a string: ")  # counter variable to count the character in a string
counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)


3.
str= input("Enter a sentence:")
hyphenated_sentence=input_sentence.replace(' '," ")
snake_case_sentence=hyphenated_sentence.lower()
words=hyphenated_sentence.split(' ')
camel_case_sentence=words[0]+''.join(word.capitalize()for word in words[1:])
print("hyphenated_sentence:",hyphenated_sentence)
print("snake_case_sentence:",snake_case_sentence)
print("")


4 .
x= input("enter a string:")
y=x[::-1]
if  x==y:
  print("The string is a palindrome.") 
else:
  print ("The string is not a palindrome.")
 

5.
#input from user
sting=str(input("Enter a string: "))
#initializing variables
alphabets=0
digits=0
special=0
upp=0
low=0
#calculating length of string
s=len(sting)
#loop to check for alphabets, digits and special characters, upper and lower case
for i in range(s):
    if sting[i].isalpha():
        alphabets=alphabets+1
        if sting[i].isupper():
            upp=upp+1
        elif sting[i].islower():
            low=low+1
    elif sting[i].isdigit():
        digits=digits+1
    elif sting[i]==" " or sting[i]=="\n" or sting[i]=="\t":
        special=special+1
#displaying results
print(f'Alphabets:{alphabets}')
print(f'Digits:{digits}')
print(f'Special Characters:{special}')
print(f'Upper Case:{upp}')
print(f'Lower Case:{low}')


6.
stion=str(input("Enter a string: "))    
print("Original String:",stion) 

#reversing order of words
j=stion.split()
l=len(j)
#loop to reverse the order of words
for i in range(-1,-l-1,-1):
    print(j[i],end=" ")


7.
string=input("enter a sentence:")
out_string=""
for char in string:
    if char not in out_string:
        out_string=out_string+char

print(out_string)

8.
x=str(input("enter the sentance:"))
word=str(input("enter the words:"))
y=x.split()
p=len(y)
print(p)
count=0
print(y[1])
if word in x:
    # x=x.count(x)
    print("present")
else:
    print("not present")
for i in range(0,p,1):
    if word==y[i]:
        count=count+1
print(count)

9.
#this program checks whether a string is pangram or not
#taking input from user
sty=str(input("Enter a string:"))
#initializing alphabet wtih all the alphabets
alphabet="abcdefghijklmnopqrstuvwxyz"
#loop to check if all the alphabets are present in the string
for char in alphabet:
    if char not in sty.lower():
        print("Not Pangram")
        break
else:
    print("Pangram")

