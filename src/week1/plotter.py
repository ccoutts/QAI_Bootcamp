from numpy import ndarray
from matplotlib import pyplot as plt

def plot_numpy_array(oneD_array: ndarray, titttle: str) -> None:
    x = oneD_array
    y = 2 * x + 5
    plt.title(titttle)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.plot(x, y)
    plt.show()

