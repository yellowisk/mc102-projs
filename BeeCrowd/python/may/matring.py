##For a N-character long message, the corresponding matring is a 4x(N+2) matrix of digits.

def decode_matring(matring):
    matrixOfRemainingColumns = []
    F = int(''.join([l[0] for l in m]))
    L = int(''.join([l[-1] for l in m]))
    for i in range(1, len(m[0])-1):
        column = [l[i] for l in m]
        matrixOfRemainingColumns.append(column)
    
    message = ""

    for col in matrixOfRemainingColumns:
        Mi = int(''.join(col))
        Ci = (F * Mi + L) % 257
        message += chr(Ci)
    
    return message

m = []
try:
    while True:
        l = input()
        m.append(l)
except EOFError:
    #To decode a matring to an string, we must calculate: Ci = (F * Mi + L) mod 257, where Ci is the ASCII-coded character of the original message at position i.
    #F is the first column of the matrix, L is the last column of the matrix, and Mi is the i-th column of the matrix.
    #The original message is the concatenation of the Ci values.
    print(decode_matring(m))