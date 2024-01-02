import matplotlib.pyplot as plt
import numpy as np
import math

def signo(x):
    return np.where(x == 0, 0, np.where(x > 0, 1, -1))

def serie(x, n):
    res = 0
    for k in range(n):
        k1 = 2*k+1
        res += np.sin(k1*x)/k1
    res = (4/math.pi)*res
    return res

if __name__ == "__main__":
    x = np.linspace(-math.pi,math.pi,10000)
    y_signo = signo(x)
    y_serie10 = serie(x,5)
    y_serie100 = serie(x,100)

    plt.plot(x, y_serie10, label='Serie n=10',alpha=0.7, color='red')
    plt.plot(x, y_serie100, label='Serie n=200',alpha=0.7, color='red')
    plt.plot(x, y_signo, label='signo(x)', color='black')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

