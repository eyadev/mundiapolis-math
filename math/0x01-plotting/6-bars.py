#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

columns_labels = ('Farrah', 'Fred', 'Felicia')
rows_labels = ('apples', 'bananas', 'oranges', 'peaches')
colors = ('red', 'yellow', '#ff8000', '#ffe5b4')

y_offset = np.zeros(3)

for row in range(len(fruit)):
    plt.bar(columns_labels, fruit[row], width=0.5, bottom=y_offset,
            color=colors[row],label = rows_labels[row])
    y_offset=list(np.add(y_offset,fruit[row]))        



plt.yticks(np.arange(0, 90, 10))
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.legend()

plt.show()