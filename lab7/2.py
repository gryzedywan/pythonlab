import numpy as np

tab1 = np.random.randint(5, size=(5,5))

print(tab1)
mini = np.min(tab1)
maxi = np.max(tab1)
print(np.max(tab1 ,axis= 0))
print(np.max(tab1 ,axis= 1))
print(maxi)
print(mini)
print(np.sum(tab1, axis=1))