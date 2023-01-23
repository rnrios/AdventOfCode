import numpy as np
S1 = 85
S2 = 145
S3 = -163
S4 = -108


def grid(x, y):
    x, y = np.meshgrid(np.arange(x[0],x[1]), np.arange(y[0],y[1]))
    return x.ravel(), y.ravel()


def get_max(val, max_val):
    return val if val>max_val else max_val


def find_highest(X, Y, V):
    X_range = np.linspace(S1, S2, S2-S1+1, endpoint=True)
    Y_range = np.linspace(S3, S4, S4-S3+1, endpoint=True)
    max_val = -np.inf
    #print(X, X_range)
    while True:  
        if X in X_range and Y in Y_range:
            return 1
        
        elif Y < S3:
            return 0
        
        X += V[0]
        Y += V[1]
    
        if V[0]!=0:
            V[0] -= V[0]/abs(V[0])
        V[1] -= 1
        


def main():
    X0 = [0, 0]
    X = Y = 0
    reached_arr = []
    xmin = 0
    xmax = S2

    ymin = S3
    ymax = int(2*S1)
    xx, yy = grid([xmin, xmax+1], [ymin, ymax+1])
    for x, y in zip (xx, yy):
        V = [x, y]
        reached_arr.append(find_highest(X, Y, V))
    print(sum(reached_arr))


if __name__ == '__main__':
    main()
