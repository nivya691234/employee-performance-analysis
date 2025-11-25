# Author: 24f1002781@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the employee data
df = pd.read_csv('employees.csv')

# Calculate frequency count for the "R&D" department
rd_count = df[df['department'] == 'R&D'].shape[0]
print(f'Frequency count for R&D department: {rd_count}')

# Create a histogram showing the distribution of departments
plt.figure(figsize=(8,6))
sns.histplot(data=df, x='department', stat='count', discrete=True, color='skyblue', edgecolor='black')
plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.tight_layout()

# Save the histogram as HTML using mpld3 for web publishing
import mpld3
html_str = mpld3.fig_to_html(plt.gcf())
with open('department_histogram.html', 'w') as f:
    f.write(html_str)
plt.close()
