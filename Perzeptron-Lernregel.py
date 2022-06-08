import matplotlib.pyplot as plt
import numpy as np
import copy



#zwei linear separierbare Mengen
M1 = [[-2.5, 1.2], [-1.5, 2.0], [-0.5, 1.5]]
M2 = [[0.5, 0.3], [1.6, 1.7], [-0.2, 3.1]]

#plotten der beiden Mengen
# plt.scatter(M1, M2)
# plt.title("Perzeptron")
# plt.show()

#Perzeptron Algorythmus 
random_w= np.random.random() #zufällige zahl zwischen [0,1]
w = [0.5,0.5]


a = 0
condition = True

while condition == True:
    p = copy.deepcopy(w)
    
    for x in range(0, len(M1)):
        if (w[0]*M1[x][0] + w[1]*M1[x][1]) <= a:
            w[0] = w[0] + M1[x][0] 
            w[1] = w[1] + M1[x][1]
    for x in range(0, len(M2)):
        if (w[0]*M2[x][0] + w[1]*M2[x][1]) > a:
            w[0] = w[0] - M2[x][0] 
            w[1] = w[1] - M2[x][1]
    if p == w:
        condition = False

print(w[0])
print(w[1])
x = np.linspace(0, 1, 100)
y = w[0]/w[1] * x

plt.plot(x,y,M1,M2)
plt.show()
    
