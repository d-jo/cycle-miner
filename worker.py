import numpy as np
import hashlib
from scipy import signal

WORKER = "0xd3adb33f"

def readFile(name):
    with open(name) as f:
        content = np.matrix(f.read())
        f.close()
        return content

def conv2d(mat1, mat2, padding='valid'):
    return signal.convolve2d(mat1, mat2, padding)

# so funny story, this isnt actually correct...
# keccak256 and sha256 are not the same
def keccak256(*args):
    al = hashlib.sha256()
    for arg in args:
        al.update(arg.encode('utf-8'))
    return al.hexdigest()

class Job:

    id = 0
    data1 = 0
    data2 = 0
    op = 0
    solution = 0
    solver = 0
    solution_fingerprint = 0

    def __init__(self, data1, data2, op):
        self.data1 = data1
        self.data2 = data2
        self.dop = op
        id = keccak256(data1, data2, op)

    
    def solve(self, solver, solution):
        self.solution = solution
        self.solver = solver
        self.solution_fingerprint = keccak256(id, solver, solution)
        return self.solution_fingerprint




mat1 = readFile('data1')
mat2 = readFile('data2')

print(keccak256(mat1, mat2, "conv"))
print(mat1)
print(mat2)

print(conv2d(mat1, mat2))

