#!/usr/bin/env/python3

# Coding practice for Week 1 Wednesday session

import numpy as np
import plotter



def main():
    numpy_basics()
    plotter.plot_numpy_array(np.arange(10), 'My Plot')

def function_header(function_name:str) -> None:
    """
    Prints a formatted function header
    """
    print('-----------')
    print(f'FUNCTION: {function_name}')
    print('-----------')

def numpy_basics() -> None:
    matrix_product(np.array([[1,2],[2,3]]), np.array([[1,2],[2,3]]))

def numpy_arange() -> None:
    function_header(numpy_arange.__name__)
    #1D array
    a = np.arange(10)
    print(a)
    #2D array
    b = np.arange(12).reshape(4,3)
    print(b)

def numpy_array() -> None:
    function_header(numpy_array.__name__)
    #1D array
    a = np.array([1.1,2.2,3.3])
    print(a)
    #2D array
    b = np.array([[1,2],[2,3]])
    print(b)

def matrix_product(matrix_a: np.ndarray, matrix_b: np.ndarray)->None:
    """
    Returns product of two matrices
    """
    function_header(matrix_product.__name__)
    print(matrix_a*matrix_b)
    print('----------')
    print(matrix_a@matrix_b)
    print('----------')
    print(matrix_a.dot(matrix_b))




if __name__ == '__main__':
    main()