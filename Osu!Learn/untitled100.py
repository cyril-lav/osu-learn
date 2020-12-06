import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sklearn as sk

rng = np.random.RandomState(42)

x = 10 * rng.rand(50)
print('la taille de notre ehantillon est :',x.shape)

y=2*x-1+ rng.randn(50)

plt.scatter(x,y);