"""
student = {"name": "Ravi", "branch": "CSE", "year": 1}

print(student["name"])
print(student["branch"])
"""

"""
student = {"name": "Ravi", "branch": "CSE"}
# Add a new key-value pair
student["year"] = 1
student["cgpa"] = 8.5

# Update an existing value
student["cgpa"] = 9.0
"""
"""
student = {"name": "Ravi", "branch": "CSE", "year": 1, "cgpa": 8.5}

# del – removes a specific key
del student["year"]
print(student)

# pop() – removes key and returns its value
removed = student.pop("cgpa")
print(removed)
print(student)

last = student.popitem()
print(last)

student.clear()
print(student)  # Output: {}
"""

#  Membership testing
student = {"name": "Ravi", "branch": "CSE", "year": 1}

# Check if a KEY exists
print("name" in student)  
print("cgpa" in student)  
print("cgpa" not in student) 
print("CSE" in student)  
