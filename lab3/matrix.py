def transpose(matrix):
    if len(matrix) == 0:
        return []
        
    transposed = []
    for oldcolumn in range(len(matrix[0])):
        newRow = []
        for oldrow in range(len(matrix)):
            newRow.append(matrix[oldrow][oldcolumn])
        transposed.append(newRow)
    return transposed

def powers(powerlist, num1, num2):
    powerlisted = []
    for powers in powerlist:
        newRow =[]
        for i in range(num1, num2+1):
            newRow.append(powers**i)
        powerlisted.append(newRow)
    return powerlisted

def matmul(A,B):
    result =[]
    for rowA in range(len(A)):
        newRow = []
        for columnB in range(len(B[0])):
            newVal = 0
            for offset in range(len(B)):
                newVal += A[rowA][offset] * B[offset][columnB]
            newRow.append(newVal)
        result.append(newRow)
    return result 

def invert(A):
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    inverted = [
        [A[1][1]/det, -A[0][1]/det],
        [-A[1][0]/det, A[0][0]/det]
    ]
    return inverted

def loadtxt(filename):
    file = open(filename)
    lines = file.readlines()
    matrix = []

    for line in lines:
        row = line.split()

        newRow = []
        for value in row:
            newRow.append(float(value))
        matrix.append(newRow)
            
    return matrix
