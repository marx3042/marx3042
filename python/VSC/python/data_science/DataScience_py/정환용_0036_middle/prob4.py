import numpy as np

students = 3.5 * np.random.randn(100) + 75
round_2_score = []

for i in students:
    round_2_score.append(round(i, 2))

round_2_score = round_2_score.reshape(10, 10)
odd_score = np.hsplit(round_2_score, 5)
print(odd_score)

