# Author: 24f1002781@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

# ----------------------------------------------------
# Load employee dataset
# ----------------------------------------------------
df = pd.read_csv("employees.csv")

# Frequency count for R&D
rd_count = df[df["department"] == "R&D"].shape[0]
print("Frequency count for R&D department:", rd_count)

# ----------------------------------------------------
# Create histogram visualization
# ----------------------------------------------------
plt.figure(figsize=(8, 6))
sns.histplot(
    data=df,
    x="department",
    stat="count",
    discrete=True,
    color="skyblue",
    edgecolor="black"
)
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Employee Distribution by Department")
plt.tight_layout()

# Convert histogram to base64 so HTML can display it
buf = BytesIO()
plt.savefig(buf, format="png")
plt.close()
buf.seek(0)
img_base64 = base64.b64encode(buf.read()).decode("utf-8")

# ----------------------------------------------------
# Prepare HTML content (visualization + email + code)
# ----------------------------------------------------
with open(__file__, "r") as f:
    python_code = f.read()

html_output = f"""
<html>
<head>
    <title>Department Histogram</title>
</head>
<body style="font-family: Arial; margin: 20px;">

<h2>Department Histogram</h2>

<img src="data:image/png;base64,{img_base64}" width="650">

<p><b>Email:</b> 24f1002781@ds.study.iitm.ac.in</p>

<h3>Python Code Used</h3>
<pre style="white-space: pre-wrap;">{python_code}</pre>

</body>
</html>
"""

# Save final HTML file
with open("department_histogram.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("HTML file generated successfully: department_histogram.html")
