import numpy as np
import matplotlib.pyplot as plt
import sys

    '''
    1. It returns zero if the input is less than zero otherwise it returns the given input.
    2. Probably the most popular choise for hidden layers
    '''
    
def relu(x):
    x1 =[]
    for i in x:
        if i < 0:
            x1.append(0)
        else:
            x1.append(i)
    
    return x1

x = np.linspace(-10,10)

plt.plot(x, relu(x))
plt.axis('tight')
plt.title('Activation Function: Relu')
plt.show()
