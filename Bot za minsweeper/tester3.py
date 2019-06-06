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