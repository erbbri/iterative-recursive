import time
import csv

def iterativePower(base, exponent): # Iterative Implementation
    retVal = 1.0
    if (exponent < 0):
        return 1.0 / iterativePower(base, -exponent)
    else:
        for x in range(1, exponent):
            retVal *= base
    return retVal


def recursivePower(base, exponent): # Recursive Implementation
    if(exponent < 0):
        return 1/recursivePower(base, -exponent)
    elif (exponent == 0):
        return 1
    else:
        return base * recursivePower(base, exponent - 1)


baseNum = 3.1415926535


with open('test.csv', mode='w') as csv_file:
    fieldnames = ['n', 'Iterative', 'Recursive']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for x in range (0,998): 
        iStart = time.perf_counter_ns()
        iterativePower(baseNum, x)
        iEnd = time.perf_counter_ns()

        rStart = time.perf_counter_ns()
        recursivePower(baseNum,x)
        rEnd = time.perf_counter_ns()

        writer.writerow({'n': x, 'Iterative': iEnd-iStart, 'Recursive': rEnd - rStart})

