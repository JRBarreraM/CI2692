from random import randint

# Movimientos
vert = [-1,-2,-2,-1,1,2,2,1];
horiz = [2,1,-1,-2,-2,-1,1,2];

# Movimiento valido
def valid(m,n,x,y):
    return 0<=x<m and 0<=y<n;

def dibujarTab(n,Kx,Ky,V):
    for i in range(n):
        for j in range(n):
            if i==Kx and j==Ky:
                print 'K',;
            elif V[i][j]:
                print 'x',;
            else:
                if i==Kx-1 and j==Ky+2:
                    print '0',;
                elif i==Kx-1 and j==Ky-2:
                    print '3',;
                elif i==Kx-2 and j==Ky+1:
                    print '1',;
                elif i==Kx-2 and j==Ky-1:
                    print '2',;             
                elif i==Kx+1 and j==Ky+2:
                    print '7',;
                elif i==Kx+1 and j==Ky-2:
                    print '4',;
                elif i==Kx+2 and j==Ky+1:
                    print '6',;
                elif i==Kx+2 and j==Ky-1:
                    print '5',;
                else:
                    print 'o',;
            print '|',;
        print '\n';

def over(n,Kx,Ky,V):
    p=False;
    for i in range(8):
        x=Kx+vert[i];
        y=Ky+horiz[i];
        if valid(n,n,x,y):
            p=p or V[x][y]==0;
    return not p

def manual(n,Kx,Ky,V,ct,Hx,Hy):
    # n: Tamano del tablero
    # Kx,Ky: Coordenadas del caballo
    # V: Tablero (1 si ya se visito, 0 sino)
    # ct: Contador de casillas visitadas
    # Hx,Hy: Historial del posiciones

    dibujarTab(n,Kx,Ky,V);

    # Ver si quedan movimientos validos
    if ct==n*n:
        return 1
    elif over(n,Kx,Ky,V):
        return 0
    

    # Pedir movimiento
    move=int(input("Movimiento (-1 == Undo): "));

    # Undo
    if move==-1:
        if len(Hx)==1:
            print "No se ha hecho ningun movimiento.";
            return manual(n,Kx,Ky,V,ct,Hx,Hy);
        else:
            Hx.pop();
            Hy.pop();
            V[Kx][Ky]=0;
            return manual(n,Hx[len(Hx)-1],Hy[len(Hy)-1],V,ct-1,Hx,Hy);

    x=Kx+vert[move];
    y=Ky+horiz[move];
    
    # Mover
    if valid(n,n,x,y):
        if V[x][y]:
            print "Ya visitado.";
            return manual(n,Kx,Ky,V,ct,Hx,Hy);
        else:
            V[x][y]=1;
            Hx.append(x);
            Hy.append(y);
            return manual(n,x,y,V,ct+1,Hx,Hy);
    else:
        print "Movimiento invalido.";
        return manual(n,Kx,Ky,V,ct,Hx,Hy);

def brute(n,Kx,Ky,V,ct,Hx,Hy,Hm):
    # n: Tamano del tablero
    # Kx,Ky: Coordenadas del caballo
    # V: Tablero (1 si ya se visito, 0 sino)
    # ct: Contador de casillas visitadas
    # Hx,Hy: Historial del posiciones
    
    #dibujarTab(n,Kx,Ky,V)
    #print "------------------"

    if ct==n*n:
        for i in range(len(Hx)):
            V[Hx[i]][Hy[i]]=i
        for i in range(n):
            for j in range(n):
                print V[i][j],
                print '|',
            print '\n'

        return 1
    elif over(n,Kx,Ky,V):
        Hx.pop()
        Hy.pop()
        Hm.pop()
        V[Kx][Ky]=0
        return 0

    for i in range(8):
            x=Kx+vert[i]
            y=Ky+horiz[i]
            if valid(n,n,x,y):
                if V[x][y]==0:
                    Hx.append(x)
                    Hy.append(y)
                    Hm.append(i)
                    V[x][y]=1
                    ret = brute(n,x,y,V,ct+1,Hx,Hy,Hm)
                    if ret:
                        return 1

    Hx.pop()
    Hy.pop()
    Hm.pop()
    V[Kx][Ky]=0
    return 0



m=int(input("Introduzca 1 para utilizar el modo 'manual', 2 para el modo 'fuerza bruta' o 3 para el modo 'divide and conquer': "));
while m>3 or m<1:
    print 'Debe introducir un numero entre 1 y 3';
    m=int(input("Introduzca 1 para utilizar el modo 'manual', 2 para el modo 'fuerza bruta' o 3 para el modo 'divide and conquer': "))
n=int(input("Introduzca la cantidad de casillas por fila o columna del tablero:"));
while n<3:
    print 'El largo debe ser mayor o igual a 3';
    n=int(input("Introduzca la cantidad de casillas por fila o columna del tablero: "));
V=[n*[0] for i in range(n)];
if m==1:
    x=int(input("Introduzca en que columna comenzar, contando desde 0: "));
    y=int(input("Introduzca en que fila comenzar, contando desde 0: "));
    V[y][x]=1;
    ret = manual(n,y,x,V,1,[y],[x]);
elif m==2:
    x=0;
    y=0;
    V[x][y]=1;
    ret=brute(n,x,y,V,1,[x],[y],[-1]);
    print ret