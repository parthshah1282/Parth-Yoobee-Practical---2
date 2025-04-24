import numpy as np
Scores = np.array([[78,85,90],[88,79,92],[84,76,88],[90,93,94],[75,80,70]])
student_average = np.mean(Scores,axis=1)
print("student Average:",student_average)
subject_average = np.mean(Scores,axis=0)
print("Subject Average:",subject_average)
total_scores = np.sum(Scores,axis=1)
top_student = np.argmax(total_scores)
Scores[:,2]+=5
print("New Updated Score:",Scores)