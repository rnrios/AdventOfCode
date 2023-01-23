import binascii


def bin2dec(binstr):
    N = len(binstr)
    dec = 0
    for i in range(N):
        dec += int(binstr[i])*2**(N-1-i)
    return dec


def check_id0(strbin, i):
    i += 1
    num = bin2dec(strbin[i:i+15])
    i += 15
    return i, num


def check_id1(strbin, i):
    i += 1
    L = bin2dec(strbin[i:i+11])
    i += 11
    return i, L


def main():
    f = open('input.txt', 'r').read().splitlines()
    strbin =   str(bin(int(f[0], 16)))[2:]
    if int(f[0][0], 16) > 7:  
        strbin = '' + strbin

    elif int(f[0][0]) > 3:
        strbin = '0' + strbin

    elif int(f[0][0]) > 1:
        strbin = '00' + strbin

    elif int(f[0][0]) <= 1:
        strbin = '000' + strbin
    
    i = v = num = L =0
    while True:
        v += bin2dec(strbin[i:i+3])
        i += 3
        if strbin[i:i+3] != '100':
            i+=3
            if strbin[i] == '1':
                i, L = check_id1(strbin, i)
            elif strbin[i] == '0':
                i, num = check_id0(strbin, i)
        else:
            i+=3
            while strbin[i] != '0':
                i+=5
            i+=5

        if strbin[i:] == len(strbin[i:])*'0':
            break    
    print(v)


if __name__ == '__main__':
    main()