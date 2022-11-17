dict1 = {1:2,2:3,6:4}
dict2 = {1:4,2:17,6:10,4:10}
dict3 = {}

for i in dict1:
    for j in dict2:
        if j == i:
            m = dict1[i] + dict2[j]
            n = {i : m}
            dict3.update(n)
print(dict3)
dict1.update(dict2)
dict1.update(dict3)
print(dict1)