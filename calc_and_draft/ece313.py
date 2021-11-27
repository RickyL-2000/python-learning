# %%
import math
import numpy as np

def C(a, b):
    return math.factorial(a) / math.factorial(a-b) / math.factorial(b)

# %%
# exam 1 q5 autograding
def correct_ans(R):
    R1, R2, R3, R4, R5, R6 = R
    return (1 - (1 - R1)*(1 - R2)*(1 - R3*R5)) * R4 + R3*R5*R6*(1 - R4)

def student_ans(R):
    R1, R2, R3, R4, R5, R6 = R
    
    ans = R3*(1 - (1-R4)*(1-R6))*R5 + R4 * (1-(1-R1)*(1-R2))*(1-R5)
    return ans

"""
fully expansion:
R3*R4*R5 + R3*R5*R6 - R3*R4*R5*R6 + R1*R4 - R1*R3*R4*R5 + R2*R4 - R2*R3*R4*R5 + R1*R2*R3*R4*R5 - R1*R2*R4

split as R6
(1-R6)*R4*(1-(1-R3*R5)*(1-(R1+R2-R1*R2))) + R6*((R1+R2-R1*R2)*R4+R3*R5-(R1+R2-R1*R2)*R4*R3*R5)

other forms
R4*(1-R5)*(1-(1-R1)*(1-R2))+R4*R5*(1-(1-R1)*(1-R2)*(1-R3)) + (1-R4)*R5*R3*R6
(1-(1-R4)*(1-R6))*R3*R5 + (1-(1-R1)*(1-R2))*R4*(1-R3*R5)
(R1+R2-R1*R2)*R4*(1-R3*R5) + (R4+R6-R4*R6)*R3*R5
"""

def grade():
    R = np.random.random(6)
    print("correct: ", correct_ans(R))
    print("student: ", student_ans(R))
    return np.isclose(correct_ans(R), student_ans(R))

grade()

# %%
# HW4 P
res = 1.0
for i in range(0, 13):
    res -= math.exp(-10) * 10**i / math.factorial(i)
print(res)

# %%
# HW p6d
for i in range(0, 8):
    print(C(7, i) * 0.8**i * (1 - 0.8)**(7-i))
