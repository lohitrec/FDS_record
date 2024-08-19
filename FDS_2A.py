import pandas as pd
import matplotlib.pyplot as plt

data = {'ROLE': ['DATA SCIENTIST', 'SOFTWARE ENGINEER', 'PRODUCT MANAGER', 'DATA ANALYST', 'UI/UX DESIGNER'],
        'COUNT': [30, 50, 20, 25, 15]}
df = pd.DataFrame(data)

# Pie-chart
plt.figure(figsize=(8, 6))
plt.pie(df['COUNT'], labels=df['ROLE'], autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Job Postings by Role')
plt.axis("equal")
plt.show()
