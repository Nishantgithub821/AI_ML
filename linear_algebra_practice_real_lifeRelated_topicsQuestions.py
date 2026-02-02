"""
✅ JAHAN REAL-LIFE CONNECT KARNA CHAHIYE (IMPORTANT 🔥)

Ye concepts systems / relations / decisions se jude hote hain:

System of equations (Ax = b)

non-homogeneous / homogeneous

unique / infinite / no solution
👉 Real life: sound system, salary distribution, load sharing, ML regression

Matrix multiplication (@, .dot)
👉 Real life: transformations, influence, data flow

Rank, determinant (solution existence)
👉 Real life: “possible hai ya nahi” type decision problems

Inverse matrix
👉 Real life: undo process, decoding, reversing effect

Trace (advanced level)
👉 Real life: energy, variance, ML/covariance context

"""
# Answers 
# real life related examples to our main topics like homo linear equatino and non homo , determinant , rank etc right lets do 
"""
✅ QUESTION STATEMENT (REAL-LIFE ANALOGY)
💰 Salary Distribution Problem (Non-Homogeneous Linear System)

A company has two employees (Employee-1 and Employee-2).
Their salaries together must satisfy certain budget conditions decided by management.

Each condition represents a salary rule imposed by the company (like total payout or weighted contribution).

Depending on these rules:

there may be exactly one way to distribute salaries,

multiple ways to distribute salaries,

or no possible way to distribute salaries.

Task:
Using Python, analyze the salary system and determine whether the salary distribution has:

a unique solution

infinite solutions

no solution

Also determine whether the system is homogeneous or non-homogeneous.
"""
# Ab question kya kehta hai ki salray distributino de rakha hai ab 2 eployees hai right un dono ki ek to total sallry budget decided kiya hai and second weighted importance ke base pe salary dena and third 
# demanded salary di hai right ab hame kya kerna hai sabse pehle check kerna hai ki ye non hai ya homogenous hai right then agar non homogenous hua to ham iske 3 parts dif dif check kernge unique infinite 
# and no solutions ab isme kya hai ki jab ham answer nikalnge iska ya homogenous ka hamesha rnak ki ye 3 checje yaad rakhenge ki 1. rank nikalnge simple taki us company ko bharosa ho sake ki jo uske rules hai 
# like total budget and weighted salary budget ye dono alag alag hai na same to nahi 2. arguumented rank ye bharosa degi ki companyki salary   demand rules ke sath match kerti hai ya nahi and 3. kitni salary deni 
# hai kitne logo ko right  

# code 
import numpy as np

# ======================================================
# CASE 0: HOMOGENEOUS SYSTEM (b = 0)
# ======================================================
print("\nCASE 0: HOMOGENEOUS SYSTEM (All zero salary demand)")

# Salary rules matrix
salary_rules = np.array([
    [1, 2],   # Employee contributions to rule-1
    [3, 4]    # Employee contributions to rule-2
])

# Homogeneous system: zero salary demand
salary_demand = np.array([0, 0])

print("Homogeneous system (all zeros)")

# Rank check
rank_rules = np.linalg.matrix_rank(salary_rules)
rank_aug = np.linalg.matrix_rank(np.c_[salary_rules, salary_demand])
num_employees = salary_rules.shape[1]

if rank_rules == num_employees:
    print("Unique solution (trivial only): all salaries = 0")
else:
    print("Infinite solutions: zero + multiple non-zero salaries possible")



# ======================================================
# CASE 1: NON-HOMOGENEOUS — UNIQUE SOLUTION
# ======================================================
print("\nCASE 1: NON-HOMOGENEOUS — UNIQUE SALARY DISTRIBUTION")

salary_rules = np.array([
    [1, 1],
    [2, 3]
])

salary_demand = np.array([50, 130])   # Target salary budget

print("Non-homogeneous system (salary demand exists)")

rank_rules = np.linalg.matrix_rank(salary_rules)
rank_aug = np.linalg.matrix_rank(np.c_[salary_rules, salary_demand])

if rank_rules == rank_aug == num_employees:
    salaries = np.linalg.solve(salary_rules, salary_demand)
    print("Unique solution:", salaries)



# ======================================================
# CASE 2: NON-HOMOGENEOUS — INFINITE SOLUTIONS
# ======================================================
print("\nCASE 2: NON-HOMOGENEOUS — INFINITE SALARY DISTRIBUTIONS")

salary_rules = np.array([
    [1, 1],
    [2, 2]
])

salary_demand = np.array([40, 80])   # Consistent demand

print("Non-homogeneous system (salary demand exists)")

rank_rules = np.linalg.matrix_rank(salary_rules)
rank_aug = np.linalg.matrix_rank(np.c_[salary_rules, salary_demand])

if rank_rules == rank_aug < num_employees:
    print("Infinite solutions: multiple ways to distribute salaries")


# ======================================================
# CASE 3: NON-HOMOGENEOUS — NO SOLUTION
# ======================================================
print("\nCASE 3: NON-HOMOGENEOUS — NO SALARY DISTRIBUTION POSSIBLE")

salary_rules = np.array([
    [1, 1],
    [2, 2]
])

salary_demand = np.array([40, 90])   # Conflicting demand

print("Non-homogeneous system (salary demand exists)")

rank_rules = np.linalg.matrix_rank(salary_rules)
rank_aug = np.linalg.matrix_rank(np.c_[salary_rules, salary_demand])

if rank_rules != rank_aug:
    print("No solution: company demands are contradictory")


#2
# This real life exmaple of cololr miizing in which we have paint matrix values and a base paint so we multiply the base paint 
# to paint matrix then our final color mixing comes and same result with dot
import numpy as np

# Paint contribution matrix
paint_matrix = np.array([
    [0.6, 0.3, 0.1],
    [0.2, 0.5, 0.3],
    [0.3, 0.3, 0.4]
])

# Base paint quantities
base_paint = np.array([10, 5, 2])

# Using @ operator
final_colors = paint_matrix @ base_paint
print("Final color quantities (@):", final_colors)

# Using .dot
final_colors_dot = np.dot(paint_matrix, base_paint)
print("Final color quantities (.dot):", final_colors_dot)
#3 rank determinant same aas ist one so no need to write again 
#4 inverse right and also here we implement the idomptent matrix real life exmaple very smaller examples right 
# now here is our 4th topic that is idempotent example that is rel lif eattendance matrix means asquare  = A
#That means the attendence is not change after apply again attending by multiplying by itself right 
# now this example is for idemptotent matrix right but we need the inverse matrix code so 
import numpy as np

# Attendance matrix for 4 students
# 1 = present, 0 = absent
# Rows = student, Columns = class session
attendance = np.array([
    [1, 0, 0, 0],  # Student-1 present in session-1
    [0, 1, 0, 0],  # Student-2 present in session-2
    [0, 0, 1, 0],  # Student-3 present in session-3
    [0, 0, 0, 1]   # Student-4 present in session-4
])

print("Original attendance matrix:\n", attendance)

# Multiply matrix with itself (re-applying attendance)
attendance_squared = attendance @ attendance
print("\nAttendance after re-applying:\n", attendance_squared)

# Check if matrix is idempotent and explain in real-life
if np.allclose(attendance_squared, attendance):
    print("\n✅ Students already marked present remain marked. No change in attendance after re-applying.")
else:
    print("\n❌ Some students' attendance changed after re-applying. Something is wrong!")

# here is the inverse matrix real life analogy code 
import numpy as np

# Involutory matrix representing a 2-switch system
# Example: flipping switch flips state, flipping twice → original
switch_matrix = np.array([
    [0, 1],  # Flip switch 1 → goes to state 2
    [1, 0]   # Flip switch 2 → goes to state 1
])

print("Original switch matrix:\n", switch_matrix)

# Multiply matrix with itself (flip twice)
switch_squared = switch_matrix @ switch_matrix
print("\nSwitch matrix squared (flip twice):\n", switch_squared)

# Identity matrix for comparison
identity = np.eye(2)

# Check involutory property
if np.allclose(switch_squared, identity):
    print("\n✅ Flipping the switches twice returns to original state. Involutory confirmed!")
else:
    print("\n❌ Flipping twice did not return to original state. Not involutory.")


# 5th topic hai trace ka 
import numpy as np

# Team contribution matrix
contribution = np.array([
    [3, 2, 1],  # Alice
    [1, 4, 2],  # Bob
    [2, 1, 5]   # Charlie
])

print("Team contribution matrix:\n", contribution)

# Calculate trace
main_contribution = np.trace(contribution)
print("\nTotal main task contribution of all team members:", main_contribution)




