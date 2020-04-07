import numpy as np
X = np.random.rand(100, 1)
y = 4 + 3 * X + .2*np.random.randn(100, 1) # noise added
one = np.ones((X.shape[0],1))
X = np.concatenate((one, X), axis = 1)

def sgrad(w, xi, yi):
    return xi.T.dot(xi.dot(w) - yi)

def my_MGD(w_init, eta):
    w = [w_init]
    for sl in range(100):
        n = X.shape[0] // 10
        tt = []
        for i in range(n):
            tt.append(np.random.randint(0, X.shape[0] ))
        data = np.array(X[tt ,:])
        label = np.array(y[tt , :])
        w_new  = w[-1] - eta * sgrad(w[-1], data, label)
        print(w_new)
        if np.linalg.norm(w_new - w[-1])/ len(w_init) < 1e-3:
            break
        w.append(w_new)
    return w

w_init = np.array([[2], [1]])
n = X.shape[0] // 10
tt = []
for i in range(n):
    tt.append(np.random.randint(0, X.shape[0] ))
data = np.array(X[tt ,:])
label = np.array(y[tt , :])
print(sgrad(w_init,data,label))

my_MGD(w_init,1)