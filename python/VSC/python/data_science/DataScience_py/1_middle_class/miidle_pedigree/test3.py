from numpy import sort


def dividset (num):
    arlist = []
    for i in range(2, num):
        if num % i == 0:
            arlist.append(i)
    
    
    return arlist

inputNum1 = 48
inputNum2 = 60
arlist = []

for i in dividset(inputNum1):
    if i in dividset(inputNum2):
        arlist.append(i)
    
relist = [min(arlist), max(arlist)]
print(relist)






        
