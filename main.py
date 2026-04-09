import matplotlib.pyplot as plt
from data_module import get_data

X, Y = get_data()

plt.plot(X, Y, marker='o')
plt.title("Графік X від Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()