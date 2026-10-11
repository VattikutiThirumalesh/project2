# IMPLEMENTATION OF TUPLES, SETS AND DICTIONARIES

# 1. TUPLE
student_tuple = ("Rahul", 21, "CSE")
print("----- TUPLE -----")
print("Student:", student_tuple)
print("Name:", student_tuple[0])
print("Age:", student_tuple[1])
print("Branch:", student_tuple[2])

# 2. SET
print("\n----- SET -----")
python_students = {"Rahul", "Priya", "Arun", "Sneha"}
java_students = {"Arun", "Sneha", "Kiran", "Vijay"}

print("Python Students:", python_students)
print("Java Students:", java_students)
print("Union:", python_students | java_students)
print("Intersection:", python_students & java_students)

# 3. DICTIONARY
print("\n----- DICTIONARY -----")
student = {
    "roll_no": "101",
    "name": "Rahul",
    "branch": "CSE",
    "cgpa": 8.5
}

for key, value in student.items():
    print(key, ":", value)