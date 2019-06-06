matrica = [[20,20,20,20,20,20,20,20,20],
           [20,20,20,20,20,20,20,20,20],
           [20,20,20, 3, 2, 2, 2,10,20],
           [20,20,20, 2, 0, 0, 1, 1,20],
           [20,20,20, 1, 0, 0, 0, 1,20],
           [20,20,20, 1, 0, 1, 1, 2,10],
           [20,20,20, 1, 0, 1,10, 2, 1],
           [20,20,20, 1, 0, 1, 1, 1, 0],
           [20,20,20, 1, 0, 0, 0, 0, 0]]
lista_keceva = []
for i in range(0,8):
    for j in range(0,8):
        if matrica[i][j] == 1:
            lista_keceva.append([i,j])
#print(lista_keceva)
#print(matrica[7][7])
for x in lista_keceva:
    m = x[0]
    n = x[1]
    print(m,n)
    if matrica[m-1][n-1] == 20 or matrica[m-1][n+1] == 20 or matrica[m+1][n-1] == 20 or matrica[m+1][n+1] == 20:
        print('jeste 20\n')
    elif matrica[m-1][n-1] == 10 or matrica[m-1][n+1] == 10 or matrica[m+1][n-1] == 10 or matrica[m+1][n+1] == 10:
        print('jeste 10\n')
    else:
        print('nije\n')