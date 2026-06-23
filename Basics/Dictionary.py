#dictionary


# declaring dict
student = {
    "roll_no": 101,
    "name": "Prachi",
    "marks": 92
}

print(student)

# Access values using keys
print(student["name"])
print(student["marks"])

# Changing value
student["marks"] = 95
print(student)

# Adding new key-value pair
student["age"] = 20
print(student)

# Removing element
del student["marks"]
print(student)

# Remove the marks key
removed_value = student.pop("name")
print("Removed Value =", removed_value)
print(student)

#remove las inserted element
removed_item = student.popitem()
print("Removed Item =", removed_item)
print(student)

# get function
print(student.get("age"))

# Looping
for key in student:
    print(key)

for key, value in student.items():
    print(key, ":", value)

# Check for key
if "age" in student:
    print("Marks key exists")



# Dictionary Methods

print(student.keys())
print(student.values())
print(student.items())
print(len(student))



# Nested Dictionary
students = {
    "student1": {
        "name": "Prachi",
        "marks": 92
    },
    "student2": {
        "name": "Rahul",
        "marks": 85
    }
}


print(students["student1"]["name"])
print(students["student2"]["marks"])



# Creating a copy 
student = {
    "roll_no": 101,
    "name": "Prachi",
    "marks": 92
}


student_copy = student.copy()
print(student_copy)

# Modify the copy
student_copy["marks"] = 95
print("Original Dictionary =", student)
print("Copied Dictionary =", student_copy)

#using in range
squared_nums = {x: x**2 for x in range(6)}
print(squared_nums)

#clear whole method
squared_nums.clear()

#default values
subjects = ["Maths", "Physics", "Chemistry"]
marks = dict.fromkeys(subjects, 0)
print(marks)