# Author: 24f1002781@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

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

buf = BytesIO()
plt.savefig(buf, format='png')
plt.close()
buf.seek(0)
encoded = base64.b64encode(buf.read()).decode('utf-8')
img_html = f'<img src="data:image/png;base64,{encoded}" alt="Department Histogram" width="600"/>'

email_html = '<p style="font-size:16px; color:black;">Email: 24f1002781@ds.study.iitm.ac.in</p>'

code_visible = """
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

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

buf = BytesIO()
plt.savefig(buf, format='png')
plt.close()
buf.seek(0)
encoded = base64.b64encode(buf.read()).decode('utf-8')
img_html = f'<img src="data:image/png;base64,{encoded}" alt="Department Histogram" width="600"/>'

email_html = '<p style="font-size:16px; color:black;">Email: 24f1002781@ds.study.iitm.ac.in</p>'
"""

code_html = f'<p><b>Python Code Used:</b></p><pre style="background:#fff;border:1px solid #ccc;font-size:14px;padding:8px;">{code_visible}</pre>'

full_html = f"""
<html>
<head>
    <meta charset="utf-8">
    <title>Department Histogram</title>
</head>
<body>
{img_html}
{email_html}
{code_html}
</body>
</html>
"""

with open('department_histogram.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("HTML file generated with chart, email, and Python code (all visible as plain text).")
