import pyautogui
import time
import pickle

time.sleep(5)
x1,y1 = (pyautogui.position())
print('sledeci')
time.sleep(5)
x2,y2 = (pyautogui.position())
print('sledeci')
time.sleep(5)
x3,y3 = (pyautogui.position())

x = (x2 - x1)/15
y = (y3 - y1)/15
print(x)
print(y)
b = 15
lista = []
for i in range(0,256):
    r = str(round(x1,-1))
    p = str(round(y1,-1))
    lista.append(r)
    lista.append(p)
    x1+= x
    if i == b:
        b = i
        y1 += y
        b+=16
        x1 = x1 - 16*x
recnik_koordinata = {}
m = 0
n = 1
for i in range(0,256):
    recnik_koordinata[i] = [lista[m],lista[n]]
    m+=2
    n+=2
print(recnik_koordinata)
file = open('koordinate.dat','wb+')
pickle.dump(recnik_koordinata,file)
file.close()