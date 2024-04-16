import numpy as np

students = 10 * np.random.randn(100) + 175

students = students.reshape(10, 10)

odd_students = np.hsplit(students,)


print(odd_students)
