# Dictionary Example
student = {"name": "Vikram", "age": 22, "course": "BSc"}

print("Dictionary:", student)          # {'name': 'Vikram', 'age': 22, 'course': 'BSc'}
print("Name:", student["name"])        # Vikram

# Update
student["age"] = 23
print("Updated Age:", student)         # {'name': 'Vikram', 'age': 23, 'course': 'BSc'}

# Add new key
student["grade"] = "A"
print("After adding grade:", student)  # {'name': 'Vikram', 'age': 23, 'course': 'BSc', 'grade': 'A'}
