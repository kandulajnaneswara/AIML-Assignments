#Output for numpy_scores
```bash
==================================================
Task 1 — Generate and Inspect the Data
==================================================
Scores of 5 students in all 4 subjects: [[88 78 64 92]
 [57 70 88 68]
 [72 60 60 73]
 [85 89 73 52]
 [71 51 73 93]]
Score of the 3rd student in the 2nd subject: 60
Scores of the last 2 students in all subjects: [[85 89 73 52]
 [71 51 73 93]]
Scores of the first 3 students in subjects 2nd and 3rd only: [[78 64]
 [70 88]
 [60 60]]
==================================================
Task 2 — Analyze with Broadcasting
==================================================
Average score per subject rounded to 2 decimal places: [74.6 69.6 71.6 75.6]
Curved scores: [[93 81 71 94]
 [62 73 95 70]
 [77 63 67 75]
 [90 92 80 54]
 [76 54 80 95]]
Best score per student: [94 95 77 92 95]
==================================================
Task 3 — Normalize and Identify
==================================================
Min value per row: [[71]
 [62]
 [63]
 [54]
 [54]]
Max value per row: [[94]
 [95]
 [77]
 [92]
 [95]]
Normalized scores of each student: [[0.95652174 0.43478261 0.         1.        ]
 [0.         0.33333333 1.         0.24242424]
 [1.         0.         0.28571429 0.85714286]
 [0.94736842 1.         0.68421053 0.        ]
 [0.53658537 0.         0.63414634 1.        ]]
Index of highest normalization value (student, subject): 0, 3
scores above 90: [93 94 95 92 95]
