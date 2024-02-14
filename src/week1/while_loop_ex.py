import numpy as np

i = 1
j = 0 
while i <= 20:
    i +=1
    if i%2 == 0:
        j = j+i
print(f"The sum of evens between 1 and 20 is {j}")
