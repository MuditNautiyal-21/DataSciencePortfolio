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


# Dictionaries - Key-Value pairs
person = {
    "name": "Mudit",
    "education": "Masters in Professional Studies in Data Science & Applications",
    "university": "University at Buffalo",
    "experience_years": 5
}
print(f"Person: {person}")
print(f"Education: {person['education']}")

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
job_description = "Looking for data scientist with Python and SQL skills."
print(f"Python in job description: {'Python' in job_description}")
print(f"Words in job description: {len(job_description.split())}")
print(f"Uppercase: {job_description.upper()}")

####################################################################################
import numpy as np

data = np.genfromtxt("dummy_data.csv", delimiter=",", skip_header=1)

# Print dataset information
print("Shape of dataset:", data.shape)
print("First 5 rows:\n", data[:5])

# Check for missing values:
print("Any missing values?", np.isnan(data).any())

# Data Preprocessing:
np.set_printoptions(suppress=True)
print(data)

x = data[:, :2] # Extract first 2 columns
y = data[:, 2] # Extract last column
print("Features:\n", x)
print("Target Variable:\n", y)


###################################################################################
# Normalize & Standardize the Data
x_min = x.min(axis=0)
x_max = x.max(axis=0)

x_normalized = (x-x_min)/(x_max - x_min)
print("Normalized Features:\n", x_normalized)

# Applying Z-Score Standardization
x_mean = x.mean(axis=0)
x_std = x.std(axis=0)

x_standardized = (x - x_mean) / x_std
print("Standardized Features:\n", x_standardized)

###################################################################################
# Feature Engineering:
from itertools import combinations

print(":::Feature Engineering:::")
# Creating a new feature by multiplying existing ones:
poly_features = np.array([x[:, i]*x[:,j]
                          for i, j in combinations(range(x.shape[1]), 2)]).T
print("Polynomial Feature:\n", poly_features)

#################################################################################
# Detecting Outliers
print("Outliers Detection")

# Compute Z-Scores for each feature
z_score = (x-x.mean(axis=0))/x.std(axis=0)

# Defining threshold for outliers (commonly 3 standard deviations)
outliers = np.abs(z_score)

# Showing results:
print("Outlier Detection (True = Outlier):\n", outliers)

# Converting Z-Score into outlier Flag
print("Outliers as Flag")
outliers = np.abs(z_score) > 3
print("Outlier Detection (True = Outlier, False = Normal):\n", outliers)

# Detect outliers using a 2 standard deviation threshold
print("Are There Any Outliers Beyond 2 Standard Deviations?")
outliers_2sd = np.abs(z_score) > 2

print("Outliers beyond 2 SD:\n", outliers_2sd)