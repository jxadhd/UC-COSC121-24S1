def afunction(value1, value2):
    '''Do something unknown and weird'''
    op1 = 0
    while op1 < value1:
        op2 = value1
        while op2 > value2:
            result = op1 * op2
            print(f"{op1:3} x {op2:3} = {result:3}")
            op2 -= 1
        op1 += 1

#Test
afunction(4, 2)
