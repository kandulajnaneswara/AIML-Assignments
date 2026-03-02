print(f"{50*"="}")
print(f"Task 1 — Generate and Inspect the Data")
print(f"{50*"="}")

import numpy as np

np.random.seed(42)
scores = np.random.randint(50,101,size=(5,4))

#scores representing 5 students and 4 subjects
print(f"Scores of 5 students in all 4 subjects: {scores}")

#score of the 3rd student in the 2nd subject
score1 = scores[2,1]
print(f"Score of the 3rd student in the 2nd subject: {score1}")

#All scores of the last 2 students (all subjects)
score2 = scores[3::]
print(f"Scores of the last 2 students in all subjects: {score2}")

#All scores for the first 3 students in subjects 2 and 3 only
score3 = scores[0:3, 1:3]
print(f"Scores of the first 3 students in subjects 2nd and 3rd only: {score3}")


print(f"{50*"="}")
print(f"Task 2 — Analyze with Broadcasting")
print(f"{50*"="}")


#column wise mean (average per subject)
avg_score = scores.mean(axis = 0)
col_mean = np.round(avg_score,2)
print(f"Average score per subject rounded to 2 decimal places: {col_mean}")

#Add curve using broadcasting
curve = np.array([5, 3, 7, 2])
curve_score=np.minimum(scores+curve,100)
print(f"Curved scores: {curve_score}")

#Row-wise max (best score per student)
max_curve_score = curve_score.max(axis = 1)
print(f"Best score per student: {max_curve_score}")


print(f"{50*"="}")
print(f"Task 3 — Normalize and Identify")
print(f"{50*"="}")

#Min-max normalization per row
row_min = curve_score.min(axis=1, keepdims=True)
print(f"Min value per row: {row_min}")
row_max = curve_score.max(axis=1, keepdims=True)
print(f"Max value per row: {row_max}")

#Normalize scores
scale = (curve_score-row_min)/(row_max-row_min)
print(f"Normalized scores of each student: {scale}")

#Index of the single highest value in normalized array
max_value = scale.max()
pos = np.where(scale == max_value)
row = pos[0][0]
col = pos[1][0]
print(f"Index of highest normalization value (student, subject): {row}, {col}")

#Extracting score > 90
mask = curve_score > 90
print(f"scores above 90: {curve_score[mask]}")
