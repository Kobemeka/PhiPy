import numpy as np

def amean(*args):
    return sum(args)/len(args)
def gmean(*args):
    return np.array(args).prod()**(1.0/len(args))
def hmean(*args):
    return len(args)*(1.0/sum(np.array(args)**(-1)))
def median(*args):
    l = np.array(args)
    l=np.sort(l)
    leng = len(l)
    if leng%2 ==1:
        return l[int((leng+1)/2)-1]
    else:
        lf = np.floor(leng/2)
        lf = int(lf)
        return (l[lf-1]+l[lf])/2
        
def riesum(func,strt,stp):
    dx = 1e-6
    val = np.arange(strt,stp,dx)
    return sum(func(val))*dx
def derivative(func,at):
    d = 1e-7
    dm = -1*d
    t1 = (func(at+d)-func(at))/d
    t2 = (func(at+dm)-func(at))/dm
    return amean(t1,t2)
