"""import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))"""


"""import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()"""

#pandas is nothing but it shows the data in columns wise or order wise
"""import pandas as n

a = [1, 7, 2, 8, 4, 9]
nav = n.Series(a)

print(nav)"""

import pandas as n

data={
    "calories":[420, 380, 390],
    "duration": [50, 40, 45]
}

df = n.DataFrame(data)

print(df)

print(df.loc[0])

