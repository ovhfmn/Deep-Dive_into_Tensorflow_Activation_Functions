import numpy as np
import matplotlib.pyplot as plt
import sys

    '''
    1. It returns a small non-zero gradient if the input is less than zero
    otherwise it returns the given input.
    2. Overcomes dying ReLU problem.
    '''
def leakyRelu(x):    
    x1 =[]
    for i in x:
        if i < 0:
            x1.append(i*0.01)
        else:
            x1.append(i)
    
    return x1

x = np.linspace(-10,10)

plt.plot(x, leakyRelu(x))
plt.axis('tight')
plt.title('Activation Function: Leaky Relu')
plt.show()
