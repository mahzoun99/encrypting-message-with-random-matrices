import numpy


alphabet = {
        ' ': 0,
        'a': 1,
        'b': -1,
        'c': 2,
        'd': -2,
        'e': 3,
        'f': -3,
        'g': 4,
        'h': -4,
        'i': 5,
        'j': -5,
        'k': 6,
        'l': -6,
        'm': 7,
        'n': -7,
        'o': 8,
        'p': -8,
        'q': 9,
        'r': -9,
        's': 10,
        't': -10,
        'u': 11,
        'v': -11,
        'w': 12,
        'x': -12,
        'y': 13,
        'z': -13
    }


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def generate_message_matrix(message):
    col_size = numpy.ceil(len(message) / 3)
    b = [[0] * int(col_size) for _ in range(3)]
    for i in range(len(message)):
        row = i % 3
        col = int(i / 3)
        b[row][col] = alphabet.get(message[i])
    return numpy.matrix(b)


def generate_random_upper_triangular_matrix():
    a = numpy.random.randint(-50, 50, size=(3, 3))
    a[0][0] = numpy.random.choice([-1, 1])
    a[1][1] = numpy.random.choice([-1, 1])
    a[2][2] = numpy.random.choice([-1, 1])
    a[1][0] = a[2][0] = a[2][1] = 0
    return numpy.matrix(a)


def generate_random_lower_triangular_matrix():
    a = numpy.random.randint(-50, 50, size=(3, 3))
    a[0][0] = numpy.random.choice([-1, 1])
    a[1][1] = numpy.random.choice([-1, 1])
    a[2][2] = numpy.random.choice([-1, 1])
    a[0][1] = a[0][2] = a[1][2] = 0
    return numpy.matrix(a)


def generate_random_matrix():  # with det one or minus one
    lo = generate_random_lower_triangular_matrix()
    up = generate_random_upper_triangular_matrix()
    case = numpy.random.randint(0, 2)
    if case:
        a = numpy.matmul(lo, up)
    else:
        a = numpy.matmul(up, lo)
    return a


m = input(Colors.HEADER + Colors.BOLD + "Enter a message: " + Colors.ENDC)
m = m.lower()
B = generate_message_matrix(m)
# input message matrix generated

A = generate_random_matrix()
C = numpy.matmul(A, B)
while True:
    print(Colors.OKBLUE + "Encrypted message: " + Colors.ENDC)
    for i in range(len(m)):
        print(C.item(i % 3, int(i / 3)), end=' ')
    print('\n' + Colors.OKBLUE + "Key matrix: " + Colors.ENDC)
    print(A)
    # message encrypted

    ch = input(Colors.OKGREEN + "Do you want to employ another key matrix to encrypt the message?(Y/N) " + Colors.ENDC)
    if ch == 'N':
        break
    A = generate_random_matrix()
    C = numpy.matmul(A, B)
    # Ask user for new matrix

# last part
print(Colors.FAIL + Colors.BOLD + "Decrypting..." + Colors.ENDC)
A_inverse = numpy.linalg.inv(A).astype(int)
A_inverse = A_inverse.astype(int)
dec_matrix = numpy.matmul(A_inverse, C)
dec_message = ""
keys = list(alphabet.keys())
vals = list(alphabet.values())
for i in range(len(m)):
    row = i % 3
    col = int(i / 3)
    dec_message += keys[vals.index(dec_matrix.item(row, col))]
print(dec_message)
del keys, vals
# message decrypted
