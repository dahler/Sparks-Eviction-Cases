import numpy as np
import csv
import pandas as pd

court = list(csv.reader(open("./csv/data_with_median_income.csv",'r')))

#court = np.array(court)
#print(court)

df = pd.DataFrame(court)
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header
#print(df)

total = np.array(df)

median_income = np.array(df['median_income'])
u_median_income, i_median_income, count_median_income = np.unique(median_income,return_inverse=True,return_counts=True)
print(np.sort(count_median_income))
district = np.array(df['DISTRICT'])
u_district, i_district, count_district = np.unique(district,return_inverse=True,return_counts=True)
print(np.sort(count_district))
#print(district)
#print(i_district)
#print(u_district)

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

s = set(stopwords.words('english'))


plaintiff = np.array(df['Plaintiff'])
plaintiff_short = []
for i in range(len(plaintiff)):
    filter(lambda w: not w in s,plaintiff[i].split())
    plaintiff_short.append(plaintiff[i].split(' ')[:1])
plaintiff_short = np.array([plaintiff_short])
#plaintiff_short = np.char.lower(plaintiff_short)
u_plaintiff, i_plaintiff, count_plaintiff = np.unique(plaintiff_short,return_inverse=True, return_counts=True)
u_plaintiff = np.array(u_plaintiff)
i_plaintiff = np.array(i_plaintiff)

print(plaintiff)
print(i_plaintiff)
print(u_plaintiff)
print(len(u_plaintiff))
print(count_plaintiff)

p_attorney = np.array(df['P-Attorney'])
u_p_attorney, i_p_attorney, count_p_attorney = np.unique(p_attorney,return_inverse=True,return_counts=True)
print(i_p_attorney)
print(count_p_attorney)

judgment_type = np.array(df['Judgement Type'])
u_judgment_type, i_judgment_type, count_judgment_type = np.unique(judgment_type, return_inverse=True, return_counts=True)
print(i_judgment_type)
print(count_judgment_type)

judgment_method = np.array(df['JudgeMent Method'])
u_judgment_method, i_judgment_method, count_judgment_method = np.unique(judgment_method, return_inverse=True,return_counts = True)
print(i_judgment_method)
print(count_judgment_method)

d_attorney = np.array(df['D-Attorney'])
u_d_attorney, i_d_attorney, count_d_attorney = np.unique(d_attorney, return_inverse=True,return_counts=True)
print(i_d_attorney)
print(count_d_attorney)

d_a = []
for j in range(len(d_attorney)):
    if d_attorney[j] == '':
        d_a.append(0)
    else:
        d_a.append(1)

u_d_a, i_d_a, count_d_a = np.unique(d_a,return_inverse=True, return_counts = True)
print(d_a)
print(i_d_a)
print(count_d_a)


import math as m

j_total = np.array(df['Judgement Total'])
j_total_hist = []
for k in range(len(j_total)):
    try:
        j_total[k] = float(j_total[k])
        j_total_hist.append(float(j_total[k]))
    except ValueError:
        j_total[k] = 0
#j_total.astype(float)
j_total_hist = np.array(j_total_hist)
print(j_total)
print(max(j_total))
print(min(j_total))
print(np.mean(j_total))

#j_total_final = np.delete(j_total_hist, j_total_hist.argmin())
j_total_final = np.delete(j_total_hist, j_total_hist.argmax())
#j_total_final = np.delete(j_total_final, j_total_final.argmax())

import matplotlib.pyplot as plt

plt.hist(j_total_final, bins=100)
plt.show()

e_total = np.array(df['Execution Total'])
e_total_hist = []
for l in range(len(e_total)):
    try:
        e_total[l] = float(e_total[l])
        e_total_hist.append(float(e_total[l]))
    except ValueError:
        e_total[l] = 0
e_total_hist = np.array(e_total_hist)
print(e_total)

plt.hist(e_total_hist, bins=100)
plt.show()

bins = np.array([0, 5000, 10000, 15000, 20000, 25000, 30000, 35000])
e_bins = np.digitize(e_total_hist,bins,right=False)
print(e_bins)
j_bins = np.digitize(j_total_hist,bins,right=False)
print(j_bins)


