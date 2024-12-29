import numpy as np
import matplotlib.pyplot as plt

    '''
    1. x * sigmoid(x)
    2. Can replace ReLU
    '''
def swish(x):
    return x/(1+np.exp(-x))

x = np.linspace(-10,10)

plt.plot(x, swish(x))
plt.axis('tight')
plt.title('Activation Function: Swish')
plt.show()
