import sys
import itertools

def read_mifdump(filename):
    return [line.strip().split(' : ') for line in open(filename).readlines()]

def insch(my_str, group=2, char=' '):
    my_str = str(my_str)
    return char.join(my_str[i:i+group] for i in range(0, len(my_str), group))

def pack(addr):
    return hex(int(addr, 16)//4)[2:].rjust(4, '0')

def split_words(dump):
    for line in dump:
        tmp = line[1].split(' ')
        line[1] = ''.join(tmp)
        # print(pack(line[0]) + ' : ' + line[1])

def conv_32b_word(mifdump):
    output = []
    l_iter_first = iter(mifdump)
    l_iter_second = iter(mifdump)
    next(l_iter_second)
    try:
        while True:
            t0 = next(l_iter_first)
            t1 = next(l_iter_second)
            if len(t0[1]) == 4:
                # print(str(t0))
                if len(t1[1]) == 4:
                    output.append([t0[0], t1[1] + t0[1]])
                next(l_iter_first)
                next(l_iter_second)
            else:
                output.append(t0)
    except StopIteration:
        if len(t1[1]) == 8:
            output.append(t1)
        return output

def write_mifdump(dump, filename):
    cnt = 0;
    with open(filename, 'w') as out:
        out.write('DEPTH = 8192;\n')
        out.write('WIDTH = 32;\n')
        out.write('ADDRESS_RADIX = HEX;\n')
        out.write('DATA_RADIX = HEX;\n')
        out.write('CONTENT\n')
        out.write('BEGIN\n')
        for (addr, data) in dump:
            print(pack(addr) + ' : ' + data + ';')
            out.write(pack(addr) + ' : ' + data + ';\n')
        out.write('END;\n')

if len(sys.argv) != 3:
    print('Usage: python3 mifgen.py <input.mifdump> <outpud.mif>')
    exit(1)

print('Input: ' + sys.argv[1])
print('Output: ' + sys.argv[2])
mifdump = read_mifdump(sys.argv[1])
split_words(mifdump)
mifdump = conv_32b_word(mifdump)
write_mifdump(mifdump, sys.argv[2])
print('\nDone!')