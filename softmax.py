import numpy as np
import matplotlib.pyplot as plt
import sys

    '''
    1. Usually is described as multiple Sigmoids.
    2. Usually it's the last layer in the multi-class classification problem
    3. It returns the values the sum of which is equal to 1
    4. The higher output for the given class the higher probability.
    '''
def softmax(x):
    z = np.exp(x)
    z_ = z/z.sum()
    return z_

x = np.linspace(-10,10)

plt.plot(x, softmax(x))
plt.axis('tight')
plt.title('Activation Function: Softmax')
plt.show()
