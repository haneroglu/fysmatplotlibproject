import matplotlib.pyplot as plt

plt.title('Freshmen in UMass by Origin (2023)')
students = [3551, 1229, 479]
labels = ['In-state', 'Out-of-state', 'International']
plt.xlabel('Student Origin')
plt.ylabel('Number of Students')

plt.pie(students, labels=labels, autopct='%1.1f%%')

plt.show()