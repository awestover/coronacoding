direction = 1
person = 0
number_of_ppl = 100
data = []
for i in range(1,5600*2):
    if i % 7 == 0:
        direction *= -1
    if i % 8 == 0:
        person += direction
    person += direction
    person = person % number_of_ppl
    data.append(person)

import matplotlib.pyplot as plt
import numpy as np

points = [(np.cos(data[i]*np.pi*2/100)*(i**0.5), np.sin(data[i]*np.pi*2/100)*(i**0.5)) for i in range(len(data))]
plt.scatter([x[0] for x in points], [x[1] for x in points])
plt.show()

