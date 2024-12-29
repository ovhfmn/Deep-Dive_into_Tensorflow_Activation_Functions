import numpy as np
import matplotlib.pyplot as plt

    '''
    1. x * tanh( ln(1 + e^x) )
    '''
def mish(x):
    return x * (
        np.tanh(
            np.log(1 + np.exp(x))
        )
    )

x = np.linspace(-10,10)

plt.plot(x, mish(x))
plt.axis('tight')
plt.title('Activation Function: Mish')
plt.show()
