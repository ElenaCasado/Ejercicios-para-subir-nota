def suma_pares(n1):
    resto=0
    total=0
    restopar=0
    while(n1>0):
        resto=n1%10
        restopar=resto%2
        if (restopar==0):
            total=total+resto
        n1=n1/10
    return total

def suma_impares(n1):
    resto=0
    total=0
    restopar=0
    while(n1>0):
        resto=n1%10
        restopar=resto%2
        if (restopar==1):
            total=total+resto
        n1=n1/10
    return total

def mayor_cifras(n1):
    resto=0
    total=0
    while(n1>0):
        resto=n1%10
        if (total<resto):
            total=resto
        n1=n1/10
    return total
    
def menormayor_cifras(n1):
    L=[]
    resto=0
    while n1>0:
        resto=n1%10
        L.append(resto)
        n1=n1/10        
    L.sort()
    return L 


def menu_operaciones(): 
    respuesta= 1
    n1=input("Dime un n�mero; ")
    while (respuesta<>0):
        print "Que deseas hacer con el n�mero?; "
        print "1.Devuelve la suma de sus cifras pares"
        print "2.Devuelve la suma de sus cifras impares"
        print "3.Devuelve la mayor de sus cifras"
        print "4.Devuelve un n�mero con las mismas cifras ordenadas de menor a mayor"
        print "0.Salir"
        respuesta=input()
        if(respuesta==1):
            print "El resultado es; ",suma_pares(n1)
        if(respuesta==2):
            print "El resultado es; ",suma_impares(n1)
        if(respuesta==3):
            print "El resultado es; ",mayor_cifras(n1)
        if (respuesta==4):
            print "El resultado es; ",menormayor_cifras(n1)

menu_operaciones()
            
    
