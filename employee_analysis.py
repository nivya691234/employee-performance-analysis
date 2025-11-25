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

email_html = '<p style="font-size:16px; color:black;">Email: 24f1002781@ds.study.iitm.ac.in</p>'

# Use <pre> for visible, scrollable text (like a code sample, but not hidden as comment or link!)
code_as_text = """
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
"""

code_html = f'<p><b>Python Code Used:</b></p><pre style="background:#fff;border:1px solid #ccc;font-size:14px;padding:8px;">{code_as_text}</pre>'

full_html = f"""
<html>
<head>
    <meta charset="utf-8">
    <title>Department Histogram</title>
</head>
<body>
{fig_html}
{email_html}
{code_html}
</body>
</html>
"""

with open('department_histogram.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("HTML file generated with email and Python code as plain visible text.")
