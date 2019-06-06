import pyautogui
import time
import cv2
import numpy as np
from matplotlib import pyplot as plt
import pickle

def coordinates_dictionary_maker():
    for i in range(0, 256):
        r = round(x1, -1)
        p = round(y1, -1)
        lista.append(r)
        lista.append(p)
        x1 += x
        if i == b:
            b = i
            y1 += y
            b += 16
            x1 = x1 - 16 * x
    recnik_koordinata = {}
    m = 0
    n = 1
    for i in range(0, 256):
        recnik_koordinata[i] = [lista[m], lista[n]]
        m += 2
        n += 2
    file = open('koordinate.dat', 'wb+')
    pickle.dump(recnik_koordinata, file)
    file.close()
    return recnik_koordinata

def matrix_maker_1():
    # PRAVI INICIJALAN MATRIKS KOJI CE BITI BROJAC SVIH POLJA

    for i in range(0, 6):
        matriks = np.zeros((16, 16))
    p = 0
    r = 0
    q = 0
    for j in range(0, 16):
        for i in range(0, 16):
            matriks[p][r] = q
            q += 1
            r += 1
        p += 1
        r = 0

    file = open('matrica_polja.dat', 'wb')
    pickle.dump(matriks, file)
    file.close()
    return matriks

def minesweeper_finder():
    lista = []
    pyautogui.screenshot('screen.png')
    img_rgb = cv2.imread('screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    for i in range(1,5):
        template = cv2.imread('full_minesweeper%s.png' %i, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.92
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            x,y = pt
            x+=15
            y+=15
            lista.append([x,y])
            pyautogui.moveTo(x,y,0.5)
            print(lista)
    return lista

def screenshot(lista): #slika ekran
    x,y = lista[0]
    x2,y2 = lista[3]
    x2 = x2 - x
    y2 = y2 - y
    pyautogui.screenshot('screenpart.png',region=(x,y,x2,y2))

def clicker(lista):
    for i in range (0,4):
        x,y = lista[i]
        if i == 0:
            x+=10
            y+=10
        elif i == 1:
            x -= 10
            y += 10
        elif i == 2:
            x += 10
            y -= 10
        elif i == 3:
            x -= 10
            y -= 10
        pyautogui.click(x,y,duration=0.3)

def number_finder(x,lista_uglova): #pronalazi gde se nalaze razlicita polja
    lista = []
    brojac = 0
    p,r = lista_uglova[0]  #uzima gornje leve koordinate najnovije slike samo polja
    file = open('lista%s.txt' % x,'w+')
    img_rgb = cv2.imread('screenpart.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('number%s.png'% x ,0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        m,n = pt
        if x == 12:
            m = m + 5 + p
            n = n + 5 + r
        else:
            m = m + 5 + p
            n = n + 5 + r
        #m = round(m,-1)
        #n = round(n,-1)
        lista.append(m)
        lista.append(n)
        pyautogui.moveTo(m,n,duration=0.2)
        brojac+=1
        mm = str(m)
        nn = str(n)
        file.write(mm + " ")
        file.write(nn + " ")
    file.close()
    print(brojac)
    return lista

def loop_generator(lista_uglova): #prolazi kroz brojeve i pokrece funkciju koja ih nalazi na slici koju je obezbedio screenshot
    main_lista = []
    empties_lista = []
    #lista = number_finder(10,lista_uglova)
    #empties_lista.append(lista)
    for i in range(0,5):
        lista = number_finder(i,lista_uglova)
        main_lista.append(lista)
    for i in range(12,13): #nalazi zastavice
        lista = number_finder(i,lista_uglova)
        main_lista.append(lista)
    return main_lista

def main():
    lista_uglova = minesweeper_finder()
    clicker(lista_uglova)
    screenshot(lista_uglova)
    list_of_fields = loop_generator(lista_uglova)
    #coordinates_dictionary = coordinates_dictionary_maker()
    #matrix_1 = matrix_maker_1()
    #print(list_of_fields)
    #print(coordinates_dictionary)
    #print(matrix_1)

main()
