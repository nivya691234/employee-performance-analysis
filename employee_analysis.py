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

# Convert matplotlib figure to HTML
html_chart = mpld3.fig_to_html(plt.gcf())
plt.close()

email = "24f1002781@ds.study.iitm.ac.in"

# Wrap inside a full HTML document
html_out = f"""
<html>
<head>
    <meta charset="utf-8">
    <title>Department Histogram</title>
</head>
<body>
{html_chart}

<p style="font-size:16px; color:black;">
    <b>Email:</b> {email}
</p>

</body>
</html>
"""

with open('department_histogram.html', 'w') as f:
    f.write(html_out)

print("HTML file generated with email included.")
