import pandas as pd
import matplotlib.pyplot as plt
data = {'YEAR':list(range(2010,2021)),'JOB POSTING':[150,300,450,600,800,1200,1600,2100,2700,3400,4200]}

df = pd.DataFrame(data)
plt.plot(df['YEAR'],df['JOB POSTING'],marker='o')
plt.title("TREND OF DATA SCIENCE JOB POSTINGS")
plt.xlabel("YEAR")
plt.ylabel("NO. OF JOB POSTINGS")
plt.show()