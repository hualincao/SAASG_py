import numpy as np
import math

mean_curve = np.load("../results/mean_curve.npy")
time_refer = np.load("../results/time.npy")

def distance_fn(a,b,t1,t2):
    return abs(a-b) + 1/(1+math.exp(-0.03*(abs(t1-t2)-100)))

def dtw(x,y,tx,ty):
    n,m=len(x),len(y)
    D=np.zeros((n,m))

    D[0,0]=distance_fn(x[0],y[0],tx[0],ty[0])

    for i in range(1,n):
        D[i,0]=D[i-1,0]+distance_fn(x[i],y[0],tx[i],ty[0])

    for j in range(1,m):
        D[0,j]=D[0,j-1]+distance_fn(x[0],y[j],tx[0],ty[j])

    for i in range(1,n):
        for j in range(1,m):
            D[i,j]=distance_fn(x[i],y[j],tx[i],ty[j]) + \
                   min(D[i-1,j],D[i,j-1],D[i-1,j-1])

    return D

print("TWDTW模块加载完成")