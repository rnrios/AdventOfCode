def main():
    f = open('input.txt', 'r').read().splitlines()
    inputs, outputs = [], []

    for line in f:
        line = line.split(' ')
        outputs.append(line[-4:])
        
    count = 0
    for output in outputs:
        output_str = []
        output_len = map(lambda x: len(x), output)
        for x in output_len:
            if x in [2, 3, 4, 7]:
                count += 1
    print(count)


if __name__ == '__main__':
        main()