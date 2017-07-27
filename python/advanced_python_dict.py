import advanced_python_regex as apyrex
import re

names = apyrex.not_pandas['name']

names_sep = []

firsts = []

mid = []

lasts = []

for name in names:
    names_sep.append(re.findall(r'[A-Z][a-z]*\.?', name))

for name in names_sep:
    if len(name) > 2:
        firsts.append(name[0])
        mid.append(name[1])
        lasts.append(name[2])
    else:
        firsts.append(name[0])
        lasts.append(name[1])

prof_tups = []

for i in range(len(firsts)):
    prof_tups.append((firsts[i], lasts[i]))


lasts_dict = {}

for name in lasts:
    lasts_dict[name] = lasts.count(name)

faculty_dict = {}

counter = 0

for name in lasts:
    if name in faculty_dict.keys():
        faculty_dict[name].append(apyrex.data[counter][1:])
        counter += 1
    else:
        faculty_dict[name] = [apyrex.data[counter][1:]]
        counter += 1

#First 3 entries in faculty_dict

for prof in list(faculty_dict.items())[0:3]:
    print(prof)



professor_dict = {}

counter = 0

for prof in prof_tups:
    professor_dict[prof] = apyrex.data[counter][1:]
    counter += 1
    
professor_dict

prof_dict_list = list(professor_dict.items())

#Print off the first 3 entries in the dictionary

for prof in prof_dict_list[0:3]:
    print(prof)

#Sort the dictionary by Prof last name

print(sorted(prof_dict_list, key = lambda x: x[0][1])[0:3])



