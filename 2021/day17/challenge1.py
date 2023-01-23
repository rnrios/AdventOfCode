import numpy as np


def grid(x, y):
    x, y = np.meshgrid(np.arange(x[0],x[1]), np.arange(y[0],y[1]))
    return x.ravel(), y.ravel()


def get_max(val, max_val):
    return val if val>max_val else max_val


def find_highest(X, Y, V):
    X_range = np.arange(85, 145)
    Y_range = np.arange(-163, -108)
    max_val = -np.inf
    while True:
        X += V[0]
        Y += V[1]
        
        if V[0]!=0:
            V[0] -= V[0]/abs(V[0])
        V[1] -= 1
        max_val = get_max(Y, max_val)
        
        if X in X_range and Y in Y_range:
            return max_val

        elif Y < -5:
            return -np.inf

def main():
    X0 = [0, 0]
    X = Y = 0
    max_arr = []
    xx, yy = grid([0, 40], [0, 180])
    for x, y in zip (xx, yy):
        V = [x, y]
        max_arr.append(find_highest(X, Y, V))
    print(max(max_arr))


if __name__ == '__main__':
    main()
