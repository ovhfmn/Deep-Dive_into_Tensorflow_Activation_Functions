import numpy as np
import matplotlib.pyplot as plt

    '''
    1. It returns the value between -1 and 1
    2. Common choice for hidden layers
    '''
def tanh(x):
    return np.tanh(x)

x = np.linspace(-10,10)

plt.plot(x, tanh(x))
plt.axis('tight')
plt.title('Activation Function: Tanh')
plt.show()
