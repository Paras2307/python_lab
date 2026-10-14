import pickle
import shelve

# Student class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


# Create an object
s1 = Student("Rahul", 85)

# Save object using pickle
with open("student.pkl", "wb") as file:
    pickle.dump(s1, file)

print("Object saved using pickle.")

# Restore object using pickle
with open("student.pkl", "rb") as file:
    s2 = pickle.load(file)

print("\nRestored Object:")
s2.display()


# Save object using shelve
with shelve.open("student_data") as db:
    db["student1"] = s1

print("\nObject saved using shelve.")

# Restore object using shelve
with shelve.open("student_data") as db:
    s3 = db["student1"]

print("\nObject restored using shelve:")
s3.display()