1.
n = int(input("Enter number of elements : "))
lst = []  # creating an empty list
for i in range(n):
    c = int(input("enter elements:"))
    lst.append(c) # adding the element
print(lst)
sum=0
for i in range(n):
 sum=sum+lst[i]
print(sum)
product=1
for i in lst:
 product = product * i
print(product)
x=0
for i in range(n):
 if lst[i]>x:
     x=lst[i]
print(x)


2.
n = int(input("Enter number of elements : "))
lst = [] 
for i in range(n):
  c = int(input("enter elements:"))  
  lst.append(c)
x=0
str= [] #new list 


3.
#taking a list as input
n=int(input("Enter number of elements : "))
l=list()
for i in range(n):
    l.append(int(input("enter a number:")))
for j in range(n):
    for k in range(j+1,n):
        if l[j]>=l[k]:
            l[j],l[k]=l[k],l[j]
print(f"the sorted list is {l}")


4.
R=int(input("enetr the number of rows:"))
C=int(input("enter number of columns:"))
matrix1=[]
for i in range(R):
    row=[]
    for j in range(C):
        x=float(input("enter the number:"))
        row.append(x)
    matrix1.append(row)

matrix2=[]
for i in range(R):
    row=[]
    for j in range(C):
        x=float(input("enter the number:"))
        row.append(x)
    matrix2.append(row)   

sum_matrix=[]
for i in range(R):
    row=[]
    for j in range(C):
        sum=matrix1[i][j]+matrix2[i][j]
        row.append(sum)
    sum_matrix.append(row)

print("Matrix1")
for i in matrix1:
    print(i)

print("Matrix2")
for i in matrix2:
    print(i)

print("Sum Matrix")
for i in sum_matrix:
    print(i)

#2
R1=int(input("enetr the number of rows for 1st matrix:"))
C1=int(input("enter number of columns for 1st matrix:"))
matrix1=[]
for i in range(R1):
    row=[]
    for j in range(C1):
        x=float(input("enter the number:"))
        row.append(x)
    matrix1.append(row)

R2=int(input("enetr the number of rows for 2nd matrix:"))
C2=int(input("enter number of columns for 2nd matrix:"))
matrix2=[]
for i in range(R2):
    row=[]
    for j in range(C2):
        x=float(input("enter the number:"))
        row.append(x)
    matrix2.append(row)   

if C2==R1:
    multiply_matrix=[]
    for i in range(R1):
        row=[]
        for j in range(C2):
            sum=0
            for k in range(C1):
                sum+=matrix1[i][k]*matrix2[k][j]
            row.append(sum)
        multiply_matrix.append(row) 
else:
    print("invalid input ,cannot multiply a matrix with column of 1st != row of 2nd")       

print("Matrix1")
for i in matrix1:
    print(i)

print("Matrix2")
for i in matrix2:
    print(i)

print("multiply Matrix")
for i in multiply_matrix:
    print(i)


# 5(a)
N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=str(input("enter a string:"))
   l.append(a)
print(f"the list of strings is {l}")
b=str(input("enter a string to be searched:"))
for j in l:
    if b==j:
        s=s+1
print(f"the string {b} is repeated {s} times")
  
#(b)
N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=int(input("enter the numbers:"))
   l.append(a)
print(f'the list  is {l}')
new_list=[]
for i in l:
    if i>0:
         new_list.append(i**2)
         
    elif i<0:
         new_list.append(0)
print(f'the new list is {new_list}')

# (c)
N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=int(input("enter the numbers:"))
   l.append(a)
print(f'the list  is {l}')
new_list=[]
for i in l:
    if i>=10 and i<=20:
         new_list.append(i**2)
         
    else:
         new_list.append(i)
print(f'the new list is {new_list}')

# (d)
N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=str(input("enter the numbers:"))
   l.append(a)
print(f'the list  is {l}')

new_list=[i.title() if not i.title() else i for i in l]
print(f'the new list is {new_list}')

6.
n = int(input("Enter the number of students: "))
records = []
for i in range(n):
    name = input("Enter student name: ")
    rollno = input("Enter roll number: ")
    marks = int(input("Enter total marks (out of 100) for {}: ".format(name)))
    records.append({'Name','RollNo', 'Marks'})
print(f'The records are {records}')
for student in records:
    print(f"Name: {student['Name']}")
    print(f"Roll No: {student['Roll No']}")
    print(f"Total Marks: {student['Total Marks']}")
    print()


#student with highest marks

    max_marks_student = records[0]
    for student in records:
        if student["Total Marks"] > max_marks_student["Total Marks"]:
            max_marks_student = student
    
     print(max_marks_student)



    if max_marks_student:
        print("Student with Maximum Marks:")
        print(f"Name: {max_marks_student['Name']}")
        print(f"Roll No: {max_marks_student['Roll No']}")
        print(f"Total Marks: {max_marks_student['Total Marks']}")
    else:
        print("No student records found.")

#part 2 of the question
for i in range(len(records)):
        rank = 1
        for j in range(len(records)):
            if records[j]["Total Marks"] > records[i]["Total Marks"]:
                rank += 1
        records[i]["Rank"] = rank

    # Display student details in ascending order of ranks
print("Student Details in Ascending Order of Ranks:")
for rank in range(1, len(records) + 1):
    for student in records:
        if student["Rank"] == rank:
            print(f"Rank: {student['Rank']}")
            print(f"Name: {student['Name']}")
            print(f"Roll No: {student['Roll No']}")
            print(f"Total Marks: {student['Total Marks']}")
            print()






            
            
