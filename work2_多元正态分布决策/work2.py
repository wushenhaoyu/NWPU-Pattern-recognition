import numpy as np
X =  np.random.rand(3, 10)
X_test = np.random.rand(3,1)
def Expected_value(X):#计算期望
    num = X.shape[1] #样本个数
    X1 = [X[:,i] for i in range(X.shape[1])]
    X1 = np.sum(X1, axis=0, keepdims=True) / num
    return X1


def Covariance_matrix(X): #计算协方差矩阵
    num = X.shape[1]
    X_e = Expected_value(X) #期望
    X_T = X.T
    X_T = [X_T[i, :].reshape(-1, 1) for i in range(X_T.shape[0])]
    X1 = [X[:,i] for i in range(X.shape[1])]
    X_sum = []
    for x, x_T in zip(X1, X_T):
        X_sum.append(x * x_T)
    return np.sum(X_sum,axis=0) / num - X_e.reshape(X.shape[0],1) * X_e.reshape(1,X.shape[0])

def gx1(X_test,X): #欧氏距离
    """X1 = [X[:, i] for i in range(X.shape[1])] - Expected_value(X)
    X1_T = []
    for x in X1:
        X1_T.append(x.reshape(-1,1))"""
    x = X_test.reshape(-1,1) - Expected_value(X).reshape(-1,1)
    return np.dot(x.T, x)

def gx2(X_test,X):#马氏距离
    x = X_test.reshape(-1, 1) - Expected_value(X).reshape(-1, 1)
    return np.dot(np.dot(x.T,np.linalg.inv(Covariance_matrix(X))) , x)

if __name__ == "__main__":
    print(gx1(X_test,X))
    print(gx2(X_test,X))