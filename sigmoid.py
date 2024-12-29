import numpy as np
import matplotlib.pyplot as plt
import sys

    '''
    1. It returns 1/(1+exp(-x)). where the value lies between zero and one
    2. Most of the times is used in the last layer for Binary classification
    3. Sometimes is used in hidden layers.
    '''
def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.linspace(-10,10)


plt.plot(x, sigmoid(x))
plt.axis('tight')
plt.title('Activation Function: Sigmoid')
plt.show()
