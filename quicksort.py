numSerie=[[0,26303183],[1,87456123],[2,65897548],[7,36303183]]

def quicksort(numSerie):
    #extraemos pivote
    pivote= numSerie.pop()
    #extraemos serial de pivote
    pivserial= pivote[1]
    #creamos las listas mayor y menor y al comparar 
    ordenada=[[]]
    mayor=[[]]
    menor=[[]]
    final= len(numSerie)
    i=0
    while i <= final:
        comparar=numSerie[i][1]
        if comparar > pivserial:
            mayor.append(numSerie[i])
        else:
            menor.append(numSerie[i])

        i=i-1
        
    ordenada.append(menor)
    ordenada.append(pivote)
    ordenada.append(mayor)
    
    return ordenada 





quicksort(numSerie)
