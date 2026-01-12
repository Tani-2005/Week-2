# Description: Calculates student grade based on marks with validation and messages

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better 😊"
    elif marks >= 60:
        return "D", "You passed. Keep practicing 💪"
    else:
        return "F", "Don't give up! Try harder next time 💡"


# Get student name
student_name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks must be between 0 and 100. Try again.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print("\n📊 RESULT FOR", student_name.upper())
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
