def count_increases(array):
    return len([x for i,x in enumerate(array) if x>0 and x>array[i-1]])