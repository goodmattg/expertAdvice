import numpy as np
import lossFunc as loss
import pdb
import math
from IPython.core.debugger import Tracer
from matplotlib import pyplot as plt

debug = Tracer()

mean = 0.5
sigma = 0.25
nexperts = 10
nrounds = 10000
lrate = math.sqrt(8 * math.log(nexperts) / nrounds)
weights = (1/nexperts) * np.ones((1,nexperts))
weights_cum = np.zeros((nexperts, nrounds))
predictions = []

advice = np.random.normal(mean, sigma, (nexperts, nrounds))
# clip distribution to ensure loss(f_i,outcome) in [0,1]
advice[advice>1] = 1
advice[advice<0] = 0

# outcomes -> specifies expert 0 as perfect
outcomes = np.random.normal(mean, sigma, (nrounds))

for it in range(nrounds):
    weights_cum[:,it] = weights

    predictions.append(np.take(np.dot(weights, advice[:,it]), 0))

    # now adjust weights
    weights = weights * np.exp(-lrate * abs(advice[:,it]-outcomes[it]))
    weights = weights / np.sum(weights)

# predictions should converge to perfect
plt.figure(0)
plt.plot(abs(predictions-outcomes))

plt.figure(1)

for e in range(nexperts):
    plt.plot(weights_cum[e,:])

plt.show()
# debug()
print('done')

# # weight of perfect expert should converge to 1
# plt.plot(weights_cum[0,:])
