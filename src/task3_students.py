import numpy as np
import pandas as pd

marks = np.array([[70, 80, 90],
                  [60, 75, 85],
                  [88, 92, 79],
                  [55, 65, 70]])
# print(marks)
print("Shape:",marks.shape)

student_average=np.mean(marks,axis=1)
print("Students average:",student_average)

subject_average=np.mean(marks,axis=0)
print("Subject average:",subject_average)

updated_marks=marks+5
print("Updated marks after adding grace 5 marks:\n",updated_marks)

weight=[0.3, 0.3, 0.4] 
weighted_score=np.dot(marks,weight)
print("Weighted scores:",weighted_score)


