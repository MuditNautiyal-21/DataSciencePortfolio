# Python Basics for Data Science: I'm starting this module/repository to re-inforce my learnings in data science, to build a good portfolio.

# 1. Variables and Data Types
name = "Mudit" # String
age = 30 # Integer (Can adjust age)
height = 5.10 # Float (Adjustable)
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")


# 2. Data Structures
# lists - Ordered, mutable collection
skills = ["Python", "SQL", "Data Analysis", "Machine Learning"]
print(f"Skills: {skills}")
print(f"First Skill: {skills[0]}")
skills.append("Data Visualization")
print(f"Updated Skills: {skills}")


# 3. Control Flow
# If-Else Statements
experience = person["experience_years"]
if experience > 5:
    seniority = "Senior"
elif experience > 2:
    seniority = "Mid-Level"
else:
    seniority = "Junior"
print(f"Seniority Level: {seniority}")

# Loops
print("Skills with their lengths:")
for skill in skills:
    print(f"{skill}: {len(skill)} characters")

# 4. Functions
def calculate_salary(base, experience, has_masters=False):
    """Calculate estimated salary based on experience and education."""
    salary = base
    salary += experience * 10000
    if has_masters:
        salary += 15000
    return salary

estimated_salary = calculate_salary(60000, experience, True)
print(f"Estimated salary: ${estimated_salary}")


# 5. String Operations