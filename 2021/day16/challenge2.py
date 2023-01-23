import binascii


def add_zeros(array, i, strbin):
    if int(array[i], 16) > 7:  
        strbin = '' + strbin

    elif int(array[i]) > 3:
        strbin = '0' + strbin      

    elif int(array[i]) > 1:
        strbin = '00' + strbin     

    elif int(array[i]) == 1:
        strbin = '000' + strbin
    return strbin


def bin2dec(binstr):
    N = len(binstr)
    dec = 0
    for i in range(N):
        dec += int(binstr[i])*2**(N-1-i)
    return dec


def check_id0(strbin, i):
    i += 1
    L = bin2dec(strbin[i:i+15]) + i + 15
    i += 15
    return i, L


def check_id1(strbin, i):
    i += 1
    num = bin2dec(strbin[i:i+11])
    i += 11
    return i, num


def get_literal(strbin, litstr, i):
    i+=1
    litstr += strbin[i:i+4]
    i+=4  
    return i, litstr


def prod(array):
    if len(array) == 1:
        return array[0]
    else: 
        return array[0]*prod(array[1:])


def calculate(operation, operands):
    if operation == '000':
        return sum(operands)
    if operation == '001':
        return prod(operands)
    if operation == '010':
        return min(operands) if len(operands) > 1 else operands[0]
    if operation == '011':
        return max(operands) if len(operands) > 1 else operands[0]
    if operation == '101':
        return 1 if operands[0] > operands[1] else 0
    if operation == '110':
        return 1 if operands[0] < operands[1] else 0
    if operation == '111':
        return 1 if operands[0] == operands[1] else 0 


def calculate_operation(strbin, i, operation=None, B=-1, L=-1, 
                        B_flag=False, L_flag = False):
    operands = []
    B_counts = 0
    while True:
        B_counts+=1
        i += 3
        T = strbin[i:i+3]
        i += 3          
        if T!= '100':           
            if strbin[i] == '0':
                i, L_next = check_id0(strbin, i) 
                i, op = calculate_operation(strbin, i, T, B, L_next, L_flag=True)
                operands.append(op)
            elif strbin[i] == '1':
                i, B_next = check_id1(strbin, i)  
                i, op = calculate_operation(strbin, i, T, B_next, L, B_flag=True) 
                operands.append(op) 
        else:     
            litstr = ''        
            while strbin[i] != '0':
                i, litstr = get_literal(strbin, litstr, i) 
            i, litstr = get_literal(strbin, litstr, i)
            operands.append(bin2dec(litstr))
        
        if B_counts == B and B_flag == True:
            operands = calculate(operation, operands)
            return i, operands
        
        if i == L and L_flag == True:   
            operands = calculate(operation, operands)
            return i, operands
        
        if strbin[i:] == len(strbin[i:])*'0':
            return operands[0]
            

def main():
    f = open('input.txt', 'r').read().splitlines()
    strbin =  str(bin(int(f[0], 16)))[2:]
    if int(f[0][0], 16) != 0:
        strbin = add_zeros(f[0], 0, strbin)
    else:
        strbin = add_zeros(f[0], 1, strbin)
        strbin = '0000' + strbin       

    print('Result of operation: {}'
    .format(calculate_operation(strbin, i=0)))


if __name__ == '__main__':
    main()