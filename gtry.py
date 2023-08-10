import numpy as np

A = np.array([[2,1,-1,8],[-3,-1,2,-11],[-2,1,2,-3]],dtype=float)

def ge(A):
    m,n = np.shape(A)
    n = n-1

    x = np.zeros(n)

    for i in range(n-1):
        for j in range(i+1,m):
            k = A[j,i]/A[i,i]
            A[j] = A[j] - A[i]*k

    # for i in range(m-1,-1,-1):
    #     sum = A[i,n]
    #     for j in range(i+1,n):
    #         sum = sum - x[j] * A[i][j]
    #     sum = sum / A[i,i]
    #     x[i] = sum

    print(A)
    # print(x)

    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            k = A[j,i]/A[i,i]
            A[j] = A[j] - A[i]*k 
    
    print(A)
    
ge(A)