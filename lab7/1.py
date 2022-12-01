import numpy as np
import random as r

l1 = [2 ** i for i in range(7,-1,-1)]
print(l1)

wagi = np.array(l1)
print(wagi)

liczba_bin = np.random.randint(2, size=8)
print(liczba_bin)

print(f'{liczba_bin} binarne to {sum(wagi * liczba_bin)} dziesietne')