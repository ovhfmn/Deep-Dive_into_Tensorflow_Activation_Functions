import numpy as np
import matplotlib.pyplot as plt

    '''
    1. Scaled version of Elu
    '''
def selu(x,a=1.0507,lmbd=1.758):
    x1 =[]
    for i in x:
        if i <= 0:
            x1.append(float(np.exp(i)-1) * lmbd)
        else:
            x1.append(i * a)

    return x1

x = np.linspace(-10,10)

plt.plot(x, selu(x))
plt.axis('tight')
plt.title('Activation Function: Selu')
plt.show()
