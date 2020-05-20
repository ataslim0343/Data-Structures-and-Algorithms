def multiplyMatrix(n1, m1, n2, m2, arr1, arr2):
    import numpy as np
    M=np.dot(arr1,arr2)
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j],end=" ")
