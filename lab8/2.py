dict1 = {'data1':10, 'data2':-4, 'data3':2}

def sum_of_values(dic):
    suma = 0
    for key in dic:
        suma = suma + dic[key]
    return suma

print(sum_of_values(dict1))