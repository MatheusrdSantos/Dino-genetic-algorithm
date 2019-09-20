import numpy as np
# obstacle params
#[distance height speed width]
X = np.array([[100, 50, 10, 50]])

#W = np.array([[1.1, 1.0], [1.5, -3.2], [0.1, 0.9], [0.2, 1.1]])
np.random.seed(1)
W = np.random.rand(4,2)
print(W)
#B = np.array([[7, -1]])
B = np.zeros((1,2))

print(X.shape)
print(W.shape)
print(B.shape)

Z = np.matmul(X, W) + (B)

with np.nditer(Z, op_flags=['readwrite']) as it:
    for item in it:
        if(item<0):
            print(item)
            item[...] = 0
print(Z[0][1])