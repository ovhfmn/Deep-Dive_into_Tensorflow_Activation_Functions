import numpy as np
import matplotlib.pyplot as plt

def binaryStep(x):
    ''' It returns '0' if the input is less then zero otherwise it returns one '''
    return np.heaviside(x,1)


x = np.linspace(-10,10)
plt.plot(x, binaryStep(x))
plt.axis('tight')
plt.title('Activation Function: Binary Step')
plt.show()
