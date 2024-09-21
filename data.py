import matplotlib.pyplot as plt

plt.title('Freshmen in UMass by Department (2023)')
students = [449, 348, 1639, 712, 150, 654, 796, 74, 352, 85]
labels = ['College of Humanities\n and Fine Arts',
          'College of Information\n and Computer Sciences',
          'College of\n Natural Sciences',
          'College of Social and\n Behavioral Sciences',
          'College of Education',
          'College of Engineering', 
          'Isenberg\n School of Management',
          'College of Nursing',
          'School of Public Health\n and Health Sciences',
          'Other']
plt.xlabel('College')
plt.ylabel('Number of Students')

plt.barh(labels, students, color='orange')

plt.show()