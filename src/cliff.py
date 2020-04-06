import numpy as np
import pandas as pd
import string


data = pd.read_csv('./csv/csvData.csv', sep=',', encoding='latin-1')
number = pd.read_csv("./csv/units.csv")

print(data.shape)
print(type(data))
print(number.shape)

#print(data.head)
#print(number.head)

data = data[data['Property Address'].notnull()]

print(data['Property Address'][:2])
print(number['Geocode Address'][:2])

def findUsage(address):
    print(address)

    a_count=number['Geocode Address'].str.contains(address).sum()
    if a_count>0:
        print("True")

    #print(address in number['Geocode Address'])


table = str.maketrans(dict.fromkeys(string.punctuation))  # OR {key: None for key in string.punctuation}

addresses = []
for x in data['Property Address']:
  splitted = x.split()
  address = splitted[0] + ' ' + splitted[1] + ' ' + splitted[2]
  address = address.translate(table) 
  address = address.replace('Street', 'St')
  addresses.append(address)

data['Address'] = addresses

for i in range(data.shape[0]):
  address = val = data['Address'].values[i]
  findUsage(address)