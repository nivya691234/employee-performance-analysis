# Author: 24f1002781@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3

df = pd.read_csv('employees.csv')
rd_count = df[df['department'] == 'R&D'].shape[0]
print(f'Frequency count for R&D department: {rd_count}')

plt.figure(figsize=(8,6))
sns.histplot(data=df, x='department', stat='count', discrete=True,
             color='skyblue', edgecolor='black')
plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.tight_layout()

fig_html = mpld3.fig_to_html(plt.gcf())
plt.close()

# Add your email visibly after the chart fragment (guaranteed to show)
email_html = '<p style="font-size:16px; color:black;">Email: 24f1002781@ds.study.iitm.ac.in</p>'

full_html = f"""
<html>
<head>
    <meta charset="utf-8">
    <title>Department Histogram</title>
</head>
<body>
{fig_html}
{email_html}
</body>
</html>
"""

with open('department_histogram.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("HTML file generated with email included and visible.")
