name = input("Enter student name: ")

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "F"

print("\n--- Result ---")
print("Name:", name)
print("Total:", total, "/300")
print("Percentage:", percentage, "%")
print("Grade:", grade)