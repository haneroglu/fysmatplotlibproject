import matplotlib.pyplot as plt

plt.title('Freshmen in UMass by Department (2023)')
students = [449, 348, 1639, 712, 150, 654, 796, 74, 352, 85]
labels = ['College of Humanities\n and Fine Arts',
          'College of\n Information and\n Computer Sciences',
          'College of\n Natural Sciences',
          'College of Social and\n Behavioral Sciences',
          'College of Education',
          'College of Engineering', 
          'Isenberg\n School of \nManagement',
          'College of Nursing',
          'School of Public\nHealth and Health\n Sciences',
          'Other']
plt.xlabel('College')
plt.ylabel('Number of Students')

plt.barh(labels, students, color='orange')

plt.show()