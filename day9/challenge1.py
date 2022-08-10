import numpy as np


def main():
    f = open('input.txt', 'r').read().splitlines()

    array = np.array([[int(x) for x in y] for y in f])
    low = []
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            flag = True 
            if i-1 >= 0 and flag==True:
                flag = True if array[i][j] < array[i-1][j] else False
            if j-1 >= 0 and flag==True:
                flag = True if array[i][j] < array[i][j-1] else False
            if j+1 <     array.shape[1] and flag==True:
                flag = True if array[i][j] < array[i][j+1] else False
            if i+1 < array.shape[0] and flag==True:
                flag = True if array[i][j] < array[i+1][j] else False
            if flag == True:
                low.append(array[i][j])
    print(np.sum(low)+len(low))


    if __name__ == '__main__':
    main()