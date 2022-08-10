def main():
    f = [line.split('\n')[0] for line in open('input1.txt').readlines()]
    text_array = [line.split(' ') for line in f]
    x, y, = 0, 0
    for element in text_array:
        if element[0][0] == 'f':
            x+=float(element[1]) 
        elif element[0][0] == 'd':
            y+=float(element[1])
        elif element[0][0] == 'u':
            y-=float(element[1])
    print(x*y)


if __name__ == '__main__':
    main()
