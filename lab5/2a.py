sample_dict= {'name':'kelly', 'surname': 'jones', 'age': 25, 'salary': 8000, 'city': 'new york'}
for k in sample_dict.keys():
    print(k, sample_dict[k])
for k, v in sample_dict.items():
    print(f'{k:<8} = {v:>8}')
d2={}
l = ["name", "age", "city",'a']
for k in l:
    if k in sample_dict.keys():
        d2[k]=sample_dict[k]
print(d2)

d3 = sample_dict.copy()

for i in l:
    if i in d3:
        d3.pop(i)

print(d3)

print('Jones' in sample_dict.values())

sample_dict['location'] = sample_dict['city']
del sample_dict['city']
print(sample_dict)