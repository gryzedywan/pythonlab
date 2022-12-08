import numpy as np

def potega(l1,l2):
    if len(l1) != len(l2):
        return []
    l3 = np.array(l1)
    l4 = np.array(l2)
    return (l3 ** l4)

l = [2,2,1,1,2]
ll = [2,2,2,2]

print(potega(l,ll))