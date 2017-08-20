import numpy as np
from scipy import signal

def readFile(name):
    with open(name) as f:
        content = np.matrix(f.read())
        f.close()
        return content

def conv2d(mat1, mat2, padding='valid'):
    return signal.convolve2d(mat1, mat2, padding)


mat1 = readFile('data1')
mat2 = readFile('data2')

print(mat1)
print(mat2)

print(conv2d(mat1, mat2))

