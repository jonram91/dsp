import csv
 
ifile = open('/Users/jonathanjramirez/GitHub/dsp/python/faculty.csv', 'rt')
reader = csv.reader(ifile)

listed = []
for row in reader:
    print(row)
    listed.append(row)
    

not_pandas = {}


header = listed[0]

clear_head = []

for item in header:
    clear_head.append(item.strip())


for col in clear_head:
    not_pandas[col] = []
    
    
data = listed[1:len(listed)]

for row in data:
    
    colnum = 0
    
    for col in clear_head:
        not_pandas[col].append(row[colnum])
        colnum += 1

degree = list((not_pandas['degree']))

degree_clean = []
      
for deg in degree:
    degree_clean.append(deg.replace('.', ''))


degree_clean2 = []

for deg in degree_clean:
    degree_clean2.append(deg.strip())
    
degrees = []    

import re


for deg in degree_clean2:
    degrees += re.findall(r'[A-Z][a-z]*[A-Z]*[a-z]*', deg)

#degrees = list(set(degrees))

degrees

degree_dict = {}

for deg in list(set(degrees)):
    degree_dict[deg] = degrees.count(deg)

titles = list(not_pandas['title'])

titles_clean = []

for i in range(len(titles)):
    if ' is ' not in titles[i]: #One entry is "Assistant Professor 'is' Biostatistics"
        titles_clean.append(titles[i])

titles_dict = {}

for title in titles_clean:
    titles_dict[title] = titles.count(title)

titles_dict['Assistant Professor of Biostatistics'] += 1

titles_clean

titles_dict

emails = not_pandas['email']

emails_data = []

for email in emails:
    emails_data.append([email])



domains = []

for email in emails:
    domains.append(re.sub(r'.*@', '', email))
    
domains = list(set(domains))

dom_data = []

for dom in domains:
    dom_data.append([dom])

import csv
    
with open("emails.csv", "w", newline = '' ) as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerows(emails_data)