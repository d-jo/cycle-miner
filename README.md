# Cycle-miner

The cycle miner is designed to fetch work from the cycle contract and compute the result. 

Jobs are given in numpy matrix string format. https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html Valid operations for the time being are here:

`conv2d[int[4] strides][padding]` - preforms a convolution on matrix A with matrix B using the steps provided.
