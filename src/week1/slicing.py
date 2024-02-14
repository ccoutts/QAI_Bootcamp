import time
import os
import numpy as np
from numpy import ndarray


def progress_bar(progress: int = 0) -> ndarray:
    """
    Creates a numpy array and populates it with two kinds of character to produce a
    progress bar
    """
    assert 0 <= progress <= 100
    bar = np.empty(100, dtype='str')
    bar[:progress] = '-'
    bar[progress:] = ' '
    return bar

def pseudo_animate_progress_bar(start: int=0, end: int=100) -> None:
    for i in range(start,end):
        bar = progress_bar(i)
        print(f"0%{''.join(bar)}100%")

def animate_progress_bar(start: int=0, end: int=100) -> None:
    for i in range(start, end):
        bar = progress_bar(i)
        print(f"0%{''.join(bar)}100%", end="\r")
        time.sleep(0.01)

def main():
    #bar = progress_bar(80)
    #print(f"0%{''.join(bar)}100%")
    #pseudo_animate_progress_bar(0,100)
    #input("Press enter to animate the bar")
    animate_progress_bar(0,100)

if __name__ == "__main__":
    main()
