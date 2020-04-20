import numpy as np
import csv
import pandas as pd

court = list(csv.reader(open("./csv/cleanData.csv",'r')))

#court = np.array(court)
#print(court)

df = pd.DataFrame(court)
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header
#print(df)

total = np.array(df)

"""
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
"""
#********************************************************************************

"""
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
"""


"""
#********************************************************
import matplotlib.pyplot as plt

units = np.array(df['units'])
print(len(units))
units_hist = []
for m in range(len(units)):
    try: 
        units[m] = float(units[m])
        units_hist.append(units[m])
    except ValueError:
        units[m] = 0
units_hist = np.array(units_hist)
plt.hist(units_hist)
plt.show()
print(len(units_hist))
#********************************************************
"""

public_housing = ['Port Landing', 'Harwell', 'Harwell Homes', 'Cambridge Housing Authority',
        'Cambridge Affordable Housing', 'Cambridge Affordable Housing Corporation',
        'Rindge', 'Rindge Apartments', 'Cast II', 'Cast II Apartments', 
        'Fresh Pond Apartments', 'Fresh Pond', 'Magazine House', 'Magazine', 
        'Walden Square', 'Walden Square Apartments', 'Portland Marcella', 
        'Memorial Drive 808', '808 Memorial', 'Inman', 'Inman Square Apartments', 
        'Close Building', 'Close', 'Briston Arms', 'Roosevelt Towers', 
        'Putnam School', 'Franklin St', 'Harvard Place', 'Brookline Pl', '131 Harvard',
        '243 Broadway', 'Cambridge Housing Authority', '241 Garden', '273 Harvard', 
        '49 Columbia', '675 Massachusetts', '411 Franklin', '77 Magazine', 
        '8 Marcella', '21 Walden', '14 Roosevelt', '86 Otis', '402 Rindge', 
        '8 Museum', '1221 Cambridge', '1 Citizen', '364 Rindge']
affordable_housing = ['Port Landing', 'Harwell', 'Harwell Homes', 'Cambridge Housing Authority',
        'Cambridge Affordable Housing', 'Cambridge Affordable Housing Corporation',
        'Rindge', 'Rindge Apartments', 'Cast II', 'Cast II Apartments', 
        'Fresh Pond Apartments', 'Fresh Pond', 'Magazine House', 'Magazine', 
        'Walden Square', 'Walden Square Apartments', 'Portland Marcella', 
        'Memorial Drive 808', '808 Memorial', 'Inman', 'Inman Square Apartments', 
        'Close Building', 'Close', 'Briston Arms', 'Roosevelt Towers', 
        'Putnam School', 'Franklin St', 'Harvard Place', 'Brookline Pl', '131 Harvard',
        '243 Broadway', 'Cambridge Housing Authority', '241 Garden', '273 Harvard', 
        '49 Columbia', '675 Massachusetts', '411 Franklin', '77 Magazine', 
        '8 Marcella', '21 Walden', '14 Roosevelt', '86 Otis', '402 Rindge', 
        '8 Museum', '1221 Cambridge', '1 Citizen', '364 Rindge', 
        '50 Churchill', '150 Erie', 'Auburn Court', '240 Green', '810 Memorial', 
        '265 Harvard', '411 Franklin', '157 6', '402 Rindge', '15 Lambert', '64 Magee', 
        '1 Jackson', '259 Harvard', '129 Franklin', '14 Roosevelt', '11 Corcoran', 
        '131 Washington', '1 Lincoln', '273 Harvard', '4 University', '1066 Cambridge', 
        '625 Putnam', '2505 Massachusetts', '1165 Cambridge', '21 Walden', '140 Franklin',
        '100 Harvard', '650 Concord', '17 Boardman', 'Squirrel', '55 Columbia', 
        '8 Lancaster', '55 Essex', 'Swartz', '2401 Massachusetts', 'Scouting Way', 
        '10 Magazine', '20 Chestnut', '2535 Massachusetts', '9 Woodrow', '26 York', 
        '820 Massachusetts', '210 Otis', '260 Putnam', '19 Market', '80 Auburn', 
        '51 Norfolk']
housing = []
meme = df['Plaintiff'] + ' ' + df['Property Address'] + ' ' + df['Address']
meme = np.array(meme)
for r in range(len(meme)):
    meme[r] = str(np.char.lower(meme[r])) 
#for s in range(len(public_housing)):
#    public_housing[s] = str(np.char.lower(public_housing[s]))
for s in range(len(affordable_housing)):
    affordable_housing[s] = str(np.char.lower(affordable_housing[s]))
######print(meme)
######print(meme.dtype)
#meme = np.char.lower(meme)
#public_housing = np.char.lower(public_housing)
"""
for n in range(len(meme)):
    for q in range(len(public_housing)):
        if public_housing[q] in meme[n]:
            housing.append(public_housing[q])
"""
for n in range(len(meme)):
    for q in range(len(affordable_housing)):
        if affordable_housing[q] in meme[n]:
            housing.append(affordable_housing[q])
print(housing)
print(len(housing))
print(len(meme))

# GENDER ***************************************************************

import gender_guesser.detector as gender

d = gender.Detector(case_sensitive=False)

p = r'\,'
x = df['Deffendant'].str.split(r'[,\s]\s*',expand=True)
print(x)
x.columns = ['Last','First','nan1','nan2','nan3','nan4','nan5','nan6','nan7','nan8','nan9']
print(x)
print(x.iloc[8])
#print(x.iloc[8])
first = np.array(x['First'])
last = np.array(x['Last'])
print(first)
print(last)

genders = []
for i in range(len(first)):
    if first[i] is None:
        first[i] = ''
    genders.append(d.get_gender(first[i]))

g_num = []
g_male = []
g_female = []
g_unknown = []
for j in range(len(genders)):
    if genders[j] == 'male' or genders[j] == 'mostly_male':
        g_num.append(1)
        g_male.append(first[j])
    elif genders[j] == 'female' or genders[j] == 'mostly_female':
        g_num.append(0)
        g_female.append(first[j])
    else:
        g_num.append(2)
        g_unknown.append(first[j])

print(genders)
print(g_num)
print(len(g_num))
print(g_num.count(2)/len(g_num))
print(g_num.count(0))
print(g_num.count(1))
print(g_num.count(0)+g_num.count(1)+g_num.count(2))
print(g_male)
print(g_female)
print(g_unknown)

# RACE *****************************************************************








