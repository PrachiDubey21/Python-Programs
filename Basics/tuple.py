# Tuple

#they are immutable
# they can hold duplicates

# declaring tuple
marks = (85, 90, 78, 92, 88 , 90)
print(marks)

# Acessing elements
print(marks[0])
print(marks[3])

# Negative indexing
print(marks[-1])

# length
print(len(marks))

# Print each mark one by one
for mark in marks:
    print(mark)

# whether element exists in the tuple
print(90 in marks)

# count() - count occurrence of an element
print(marks.count(90))

# index() - find index of an element
print(marks.index(92))

# Concatenation
semester1 = (85, 90, 78)
semester2 = (92, 88)
all_marks = semester1 + semester2
print(all_marks)

# Repetition
grades = ("A", "B")
print(grades * 3)

# Slicing

# accessing index range
print(marks[1:5])

# from beginning to index 3
print(marks[:4])

# from index 2 to end
print(marks[2:])

# Copying tuple
new_marks = marks[:]
print(new_marks)

# Select every second element
print(marks[::2])

# Select elements at odd indices
print(marks[1::2])

# Extract last three elements
print(marks[-3:])

# Reverse the tuple
print(marks[::-1])

# Extract from -5 to -2
print(marks[-5:-1])

# Print all marks in one line
for mark in marks:
    print(mark, end=" , ")

print()

# Check marks greater than 80
for mark in marks:
    if mark > 80:
        print(mark, "is greater than 80")

# Check if element is present
if 90 in marks:
    print("90 is present in the tuple")

# Tuple packing
student = (101, "Prachi", 92)
print(student)

# Tuple unpacking
roll_no, name, score = student
print(roll_no)
print(name)
print(score)

# Single element tuple
single_mark = (85,)
print(single_mark)
print(type(single_mark))

# Nested tuple
students = (
    ("Prachi", 92),
    ("Rahul", 85),
    ("Aman", 78)
)
print(students)

# Access nested tuple elements
print(students[0])
print(students[0][1])

# Generator Expression.
marks = (85, 90, 78, 92, 88)
squares = tuple(mark * mark for mark in marks)
print("Original Tuple:", marks)
print("Squared Tuple:", squares)