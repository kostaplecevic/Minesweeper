import pyautogui
import time
import numpy as np
import pickle

#PRAVI INICIJALAN MATRIKS KOJI CE BITI BROJAC SVIH POLJA

for i in range(0,6):
    matriks = np.zeros((16, 16))
p = 0
r = 0
q = 1
for j in range(0,16):
    for i in range(0,16):
        matriks[p][r] = q
        q+=1
        r+=1
    p+=1
    r = 0

file = open('matrica_polja.dat','wb')
pickle.dump(matriks,file)
file.close()

print(matriks)