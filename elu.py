import numpy as np
import matplotlib.pyplot as plt

    ''' 
    1. In most cases performs better than ReLU, or Leaky ReLU
    '''
def elu(x,a=0.01):
    x1 =[]
    for i in x:
        if i <= 0:
            x1.append(float(np.exp(i)-1))
        else:
            x1.append(i)
    
    return x1

x = np.linspace(-10,10)

plt.plot(x, elu(x))
plt.axis('tight')
plt.title('Activation Function: Elu')
plt.show()
