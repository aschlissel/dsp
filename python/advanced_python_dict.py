#read csv using pandas, skip spaces in header
import pandas as pd
csv_pd = pd.read_csv('faculty.csv', skipinitialspace=True)

df = pd.DataFrame(csv_pd)

#Q6

#create a new column for last names
df['last_names'] = [item.split(' ')[-1] for item in df['name']]
last_names = df['last_names']

names = df['name']

#create dictionary
q6_name_dict = {}
for this_name in names:
    x = df[names == this_name]
    for index, row in x.iterrows():
        q6_name_dict.setdefault(row['last_names'], []).append(row[['degree', 'title', 'email']].tolist())

for key in q6_name_dict.keys()[:3]:
    print key, q6_name_dict[key]
    
    
#Q7

q7_dict = {}
for index,row in df.iterrows():
    q7_dict.setdefault((row['name'].split()[0], row['name'].split()[-1]), []).append(row[['degree', 'title', 'email']].tolist())

for key in q7_dict.keys()[:3]:
    print key, q7_dict[key]
