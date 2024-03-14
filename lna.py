import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, widgets

w = 3.29553e10
gm = 0.0072133
Cgs = 35.47e-15

def L(l):
    a = complex(0, w*l)
    b = complex(20*w*l, 0)
    return ((a*b)/(a+b))

def Zg(s):
    return (1+gm*L(s))/(Cgs*w*complex(0, 1)) + L(s)

def Zin(s, g, Cextra):
    Xc = complex(0, -1/(w*Cextra))
    return (Zg(s)*Xc)/(Zg(s)+Xc) + L(g)

# Define range for Cextra
Cextra_values = np.linspace(1e-15, 20e-15, 400)

@interact(s=(1e-10, 1e-8, 1e-10), g=(1e-10, 1e-8, 1e-10))
def plot_Zin(s=5e-9, g=5e-9):
    Zin_values = [abs(Zin(s, g, Cextra)) for Cextra in Cextra_values]
    
    plt.figure(figsize=(10, 6))
    plt.plot(Cextra_values, Zin_values)
    plt.xlabel('Cextra')
    plt.ylabel('|Zin|')
    plt.title('Zin vs Cextra')
    plt.grid(True)
    plt.show()
