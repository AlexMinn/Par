print('Escriba el archivo donde esta el fichero')
ruta='C:\\Users\\amima\\Desktop\\Uni\\2º cuatri\\Par\\datos.txt'    
#################QUE SE ELIGA EL NOMBRE DEL FICHERO, SISTEMA DE PUNTUACION
fallo=False                                                         #variable calcula cuando has perdido   
f = open (ruta,'r') 
nuevalinea=[]
bloques=[]
for x in range(0,12):                                                #definimos la matriz 
    lista=[]
    for y in range(10):
        lista.append(' ')
    lista.append('x')
    bloques.append(lista)
simbol={'A':'#','a':'#','B':'$','b':'$',' ':' ','<':-1,'>':1}
change={'A':'a','a':'A','B':'b','b':'B',' ':' ','x':'x'}
elichange={'A':'A','a':'A','B':'B','b':'B'}
elimi=True
puntuacion=0

def imprimir (bloq):                                            #imprime lo que tenga la matriz
    margen=' +---+---+---+---+---+---+---+---+---+---+' 
    x=0
    for num in range(0,25):
        if num%2==0:                                                    #si es par escribe el margen
            print("")
            print(margen)
        else:                                                           #si es impar hace lo siguiente
            print(chr(x+65),end="")                                         #escribe la letra
            print('|',end="")                                               
            for i in range(10):                                             #recorre la matriz analizando cada fila                      #si es A o a 
                print(simbol[bloq[x][i]]*3,end="")
                if (i<=8 and simbol[bloq[x][i]]!=' '):                                                      #las primeras 9 posiciones 
                    if (bloq[x][i]==bloq[x][i+1]):                                  #si es igual que la siguiente
                        print(simbol[bloq[x][i]],end="")
                    else:                                                           #sino es igual
                        print('|',end="")
                else:                                                           #la ultima posicion
                    print('|',end="")
            x=x+1
    print('   0   1   2   3   4   5   6   7   8   9')
    return None

def qinstru (ins,repit):
    repit=False
    coords=[-1,-1,-1]
    try:
        coords[2]=ins[2]
        coords[0]=ord(ins[0])-65
        coords[1]=ord(ins[1])-48
    except Exception :
        print('Faltan instrucciones')
        repit=True
    if (coords[0]<0 or coords[0]>11) and repit==False:
        print('Error de sintaxis en jugada')
        repit=True
    elif (coords[1]<0 or coords[1]>9):
        print('Error de sintaxis en jugada')
        repit=True
    elif (coords[2]=='<' or coords[2]=='>' ):
        if (bloques[coords[0]][coords[1]]==' '):
            print('No hay ningún bloque en esa celda')
            repit=True
        else:
            a=simbol[coords[2]]
            if bloques[coords[0]][coords[1]+a]==' ':            #bloque de 1
                movimiento(bloques,coords)
            elif bloques[coords[0]][coords[1]+a]==bloques[coords[0]][coords[1]]:
                if bloques[coords[0]][coords[1]+a*2]==' ':      #bloque de 2
                    coords[1]=coords[1]+a 
                    movimiento(bloques,coords)
                elif bloques[coords[0]][coords[1]+a*2]==bloques[coords[0]][coords[1]]:
                    if bloques[coords[0]][coords[1]+a*3]==' ':              #bloque de 3
                        coords[1]=coords[1]+a*2
                        movimiento(bloques,coords)
                    elif bloques[coords[0]][coords[1]+a*3]==bloques[coords[0]][coords[1]]:
                        if bloques[coords[0]][coords[1]+a*4]==' ':              #bloque de 4
                            coords[1]=coords[1]+a*3
                            movimiento(bloques,coords)
                        else:
                            print('El bloque no puede moverse en esa dirección')
                            repit=True 
                    else:
                        print('El bloque no puede moverse en esa dirección')
                        repit=True 
                else:
                    print('El bloque no puede moverse en esa dirección')
                    repit=True   
            else:      
                print('El bloque no puede moverse en esa dirección')
                repit=True
    else:
        print('Error de sintaxis en jugada')
        repit=True
    return coords,repit

def movimiento(bloques,coords):        
    nomasb=False
    a=simbol[coords[2]]
    i=2*a
    while nomasb==False:
        if bloques[coords[0]][coords[1]+i]!=' ':
            i=i-(1*a)
            nomasb=True
            bloques[coords[0]][coords[1]+i]=bloques[coords[0]][coords[1]]
            bloques[coords[0]][coords[1]]=' '
            if bloques[coords[0]][coords[1]-(1*a)]==bloques[coords[0]][coords[1]+i]:
                bloques[coords[0]][coords[1]+i-(1*a)]=bloques[coords[0]][coords[1]+i]
                bloques[coords[0]][coords[1]-1*a]=' '
                if bloques[coords[0]][coords[1]-2*a]==bloques[coords[0]][coords[1]+i]:
                    bloques[coords[0]][coords[1]+i-(2*a)]=bloques[coords[0]][coords[1]+i]
                    bloques[coords[0]][coords[1]-2*a]=' '
                    if bloques[coords[0]][coords[1]-3*a]==bloques[coords[0]][coords[1]+i]:
                        bloques[coords[0]][coords[1]+i-(3*a)]=bloques[coords[0]][coords[1]+i]
                        bloques[coords[0]][coords[1]-3*a]=' '
            if(a==1):
                fusion(100,coords[1]+i,coords[0],bloques)
            elif(a==-1):
                fusion(coords[1]+i,100,coords[0],bloques)
        i=i+(1*a)
    print('MOVIMIENTO')
    imprimir(bloques)
    return None

def bajada(bloques):
    lis1=[10,9,8,7,6,5,4,3,2,1,0]
    lis2=[0,1,2,3,4,5,6,7,8,9]
    for y in lis1:                                                            #recorre la matriz de abajo a arriba
        j=y
        pabajo=True
        while pabajo==True:                                                     #recorre la matriz desde arriba a abajo para llevar lomas bajo posible     
            conti=True
            x=0
            while conti==True:
                if bloques[j][x]!=bloques[j][x+1]:            #bloque de 1
                    if bloques[j+1][x]==' ':
                        bloques[j+1][x]=bloques[j][x]
                        bloques[j][x]=' '
                        fusion(x,x,j+1,bloques)
                    x=x+1
                elif bloques[j][x+1]!=bloques[j][x+2]:        #bloque de 2
                    if bloques[j+1][x]==' ' and bloques[j+1][x+1]==' ':
                        bloques[j+1][x]=bloques[j][x]
                        bloques[j+1][x+1]=bloques[j][x+1]
                        bloques[j][x]=' '
                        bloques[j][x+1]=' '
                        fusion(x,x+1,j+1,bloques)
                    x=x+2
                elif bloques[j][x+2]!=bloques[j][x+3]:              #bloque de 3
                    if bloques[j+1][x]==' ' and bloques[j+1][x+1]==' ' and bloques[j+1][x+2]==' ':
                        bloques[j+1][x]=bloques[j][x]
                        bloques[j+1][x+1]=bloques[j][x+1]
                        bloques[j+1][x+2]=bloques[j][x+2]
                        bloques[j][x]=' '
                        bloques[j][x+1]=' '
                        bloques[j][x+2]=' '
                        fusion(x,x+2,j+1,bloques)
                    x=x+3
                elif bloques[j][x+3]!=bloques[j][x+4]:                  #bloque de 4
                    if bloques[j+1][x]==' ' and bloques[j+1][x+1]==' ' and bloques[j+1][x+2]==' ' and bloques[j+1][x+3]==' ':
                        bloques[j+1][x]=bloques[j][x]
                        bloques[j+1][x+1]=bloques[j][x+1]
                        bloques[j+1][x+2]=bloques[j][x+2]
                        bloques[j+1][x+3]=bloques[j][x+3]
                        bloques[j][x]=' '
                        bloques[j][x+1]=' '
                        bloques[j][x+2]=' '
                        bloques[j][x+3]=' '
                        fusion(x,x+3,j+1,bloques)
                    x=x+4
                else:
                    x=x+1
                if x==10:
                    conti=False
            j=j+1
            if j==11:
                pabajo=False
    print('CAIDA')
    imprimir(bloques)
    return bloques

def eliminacion(bloques,puntuacion):
    complete=True
    lis=[11,10,9,8,7,6,5,4,3,2,1,0]
    col=11
    puntu=0
    while col>-1:
        fil=0
        elimi=True
        while fil<10:                                           #SI UNA LINEA TIENE ' ' NO LA ELIMINA
            if(bloques[col][fil]==' '):
                elimi=False
            fil=fil+1
        if(elimi==True):
            for v in range(9):                                  #SI CADA PARAMETRO DE UNA LINEA ES IGUAL 
                if(elichange[bloques[col][v]]!=elichange[bloques[col][v+1]]):
                    complete=False
            if complete==True:                                  #SI CUMPLE ANTERIOR, ELIMINACION COMPLETA
                for x in range(12):
                    for y in range(10):
                        if bloques[x][y]!=' ':
                            bloques[x][y]=' '
                            puntu=puntu+1
            else:                                               #SI NO CUMPLE SOLO ELIMINA UNA LINEA
                for x in range(10):
                    bloques[col][x]=' '
                    puntu=puntu+1
            print('ELIMINACION')
            imprimir(bloques)
            bajada(bloques)
            col=12
        col=col-1
    return elimi,puntu

def fusion(izq,der,col,bloques):
    if (izq!=100):
        if bloques[col][izq]==' ':
            return None
        if(bloques[col][izq]==bloques[col][izq-1]):
            acabo=False
            p=izq-1
            while acabo==False:
                bloques[col][p]=change[bloques[col][p]]
                p=p-1
                if p<0:
                    acabo=True
    if (der!=100):
        if (bloques[col][der]==bloques[col][der+1]):
            acabo=False
            p=der+1
            while acabo==False:
                bloques[col][p]=change[bloques[col][p]]
                p=p+1
                if p>10:
                    acabo=True      
    return bloques

while fallo==False:
    nuevalinea=f.readline()
    if nuevalinea=='':                                               # este bucle consigue que el texto se lea infinitas veces
        f.close()
        f = open (ruta,'r')
        nuevalinea=f.readline()

    for x in range(0,10):                                              #este bucle separa la frase para nuestra matriz
        bloques[0][x]=nuevalinea[x]

    print('INSERCIÓN FILA')    
    imprimir(bloques)
    print ('PUNTUACIÓN: ',end='')
    print (puntuacion)
    repit=True
    while repit==True:
        print('Introduzca jugada o ‐‐‐ o FIN:')
        instruccion=input()
        if instruccion=='FIN':
            fallo=True
            repit=False
        elif instruccion=='---':
            repit=False
        else:
            instruccion=qinstru(instruccion,repit)
        repit=instruccion[1]

    bajada(bloques)

    elimina=True
    while elimina==True:
        elimi=eliminacion(bloques,puntuacion)
        elimina=elimi[0]
        puntuacion=puntuacion+elimi[1]

    for n in range(10):                                                 #SI SE RELLENA LA PRIMERA FILA PIERDES
        if bloques[0][n]!=' ':
            fallo=True

print('HAS PERDIDO')
f.close()