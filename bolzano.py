import matplotlib.pyplot as plt
import numpy as np
from math import *

# f(x) = e^x + x
def f(x):
    return pow(e, x) + x

def mid(s):
    return s.center(11, ' ')

def header():
    print('\n'+(''.join(map(str, ['-' for i in range(93)]))))
    print(mid('x1'), mid('f(x1)'), mid('x2'), mid('f(x2)'),  mid('x3'), mid('f(x3)'), sep='\t', end='\n')
    print((''.join(map(str, ['-' for i in range(92)]))), end='\n')

def cek(fA, fB, fX, x1, x2, x3):
    return x1 if (min(abs(fA), min(abs(fB), abs(fX)))==abs(fA)) else x2 if (min(abs(fA), min(abs(fB), abs(fX)))==abs(fB)) else x3

def grafik(x1, x2, arr):
    lst_clr = ['r', 'orange', 'y', 'g', 'b', 'violet', 'purple', 'c']
    x = np.arange(x1, x2, 0.1)
    y = np.vectorize(f)
    
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('bolzano')
    plt.plot(x, y(x))
    plt.hlines(y=0, xmin=x1, xmax=x2, color='black')

    j = 0
    for i in arr:
        plt.axvline(x=i, c=lst_clr[j])
        j += 1 if j < 7 else 0
    plt.show()

def fmt(x):
    return "{temp:11.10f}".format(temp=x)

def bolza(x1, x2, x3, fA, fB, fX):
    if abs(fX) > 0.0001:
        print(fmt(x1), fmt(fA), fmt(x2), fmt(fB), fmt(x3), fmt(fX), sep='\t', end='\n')
        if fA * fX > 0: x1, fA, fB = x3, fX, f(x2)
        else: x2, fB, fA = x3, fX, f(x1)

        x3 = (x1 + x2)/2
        fX = f(x3)
        list_x.append(cek(fA, fB, fX, x1, x2, x3))
        
        bolza(x1, x2, x3, fA, fB, fX)
    else: print("\nx akhir =", cek(fA, fB, fX, x1, x2, x3))

if __name__ == "__main__":
    list_x = []
    x1 = float(input('\nmasukkan batas bawah\t: '))
    x2 = float(input('masukkan batas atas\t: '))
    x3 = (x1+x2)/2

    fA, fB, fX = f(x1), f(x2), f(x3)
    list_x.append(cek(fA, fB, fX, x1, x2, x3))

    if fA * fB >= 0:
        print('tanda sama')
        exit()

    header()
    bolza(x1, x2, x3, fA, fB, fX)
    grafik(x1, x2, np.array(list_x))