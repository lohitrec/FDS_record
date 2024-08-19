import pandas as pd
import matplotlib.pyplot as plt

data = {'ROLE': ['DATA SCIENTIST', 'SOFTWARE ENGINEER', 'PRODUCT MANAGER', 'DATA ANALYST', 'UI/UX DESIGNER'],
        'COUNT': [30, 50, 20, 25, 15]}

df = pd.DataFrame(data)
plt.figure(figsize=(10,6))
plt.bar(df['ROLE'] , df['COUNT'] , color = 'orange')
plt.title('DISTRIBUTION OF JOB POSTINGS BY ROLE')
plt.xlabel('ROLES')
plt.ylabel('NO. OF JOB POSTINGS')
plt.xticks(rotation = 40)
plt.tight_layout()
plt.show()
