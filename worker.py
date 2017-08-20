import numpy as np
import hashlib
from scipy import signal

def readFile(name):
    with open(name) as f:
        content = np.matrix(f.read())
        f.close()
        return content

def conv2d(mat1, mat2, padding='valid'):
    return signal.convolve2d(mat1, mat2, padding)

def keccak256(data1, data2, op):
    al = hashlib.sha256()
    al.update(data1.encode('utf-8'))
    al.update(data2.encode('utf-8'))
    al.update(op.encode('utf-8'))
    return al.hexdigest()

mat1 = readFile('data1')
mat2 = readFile('data2')

print(keccak256(mat1, mat2, "conv"))
print(mat1)
print(mat2)

print(conv2d(mat1, mat2))

