sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

for k, v in sample_dict.items():
    print(f'{k:<8} = {v:>8}')

lista = ['name', 'surname']
new_dict = {}
for i in lista:
    if i in sample_dict.keys():
       m = {i : sample_dict[i]}
       new_dict.update(m)

print(new_dict)

for i in lista:
    if i in sample_dict.keys():

       sample_dict.pop(i)

print(sample_dict)

print('Jones' in sample_dict)
sample_dict['city'] =