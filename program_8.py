# Custom Flexible Student Grade & Statistics Calculator

def calculate_grades(*args, **kwargs):
    # Calculate minimum, maximum, and average
    minimum = min(args)
    maximum = max(args)
    average = sum(args) / len(args)

    # Calculate letter grade
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Display assessment details
    print("\nAssessment Details:")
    for key, value in kwargs.items():
        print(key, ":", value)

    # Return multiple values as a tuple
    return minimum, maximum, average, grade


# Function call
result = calculate_grades(
    85, 90, 78, 95, 88,
    Math="85",
    Science="90",
    English="78"
)

# Tuple unpacking
minimum, maximum, average, grade = result

print("\nStudent Statistics:")
print("Minimum Marks:", minimum)
print("Maximum Marks:", maximum)
print("Average Marks:", round(average, 2))
print("Final Letter Grade:", grade)