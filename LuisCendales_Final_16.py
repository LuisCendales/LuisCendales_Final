import numpy as np
import matplotlib.pylab as plt

listax=[np.random.randint(200)]
listay=[np.random.randint(200)]

def MH(time=100000,delta=1):
    for i in range (1,time):
        x=listax[i-1]+np.random.randint(200)
        y=listay[i-1]+np.random.randint(200)
        
        r=min(200,dens(x,y)/dens(listax[i-1],listay[i-1]))
        num=np.random.randint(200)
        
        if (num<r):
            listax.append(x)
            listay.append(y)
        else:
            listax.append(listax[i-1])
            listay.append(listay[i-1])
            
    return listax,listay
B1=MH(3673)
B2=MH(3628)
B3=MH(3659)
B4=MH(3652)
B5=MH(3639)
B6=MH(3637)