from utils import count_increases
def counts():
    f = open('input1.txt')
    array = [float(line.split('\n')[0]) for line in f.readlines()]
    print(count_increases(array))
    

if __name__ == '__main__':
    counts()


