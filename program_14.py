import pickle
import shelve

# Create a class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

# Create object
s1 = Student("Rahul", 90)

# Save object using pickle
with open("student.pkl", "wb") as file:
    pickle.dump(s1, file)

print("Object saved using pickle")

# Load object using pickle
with open("student.pkl", "rb") as file:
    s2 = pickle.load(file)

print("Name:", s2.name)
print("Marks:", s2.marks)

# Save data using shelve
with shelve.open("student_data") as db:
    db["student"] = s1

print("Object saved using shelve")

# Read data using shelve
with shelve.open("student_data") as db:
    s3 = db["student"]
    print("Name:", s3.name)
    print("Marks:", s3.marks)