# 1.(a)
n = int(input("Enter positive integers: "))
lst=[]
for i in range(n):
    c = int(input("enter elements:"))
    lst.append(c) # adding the element
print(lst)

# (b)
l1= list(map(int,input().split()))
l2 =[]
s1=set()
for j in l1:
   if j not in s1:
      s1.add(j)
      l2.append(j)
print(l2)
print(s1)

#2.
my_list1 = [1 ,2 ,3, 3, 4, 5,'Lucas', 5]
print(my_list1)
my_set1 = set(my_list1) 
print(my_set1)

my_list2 = ['John','Lara','Max','Lucas',5]
print(my_list2)
my_set2 = set(my_list2) 
print(my_set2)

print("Union :", my_set1 | my_set2) #union
print("Intersection :", my_set1 & my_set2) # intersection
print("Difference :", my_set1 - my_set2)  #difference 
print("Symmetric difference :", my_set1 ^ my_set2)  # symmetric difference 

newList1 = []
newList1.extend(my_list1)
for element in my_list2:
    if element not in newList1:
        newList1.append(element)
print("Union of the lists is:", newList1)

newList2 = []
newList2.extend(my_list1)
for element in my_list2:
    if element not in newList2:
         newList2.append(element)
print("Intersection of the lists is:", newList2)

# 3.
N = int(input('enter the size of square matrix: '))
M= []
print('enter matrix elements:')
for i in range(N):
    r= [int(x) for x in input().split()]
    M.append(r)
print(M)   

# sum of diagonals of matrix
d1 = sum(M[i][i] for i in range(len(M))) # principle diagonal
d2 = sum(M[i][len(M)-1-i] for i in range(len(M))) # non-principle diagonal
print('sum of principle diagonal: ',d1)
print('sum o non-principle diagonal: ',d2)

# transpose
def t(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

MT= t(M)
print('transpose is: ',MT)

# check for symmetric
if M==MT:
    print('Matrix is symmetric.')
else:
    print('Not symmetric.')

# check for upper and lower triangular
def up_tr(matrix):
    return all(matrix[i][j] == 0 for i in range(1,len(matrix)) for j in range(i))

def lo_tr(matrix):
    return all(matrix[i][j] == 0 for i in range(len(matrix)) for j in range(i+1, len(matrix[0])))

print('is this matrix upper triangular? :', up_tr(M))
print('is this matrix lower triangular? :', lo_tr(M))


4.
# Input for matrix dimension
n = int(input("Enter the dimension of the square matrix (N): "))

# Input for the matrix
matrix = []
print(f"Enter elements for a {n}x{n} matrix:")
for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

# Convert the matrix to row echelon form
current_column = 0

for row in range(n):
    # Find the first non-zero element in the current row
    while current_column < n and matrix[row][current_column] == 0:
        current_column += 1

    # If all elements in the current column are zero, move to the next column
    if current_column == n:
        continue

    # If the non-zero element is not in the current row, swap rows
    if matrix[row][current_column] != 1:
        for i in range(row + 1, n):
            if matrix[i][current_column] == 1:
                matrix[row], matrix[i] = matrix[i], matrix[row]
                break

    # Normalize the current row
    pivot = matrix[row][current_column]
    matrix[row] = [element / pivot for element in matrix[row]]

    # Eliminate non-zero elements below the pivot
    for i in range(row + 1, n):
        factor = matrix[i][current_column]
        matrix[i] = [a - factor * b for a, b in zip(matrix[i], matrix[row])]

    # Increment current_column
    current_column += 1

# Display the matrix in row echelon form
print("\nMatrix in Row Echelon Form:")
for row in matrix:
    print(row)

    