# Author: 24f1002781@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3

# Load the employee data
df = pd.read_csv('employees.csv')

# Calculate frequency count for the "R&D" department
rd_count = df[df['department'] == 'R&D'].shape[0]
print(f'Frequency count for R&D department: {rd_count}')

# Create a histogram showing the distribution of departments
plt.figure(figsize=(8,6))
sns.histplot(data=df, x='department', stat='count', discrete=True,
             color='skyblue', edgecolor='black')
plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.tight_layout()

# Convert matplotlib figure to HTML with mpld3
fig_html = mpld3.fig_to_html(plt.gcf())
plt.close()

# Add your email (plain visible text)
email_html = '<p style="font-size:16px; color:black;">Email: 24f1002781@ds.study.iitm.ac.in</p>'

# Add your actual Python code as a code block (escaped for HTML)
python_code = '''
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
email_html = '<p style="font-size:16px; color:black;">Email: 24f1002781@ds.study.iitm.ac.in</p>'
python_code_html = ...
'''

python_code_html = f'<h3>Python Code Used:</h3><pre style="background:#f8f8f8; color:#222; padding:10px;"><code>{python_code}</code></pre>'

# Compose the final HTML output
full_html = f"""
<html>
<head>
    <meta charset="utf-8">
    <title>Department Histogram</title>
</head>
<body>
{fig_html}
{email_html}
{python_code_html}
</body>
</html>
"""

with open('department_histogram.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("HTML file generated with plain email and code block included.")
