import numpy as np
import sha3
from scipy import signal

def readFile(name):
    with open(name) as f:
        content = np.matrix(f.read())
        f.close()
        return content

def conv2d(mat1, mat2, padding='valid'):
    return signal.convolve2d(mat1, mat2, padding)

def keccak256(data1, data2, op):
    al = sha3.keccak_256()
    al.update(data1, data2, op)
    return al.hexdigest()

mat1 = readFile('data1')
mat2 = readFile('data2')

print(mat1)
print(mat2)

print(conv2d(mat1, mat2))

