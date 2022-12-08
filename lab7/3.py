import numpy as np

t1 = np.zeros((3,3))
print(t1)
#t1[1:,:2].fill(1)
#t1[:,2] = 1
#t1[:2,:] = 1
#t1[:2,:1] = 1
t1[:2,[0,2]] = 1

print(t1)